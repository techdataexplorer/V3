# Created on June 30th 2021
# Reference: https://github.com/marcelotduarte/cx_Freeze/blob/main/cx_Freeze/samples/PyQt5/setup.py
# A simple setup script to create an executable using PyQt5. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt5app.py is a very simple type of PyQt5 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application
import sys
from cx_Freeze import setup, Executable
base = None
if sys.platform == "win32":
    base = "Win32GUI"
options = {"build_exe": {"includes": "atexit"}}
executables = [Executable("main.py", base=base)]
setup(
    name="TDX Desktop",
    version="1.0.1",
    description="V3 TDX Desktop",
    options=options,
    executables=executables,
)
