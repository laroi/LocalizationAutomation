#####################################################################
# Script to update Language Files
# Created By : Akbar <akbarali1klr@gmail.com>
# Created Date : 09-08-2014
#####################################################################

#
#imports
#
import argparse

## User defined modules
from modules import android
from modules import ios
from modules import web

#
#parsing arguments
#
parser = argparse.ArgumentParser(description = "Updates Language File")
parser.add_argument("-t", "--appType", help = "type of the application need to be updated eg: android, ios or web", required = True)
parser.add_argument("-v", "--variable", help = "name of the variable to be added", required = True)
parser.add_argument("-i", "--input", default = "", help = "Input string", required = True)
parser.add_argument("-e", "--existing", default = "", help = "Under the existing header you want to add the translation eg:- log_in_page")
parser.add_argument("-n", "--new", default = "", help = "Under the new header you want to add the translation eg:- log_in_page")
args = parser.parse_args()

## Check which type of files need to be update, and update respective files
def checkType() :
    type = args.appType.lower();
    
    if (type == "android") :
        print ("Updating .xml files")
        android.localizeMe(args)
    
    elif (type == "ios") :
        print ("Updating .strings files")
        ios.localizeMe(args)
    
    elif (type == "web") :
        print ("Updating .properties files")
        web.localizeMe(args)
    
    else :
        print ("Only android ios or web is supported, Please reverify your appType");

checkType()