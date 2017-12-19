# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 15:59:31 2017

@author: Isaac
"""
import testLogging as log

log.logMsg (__name__, log._iWARNING, "a warning message")
log.logMsg (__name__, log._iINFO, "an info message")
log.logMsg (__name__, log._iDEBUG, "a debug message")
log.logMsg (__name__, log._iCRITICAL, "a critical message")