import os
import hashlib 
import collections

# Set the directory you want to start from
rootDir = 'C:\\Users\\krishma\\Desktop\\prep'

def parsing_dir_files(rootDir):
	for dirName, subdirList, fileList in os.walk(rootDir):
	    #print('Found directory:: %s' % dirName)
	    for fname in fileList:
	       # print('\t%s' % fname)
	        #Get Hash
	        hash_of_files = hashlib.md5()
	        hash_of_files.update(fname)
	        hash_of_files = hash_of_files.hexdigest()

	        data_dict = {fname:hash_of_files}

	        return data_dict

def return_dups(file_list_dict):

	value_occurences = collections.Counter(file_list_dict.values())
	filtered_dict = {key: value for key, value in file_list_dict.items()
		                 if value_occurences[value] == 1}
		       
	print (filtered_dict) 
	return filtered_dict

def main():
	file_list = parsing_dir_files(rootDir)
	dup_list = return_dups(file_list)
	print(dup_list)

main()

   

 