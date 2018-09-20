import os
import sys
import inspect

_, me = os.path.split(inspect.stack()[0][1])

bat_dir = sys.argv[1]

REAL_SCRIPT_EXTENSION = '.py'

scripts = [file for file in os.listdir(os.path.join(bat_dir,'PythonScripts')) if file.endswith(REAL_SCRIPT_EXTENSION)]
saved_dir = os.getcwd()
os.chdir(bat_dir)
for script in scripts:
	print(os.path.join('PythonScripts',script))
	with open(script[0:-len(REAL_SCRIPT_EXTENSION)]+'.bat', 'w') as exeScript:
		exeScript.write('@echo off\n')
		# in .bat %~dp0 is the abs\directory\path\ of the script
		# https://web.archive.org/web/20180120021145/https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/percent.mspx?mfr=true
		exeScript.write('\n')
		if script == me:
			args = r'%~dp0'
		else:
			args = '%*'
		exeScript.write(r'python %~dp0' + os.path.join('PythonScripts',script) + ' ' + args)
		exeScript.close()

os.chdir(saved_dir)