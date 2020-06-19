from time import gmtime, strftime
import os

current_time = strftime("%Y%m%d%H%M%S", gmtime())


permBasePath = '%s\\eliasbenb\\EzSetup' %  os.environ['APPDATA']
permImagesPath = '%s\\eliasbenb\\EzSetup\\images' %  os.environ['APPDATA']
permIconPath = permImagesPath+'\\icon.ico'


tempBasePath = '%s\\eliasbenb\\EzSetup\\' %  (os.environ['TEMP'])
tempExportPath = '%s\\eliasbenb\\EzSetup\\Export\\%s' %  (os.environ['TEMP'], current_time)
tempImportPath = '%s\\eliasbenb\\EzSetup\\Import\\%s' %  (os.environ['TEMP'], current_time)

exportInfoPath = tempExportPath+'\\Info'
exportBackgroundPath = tempExportPath+'\\Background\\background.png'
exportBackgroundSourcePath = exportInfoPath+'\\background_source.txt'
exportFilesPath = tempExportPath+'\\Files'
exportFilesListPath = exportInfoPath+'\\files_list.txt'
exportFontsPath = tempExportPath+'\\Fonts'
exportFontsListPath = exportInfoPath+'\\fonts_list.txt'
exportSoftwareListPath = exportInfoPath+'\\software_list.txt'
exportSoftwareLinksPath = exportInfoPath+'\\software_links.txt'


importInfoPath = tempImportPath+'\\Info'
importBackgroundPath = tempImportPath+'\\Background\\background.png'
importBackgroundSourcePath = importInfoPath+'\\background_source.txt'
importFilesPath = tempImportPath+'\\Files'
importFilesListPath = importInfoPath+'\\files_list.txt'
importFontsPath = tempImportPath+'\\Fonts'
importFontsListPath = importInfoPath+'\\fonts_list.txt'
importSoftwareListPath = importInfoPath+'\\software_list.txt'
importSoftwareLinksPath = importInfoPath+'\\software_links.txt'


fontsInstallDir = '%s\\Fonts' % (os.environ['WINDIR'])

current_dir = os.getcwd()
software_save_path = current_dir+'\\EzSetup Software'
files_save_path = current_dir+'\\EzSetup Files'