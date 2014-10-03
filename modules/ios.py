
## Importing modules
import os
from os import path

## Importing user defined modules
import utils

## function makeString starts here
## Functions creates string, required to be written to the language file
def makeString(lang, args, data, env) :
    key       = "";
    value     = "";
    header    = ""; # Name of the header under which string needs to be stored.
    platform  = ""; # To check if the web platform is set to true in master file.
    reqString = ""; # Required string to be written to the languages file.
    filePath  = ""; # Path for the language file.
    langCode  = ""; # Target language code
    master    = ""; # Master file data (master.json)
    envData   = ""; # Environment varialbles (settings.json)
    fileObj   = "";
    fileData  = "";
    
    langCode = lang;
    master   = data;
    envData  = env;
    filePath = path.abspath(envData["result"] + "/" + "ios" + "/" + langCode + ".lproj" + "/" + "Localizable.strings");
    key      = args.variable;
    
    # if args.new create new header and append the translation (key, value pair) under the new header.
    # else append the translation (key, value pair) under existing header.
    if (args.new) :
        header = args.new;
    else :
        header = args.existing;
    platform = data[header][key]["platform"]["ios"];
    value    = data[header][key]["locale"][langCode];

    if (platform) :
    	try :
    		fileObj = open(filePath, 'rw+');
    		fileData = fileObj.read();
    	except Exception as e :
    		print "error while writing key value pair into localization files" + e;
    else :
    	print "Sorry! The given translation is not required for web app";

## function makeString ends here

#function iosLocalizer starts here
def iosLocalizer(args) :
	masterfilePath = "";
	masterData     = "";
	targetLanguage = "";
	envData = [];
	
	# Get the environment variables (Settings data)
	envData = utils.getEnvData();
	targetLanguage = envData["target"];

	if (envData) :
		masterfilePath = utils.getMasterFilePath();
	 	masterData = utils.readJson(masterfilePath);

        # to check if the master string file is loaded or not
        if (masterData) :
            for lang in targetLanguage :
                targetLangugaeCode = utils.getLanguageCode(lang);
                makeString(targetLangugaeCode, args, masterData, envData);
#function iosLocalizer ends here


def localizeMe(args) :
	iosLocalizer(args);