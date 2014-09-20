#####################################################################
# Script to update master file
# Created By : Akbar <akbarali1klr@gmail.com>
# Created Date : 20-09-2014
#####################################################################

# Importing user created modules
import utils
import android
import ios
import web

def checkType(args) :
	appType = args.appType;
	print appType;

	if ("android" in appType) :
		print "android";
		#android.localizeMe(args);

	if ("ios" in appType) :
		print "ios";
		ios.localizeMe(args)

	if ("web" in appType) :
		print "web";
		#web.localizeMe(args)

def updateLanguageFile(args) :
	checkType(args);

def updateMasterFile(args) :
	updateLanguageFile(args);
