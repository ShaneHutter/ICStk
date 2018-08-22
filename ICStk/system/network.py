#/usr/env/bin python
"""
ICStk.system.network

    Methods and classes for working with networks.
"""

from ..                 import *
from .shell             import shellPid
from os                 import kill
from signal             import SIGTERM
from socket             import gethostname



class SshTunnel:
    """
        Instatiate an SSH Tunnel
    """

    AVAILABLE_KWARGS = (
            "remoteUser"  , "remoteSshPort"   , "localPort"     ,
            )

    # ssh -p PORT -NL LOCAL_PORT:localhost:REMOTE_PORT -l REMOTE_USER REMOTE_HOST
    SSH_TUNNEL_COMMAND  = "ssh {0} -NL {1}:localhost:{2} {3} {4}"

    def __init__(
            self                ,
            remoteHost  = str() ,
            remotePort  = int() ,
            **kwargs
            ):
        """
            Initialize the class
        """

        ## Check kwargs
        # Check for bogus arguments
        for argument in kwargs:
            if argument not in self.AVAILABLE_KWARGS:
                self.close( NotImplementedError )
        
        # localPort
        if "localPort" not in kwargs:
            # Local port mirrors remote port
            self.localPort  = str( remotePort )
        else:
            # Ensure passed value is the correct type
            if type( 
                    kwargs[ "localPort" ] 
                    ) == str or type(
                        kwargs[ "localPort" ]
                        ) == int:
                self.localPort  = str(
                        kwargs[ "localPort" ]
                        )
            else:
                self.close( TypeError )

        # remoteSshPort
        if "remoteSshPort" not in kwargs:
            # Use default ssh port for remote host
            self.remoteSshPort  = str()
        else:
            # Ensure passed value is the correct type
            if type( 
                    kwargs[ "remoteSshPort" ] 
                    ) == str or type( 
                        kwargs[ "remoteSshPort" ] 
                        ) == int:
                self.remoteSshPort  = "-p{0}".format(
                        str(
                            kwargs[ "remoteSshPort" ]
                            )
                        )
            else:
                self.close( TypeError )

        # remoteUser
        if "remoteUser" not in kwargs:
            self.remoteUser = str()
        else:
            # Ensure passed value is the correct type
            if type(
                    kwargs[ "remoteUser" ]
                    ) == str:
                self.remoteUser = "-l{0}".format(
                        str(
                            kwargs[ "remoteUser" ]
                            )
                        )

        self.sshTun = shellPid(
                self.SSH_TUNNEL_COMMAND.format(
                    self.remoteSshPort  ,
                    self.localPort      ,
                    remotePort          ,
                    self.remoteUser     ,
                    remoteHost          ,
                    )
                )


    def close( 
            self            ,
            error   = None  ,
            ):
        """
            Clean up
        """
        kill( self.sshTun , SIGTERM )
        if error:
            raise error
        return



    def __enter__( self ):
        return self



    def __exit__(
            self        ,
            exc_type    ,
            exc_value   ,
            traceback   ,
            ):
        return self.close()
