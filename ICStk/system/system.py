#!/usr/bin/env python
"""
ICStk.system

    A Set of methods for working with Linux/Unix/MacOS systems.
    May include Windows in the future.
"""

from .shell     import (
        shell       ,
        shellLines  ,
        )


## Encase functions in if statements to block importaion on wrong OS

def isfifo( checkFifo = str() ):
    """ Determine if a file is a fifo pipe """
    return shell( 
            "if [ -p \""        +
            checkFifo           +
            "\" ]; then exit; else exit 1 ; fi" ,
            )



def isfile( checkFifo = str() ):
    """ Determine if a file is a fifo pipe """
    return shell( 
            "if [ -f \""        +
            checkFifo           +
            "\" ]; then exit; else exit 1 ; fi" ,
            )



def isdir( checkFifo = str() ):
    """ Determine if a file is a fifo pipe """
    return shell( 
            "if [ -d \""        +
            checkFifo           +
            "\" ]; then exit; else exit 1 ; fi" ,
            )
