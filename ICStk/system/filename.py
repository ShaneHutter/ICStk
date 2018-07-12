#/usr/env/bin python
"""
ICStk.system.filename
    
    Modules to assist in naming files.
"""


from ..     import *
from sys    import (
        exit            ,
        version_info    ,
        )



# Global Constant declaration
DEBUG_MODE  = True
PYTHON3     = 3


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



def padZeros(
        currentNumber   = int() ,
        maxNumber       = int() ,
        ):
    """
        Takes the current and maximum number of a sequence and returns a string with padded zeros
            i.e.
                current = 3
                max     = 333
                output  = "003"
    """
    zeros = str()
    for zero in range(
            len(
                str( maxNumber )
                ) - len(
                    str( currentNumber )
                    )
                ):
        zeros += "0"
    return zeros + str( currentNumber )

