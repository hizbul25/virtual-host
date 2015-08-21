from time import sleep
import os

def msg(data):
    print(data)

msg('What would be the domain name?')
domain = input()
msg('Creating virtual host config file...')
os.system('sudo chmod -R 0777 /etc/apache2/sites-available')
host_file = open('/etc/apache2/sites-available/'+domain+'.conf', 'w')
