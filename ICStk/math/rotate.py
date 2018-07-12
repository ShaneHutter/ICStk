#!/usr/bin/env python
"""
ICStk.math.rotate
"""


from math   import (
        radians ,
        cos     ,
        sin     ,
        )



def rotatePoint(
        centerPoint ,
        point       ,
        angle       ,
        ):
    # counter clockwise point rotation
    # Point needs to be a tuple, returns a tuple ( x , y )
    angle = radians( angle )
    rotated = (
            point[ 0 ] - centerPoint[ 0 ]   , 
            point[ 1 ] - centerPoint[ 1 ]   ,
            )
    rotated = (
            rotated[ 0 ]        * 
            cos( angle )   -
            rotated[ 1 ]        * 
            sin( angle )   , 
            rotated[ 0 ]        *
            sin( angle )   +
            rotated[ 1 ]        *
            cos( angle )   ,
            )
    return (
            rotated[ 0 ]        +
            centerPoint[ 0 ]    , 
            rotated[ 1 ]        +
            centerPoint[ 1 ]    ,
            )
