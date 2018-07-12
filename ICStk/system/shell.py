#!/usr/bin/env python
"""
ICStk.shell
    Functions for shell based operations

    Author:
        Shane Hutter
"""

from ..         import *
from os         import system
from os.path    import isfile
from platform   import system       as sysname
from shlex      import split        as slxsplit
from subprocess import (
        check_output    ,
        PIPE            ,
        Popen           ,
        STDOUT          ,
        )

## Constants
NO_EXTRA_LINE           = -1    # remove newline from shellLines


'''
Use $PATH
there should be an os method for environment variables
def findBin(binary):
    """ Return the location of an executable binary. """

    for binLocation in :
        if isfile(
                binLocation +
                binary
                ):
            return binLocation + binary
'''


def shell( command ):
    """ Execute shell command and return boolean based on success. """
    return not(
            bool(
                system(
                    command
                    )
                ) 
            )   



def shellLines( *args ):
    """
    Run a shell command, and return the output as lines.
    Pass extra arguments as commands to pipe data.
    """
    ARRAYS_START_AT_ZERO    = 1 

    if len( args ) - ARRAYS_START_AT_ZERO:
        #There is more than one Command
        pipedOutput = None
        for arg in enumerate( args ):
            if arg[ 
                    ENUMERATION_ITERATE_INDEX 
                    ] + ARRAYS_START_AT_ZERO == len( args ):
                # Final command
                # data piped in, return output as list of lines
                return check_output(
                        slxsplit(
                            arg[ ENUMERATION_VALUE_INDEX ]
                            )                           ,
                        stdin   = pipedOutput.stdout    ,
                        ).decode()[
                                :NO_EXTRA_LINE
                                ].split('\n')
            elif arg[ ENUMERATION_ITERATE_INDEX ]:
                # Middle commands
                # data piped in and out
                pipedOutput = Popen(
                        slxsplit(
                                
                            arg[ ENUMERATION_VALUE_INDEX ]
                            )                           ,
                        stdin   = pipedOutput.stdout    ,
                        stdout  = PIPE                  ,
                        )
            else:
                # First command
                # data piped out
                pipedOutput = Popen(
                        slxsplit(
                            arg[ ENUMERATION_VALUE_INDEX ]
                            )           ,
                        stdout  = PIPE  ,
                        )
    else:
        # There is only one command, do not pipe
        return check_output(
                slxsplit(
                    args[ ONLY_INDEX ]
                    )
                ).decode()[
                        :NO_EXTRA_LINE
                        ].split('\n')

def shellOut( *args ):
    """
    Run a shell command, and return the output in a single string.
    Pass extra arguments as commands to pipe data.
    """
    ARRAYS_START_AT_ZERO    = 1 
    if len( args ) - ARRAYS_START_AT_ZERO:
        #There is more than one Command
        pipedOutput = None
        for arg in enumerate( args ):
            if arg[ 
                    ENUMERATION_ITERATE_INDEX 
                    ] + ARRAYS_START_AT_ZERO == len( args ):
                # Final command
                # data piped in, return output as list of lines
                return check_output(
                        slxsplit(
                            arg[ ENUMERATION_VALUE_INDEX ]
                            )                           ,
                        stdin   = pipedOutput.stdout    ,
                        ).decode()
            elif arg[ ENUMERATION_ITERATE_INDEX ]:
                # Middle commands
                # data piped in and out
                pipedOutput = Popen(
                        slxsplit(
                            arg[ ENUMERATION_VALUE_INDEX ]
                            )                           ,
                        stdin   = pipedOutput.stdout    ,
                        stdout  = PIPE                  ,
                        )
            else:
                # First command
                # data piped out
                pipedOutput = Popen(
                        slxsplit(
                            arg[ ENUMERATION_VALUE_INDEX ] 
                            )           ,
                        stdout  = PIPE  ,
                        )
    else:
        # There is only one command, do not pipe
        return check_output(
                slxsplit(
                    args[ ONLY_INDEX ]
                    )
                ).decode()


        
def shellRaw( *args ):
    """
    Run a shell command, and return the raw output.
    Pass extra arguments as commands to pipe data.
    """
    ARRAYS_START_AT_ZERO    = 1 
    if len( args ) - ARRAYS_START_AT_ZERO:
        #There is more than one Command
        pipedOutput = None
        for arg in enumerate( args ):
            if arg[ 
                    ENUMERATION_ITERATE_INDEX 
                    ] + ARRAYS_START_AT_ZERO == len( args ):
                # Final command
                # data piped in, return output as list of lines
                return check_output(
                        slxsplit(
                            arg[ ENUMERATION_VALUE_INDEX ]
                            )                           ,
                        stdin   = pipedOutput.stdout    ,
                        )
            elif arg[ ENUMERATION_ITERATE_INDEX ]:
                # Middle commands
                # data piped in and out
                pipedOutput = Popen(
                        slxsplit(
                            arg[ ENUMERATION_VALUE_INDEX ]
                            )                           ,
                        stdin   = pipedOutput.stdout    ,
                        stdout  = PIPE                  ,
                        )
            else:
                # First command
                # data piped out
                pipedOutput = Popen(
                        slxsplit(
                            arg[ ENUMERATION_VALUE_INDEX ] 
                            )           ,
                        stdout  = PIPE  ,
                        )
    else:
        # There is only one command, do not pipe
        return check_output(
                slxsplit(
                    args[ ONLY_INDEX ]
                    )
                )

