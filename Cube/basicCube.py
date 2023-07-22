import maya.cmds as cmds

def crear_cubo():
    # Verificar si ya existe un cubo en la escena con el mismo nombre, y eliminarlo si es necesario
    if cmds.objExists('mi_cubo'):
        cmds.delete('mi_cubo')
    
    # Obtener los valores ingresados por el usuario para los tamaños del cubo
    ancho = float(input("Ingrese el ancho del cubo: "))
    alto = float(input("Ingrese el alto del cubo: "))
    profundidad = float(input("Ingrese la profundidad del cubo: "))
    
    # Crear un cubo con un nombre específico ('mi_cubo') y los tamaños proporcionados por el usuario
    cmds.polyCube(w=ancho, h=alto, d=profundidad, name='mi_cubo')
    
# Llamar a la función para crear el cubo
crear_cubo()