import nuke
import os
import menu_gen

root = os.path.dirname(__file__)

gizmos = os.path.join(root, 'icons')
nuke.pluginAddPath(gizmos, addToSysPath=False) 

# Add custom menu to the application menu
menubar = nuke.menu('Nuke')

RfxMenu = menubar.addMenu('Tools')
RfxMenu.addCommand('Test T01', 'nuke.createNode("Transform")' )
RfxMenu.addCommand('Test T02', lambda : nuke.nodes.Transform())
RfxMenu.addCommand('Fix Reads', "import fixReads;reload(fixReads);fixReads.start()")
RfxMenu.addCommand('Split EXR Channels', "import splitChannel;reload(splitChannel);splitChannel.split()")

menu_name = "TESTMENU"
menu_generator = menu_gen.NukeMenuGenerator(menu_name)
menu_generator.create_menu()


# Add custom menu to the toolbar(also in r_click menu of the node graph)
nodes = nuke.menu('Nodes')
gizmos = nodes.addMenu('Gizmos', icon='NAS-52.png')


gizpath = os.path.join(root, 'gizmos')
for gizmo in os.listdir(gizpath):
    if os.path.splitext(gizmo)[-1] == '.gizmo':
        name = os.path.splitext(gizmo)[0]
        ico = name+'.png'
        gizmos.addCommand(name, "nuke.createNode('{0}')".format(name, icon = ico))


# add favorite directories in file browser
nuke.addFavoriteDir('pipeline', root, nuke.IMAGE | nuke.GEO)
os.environ['JOB']  = os.path.normpath(r'C:\dev\assetsUsd')
nuke.addFavoriteDir('JOB', '[getenv JOB]')