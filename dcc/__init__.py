"""
Django Contributing Commons.

Django-CC makes contributing to PyPI packages a breeze.
It will download the package source code and sets you up
so you can focus on developing amazing new features.
"""
from distutils.spawn import find_executable

import os

VERSION = (0, 1, 0)

__version__ = '.'.join(str(i) for i in VERSION)
__author__ = 'Johannes Hoppe'
__licence__ = """This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>"""

HUB = find_executable('hub')
PIP = find_executable('pip')
VIRTUALENV = find_executable('virtualenv')
SOURCE = find_executable('source')
BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class DjangoCCError(Exception):
    """dcc runtime error."""

    pass