#/usr/env/bin python
"""
ICStk.system.datatype
    
    This module provides extra methods for working with datatypes in Python
"""


from ..     import *
from sys    import (
        exit            ,
        version_info    ,
        )


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


def strConvert( 
        input = str()
        ):
    """
        This method takes a string for input, and attempts to convert it to either a float/int or evaluate it.
        If conversion fails, input remains a string as is passed back out of the method.
    """
    if '.' in input:
        # Input may be a floating point, or an equation
        try:
            # Try to convert to floating point
            return float( input )
        except:
            try:
                # Try to evalutae as an equation
                return eval( input )
            except:
                # If all else fails return as original string
                return input
    else:
        # Input may be an integer or an equation
        try:
            # Try to convert to an integer
            return int( input )
        except:
            try:
                # Try to evaluate as an equation
                return eval( input )
            except:
                # If all else fails return as original string
                return input
