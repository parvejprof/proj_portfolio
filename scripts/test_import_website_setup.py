#!/usr/bin/python
import os
import argparse
import shutil
import zipfile


parser = argparse.ArgumentParser()
parser.add_argument("-p")
parser.add_argument("-t")
args = parser.parse_args()

print(args)
site_name = args.p
imported_file = args.t
print(site_name)
print(imported_file)

imported_file_without_ext = os.path.splitext(imported_file)[0]
print(imported_file_without_ext)


src_import_file = './media/'+ imported_file
target_site_import = "/var/www/"+site_name+"/"  

# print target_site_import

# shutil.copy2(src_import_file, target_site_import) 


with zipfile.ZipFile(src_import_file,"r") as zip_ref:
    zip_ref.extractall(target_site_import)


source = target_site_import + imported_file_without_ext
destination = target_site_import

files_list =  os.listdir(source)
for files in files_list:
    files_dst = destination+files
    files = source+"/"+files
  
    if os.path.exists(files_dst):
        os.remove(files_dst)
  
    shutil.move(files, destination)