import os
import subprocess


root = os.path.dirname(__file__)


os.environ['HOME'] = root
os.environ['NUKE_PATH'] = root


#start Nuke
if os.name == 'nt':
    exe = (r'C:\Program Files\Nuke11.3v5\Nuke11.3.exe')
    os.path.normpath(exe) 
else:
    exe = None
    
subprocess.Popen([exe, '--nukex']) 

