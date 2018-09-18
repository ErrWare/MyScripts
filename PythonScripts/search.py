import webbrowser
import sys

searchSite = 'https://duckduckgo.com/?q='

webbrowser.open_new_tab(searchSite 
+ '+'.join(sys.argv[1:]))