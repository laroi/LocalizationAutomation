
## Importing modules
import json
import urllib2
import os
from os import path

## variables
envData = []

## Reading settings
def getEnvData() :
    return readJson('../settings.json')

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

#function to read any json file from specific path
def readJson(_path):
    with open(_path) as json_data :
	    _json_data = json.load(json_data)
	    json_data.close()
	    return _json_data;
