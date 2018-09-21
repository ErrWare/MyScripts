import webbrowser
import json
import inspect
import os

py_dir = os.path.dirname(inspect.stack()[0][1])

with open(os.path.join(py_dir,'socList.json'),'r') as jfile:
	socList = json.load(jfile)

for site in socList:
	webbrowser.open(site)
