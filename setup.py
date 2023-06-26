import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    # base="Win64GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "IVS System",
    version = "1.0",
    description = "Intelligent video surveillance system",
    author = "Nathaniel Bekalu",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
