import os, re
from time import gmtime, strftime

current_time = strftime("%Y%m%d%H%M%S", gmtime())


permBasePath = '%s\\eliasbenb\\EzSetup' %  os.environ['APPDATA']
permImagesPath = '%s\\eliasbenb\\EzSetup\\images' %  os.environ['APPDATA']
permIconPath = permImagesPath+'\\icon.ico'


tempBasePath = '%s\\eliasbenb\\EzSetup\\' %  (os.environ['TEMP'])
tempExportPath = '%s\\eliasbenb\\EzSetup\\Export\\%s' %  (os.environ['TEMP'], current_time)
tempImportPath = '%s\\eliasbenb\\EzSetup\\Import\\%s' %  (os.environ['TEMP'], current_time)

exportInfoPath = tempExportPath+'\\Info'
exportBackgroundPath = tempExportPath+'\\Background\\background.png'
exportBackgroundSourcePath = exportInfoPath+'background_source.txt'
exportFilesPath = tempExportPath+'\\Files'
exportFilesListPath = exportInfoPath+'files_list.txt'
exportFontsPath = tempExportPath+'\\Fonts'
exportSoftwarePath = exportInfoPath+'\\software_list.txt'


importInfoPath = tempImportPath+'\\Info'
importBackgroundPath = tempImportPath+'\\Background\\background.png'
importBackgroundSourcePath = importInfoPath+'background_source.txt'
importFilesPath = tempImportPath+'\\Files'
importFilesListPath = importInfoPath+'\\files_list.txt'
importFontsPath = tempImportPath+'\\Fonts'
importSoftwarePath = importInfoPath+'\\software_list.txt'


software_save_path = r'EzSetup Software\\'
files_save_path = r'EzSetup Files\\'
current_dir = os.getcwd()