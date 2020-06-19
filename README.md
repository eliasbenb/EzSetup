<a href="#"><h3 align="center"><img src="https://i.ibb.co/ZWtwXrg/Ez-Setup-Header.png" width="600px"></h3></a>
<p align="center">
  <a href="https://github.com/eliasbenb/EzSetup/releases"><img src="https://img.shields.io/github/downloads/eliasbenb/EzSetup/total?color=ff0000&style=for-the-badge"></a>
  <a href="https://github.com/eliasbenb/EzSetup/releases/latest"><img src="https://img.shields.io/github/v/release/eliasbenb/EzSetup?color=ff0000&style=for-the-badge"></a>
</p>
<p align="center">
  <a href="https://eliasbenb.github.io"><img
src="https://i.ibb.co/RDg0dkV/Produced-By-eliasbenb-Red.png" width="180"></a>
</p>

# What is this repo?
EzSetup is a Python app that uses a PyQt5 GUI. It eases the process of setting up your Windows PC.


## Features supported:
- Importing and exporting backups
- Automatically downloading the latest version of specified apps
- Backing up folders
- Backing up backgrounds and automatically setting them
- Backup up fonts and automatically installing them

## To do list:
- Add a progress bar for some tasks

# Installation
- **Windows:** To install EzSetup download the latest executable file from [here](https://github.com/eliasbenb/EzSetup/releases)

# Usage:
### Home Screen:
- On launch you get 5 options of buttons to press, each will be explained below
- The menu bar contains the export/import button option which is pretty self explanatory. A `.ez` file will be exported containing all backed up information
![Home Screen](https://user-images.githubusercontent.com/54410649/85155412-c7b41700-b269-11ea-89b3-00fbc2c03f33.PNG)

### Background:
- The background tab contains a browse button, this will open a windows file explorer, from there locate the background you want to back up
- The background will be displayed on the app after selection
![Background](https://user-images.githubusercontent.com/54410649/85155417-c8e54400-b269-11ea-8e83-e78a101b8ab4.PNG)

### Files:
- The files tab has a browse button, this will open a windows file explorer, from there locate the folder you want to be backed up
- You can set the destination to save the folder on setup by clicking on the table item you want to change
![Files](https://user-images.githubusercontent.com/54410649/85155421-c8e54400-b269-11ea-8905-d3ed777169d2.PNG)

### Fonts:
- The fonts tab contains a browse button, this will open a windows file explorer, from there locate the font file you want to back up
- The font's information will be displayed on the window's table
![Fonts](https://user-images.githubusercontent.com/54410649/85155423-c97dda80-b269-11ea-9d8c-57ab4c09de5c.PNG)

### Software:
- In the Software tab you can add apps you would like to be automatically downloaded on setup
- Inputing a query in the input box will search for an app matching the keywords on FileHippo, putting the direct link to the FileHippo page will also work
![Software](https://user-images.githubusercontent.com/54410649/85155424-c97dda80-b269-11ea-9044-57d4f4a09274.PNG)

# Error Messages:
- IMP: import module error
- EXP: export module error
- FIL: 'Files' section error
- FNT: 'Fonts' section error
- SOF: 'Software' section error
- BG: 'Background' section error
- SYS: system error (normally to do with file management)