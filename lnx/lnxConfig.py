#!/usr/bin/env python3

from netmiko import ConnectHandler

lnx = {
    'ip': 'localhost',
    'username': 'rortega',
    'password': 'Lnx#2020',
    'device_type': 'linux',
    'secret': 'Lnx#2020',
    'verbose': True
}

connection = ConnectHandler(**lnx)

connection.enable()

output0001 = connection.send_command('wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add - && sudo apt-get install apt-transport-https && echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list && sudo apt update && sudo apt install -y elasticsearch kibana')
print(output0001)

output0002 = connection.send_command('ip address show dev eth0 | grep inet')
with open("temporal.txt", 'w') as out:
    out.write(output0002)
f = open('temporal.txt', 'r')
netlist = list()
netlist = f.readline().split()
ipadd = str(netlist[1]).rstrip('/28')
print(ipadd)
f.close()
connection.send_command('rm -f temporal.txt')
