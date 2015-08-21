#@author Hizbul Bahar
#@email hizbul.ku@gmail.com

#!/usr/bin/env python
import os

# Clear the terminal.
os.system("clear")


def msg(stat):
    print(stat)


def newline():
    print("")


def creat_host(domain, project_dir):
    msg(" Creating the Directory Structure ")
    os.system("sudo mkdir -p "+project_dir+"/"+domain)

    newline()

    msg(" Granting Proper Permissions ")
    os.system("sudo chown -R $USER:$USER "+project_dir+"/"+domain)

    newline()

    msg(" Making Sure Read Access is Permitted ")
    os.system("sudo chmod -R 755"+project_dir+"")

    newline()

    msg(" Adding A Demo Page ")
    file_object = open(project_dir+"/"+domain+"/index.html", "w")
    file_object.write("<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><title>Virtual Hosts Created Successfully!</title><style>html{background-color: #508bc9;color: #fff;font-family: sans-serif, arial;}.container{width: 80%;margin: auto auto;}.inl{text-align: center;}.inl img{border-radius: 10px;}a{color: #f2d8ab;}</style></head><body><div class='container'><h1>Virtual Hosts Created Successfully!</h1><p><b>Apache Virtual Hosts Generator</b> has successfully created a virtual host in your server.<br>We can code it better! Join at <a href='https://github.com/rakibtg/Apache-Virtual-Hosts-Creator' target='_blank'>GitHub</a><br>Created by <a href='https://www.twitter.com/rakibtg' target='_blank'>Hasan</a></p><div class='divider'><div class='inl'><h1>Let's celebrate!</h1><img src='http://i.imgur.com/vCbBhwy.gif' alt='Scene from Spider Man Movie (C) Spider Man Movie ..'></div></div></div></body></html>")
    file_object.close()

    newline()

    msg(" Creating Virtual Host Config File ")
    host_file = open("/tmp/"+domain+".conf", "w")
    host_file.write("<VirtualHost *:80>\nServerAdmin localserver@localhost\nServerName "+domain+"\nServerAlias www."+domain+"\nDocumentRoot "+project_dir+"/"+domain+"\n<Directory '"+project_dir+"/"+domain+"/""'>\n\tAllowOverride All\n\tRequire all granted\n</Directory>\n</VirtualHost>")
    host_file.close()
    os.system("sudo mv \"/tmp/"+domain+".conf\" \"/etc/apache2/sites-available/\"")

    newline()

    msg(" Activating New Virtual Host ")
    os.system("sudo a2ensite "+domain+".conf")

    newline()

    msg(" Restarting Apache ")
    os.system("sudo service apache2 restart")
    os.system("service apache2 reload")

    newline()

    msg(" Setting Up Local Host File ")
    if host_flag == 0:
        os.system("sudo sed -i -e '1i127.0.1.1   "+domain+"\' \"/etc/hosts\"")
    else:
        print(" Skipped! ")

    print("\nCongratulations! now you can visit http://"+domain+"/ from any web browser\n\n")

host_flag = 0

newline()

print("\n Welcome to Apache Virtual Hosts Generator\n - This script will setup a Apache Virtual Hosts for you\n - All you have to do, answer 2 questions\n - Make sure you have Apache configured\n ")

newline()
msg(' What would be the project directory? eg. /var/www/html or /home/hostname/some_directory/projects')
project_dir = input()
newline()
msg(" What would be the domain name? ")
domain = input()

if os.path.exists(project_dir+"/"+domain):
    msg(" IMPORTANT: It seems that you have already configured a virtual hosts with the same domain name \n If you continue then all your data of http://"+domain+"/ will be overwritten and can not be undo \n Continue? (yes/no) ")
    flag = input()
    host_flag = 1

    if (flag == "no" or flag == ""):
        newline()
        msg(" This virtual host is already exist. \n Please choose a different name and try again. ")
        newline()
    if flag == "yes":
        newline()
        msg(" Existing host will be overwritten ... ")
        creat_host(domain, project_dir)
else:
    creat_host(domain, project_dir)
