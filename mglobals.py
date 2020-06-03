from pathlib import Path, PureWindowsPath
import os, platform

_platform_ = platform.system()


if _platform_ == 'Windows':
    base_path = PureWindowsPath('%s\\eliasbenb\\EzSetup' %  os.environ['APPDATA'])
    images_path = PureWindowsPath('%s\\eliasbenb\\EzSetup\\images' %  os.environ['APPDATA'])
else:
    base_path = Path('%s/eliasbenb/EzSetup' % os.environ['HOME'])
    images_path = Path('%s/eliasbenb/EzSetup/images' % os.environ['HOME'])

save_path = 'EzSetup Downloads'
app_list_path = base_path/'app_list.txt'
icon_path = str(images_path/'icon.ico')