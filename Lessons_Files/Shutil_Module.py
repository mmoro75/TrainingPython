############################################## Shutil Module #################################################################

# shutil module is a python integrated module and provide capabilities for operations on file and folders like: copy, move , remove
# it can be used both in windows and linux

import shutil

print(dir(shutil))   # shutil module is more advanced than OS module for such operations

########################################### copy files or directories #################################################

src="sorce_file"
dest="dest_file"
shutil.copyfile(src,dest)  # providing source and destination will copy file from source to dest ( no permissions preserved)
shutil.copy(src,dest) # this operation will also copy file from source to destination, but it would also keep same permissions
shutil.copy2(src,dest)  # this operation will keep also metadata of your original file ( ex same permission and timestamp)
shutil.copymode(src,dest) # it will give permissions from source file to destination file ( it is a copy permission not file content)
shutil.copystat(src,dest) # it will copy metadata from source file to destination file ( it is a metadata copy not file content)

fo1=("file_name1","r") #open file in read mode
fo2=("file_name2", "w") # open file in write mode
shutil.copyfileobj(fo1,fo2)  # copy content file 1 to file 2 with shutil function

dir_src="directory to copy"
dir_dest="destination directory"
shutil.copytree(dir_src,dir_dest) # it will copy entire directory structure into source directory (including permissions and metadate)

shutil.rmtree(dir_dest) # it will remove all the directory tree



