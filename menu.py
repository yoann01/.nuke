# -------------------------------------
#   init.py
#   version: 1.0.0
#   Last Update:
# -------------------------------------
import nuke 
import platform


#  OS specific variables (no Linux support)
Win = ''
OSX = ''
LINUX = ''

if (platform.system() == 'Windows'):
	dir = Win
elif (platform.system() == 'Darwin'):
	dir = OSX
elif (platform.system() == 'Linux'):
	dir = LINUX
else:
	dir = None


toolbar = nuke.menu("Nuke")

wptkMenu = toolbar.addMenu('World Position Tool Kit')
wptkMenu.addCommand('Mask3DCubical_ik', 'nuke.createNode("Mask3DCubical_ik")') 
wptkMenu.addCommand('Mask3DGradient_ik', 'nuke.createNode("Mask3DGradient_ik")') 
wptkMenu.addCommand('Mask3DSpherical_ik', 'nuke.createNode("Mask3DSpherical_ik")') 
wptkMenu.addCommand('TransformWorld_ik', 'nuke.createNode("TransformWorld_ik")') 
wptkMenu.addCommand('WorldPos_Texture_Projection_ik', 'nuke.createNode("WorldPos_Texture_Projection_ik")') 
wptkMenu.addCommand('WorldPos_Texture_Generator_ik', 'nuke.createNode("WorldPos_Texture_Generator_ik")') 
wptkMenu.addCommand('WorldPos_Lambert_Shader_ik', 'nuke.createNode("WorldPos_Lambert_Shader_ik")') 