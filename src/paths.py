import os, re
from time import gmtime, strftime

current_time = strftime("%Y%m%d%H%M%S", gmtime())

permBasePath = '%s\\eliasbenb\\EzSetup' %  os.environ['APPDATA']
permImagesPath = '%s\\eliasbenb\\EzSetup\\images' %  os.environ['APPDATA']
permIconPath = permImagesPath+'\\icon.ico'

tempBasePath = '%s\\eliasbenb\\EzSetup\\' %  (os.environ['TEMP'])
tempExportPath = '%s\\eliasbenb\\EzSetup\\Export\\%s' %  (os.environ['TEMP'], current_time)
tempImportPath = '%s\\eliasbenb\\EzSetup\\Import\\%s' %  (os.environ['TEMP'], current_time)


exportBackgroundPath = tempExportPath+'\\Background\\background.png'
exportBackgroundSourcePath = tempExportPath+'\\Background\\source.txt'

exportFilesPath = tempExportPath+'\\Files'
exportFilesListPath = exportFilesPath+'\\file_list.txt'

exportFontsPath = tempExportPath+'\\Fonts'

exportSoftwarePath = tempExportPath+'\\Software\\software.txt'

importBackgroundPath = tempImportPath+'\\Background\\background.png'

importFilesPath = tempImportPath+'\\Files'
importFilesListPath = importFilesPath+'\\file_list.txt'

importFontsPath = tempImportPath+'\\Fonts'

importSoftwarePath = tempImportPath+'\\Software\\software.txt'


software_save_path = r'EzSetup Software\\'
files_save_path = r'EzSetup Files\\'
current_dir = os.getcwd()