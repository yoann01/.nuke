import nuke
import os
import sys

root = os.path.dirname(__file__)

#plugin
gizmos = os.path.join(root, 'gizmos')
nuke.pluginAddPath(gizmos, addToSysPath=False)

#python
py = os.path.join(root, 'python')
sys.path.append(py)

# custom formats
nuke.addFormat('320 240 1.0 RFX_320p')
#nuke.knobDefault('Root.format', 'RFX_320p')
nuke.addFormat('3072 3072 square_3K')
nuke.addFormat('4096 4096 square_4K')
nuke.addFormat('3424 2202 AlexaMini_OpenGate')
nuke.addFormat('3200 1800 Amira_3.2K')
