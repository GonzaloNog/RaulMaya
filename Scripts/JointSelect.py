import maya.cmds as cmds

# hacemos una lista de lo seleccionado
sel = cmds.ls (sl = 1)[0]

# cogemos los huesos que influyen en el skinCluster del objeto seleccionado
infList = cmds.skinCluster (sel, q=True, inf = True)

# selecciona todos los objetos de la variable infList
cmds.select (infList)