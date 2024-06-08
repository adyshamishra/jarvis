import os

import eel

eel.init("www")

os.system('start msedge.exe --app="D:/Jarvis/.vscode/engine/www/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)
