#!/usr/bin/python
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p")
args = parser.parse_args()

domain_name = args.p
newfile = "/etc/httpd/conf.d/" + domain_name +".conf"

line1 = "<VirtualHost *:80>\n"
line2 = "\tServerAdmin admin@"+domain_name+"\n"
line3 = "\tServerName www."+domain_name+"\n"
line4 = "\tServerAlias www."+domain_name+"\n"
line5 = "\tDocumentRoot /var/www/"+domain_name+"\n"
line6 = "</VirtualHost>\n"
with open(newfile,'w') as out:
    out.writelines([line1, line2, line3, line4, line5, line6])

indexfile = "/var/www/"+domain_name+"/index.html"

line7 = "<h1>Greetings!!, your site <b>"+domain_name+"</b> ready!</h1>"
with open(indexfile,'w') as out:
    out.writelines([line7])


os.system("systemctl reload httpd")
