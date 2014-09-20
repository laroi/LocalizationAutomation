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
jsonData = {}
locale = {}
platform = {}
def updateMasterFile(variable, section, newSection, description, tag, platforms, languages):
    if(not variable):
        print "Variable not found"
        return False;
    if(not section):
        print "section not found"
        return False;
    if(not tag):
        print "tag not found"
        return False;

    masterData = utils.readJson('../res/master.json')
    if (newSection):
        jsonData[section] = {variable:{'locale':{}, 'platform':{}}}
    else:
        if(masterData[section]):
            jsonData[section] = {variable:{'locale':{}, 'platform':{}}}
    if(languages and len(languages) > 0):
        for lan in laguages:
            locale [lan] = ""
    else:
        for lan in _envData["target"]:
            locale [lan] = ""
    if(platforms and len(platforms) > 0):
        for plat in platforms:
            platform [plat] = True
    else:
        for plat in _envData["platform"]:
            platform [plat] = True
    jsonData[section][variable]['locale'] = locale
    jsonData[section][variable]['platform'] = platform
    print jsonData

updateMasterFile("m_login", "log in", True, "this is test", "login", False, False);
