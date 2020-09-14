#!/usr/local/bin/python3
# importing linrary 
import os 
import subprocess 
import sys 
import getpass 
import crypt





import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p")
args = parser.parse_args()

username = args.p
print(username)
  
# add user function 
def add_user():

     # Ask for the input 
     #username = input("Enter Username ")    
     #print("username")
  
     # Asking for users password 
     #password = getpass.getpass()
     password = "123456"
     encPass = crypt.crypt(password,"22")
         
     try: 
         # executing useradd command using subprocess module 
         #os.system("useradd -p "+encPass+" johnsmith")
         subprocess.run(['useradd', '-p', encPass, username])       
         #subprocess.run(['useradd', username])       
     except: 
         print("Failed to add user.")                      
         sys.exit(1) 
#  
add_user() 
