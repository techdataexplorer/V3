#!/usr/bin/env python3
# coding: utf-8

import os
import warnings
import sys
from distutils.core import setup
import py2exe

option = {
    'compressed': 1,
    'optimize': 2,
    'bundle_files': 1,
}

setup(
    options = {
        'py2exe': option,
    },
    console = [
        {'script': 'main.py'}
    ],
    zipfile = None,
)


# Write a script to handle lib dependencies
# for each OS env
# get os platform
# Used for distribution / setup
# os_type = platform.system()

# DATA_FILES = []

# setup(
#     name='TDX Desktop',
#     version='1.1.0',
#     license='',
#     description=,''
#     include_package_data=True,
#     url='',
#     author='Che Blankenship',
#     author_email='che.blankenship@utdallas.edu',
#     maintainer='Che Blankenship',
#     maintainer_email='che.blankenship@utdallas.edu',
#     packages=(
#         'TDX-Desktop', 'TDX-Desktop.constants',
#         'TDX-Desktop.scripts', 'TDX-Desktop.gui',
#     ),
#     # data_files=DATA_FILES,
#     entry_points={
#         'console_scripts': [
#             'persepolis = persepolis.__main__'
#         ]
#     }
# )
