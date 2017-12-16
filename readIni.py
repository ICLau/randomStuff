# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 22:54:40 2017

@author: Isaac

*** NOTE: requires ConfigObj
***   use: pip install configobj 
***   to acquire and install it
"""

from configobj import ConfigObj

iniCached = False
config = []
iniFilename = 'config.ini'

# =============================================================================
def isCached ():
    global iniCached
    return iniCached

# =============================================================================
def readINI (filename = 'config.ini'):
    if (isCached()): return

    global config
    config = ConfigObj(filename)
    
    global iniCached
    iniCached = True
    
    global iniFilename
    iniFilename = filename

    print ('** Not cached, loaded INI file:', iniFilename)

    
# =============================================================================
def get_sectionNames():
    if (~isCached()):
        readINI (iniFilename)  # need to somehow capture the ini filename somewhere

    return True, config.sections

# =============================================================================
def get_sectionKeys(sName):
    if (~isCached()):
        readINI (iniFilename)
    
    sKeys = None
    if (sName not in config.sections): return False, None
    
    sSection = config[sName]
    sKeys = [k for k in sSection]

    return True, sKeys

# =============================================================================
def get_sectionKeyValues (sName, kName):
    bSuccess, sKeys = get_sectionKeys (sName)

    if (~bSuccess): return False, None
    
    if (kName not in sKeys): return False, None
    
    return True, config[sName][kName]

# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================


readINI()
bool_Success, SectionNameList = get_sectionNames ()
print ('get_sectionNames() returns', bool_Success)
if (bool_Success): 
    print ('* sectionNames are:', SectionNameList)


