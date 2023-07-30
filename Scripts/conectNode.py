import maya.cmds as cmds


crv = "L_curve01_CRVShape"
motPath = cmds.createNode ("motionPath")
jnt = cmds.joint()
cmds.connectAttr(crv + '.worldSpace' , motPath + '.geometryPath')
cmds.connectAttr(motPath + '.allCoordinates' , jnt + '.translate')
cmds.connectAttr(motPath + '.rotate' , jnt + '.rotate')

