
## Importing modules
import json
import urllib2
import os
from os import path

## variables
envData = []

## Reading settings
def getEnvData() :
	with open('./settings.json') as json_data :
		envData = json.load(json_data)
		json_data.close()
		return envData;

## Function to get correspodning Language code
def getLanguageCode(Language):
	languageCode = ""
	if Language == "dutch":
		languageCode = "nl"
	elif Language == "german":
		languageCode = "de"
	elif Language == "turkish":
		languageCode = "tr"
	elif Language == "english":
		languageCode = "en"
	return languageCode
#print "Translating < "+ args.input + " > from "+ envData["source"] +" to "+ ",".join(envData["target"])