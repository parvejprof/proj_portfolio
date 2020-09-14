line1 = "<VirtualHost *:80>\n"
line2 = "\tServerAdmin admin@example3.com\n"
line3 = "\tServerName www.example3.com\n"
line4 = "\tServerAlias www.example3.com\n"
line5 = "\tDocumentRoot /var/www/example3\n"
line6 = "</VirtualHost>\n"
with open('my_file.txt','w') as out:
    out.writelines([line1, line2, line3, line4, line5, line6])
