import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "guifoo",
    version = "0.1",
    description = "My GUI application!",
    #options = {"build_exe": build_exe_options},
    executables = [Executable("BMI2.py", base=base)]
)
import sys
from cx_Freeze import setup,Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name = 'Binary',
    version = '1.0',
    description = 'Binary conversion',
    executables =[Executable('bai44.py',base = base)] 
)