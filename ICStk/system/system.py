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

# Perhaps have a method return a dictionary of booleans for eachg type?
#   as well as individual calls for simplicity on some
#       i.e.  isfifo, issocket, issymlink, isblkdev, ischardev, etc...
#  Maybe just an attribute distionary for attribute bools, and a type key that specifies fifo
#   socket, blkdev, etc...
#       Becuae these cant be both
'''
Shell File test operators
-e
file exists

-a
file exists

This is identical in effect to -e. It has been "deprecated," [1] and its use is discouraged.

-f
file is a regular file (not a directory or device file)

-s
file is not zero size

-d
file is a directory

-b
file is a block device


-c
file is a character device

-p
file is a pipe

-h
file is a symbolic link

-L
file is a symbolic link

-S
file is a socket

-t
file (descriptor) is associated with a terminal device

This test option may be used to check whether the stdin [ -t 0 ] or stdout [ -t 1 ] in a given script is a terminal.

-r
file has read permission (for the user running the test)

-w
file has write permission (for the user running the test)

-x
file has execute permission (for the user running the test)

-g
set-group-id (sgid) flag set on file or directory

If a directory has the sgid flag set, then a file created within that directory belongs to the group that owns the directory, not necessarily to the group of the user who created the file. This may be useful for a directory shared by a workgroup.

-u

set-user-id (suid) flag set on file

A binary owned by root with set-user-id flag set runs with root privileges, even when an ordinary user invokes it. [2] This is useful for executables (such as pppd and cdrecord) that need to access system hardware. Lacking the suid flag, these binaries could not be invoked by a non-root user.

-k
sticky bit set

Commonly known as the sticky bit, the save-text-mode flag is a special type of file permission. If a file has this flag set, that file will be kept in cache memory, for quicker access. [3] If set on a directory, it restricts write permission. Setting the sticky bit adds a t to the permissions on the file or directory listing. This restricts altering or deleting specific files in that directory to the owner of those files.

-O
you are owner of file

-G
group-id of file same as yours

-N
file modified since it was last read

f1 -nt f2
file f1 is newer than f2

f1 -ot f2
file f1 is older than f2

f1 -ef f2
files f1 and f2 are hard links to the same file

!
"not" -- reverses the sense of the tests above (returns true if condition absent).
'''

def issocket( 
        checkSocket = str() 
        ):
    """
        Determine if file is a Unix Socket
    """
    return shell( 
            "if [ -S \""        +
            checkSocket           +
            "\" ]; then exit; else exit 1 ; fi" ,
            )

def isfifo( 
        checkFifo = str() 
        ):
    """ 
        Determine if a file is a fifo pipe 
    """
    return shell( 
            "if [ -p \""        +
            checkFifo           +
            "\" ]; then exit; else exit 1 ; fi" ,
            )



def isfile( 
        checkFile = str() 
        ):
    """ 
        Determine if a file is a fifo pipe """
    return shell( 
            "if [ -f \""        +
            checkFile           +
            "\" ]; then exit; else exit 1 ; fi" ,
            )



def isdir( 
        checkDir = str() 
        ):
    """ 
        Determine if a file is a fifo pipe 
    """
    return shell( 
            "if [ -d \""        +
            checkDir           +
            "\" ]; then exit; else exit 1 ; fi" ,
            )
