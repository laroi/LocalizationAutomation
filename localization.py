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

from modules import master
#
#parsing arguments
#
parser = argparse.ArgumentParser(description = "Updates Language File") 
parser.add_argument("-t", "--appType", help = "type of the application need to be updated eg: android, ios or web", nargs = '+', required = True)
parser.add_argument("-v", "--variable", help = "name of the variable to be added", required = True)
parser.add_argument("-i", "--input", default = "", help = "Input string", required = True)
parser.add_argument("-e", "--existing", default = "", help = "Under the existing header you want to add the translation eg:- log_in_page")
parser.add_argument("-n", "--new", default = "", help = "Under the new header you want to add the translation eg:- log_in_page")
args = parser.parse_args()

# Example command to run
# python localization.py  -t "android" -v "m_btn_login" -i "login" -e "login_page"
# python localization.py  -t "ios" -v "m_btn_login" -i "login" -e "login_page"
# python localization.py  -t "web" -v "m_btn_login" -i "login" -e "login_page"

print "-----Localization-----";
master.updateMasterFile(args);