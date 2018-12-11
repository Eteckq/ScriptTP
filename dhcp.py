import os

os.system('ls -la');
print("-------------------------------------")
print("Configuration DHCP")
print("-------------------------------------")

#Modification du fichier /etc/sysctl.conf


lines = None
with file = open('/etc/sysctl.conf', 'r') :
    lines = [l in file.readlines() if l!='#net.ipv4.ip_forward=1']
with file = open('/etc/sysctl.conf', 'w'):
    file.write("net.ipv4.ip_forward=1".join(lines))

