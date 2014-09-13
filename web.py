## Importing modules
import os
from os import path

## Importing user defined modules
import utils

## Variables
envData = []
sourceLanguageCode = ""
targetLangugaeCode = ""
languageFile = ""
filePath = ""
index = 0
newString = ""

## Function to write to file
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

def webLocalizer(args) :
	envData = utils.getEnvData()
	sourceLanguageCode = utils.getLanguageCode(envData["source"])

	## writing word.properties first with input string
	filePath = path.abspath(envData["project"] + "/" + "web" + "/" + "word.properties")
	#writeToFile(filePath, args.input)

	## Looping through target Languages
	
	for lang in envData["target"] :
		targetLangugaeCode = getLanguageCode(lang);
		try:
			data = json.load(urllib2.urlopen('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20140802T110726Z.747086742c9049f1.dccfdbd9845f6c754dc7bfe9d83e72d34aa33993&lang=' + sourceLanguageCode + "-" + targetLangugaeCode + '&text='+args.input))
			if (data["code"] == 200) :
				filePath = path.abspath(envData["project"] + "/" + "web" + "/" + "word_" + targetLangugaeCode + ".properties")
				writeToFile(filePath, data['text'][0].encode('utf-8'))
		except Exception as e :
			print e

def localizeMe(args) :
	webLocalizer(args)