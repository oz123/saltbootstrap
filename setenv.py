import _winreg
import sys


def get_registry_value(reg, key, value_name):
	k = _winreg.OpenKey(reg, key)
	value = _winreg.QueryValueEx(k, value_name)[0]
	_winreg.CloseKey(k)
	return value
def set_registry_value(reg, key, value_name, value, value_type=_winreg.REG_SZ):
	k = _winreg.OpenKey(reg, key, 0, _winreg.KEY_WRITE)
	_winreg.SetValueEx(k, value_name, 0, value_type, value)
	_winreg.CloseKey(k)
	
	
reg = _winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
key = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
path = get_registry_value(reg, key, "Path")

path += ";" + sys.argv[1]
set_registry_value(reg, key, "Path", path, _winreg.REG_EXPAND_SZ)
