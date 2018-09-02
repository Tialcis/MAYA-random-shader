import os
import pprint

from maya import cmds

import randomShader as rs
reload(rs)
from PySide2 import QtWidgets as qw
from PySide2 import QtCore, QtGui


class RandomShaderUI(qw.QDialog):
    """
    The RandomShaderUI is a dialog that lets us apply any shaders to any objects randomly
    """

    def __init__(self):
        super(RandomShaderUI, self).__init__()

        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.setWindowTitle('Random Shader')
        self.shader = rs.RandomShader()


        self.buildUI()

    def buildUI(self):

        mainLayout = qw.QVBoxLayout(self)

        select_widget = qw.QWidget()
        select_layout = qw.QHBoxLayout(select_widget)
        mainLayout.addWidget(select_widget)

        bake_obj_btn = qw.QPushButton('1. Set Selection as Objects')
        bake_obj_btn.clicked.connect(self.shader.bake_objects)
        select_layout.addWidget(bake_obj_btn)

        bake_shaders_btn = qw.QPushButton('2. Set Selection as Shaders')
        bake_shaders_btn.clicked.connect(self.shader.bake_shaders)
        select_layout.addWidget(bake_shaders_btn)

        assign_widget = qw.QWidget()
        assign_layout = qw.QHBoxLayout(assign_widget)
        mainLayout.addWidget(assign_widget)

        assign_randomly_btn = qw.QPushButton('3. Assign Shaders Randomly!')
        assign_randomly_btn.clicked.connect(self.shader.assign_randomly)
        assign_layout.addWidget(assign_randomly_btn)

        assign_normal_btn = qw.QPushButton('Or Assign Rainbow Normally!')
        assign_normal_btn.clicked.connect(self.shader.assign_distribution)
        assign_layout.addWidget(assign_normal_btn)


def showUI():
    ui = RandomShaderUI()
    ui.show()

    return ui
