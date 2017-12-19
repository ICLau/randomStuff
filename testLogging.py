# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 09:56:27 2017

@author: Isaac
"""
import logging
import readIni as ini
from datetime import datetime as dt

# basicConfig() can only be called ONCE!!!
logFilename = dt.today().strftime('%Y-%m-%d') + '.log'
bInit = False
logLevel = logging.INFO     # default at INFO level
logWarning = None
logInfo = None
logDebug = None
logCritical = None

logFunc = {logging.DEBUG    : logging.debug,
           logging.INFO     : logging.info,
           logging.WARN     : logging.warning,
           logging.CRITICAL : logging.critical}

_iWARNING = logging.WARNING
_iINFO = logging.INFO
_iDEBUG = logging.DEBUG
_iCRITICAL = logging.CRITICAL

logLevelDict = {'DEBUG'    : logging.DEBUG,
                'INFO'     : logging.INFO,
                'WARNING'  : logging.WARNING,
                'CRITICAL' : logging.CRITICAL}

# =============================================================================
def isInit ():
    return bInit

# =============================================================================
def logMsg (module, level, message):
    if (level >= logLevel):
        oMsg = "[{0}]: {1}".format(module, message)
        logFunc[level](oMsg)

# =============================================================================
def initLog():
    if (isInit() == False):
        # should get the config.ini setting 
        logging.basicConfig(filename=logFilename, 
                            filemode='a+', 
                            level=logLevel, 
                            format='%(asctime)s %(message)s')    # default date/time display (ISO8601)
        print ('*** logFilename="{0}" initialized.'.format(logFilename))
        
        global bInit
        bInit = True

    global logWarning
    logWarning = logging.warning
    
    global logInfo
    logInfo = logging.warning
    
    global logDebug
    logDebug = logging.debug
    
    global logCritical
    logCritical = logging.critical

# =============================================================================

bOK, sLogLevel = ini.get_sectionKeyValues ("logging", "logLevel")
if (bOK == True and sLogLevel != None):
    logLevel = logLevelDict[sLogLevel]

print ('*** logLevel = {0}'.format(logLevel))
initLog()
logMsg (__name__, logging.WARN, "warning message")

if (__name__ == '__main__'):

    logMsg ('[module1]', logging.WARN, "warning message")
    logMsg ('[module2]', logging.DEBUG, "debug message")
    logMsg ('[module3]', logging.INFO, "info message")
    logMsg ('[module4]', logging.CRITICAL, "critical message")

