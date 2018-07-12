#!/usr/bin/env python
"""
ICStk module
    Intentropy Creative Studios toolkit

    Contributing Authors:
        Shane Hutter
"""

## Indexing constants
# Index values for enumerating iterable data types
ENUMERATION_ITERATE_INDEX   = 0
ENUMERATION_VALUE_INDEX     = 1

# Indexes for converting list to dictionaries
KEY_INDEX   = 0
VALUE_INDEX = 1

# When there only one index, you want the first index, or all but first index [ 1: ]
FIRST_INDEX     = ONLY_INDEX    = 0
NO_FIRST_INDEX  = 1
# Final index used as [ -1: ]
FINAL_INDEX     = -1

# Exit code for errorless exit
CLEAN = 0


# Python version testing
PYTHON3 = 3
PYTHON2 = 2


## Port constants
# SSH
DEFAULT_SSH_PORT    = 22

# Mail
SMTP_PORT   = 25

# Web
HTTP_PORT   = 80
HTTPS_PORT  = 443


# Delimiters
NEW_LINE    = "\n"
