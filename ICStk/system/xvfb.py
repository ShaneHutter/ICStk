#!/usr/bin/env python
"""
ICStk.system.xvfb

    Methods for working with X Virtual Frame Buffer
"""


from .shell import shell

DEFAULT_SCREEN_WIDTH    = 1024
DEFAULT_SCREEN_HEIGHT   = 768


def createXvfb(
        display = int()                 ,
        width   = DEFAULT_SCREEN_WIDTH  ,
        height  = DEFAULT_SCREEN_HEIGHT ,
        ):
    """
    Create an X Virtual Frame buffer

    This method takes inegers as argumetns, and converts into usable strings
        i.e.
            display 12 will be conveted into ":12"
    Also, this over simplifies creation, nd is not intended to be robust

        display = virtual display number
    """
    return shell(
            "Xvfb :"        +
            str( display )  +
            " -screen 0 "   +
            str( width )    +
            "x"             +
            str( height )   +
            "x24"           ,
            )

