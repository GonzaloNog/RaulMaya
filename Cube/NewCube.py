import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore

class CuboDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CuboDialog, self).__init__(parent)
        self.setWindowTitle("Crear Cubo")
        self.setFixedSize(250, 150)

        self.nombre_label = QtWidgets.QLabel("Nombre del Cubo:")
        self.ancho_label = QtWidgets.QLabel("Ancho:")
        self.alto_label = QtWidgets.QLabel("Alto:")
        self.profundidad_label = QtWidgets.QLabel("Profundidad:")

        self.nombre_input = QtWidgets.QLineEdit()
        self.ancho_input = QtWidgets.QDoubleSpinBox()
        self.ancho_input.setRange(0.1, 1000.0)
        self.alto_input = QtWidgets.QDoubleSpinBox()
        self.alto_input.setRange(0.1, 1000.0)
        self.profundidad_input = QtWidgets.QDoubleSpinBox()
        self.profundidad_input.setRange(0.1, 1000.0)

        self.crear_cubo_button = QtWidgets.QPushButton("Crear Cubo")
        self.crear_cubo_button.clicked.connect(self.crear_cubo)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.nombre_label, 0, 0)
        layout.addWidget(self.nombre_input, 0, 1, 1, 2)
        layout.addWidget(self.ancho_label, 1, 0)
        layout.addWidget(self.ancho_input, 1, 1)
        layout.addWidget(self.alto_label, 2, 0)
        layout.addWidget(self.alto_input, 2, 1)
        layout.addWidget(self.profundidad_label, 3, 0)
        layout.addWidget(self.profundidad_input, 3, 1)
        layout.addWidget(self.crear_cubo_button, 4, 0, 1, 3)

        self.setLayout(layout)

    def crear_cubo(self):
        nombre_cubo = self.nombre_input.text()
        ancho = self.ancho_input.value()
        alto = self.alto_input.value()
        profundidad = self.profundidad_input.value()

        # Verificar si ya existe un cubo en la escena con el mismo nombre, y eliminarlo si es necesario
        if cmds.objExists(nombre_cubo):
            cmds.delete(nombre_cubo)

        # Crear un cubo con el nombre proporcionado y los tamaños ingresados por el usuario
        cmds.polyCube(w=ancho, h=alto, d=profundidad, name=nombre_cubo)

# Crear la ventana personalizada y mostrarla
dialog = CuboDialog()
dialog.show()