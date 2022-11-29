# import shutil, os 

# ##COPY file
# os.chdir('C:\\')
# shutil.copy('C:\\spam.txt','C:\\delicious') #.copy(source, destination)
# #'C:\\delicious\\spam.txt'

# ##BACKING UP a folder with copytree - TAKES all contents in the bacon folder  

# os.chdir('C:\\')
# shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
# #'C:\\bacon_backup'

# ## Moving files or folders
# shutil.move('C:\\bacon.txt', 'C:\\eggs')
# #'C:\\eggs\\bacon.txt'
# shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
# #'C:\\eggs\\new_bacon' IT CHANGES the name of the file in the folder

# #Delete folders with send2trash

# import send2trash

# baconFile = open('bacon.txt','a') #creates the file
# baconFile.write('Bacon is not a vegetable.')
# baconFile.close()
# send2trash.send2trash('bacon.txt')

# ## walk through folders with os.walk()

# import os 

# for folderName, subfolders, filenames in os.walk('C:\\delicious'):
# 	print('The current folder is ' + folderName)

# 	for subfolder in subfolders:
# 		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

# 	for filename in filenames:
# 		print('FILE INSIDE ' + folderName + ': '+ filename)

# 	print('')

## CREATING ZIP files 

import zipfile, os 

os.chdir('C:\\Users\\usuario\\Desktop\\TEST\\shutilmod\\Automate_the_Boring_Stuff_2e_onlinematerials.zip')
exampleZip = zipfile.ZipFile('Automate_the_Boring_Stuff_2e_onlinematerials.zip')
exampleZip.namelist()

