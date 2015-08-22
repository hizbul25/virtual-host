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


def create_host(domain, project_dir):
    project_path = project_dir+"/"+domain
    msg(" Creating the Directory Structure ")
    os.system("sudo mkdir -p "+project_path)

    newline()

    msg(" Granting Proper Permissions ")
    os.system("sudo chown -R $USER:$USER "+project_path)

    newline()

    msg(" Making Sure Read Access is Permitted ")
    os.system("sudo chmod -R 755"+project_dir+"")

    newline()

    msg(" Adding A demo Welcome Page ")
    if not os.path.exists(project_path):
        os.makedirs(project_path)

    if os.path.exists(project_path):
        os.system('sudo cp '+os.getcwd()+'/index.html '+project_path+'/index.html')

    newline()

    msg(" Creating Virtual Host Config File ")
    host_file = open("/tmp/"+domain+".conf", "w")
    host_file.write("<VirtualHost *:80>\nServerAdmin localserver@localhost\nServerName "+domain+"\nServerAlias www."+domain+"\nDocumentRoot "+project_path+"\n<Directory '"+project_path+"/""'>\n\tAllowOverride All\n\tRequire all granted\n</Directory>\n</VirtualHost>")
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
msg(' What would be the project directory? \n example: /var/www/html or /home/hostname/some_directory/projects')
project_dir = input()
newline()
msg(" What would be the domain name? ")
domain = input()

if os.path.exists(project_dir+"/"+domain):
    msg(" IMPORTANT: It seems that you have already configured a virtual hosts with the same domain name \n If you continue then all your data of http://"+domain+"/ will be overwritten and can not be undo \n Continue? (yes/no) ")
    flag = input()
    host_flag = 1

    if flag == "no" or flag == "":
        newline()
        msg(" This virtual host is already exist. \n Please choose a different name and try again. ")
        newline()
    if flag == "yes":
        newline()
        msg(" Existing host will be overwritten ... ")
        create_host(domain, project_dir)
else:
    create_host(domain, project_dir)
