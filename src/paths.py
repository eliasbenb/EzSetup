import os, re
from time import gmtime, strftime

current_time = strftime("%Y%m%d%H%M%S", gmtime())

base_path = '%s\\eliasbenb\\EzSetup' %  os.environ['APPDATA']
images_path = '%s\\eliasbenb\\EzSetup\\images' %  os.environ['APPDATA']
icon_path = images_path+'\\icon.ico'

temp_path = '%s\\eliasbenb\\EzSetup\\' %  (os.environ['TEMP'])
export_path = '%s\\eliasbenb\\EzSetup\\Export\\%s' %  (os.environ['TEMP'], current_time)
import_path = '%s\\eliasbenb\\EzSetup\\Import\\%s' %  (os.environ['TEMP'], current_time)

export_app_list_path = export_path+'\\app_list.txt'
export_background_path = export_path+'\\background.png'
export_files_path = export_path+'\\Files'

import_app_list_path = import_path+'\\app_list.txt'
import_background_path = import_path+'\\background.png'
import_files_path = import_path+'\\Files'

software_save_path = r'EzSetup Software\\'
files_save_path = r'EzSetup Files\\'
current_dir = os.getcwd()