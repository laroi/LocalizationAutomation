#####################################################################
# Script to update Language Files
# Created By : Akbar <akbarali1klr@gmail.com>
# Created Date : 09-08-2014
#####################################################################

#
#imports
#
import argparse
import json
import urllib2
import os
from os import path

#
#variables
#
envData = []
sourceLanguageCode = ""
targetLangugaeCode = ""
languageFile = ""
filePath = ""
index = 0
newString="" 

#
#parsing arguments
#
parser = argparse.ArgumentParser(description='Updates Language File')
parser.add_argument("-v", "--variable", help="name of the variable to be added", required=True)
parser.add_argument("-i", "--input", default="", help="Input string", required=True)
parser.add_argument("-e", "--existing", default="", help="Under the existing header you want to add the translation eg:- log_in_page")
parser.add_argument("-n", "--new", default="", help="Under the new header you want to add the translation eg:- log_in_page")
args = parser.parse_args()

#
#Reading settings
#
with open('./settings.json') as json_data:
    envData = json.load(json_data)
    json_data.close()

print "Translating < "+ args.input + " > from "+ envData["source"] +" to "+ ",".join(envData["target"])

#
# Function to get correspodning Language code
#
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

#
# Function to write to file
#
def writeToFile(filePath, inString):
    fileObj = open(filePath, 'rw+')
    languageFile = fileObj.read()
    if(args.existing):
        if(args.existing != ""):
            if("#" + args.existing in languageFile):
                print "[MANIPULATE FILE] Found " + args.existing + " header in " + envData["project"] + "/" + "word_" + targetLangugaeCode + ".properties"
                index = languageFile.index("#" + args.existing) + len("#" + args.existing)
                newString = "\n" + args.variable.encode('utf-8')
                for i in range(0, 25 - len(args.variable.encode('utf-8'))):
                    newString += " "
                newString += "="
                newString += "          "
                newString += inString
                fileObj.seek(0)
                fileObj.write(languageFile[:index] + newString + languageFile[index:])
                fileObj.truncate()
                print "File " + envData["project"] + "/" + "word_" + targetLangugaeCode + ".properties is written with " + args.variable
    fileObj.close()

sourceLanguageCode = getLanguageCode(envData["source"])

#
#writing word.properties first with input string
#
filePath = path.abspath(envData["project"] + "/" + "word.properties")
writeToFile(filePath, args.input)

#
# Looping through target Languages
#
for lang in envData["target"]:
    targetLangugaeCode = getLanguageCode(lang);
    try:
        data = json.load(urllib2.urlopen('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20140802T110726Z.747086742c9049f1.dccfdbd9845f6c754dc7bfe9d83e72d34aa33993&lang=' + sourceLanguageCode + "-" + targetLangugaeCode + '&text='+args.input))
        if data["code"] == 200:
            filePath = path.abspath(envData["project"] + "/" + "word_" + targetLangugaeCode + ".properties")
            writeToFile(filePath, data['text'][0].encode('utf-8'))
    except Exception as e:
        print e
