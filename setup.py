#!/usr/bin/env python
"""
    Intentropy Creative Studios toolkit, setup file
"""

from distutils.core import setup

setup(
        name                = 'python-ICStk'                                        ,
        version             = '0.0.2'                                               ,
        author              = 'Shane Hutter'                                        ,
        author_email        = 'shane.hutter86@gmail.com'                            ,
        description         = 'Intentropy Creative Studios toolkit Python module'   ,
        long_description    = open( 'README.md' ).read()                               ,
        license             = open( 'LICENSE' ).read()                              ,
        packages            = [ 
            'ICStk'             , 
            'ICStk.math'        ,
            'ICStk.system'      ,
            'ICStk.visual'      ,
            ]                                                                       ,
        )
