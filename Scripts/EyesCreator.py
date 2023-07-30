# primera parte / create joint


from maya import cmds, OpenMaya

center = 'center'
vtx = cmds.ls(sl = 1 , fl = 1)


for v in vtx :
    cmds.select(cl = 1)
    jnt = cmds.joint()
    post = cmds.xform(v , q =1 , ws =1, t =1)
    cmds.xform(jnt , ws =1 , t = post)
    posC = cmds.xform(center , q =1 , ws =1, t =1)
    cmds.select(cl =1)
    jntC = cmds.joint()
    cmds.xform(jntC , ws =1 , t = posC )
    cmds.parent(jnt, jntC)
    #joint -e  -oj xyz -secondaryAxisOrient yup -ch -zso;
    cmds.joint (jntC , e= 1 , oj = 'xyz' , secondaryAxisOrient= 'yup', ch = 1 , zso =1 )

# segunda parte

sel = cmds.ls(sl =1)

for s in sel :
    loc = cmds.spaceLocator()[0]
    pos = cmds.xform(s , q =1 , ws =1 , t =1 )
    cmds.xform(loc, ws =1 , t = pos)
    par = cmds.listRelatives (s , p =1)[0]

     # aimCostraint

     cmds.aimConstraint(loc, par , mo = 1 , weight = 1 , aimVector = (1,0,0), upVector = (0,1,0),  worldUpType = 'object' , worldUpObject = 'L_guiaUpEyesSnake_LOC')

    
# conetion winth curve and point
from maya import cmds, OpenMaya

sel = cmds.ls(sl =1)
crv = "L_lowEyesHigh_CVShape"
for s in sel :
    pos = cmds.xform(s ,q = 1 , ws = 1 , t = 1)
    u = getUParam(pos , crv)
    name = s.replace("_LOC" , "_PCI")
    pci = cmds.createNode("pointOnCurveInfo" , n = name )
    cmds.connectAttr(crv + '.worldSpace' , pci + '.inputCurve')
    cmds.setAttr(pci + '.parameter' , u )
    cmds.connectAttr( pci + '.position' , s + '.t')

#-----------------------------------------------------------------------------------------------    

def getUParam( pnt = [], crv = None):

    point = OpenMaya.MPoint(pnt[0],pnt[1],pnt[2])
    curveFn = OpenMaya.MFnNurbsCurve(getDagPath(crv))
    paramUtill=OpenMaya.MScriptUtil()
    paramPtr=paramUtill.asDoublePtr()
    isOnCurve = curveFn.isPointOnCurve(point)
    if isOnCurve == False:
        
        curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
    else :
        point = curveFn.closestPoint(point,paramPtr,0.001,OpenMaya.MSpace.kObject)
        curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
    
    param = paramUtill.getDouble(paramPtr)  
    return param

def getDagPath( objectName):
    
    if isinstance(objectName, list)==True:
        oNodeList=[]
        for o in objectName:
            selectionList = OpenMaya.MSelectionList()
            selectionList.add(o)
            oNode = OpenMaya.MDagPath()
            selectionList.getDagPath(0, oNode)
            oNodeList.append(oNode)
        return oNodeList
    else:
        selectionList = OpenMaya.MSelectionList()
        selectionList.add(objectName)
        oNode = OpenMaya.MDagPath()
        selectionList.getDagPath(0, oNode)
        return oNode