def shellErr( *args ):
    """
    Run a shell command, and return the error output.
    Pass extra arguments as commands to pipe data.
    Final command will return error
        i.e.
            2>&1
    """
    ARRAYS_START_AT_ZERO    = 1 
    if len( args ) - ARRAYS_START_AT_ZERO:
        #There is more than one Command
        pipedOutput = None
        for arg in enumerate( args ):
            if arg[ 
                    ENUMERATION_ITERATE_INDEX 
                    ] + ARRAYS_START_AT_ZERO == len( args ):
                # Final command
                # data piped in, return output as list of lines
                return Popen(
                        slxsplit(
                            arg[ ENUMERATION_VALUE_INDEX ]
                            )                           ,
                        stdin   = pipedOutput.stdout    ,
                        stdout  = PIPE                  ,
                        stderr  = STDOUT                ,
                        ).communicate()[ ONLY_INDEX ].decode()
            elif arg[ ENUMERATION_ITERATE_INDEX ]:
                # Middle commands
                # data piped in and out
                pipedOutput = Popen(
                        slxsplit(
                            arg[ ENUMERATION_VALUE_INDEX ]
                            )                           ,
                        stdin   = pipedOutput.stdout    ,
                        stdout  = PIPE                  ,
                        )
            else:
                # First command
                # data piped out
                pipedOutput = Popen(
                        slxsplit(
                            arg[ ENUMERATION_VALUE_INDEX ] 
                            )           ,
                        stdout  = PIPE  ,
                        )
    else:
        # There is only one command, do not pipe
        return Popen(
                slxsplit(
                    args[ ONLY_INDEX ]
                    )               ,
                stdout  = PIPE      ,
                stderr  = STDOUT    ,
                ).communicate()[ ONLY_INDEX ].decode()



def shellErrLines( *args ):
    """
    Run a shell command, and return the error output.
    Pass extra arguments as commands to pipe data.
    Final command will return error
        i.e.
            2>&1
    """
    ARRAYS_START_AT_ZERO    = 1 
    if len( args ) - ARRAYS_START_AT_ZERO:
        #There is more than one Command
        pipedOutput = None
        for arg in enumerate( args ):
            if arg[ 
                    ENUMERATION_ITERATE_INDEX 
                    ] + ARRAYS_START_AT_ZERO == len( args ):
                # Final command
                # data piped in, return output as list of lines
                return Popen(
                        slxsplit(
                            arg[ ENUMERATION_VALUE_INDEX ]
                            )                           ,
                        stdin   = pipedOutput.stdout    ,
                        stdout  = PIPE                  ,
                        stderr  = STDOUT                ,
                        ).communicate()[ ONLY_INDEX ].decode().split( "\n" )[ :NO_EXTRA_LINE ]
            elif arg[ ENUMERATION_ITERATE_INDEX ]:
                # Middle commands
                # data piped in and out
                pipedOutput = Popen(
                        slxsplit(
                            arg[ ENUMERATION_VALUE_INDEX ]
                            )                           ,
                        stdin   = pipedOutput.stdout    ,
                        stdout  = PIPE                  ,
                        )
            else:
                # First command
                # data piped out
                pipedOutput = Popen(
                        slxsplit(
                            arg[ ENUMERATION_VALUE_INDEX ] 
                            )           ,
                        stdout  = PIPE  ,
                        )
    else:
        # There is only one command, do not pipe
        return Popen(
                slxsplit(
                    args[ ONLY_INDEX ]
                    )               ,
                stdout  = PIPE      ,
                stderr  = STDOUT    ,
                ).communicate()[ ONLY_INDEX ].decode().split( "\n" )[ :NO_EXTRA_LINE ]


def shellPid( command ):
    """
        Launch and background a process returning an integeral PID
    """
    return Popen(
            slxsplit( command )
            ).pid



def sshLines( 
        command = ""                , 
        ip      = ""                , 
        port    = DEFAULT_SSH_PORT  ,
        ):
    """
    SSH into IP and execute command, return as lines in list
    """
    return shellLines(
            "ssh -o StrictHostKeyChecking=no "  +
            ip  +   ' -p'       +   str(port)   +
            " -T '" + command   + "'"           ,
            )



## Mac Specific methods
if sysname() == "Darwin":
    def shellCopy( command ):
        """
        Run a shell command and divert stdout to clipboard
        """
        try:
            return shell(
                    "echo \""               +
                    check_output(
                        slxsplit(
                            command         ,
                            )
                        ).decode()[ 
                            :NO_EXTRA_LINE 
                            ]               +
                    "\" | pbcopy"           ,
                    )
        except:
            return False
