#####################################################################
# Script to update master file
# Created By : Akbar <akbarali1klr@gmail.com>
# Created Date : 20-09-2014
#####################################################################

import utils
########################################################################################################################
#
#params : variable    => name of the variable to be used in app eg - m_login,
#         section     => under which section the string comes eg:- Login Page,
#         newSection  => if user wants to create new section 
#         description => where is the string used exactly,
#         platforms   => in whcih are platform need the translation defaults to ['android' , 'ios', 'web'], 
#         languages   => in which all languages you need this translation defaluts to ['dutch' , 'turkish', 'german'],
#         tag         => something to filter the strings  
#
#########################################################################################################################

_envData = utils.getEnvData()
jsonData = ""
def updateMasterFile(variable, section, newSection, description, platforms, languages, tag):
    if(!variable):
        print "Variable not found"
        return false;
    if(!section):
        print "section not found"
        return false;
    if(!tag):
        print "tag not found"
        return false;

    masterData = utils.readJson('../res/master.json')
    if (newSection):
        
    

updateMasterFile()

