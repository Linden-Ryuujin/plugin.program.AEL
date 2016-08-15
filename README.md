# Advanced Emulator Launcher #

Multi-emulator front-end for Kodi scalable to collections of thousands of ROMs. Includes offline 
scrapers for MAME and No-Intro ROM sets and also supports scrapping ROM metadata and artwork online. 
ROM auditing for No-Intro ROMs using No-Intro XML DATs. Launching of games and 
standalone applications is also available.

## WARNING ##

On 16/Aug/2016 (commit 2cafa23) AEL has introduced a new storage format that enables many more
types of artwork. Unfortunately, this new model is incompatible with previous versions of AEL.
You will notice this if you see menus dissapearing and erratic AEL behaviour. The easiest way to 
migrate is to delete the `ADDON_DATA_DIR` directory and start fresh from scratch.

Good news is that AEL now supports a lot more features (including ROM collections) and the data storage 
format probably will not change for a while.

## Installation instructions ##

It is important that you follow this instructions or Advanced Emulator Launcher won't work well.

  1) In this page click on the green button `Clone or Download` --> `Download ZIP`

  2) Uncompress this ZIP file. This will create a folder named `plugin.program.advanced.emulator.launcher-master`

  3) Rename that folder to `plugin.program.advanced.emulator.launcher`

  4) Compress that folder again into a ZIP file. 

  5) In Kodi, use that ZIP file (and not the original one) to install the plugin in `System` --> `Addons` 
     --> `Install from ZIP file`.

  6) You are done!
