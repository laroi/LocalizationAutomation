#####################################################################
# Script to update master file
# Created By : Akbar <akbarali1klr@gmail.com>
# Created Date : 20-09-2014
#####################################################################

import utils

_envData = utils.getEnvData()
def updateMasterFile():
    print utils.readJson('../res/master.json')
updateMasterFile()

