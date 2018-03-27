import maya.cmds as cmds

def mobiPipe() :

    if cmds.window("mobiPipeWD",exists=1) :
        cmds.deleteUI("mobiPipeWD")

    cmds.window("mobiPipeWD", title="mobiPipe" )
    form = cmds.formLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )

    tab1 = cmds.columnLayout(adj=1)
    cmds.separator(h=10)
    cmds.textFieldButtonGrp( w=100, adj= 1 ,label='current Set Project', ed=0, buttonLabel='set Project' )
    cmds.textFieldButtonGrp( cal = [1,"center"] , adj= 1 ,label='current User', ed=0, buttonLabel='set User' )
    cmds.separator(h=10)
    cmds.setParent( '..' )

    tab2 = cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button()
    cmds.button()
    cmds.button()
    cmds.setParent( '..' )

    cmds.tabLayout( tabs, edit=True, tabLabel=((tab1, 'Assets Manager'), (tab2, 'cleaning Tools')) )
    cmds.showWindow("mobiPipeWD")

mobiPipe()
