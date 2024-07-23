# Date: 2024-07-23
# Author : Rob Rong

import subprocess
import os

prepare_command = ["sudo", "apt-get", "update"]

# apt-get install -y libssl-dev libldns-dev libck-dev libnghttp2-dev

install_command = ["sudo", "apt-get", "install", "-y","dnsmasq"]
subprocess.call(install_command)

#start service
start_command = ["sudo", "systemctl", "start", "dnsmasq"]
subprocess.call(start_command)

#check service
check_service_command = ["sudo", "systemctl", "status", "dnsmasq"]
output = subprocess.check_output(check_service_command)

#return is butes object
print(output.decode('utf-8'))

# set up upgrade DNS server
print(f"set upgrade DNS server  as 8.8.8.8")

add_dns_command = ["sudo", "echo", "'server=8.8.8.8'", ">>","/etc/dnsmasq.conf"]
#subprocess.call(add_dns_command )

#enable the logs
enable_log_command = ["sudo", "sed", "-i", "s/^#\s*log-queries/log-queries/","/etc/dnsmasq.conf"]
subprocess.call(enable_log_command )

#restart service
restart_command = ["sudo", "systemctl", "restart", "dnsmasq"]
subprocess.call(restart_command)
