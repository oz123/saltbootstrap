"""
This script is part of the win32 bootstrap for salt, 
it does the final configuration and tuning of windows, and 
starts the salt service

This script was written by Oz Nahum <nahumoz@gmail.com>
License: GPL
"""
import os
import shutil
import subprocess as sp

def install_log(executable, logname):
    logname = open(logname,"w")
    instcmd = sp.Popen("cmd /c "+executable, stdout = logname, stderr = logname, cwd=r"c:\temp\salt")
    instcmd.communicate()


#Some general firewall settings
#Allows ping backs""

pingback='netsh advfirewall firewall add rule name="ALL ICMP V4" protocol=icmpv4:any,any dir=in action=allow'
print "will configure pingback"
install_log(pingback,"c:\\salt\\log\\netsh_ping_back.log")

print "ping back configured..."

#Allows remote management
remote_mgmt='netsh advfirewall firewall set rule group="remote service management" new enable=yes'
install_log(remote_mgmt,"c:\\salt\\log\\netsh_remote_mgmt.log")
	
print "successfully configured firewall"

pkipath="c:\\salt\\conf\\pki"
if not os.path.exists(pkipath):
   os.makedirs(pkipath)
saltsys="c:\\salt\\sys\\"
if not os.path.exists(saltsys):
   os.mkdir(saltsys)

if not os.path.exists("c:\\salt\\sys\\nssm.exe"):
   shutil.copy2("c:\\temp\\salt\\nssm.exe", "c:\\salt\\sys\\")

shutil.copy2("c:\\temp\\salt\\minion.template", "c:\\salt\\conf\\minion")

create_salt_service="c:\\salt\\sys\\nssm.exe install salt-minion c:\\salt\\python27\\python c:\\salt\\python27\\scripts\\salt-minion -c c:\\salt\\conf"
install_log(create_salt_service,"c:\\salt\\log\\mkservice.log")

start_salt="net start salt-minion"
install_log(start_salt,"c:\\salt\\log\\salt_start.log")
rem_execution='sc config winexesvc start= auto'
install_log(rem_execution,"c:\\salt\\log\\rem_execution.log")
