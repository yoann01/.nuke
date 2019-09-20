import nuke



OFFSET = 80


#
## @brief Split all channels from an EXR  
#
# @param 
#
# @exception N/A
#
# @retval None - None.
def split():
    sel = nuke.selectedNodes()

    if len(sel) == 0:
        nuke.message('At least one EXR is needed ') 
    else:
        for node in sel:
            chan = node.channels()
            chan = list(set([x.split('.')[0] for x in chan]))
            shs = []

            for ch in chan:
                sh = nuke.nodes.Shuffle(name=ch,
                                            inputs=[node],
                                            postage_stamp= True,
                                            hide_input=False)
                sh['in'].setValue(ch)
                shs.append(sh)

                nuke.nodes.ColorCorrect(inputs=[sh])

            y = node.ypos() + OFFSET
            x = node.xpos()
            for i, s in enumerate(shs):
                nx = x +  (OFFSET*i)
                s.setXYpos(nx, y)