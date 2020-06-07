import os, re
from time import gmtime, strftime

current_time = strftime("%Y%m%d%H%M%S", gmtime())

base_path = '%s\\eliasbenb\\EzSetup' %  os.environ['APPDATA']
images_path = '%s\\eliasbenb\\EzSetup\\images' %  os.environ['APPDATA']
icon_path = images_path+'\\icon.ico'

export_path = '%s\\eliasbenb\\EzSetup\\Export\\%s' %  (os.environ['TEMP'], current_time)

app_list_path = export_path+'\\app_list.txt'
background_path = export_path+'\\background.png'
files_path = export_path+'\\Files'

save_path = 'EzSetup Downloads'