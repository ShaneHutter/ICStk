#/usr/env/bin python
"""
ICStk.art.audio
    ICStk module for creating art with sound
"""


from .      import *
from sys    import (
        exit            ,
        version_info    ,
        )


# Detect python version
python3     = False
if version_info.major == PYTHON3:
    python3 = True


# Python version specific imports`
if python3:
    # imports for Python 3.x
    pass
else:
    # Imports for Python 2.x
    pass
