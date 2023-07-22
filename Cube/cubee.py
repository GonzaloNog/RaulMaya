import maya.cmds as cmds

def crear_cubo():
    # Verificar si ya existe un cubo en la escena con el mismo nombre, y eliminarlo si es necesario
    if cmds.objExists('mi_cubo'):
        cmds.delete('mi_cubo')
    
    # Crear un cubo con un nombre específico ('mi_cubo') y tamaño predeterminado
    cmds.polyCube(w=1, h=1, d=1, name='mi_cubo')
    
# Llamar a la función para crear el cubo
crear_cubo()