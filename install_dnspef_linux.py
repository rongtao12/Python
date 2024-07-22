import subprocess  
import os
  
#In this corrected code, we're passing the install_command as a list of strings to the subprocess.call() method. Each element of the list represents one part of the command to be executed, with the first element being the command itself, and the subsequent elements representing its arguments.
#It's important to pass the command and its arguments as a list of strings rather than as a single string, as this allows the subprocess module to properly escape any special characters or spaces that might be present in the command or its arguments.
#Also note that in order to run the sudo command, the Python script needs to be run with appropriate permissions, such as by running the script with sudo itself.

prepare_command = ["sudo", "apt-get", "update"]  

#apt-get install -y libssl-dev libldns-dev libck-dev libnghttp2-dev

install_command = ["sudo", "apt-get", "install", "-y","libssl-dev","libldns-dev","libck-dev","libnghttp2-dev"]  
subprocess.call(install_command)  

with open("install_dnsperf.sh",'w') as file:
	file.write("git clone https://github.com/DNS-OARC/dnsperf.git")
	file.write("cd dnsperf")
	file.write("./autogen.sh")
	file.write("./configure")
	file.write("make")
	file.write("make install")

run_install_dnsperf_command = ["sudo", "sh", "install_dnsperf.sh"]  
subprocess.call(run_install_dnsperf_command)  

with open("queries.txt",'w') as file:
	file.write("www.google.com")
	file.write("www.microsoft.com")
	file.write("www.facebook.com")
	
with open("server.txt",'w') as file:
	file.write("8.8.8.8")
	file.write("1.1.1.1")

run_command = ["dnsperf","-s","server.txt","-d","queries.txt","-l","60","-c","10"]
subprocess.call(run_command) 
