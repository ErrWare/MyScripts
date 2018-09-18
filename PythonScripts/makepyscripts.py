import os
scripts = [file for file in os.listdir('.') if file.endswith('.py')]
os.chdir('..')
for script in scripts:
	print(script)
	exeScript = open(script[0:-3]+'.bat', 'w')
	exeScript.write('@echo off\n')
	# in .bat %~dp0 is the directory/ of the script
	# https://web.archive.org/web/20180120021145/https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/percent.mspx?mfr=true
	exeScript.write(r'cd %~dp0PythonScripts')
	exeScript.write('\n')
	exeScript.write('python ' + script + ' %*')
	exeScript.close()