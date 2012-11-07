"""
This script installs salt dependencies on windows 32 bit.
"""
import sys
import subprocess as sp

def install_log(executable, logname):
	logname = open(logname,"w")
	instcmd = sp.Popen("cmd /c "+executable, stdout = logname, stderr = logname, cwd=r"c:\temp\salt")
	instcmd.communicate()

def msiexec(executable):
	instcmd = sp.Popen("msiexec /i "+executable, cwd=r"c:\temp\salt")
	instcmd.communicate()	
# todo install pywin32

def easyinstall(executable,logname):
	logname = open(logname,"w")
	easyinst = sp.Popen("cmd /c easy_install "+executable+ " c:\\salt\\python27", cwd=r"c:\temp\salt", stdout = logname, stderr = logname)
	easyinst.communicate()
	
install_log("vcredist_x86.exe /q", r"c:\salt\log\vclog.log")
#install_log("Win32OpenSSL-1_0_0e.exe /silent /verysilent /sp- /suppressmsgboxes", r"c:\salt\log\openssl.log")
zeromq = """pyzmq-2.1.11.win32-py2.7.msi TARGETDIR="c:\salt\python27" /quiet /norestart /log c:\salt\log\pyzmq_install.log ALLUSERS=1"""
msiexec(zeromq)
#m2crypto = r"M2Crypto-0.21.1.win32 /quiet /norestart /log c:\salt\log\m2crypto.log ALLUSERS=1"
#msiexec(m2crypto)
easyinstall("Cython-0.15.1.win32-py2.7.exe", "c:\salt\log\Cython.log")
easyinstall("msgpack-python-0.1.12.win32-py2.7.exe", "c:\salt\log\msgpack.log")
easyinstall("pywin32-216.win32-py2.7.exe", "c:\salt\log\pywin32.log")
msiexec("""pycrypto-2.3.win32-py2.7.msi TARGETDIR="c:\salt\python27" /quiet /norestart /log c:\salt\log\pycryto.log ALLUSERS=1""")