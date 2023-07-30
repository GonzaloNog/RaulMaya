import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore

class CuboDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CuboDialog, self).__init__(parent)
        self.setWindowTitle("PROBANDO")
        self.setFixedSize(500, 500)

        self.nombre_label = QtWidgets.QLabel("Nombre 1")
        self.ancho_label = QtWidgets.QLabel("Nombre 2")

        self.nombre_input = QtWidgets.QLineEdit()

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.nombre_label, 0, 0)
        layout.addWidget(self.nombre_input, 0, 1, 1, 1)
        

        self.setLayout(layout)

ventana = CuboDialog()
ventana.show()