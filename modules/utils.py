
## Importing modules
import json
import urllib2
import os
from os import path

## variables
envData = [];
masterFilePath = "";

## Reading settings
def getEnvData() :
	try :
		envData = readJson('./settings.json');
		return envData;
	except Exception as e :
		print "error loading env data" + e;
		return False;
## Reading settings ends here

## function to set master file path starts here
def getMasterFilePath() :
	masterFilePath = path.abspath("./res" + "/" + "master.json");
	return masterFilePath;
## function to set master file path ends here

## Function to get correspodning Language code starts here
def getLanguageCode(Language) :
	if (Language) :
		if (Language == "dutch") :
			return "nl";
		elif (Language == "english") :
			return "en";
		elif (Language == "german") :
			return "de";
		elif (Language == "turkish") :
			return "tr";
		return False;
	return False;
## function to get corresponding language code ends here    

# function to read any json file from specific path
def readJson(_path) :
	try :
		with open(_path) as json_data :
			_json_data = json.load(json_data);
			json_data.close();
			return _json_data;
	except Exception as e :
		print "error loading master file" + e;
		return False;
# function teo read any json file ends here
