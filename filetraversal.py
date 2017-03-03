# Import the os module, for the os.walk function
import os
 
# Set the directory you want to start from
rootDir = 'C:\\Users\\krishma\\Desktop\\prep\\Test1'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
      	if len(subdirList)>0:
      		print("Hello", subdirList)

