#!/usr/bin/python
import os
import argparse
import shutil
import zipfile

shutil.copy2('../media/imagine.zip', '/var/www/kkk.com/') 

with zipfile.ZipFile("/var/www/kkk.com/imagine.zip","r") as zip_ref:
    zip_ref.extractall("/var/www/kkk.com/")


source = "/var/www/kkk.com/imagine"
destination = "/var/www/kkk.com/"
files_list =  os.listdir(source)
for files in files_list:
    files = source+"/"+files
    shutil.move(files, destination)
