
## Importing modules
import os
from os import path

## Importing user defined modules
import utils

## Variables
envData = [];
path = ""
filePath = "";
languageFile = "";
targetLangugaeCode = "";

def iosLocalizer(args) :
	envData = utils.getEnvData();
	'''
	path = envData["resultLocation"] + "/" + "ios"  + "/";
	print path;
	
	for lang in envData["target"] :
		targetLangugaeCode = utils.getLanguageCode(lang);
		filePath = path + targetLangugaeCode + ".lproj" + "/" + "Localizable.strings";
		print (filePath)'''

def localizeMe(args) :
	print "Updating ios compatable .strings file"
	iosLocalizer(args);
	
	