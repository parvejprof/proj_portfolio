import shutil, os, glob
import zipfile

with zipfile.ZipFile("/var/www/html/imagine.zip","r") as zip_ref:
    zip_ref.extractall("/tmp/www/kkk.com/")


def moveAllFilesinDir(srcDir, dstDir):
    # Check if both the are directories
    if os.path.isdir(srcDir) and os.path.isdir(dstDir) :
        # Iterate over all the files in source directory
        for filePath in glob.glob(srcDir + '\*'):
            # Move each file to destination Directory
            shutil.move(filePath, dstDir);
    else:
        print("srcDir & dstDir should be Directories")

sourceDir = '/tmp/www/kkk.com/imagine'
destDir =  '/var/www/kkk.com/'
    
moveAllFilesinDir(sourceDir,destDir)
