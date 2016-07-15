import requests
import ast
import pprint
import re
pp = pprint.PrettyPrinter(depth=6)
import nltk

def get_relations(review):
	url = "http://access.alchemyapi.com/calls/text/TextGetTypedRelations?showSourceText=1&model=913207d1-81b0-42be-89c4-9b82bedfc9d9&apikey=dd8e269c92c4149bbf3e3b81490de0de4378dcab&outputMode=json"
	#url = "http://access.alchemyapi.com/calls/text/TextGetTypedRelations?showSourceText=1&model=ae997404-c8d5-433a-995c-dceeacf22e34&apikey=ffd7397f4be657f7740a84038f903271b2707a11&outputMode=json"
	f = requests.get(url, params={'text':review})
	response = f.content
	response = ast.literal_eval(response)
	return response

def get_entities(review):
	url = "http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities?showSourceText=1&model=913207d1-81b0-42be-89c4-9b82bedfc9d9&apikey=dd8e269c92c4149bbf3e3b81490de0de4378dcab&outputMode=json&sentiment=1"
	f = requests.get(url, params={'text':review})
	response = f.content
	response = ast.literal_eval(response)
	return response

def token_replacement(review):
	processed = get_entities(review)
	if 'statusInfo' in processed:
		return review
	if 'entities' in processed:
		entities = processed['entities']
		text = processed['text']
		for i in entities:
			token = i['text']
			classification = "<" + i['type'] + ">"
			text = re.replace(r"\b%s\b" % token, classification, text,count=1)
	return text
