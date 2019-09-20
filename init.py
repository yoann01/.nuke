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
nuke.knobDefault('Root.format', 'RFX_320p')