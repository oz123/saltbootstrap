#!/bin/bash

# This script installs salt dependencies on windows 32 bit.

# This script is part of the win32 bootstrap for salt, 
# it does the final configuration and tuning of windows, and 
# starts the salt service

# This script was written by Oz Nahum <nahumoz@gmail.com>
# License: GPL


# WARNING : This script is not password safe!!!
# 1. It sends password unecrypted on the network!
# 2. Other users on the linux host can find the password for
#    the shared drive using `ps`, if you are not comfortable
#    with it, change the script to read a password from a file
#    with correct permission or from command line.




PROGNAME=$0
HOSTNAME=$1
SHARENAME=$2
USERNAME=$3 
PASS=$4

function usage(){
  echo "Usage: $PROGNAME <hostname> <sharename> <username> <pass>"
  exit 1
}

if [ -z "$HOSTNAME" ]; then
   usage   
else

winexe -U ${HOSTNAME}/Administrator //${HOSTNAME} \
   "cmd /c net use k: /user:$USERNAME \\\\$SHARENAME ${PASS} /persistent:no \
   && cmd /c if exist c:\temp\salt (echo c:\temp\salt exists) else ( md  c:\temp\salt) \
   && cmd /c xcopy k:\software\salt_deps_32bit c:\temp\salt /e /y \
   && cmd /c net use k: /delete \
   && cmd /c if exist c:\salt\log (echo c:\temp\salt exists) else ( md  c:\salt\log) \
   && cmd /c msiexec /i c:\temp\salt\python-2.7.3.msi /quiet /norestart /log  c:\salt\log\python_install.log TARGETDIR=c:\salt\python27 ALLUSERS=1 \
   && cmd /c c:\salt\python27\pythonw.exe --version \
   && cmd /c c:\salt\python27\python.exe c:\temp\salt\distribute_setup.py \
   && cmd /c c:\salt\python27\python.exe c:\temp\salt\get-pip.py \
   && cmd /c c:\salt\python27\pythonw.exe c:\temp\salt\setenv.py c:\salt\python27;c:\salt\python27\scripts  \
   && cmd /c c:\salt\python27\Scripts\pip.exe install c:\temp\salt\PyYAML-3.10.tar.gz --log c:\salt\log\PyYAML_install.log \
   && cmd /c c:\salt\python27\Scripts\pip.exe install c:\temp\salt\Jinja2-2.6.tar.gz --log c:\salt\log\Jinja2_install.log \
   && echo Finished bootstrap stage 1  \
   && cmd /c c:\salt\python27\pythonw.exe c:\temp\salt\bootstrap_stage2.py \
   && echo Finish bootstrap stage 2 \
   && echo Installing SALT ... \
   && cmd /c c:\salt\python27\Scripts\pip.exe install c:\temp\salt\salt-0.10.4.tar.gz --log c:\salt\log\salt_install.log \
   && echo Finished salt installation ... \
   && echo Starting stage 3, launching salt.. \
   && cmd /c c:\salt\python27\pythonw.exe c:\temp\salt\bootstrap_stage3.py"

fi
