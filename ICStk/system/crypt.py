#!/usr/bin/env python
"""
ICStk.crypt

    A collection of methods dealing with encryption.

    This module will depend on some optional dependancies:
        gpg
        openssl

    Methods may return None or False if checked optional dependacy is not on the system.
"""

from .shell     import (
        shellLines  ,
        shellOut    ,
        shellRaw    ,
        )
from os         import environ
from os.path    import isfile


'''
NOTES:
    * GPG
        ascii encrypt file:
            gpg -r [recipient] -ae < [file]

        ascii encrypt string:
            echo [string] | gpg -r [recipient] -ae

        ascii decrypt a string
            echo [string] | gpg -dr [ recipient ]
        
'''


## Check for optional dependancies
binLocations = environ[ 'PATH' ].split( ':' )
dependancies = {
        "gpg":      bool()  ,
        "openssl":  bool()  ,
        }
for dependancy in dependancies:
    for location in binLocations:
        if isfile( location + "/" + dependancy ):
            dependancies[ dependancy ] = True



### GnuPG methods

'''
    Notes:  build a function using shellRaw to utilize gpg via raw binary data
            not using ascii armor
'''


if dependancies[ "gpg" ]:
    """
        These methods require gpg
    """
    def encryptString( 
            data        = str()     ,
            recipient   = str()     ,
            ):
        """
            Encrypt a string and return its encrytped output as 
            ascii armored text
            Use keypairs, and pass the recipient as argument.
        """
        return shellOut(
                "echo \""   +
                data        +
                "\""        ,
                "gpg -aer " +
                recipient   ,
                )
          

    def decryptString( 
            data        = str()     ,
            recipient   = str()     ,
            ):
        """
            Encrypt a string and return its encrytped output as 
            ascii armored text
            Use keypairs, and pass the recipient as argument.
        """
        if recipient:
            return shellLines(
                    "echo \""   +
                    data        +
                    "\""        ,
                    "gpg -qdr " +
                    recipient   ,
                    )
        else:
            # Raise no recipient error
            return



### OpenSSL methods
if dependancies[ "openssl" ]:
    """
        These methods require openssl
    """
    pass



