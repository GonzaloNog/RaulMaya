import maya.cmds as cmds

selection = cmds.ls(selection=True)
# print (selection)
if len(selection) < 2:
    cmds.warning('seleciona target uno o mas ')
else:
    print ('vamos a alinear')
    target = selection[0] # target (primer elemento)
    for i in range(1, len(selection)):
        objecto = selection[i]
        constraint = cmds.parentConstraint(target, objecto, maintainOffset = False)
        #print(constraint)
        cmds.delete(constraint)
    
    
    
        



