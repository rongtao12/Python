import subprocess  
import os
  
prepare_command = ["sudo", "apt-get", "update"]  

# apt-get install -y libssl-dev libldns-dev libck-dev libnghttp2-dev
install_command = ["sudo", "apt-get", "install", "-y","libssl-dev","libldns-dev","libck-dev","libnghttp2-dev","dnsperf"]  
subprocess.call(install_command)  

with open("queries.txt",'w') as file:
    file.write("www.google.com A \n")
    file.write("www.microsoft.com A \n")
    file.write("www.facebook.com A \n")
	
dns_server = "8.8.8.8"

run_command = ["dnsperf","-s",dns_server,"-d","queries.txt","-l","60","-c","10"]
subprocess.call(run_command) 
