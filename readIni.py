# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 22:54:40 2017

@author: Isaac

*** NOTE: requires ConfigObj
***   use: pip install configobj 
***   to acquire and install it
"""
# =============================================================================
# import numpy as np
# 
# ini = np.loadtxt('config.ini', 
#                  dtype={'names':('key', 'value'),
#                         'formats':('S100', 'S255')}, 
#                  comments='!', 
#                  delimiter='=',
#                  converters = {0: lambda s: s.strip(),
#                                1: lambda s: s.strip()})
# 
# ini2 = np.genfromtxt('config.ini', dtype=[('myKey','S100'),
#                                           ('myValue', 'S255')], delimiter='=', comments='!' )
# 
# =============================================================================

# the test config.ini is in the same folder

from configobj import ConfigObj

filename = 'config.ini'
config = ConfigObj(filename)

sInputSection = 'inputs'
sUsersSection = 'Users'
sCleansedDataSection = 'CleansedData'
sBarSection = 'BarGraph'

InputSection = config[sInputSection]
UsersSection = config[sUsersSection]
CleansedDataSection = config[sCleansedDataSection]
BarSection = config[sBarSection]


# for removeusers, detect if the 1st and/or last character is '*'.
# if so, remove them and conduct a substring search on user
# if no '*' detected (1st and last char), then do an exact match 

user1 = 'Gerald Lee'
user2 = 'abc Gerald Lee'
user3 = 'Gerald Lee abc'
user4 = 'abc Gerald Lee def'

user5 = 'Epic'
user6 = 'aEpic'
user7 = 'epicB'
user8 = 'Epik'

print ('config.keys:')
for s in config.sections:
    sName = s
    print (sName)

sectionKeys = config.sections

print ('is', sUsersSection, 'in', sectionKeys, ':', (sUsersSection in sectionKeys))
print ('is abc in', sectionKeys, ':', ('abc' in sectionKeys))
print ('is users in', sectionKeys, ':', ('users' in sectionKeys))

print ('*'*10)
for s in UsersSection:
    print ('UserSection key name =', s)
    sValue = UsersSection[s]
    print ('   value =', sValue)


