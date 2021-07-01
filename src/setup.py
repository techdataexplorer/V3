# Created on June 30th 2021
# Reference: https://github.com/marcelotduarte/cx_Freeze/blob/main/cx_Freeze/samples/PyQt5/setup.py
import sys
from cx_Freeze import setup, Executable
# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"]}
# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"
setup(
    name = "TDX Desktop V3",
    version = "1.0.1",
    description = "This is TDX Desktop V3 1.0.1. Application is designed for distributing on windows.",
    options = {"build_exe": build_exe_options},
    executables = [Executable("TDX-Desktop-V3.py", base=base)]
)
