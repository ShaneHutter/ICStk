#/usr/env/bin python
"""
ICStk.visual.imagemagick
"""

from ..                 import *
from ..system.datatype  import strConvert
from ..system.shell     import (
        shell       ,
        shellOut    ,
        )
from ..system.system    import isdir
from sys                import (
        exit            ,
        version_info    ,
        )



# Global Constant declaration
DEBUG_MODE  = True
PYTHON3     = 3


FFPROBE_STREAMS_KEY     = "streams"
FFPROBE_FORMAT_KEY      = "format"


# Global variable declaration
python3     = False



# Detect python version
if version_info.major == PYTHON3:
    python3 = True


# Python version specific imports`
if python3:
    # imports for Python 3.x
    pass
else:
    # Imports for Python 2.x
    pass


# Check for ImageMagick, and exit if not installed
def screenCapture(
        output  = str()     ,
        width   = int()     ,
        height  = int()     ,
        x       = 0         ,
        y       = 0         ,
        display = ":0.0"    ,
        ):
    """
        Use import to screen capture

        This seems to be the fastest way to capture a small area of the screen
    """
    return shell(
            "import -window root -crop "        +
            str( width )                        +
            "x"                                 +
            str( height )                       +
            "+"                                 +
            str( x )                            +
            "+"                                 +
            str( y )                            +
            " -display "                        +
            display                             +
            " "                                 +
            output                              ,
            )

