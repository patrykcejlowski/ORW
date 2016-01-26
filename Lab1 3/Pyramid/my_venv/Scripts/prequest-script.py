#!C:\Users\Basia\Desktop\PePE\Pyramid\my_venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyramid==1.6','console_scripts','prequest'
__requires__ = 'pyramid==1.6'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pyramid==1.6', 'console_scripts', 'prequest')()
    )
