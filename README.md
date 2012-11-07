saltbootstrap
=============

A collection of scripts to bootstrap salt on Windows

# A word about security!
  This script is INSECURE in the sense that it sends passwords unencrypted.
  If you are using a shared drive and and you dont want your passwords to
  be revealed, change the script to read a configuration file. 

# Requirements
  - A shared drive holding all the binaries need to install salt. This shared
    Drive can be mapped using "net use ..." in Windows.
  - `winexe` from the SAMBA project.
  - Windows hosts which have a know Administrator user with know password.
  
# Usage
  
    bootstrap_salt32bin.sh COMPANY-PC filer1\\public  filer1\\user pass


