import zipfile, os 


## READING FROM ZIP files
os.chdir('C:\\Users\\usuario\\Desktop\\TEST\\shutilmod')
exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist()) #GIVES THE CONTENTS IN THE zip
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size # original file size
spamInfo.compress_size # compressed file size 
'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
exampleZip.close()

##EXTRACTING FROM ZIP files 

os.chdir('C:\\Users\\usuario\\Desktop\\TEST\\shutilmod')
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall() #IF you add a folder it will create it and extract all there
exampleZip.close()

## Extracting only 1 file from Zip file
exampleZip.extract('spam.txt')
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
exampleZip.close()

#CREATING and ADDING to ZIP files
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type = zipfile.ZIP_DEFLATED)
newZip.close()