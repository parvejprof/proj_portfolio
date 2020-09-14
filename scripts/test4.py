import shutil
import os

source = "/var/www/kkk.com/imagine"
destination = "/var/www/kkk.com/"
files_list =  os.listdir(source)
for files in files_list:
    files = source+"/"+files
    shutil.move(files, destination)
