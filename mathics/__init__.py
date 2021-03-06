# -*- coding: utf8 -*-

import mathics.core # load core to init sage

#try:
#    from sage import all
#    # load Sage right on start of Mathics to prevent error in mathicsserver:
#    # "ValueError: signal only works in main thread"
#except ImportError:
#    pass

#import sys
#sys.setrecursionlimit(3000)

def get_version():
    version = {}
    
    from mathics.optional import sage_version
    import sympy
    import mpmath
    import gmpy
    try:
        import django
        from django.conf import settings
        version['mathics'] = settings.VERSION
        version['django'] = django.get_version()        
    except ImportError:
        from mathics import settings
        version['mathics'] = settings.VERSION
    if sage_version is not None:
        version['sage'] = sage_version
    version['sympy'] = sympy.__version__
    version['mpmath'] = mpmath.__version__
    version['gmpy'] = gmpy.version()
    return version

def get_version_string(is_server, newlines=False):
    version = get_version()
    result = []
    result.append(u"Mathics %s" % version['mathics'])
    if 'sage' in version:
        result.append(u"on %s" % version['sage'])
    libs = []
    if 'django' in version and is_server:
        libs.append("Django %s" % version['django'])
    libs += ["SymPy %s" % version['sympy'], "mpmath %s" % version['mpmath'],
        "GMPY %s" % version['gmpy']]
    result.append(u"using %s" % ", ".join(libs))
    return ("\n" if newlines else " ").join(result)

def print_version(is_server):
    print "\n" + get_version_string(is_server, newlines=True)
    
def print_license():
    print u"""
Copyright (C) 2011 Jan Pöschko
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
See the documentation for the full license.
"""