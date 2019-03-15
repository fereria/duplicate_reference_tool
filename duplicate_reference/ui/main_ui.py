# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'S:\work\proj\script_work\maya_scripts\duplicate_reference\ui\main_ui.ui'
#
# Created: Fri Mar 15 21:30:27 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(456, 139)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.is_translate = QtWidgets.QCheckBox(Form)
        self.is_translate.setChecked(True)
        self.is_translate.setObjectName("is_translate")
        self.gridLayout.addWidget(self.is_translate, 0, 0, 1, 1)
        self.is_rotate = QtWidgets.QCheckBox(Form)
        self.is_rotate.setChecked(True)
        self.is_rotate.setObjectName("is_rotate")
        self.gridLayout.addWidget(self.is_rotate, 0, 1, 1, 1)
        self.is_scale = QtWidgets.QCheckBox(Form)
        self.is_scale.setChecked(True)
        self.is_scale.setObjectName("is_scale")
        self.gridLayout.addWidget(self.is_scale, 0, 2, 1, 1)
        self.is_visible = QtWidgets.QCheckBox(Form)
        self.is_visible.setChecked(True)
        self.is_visible.setObjectName("is_visible")
        self.gridLayout.addWidget(self.is_visible, 1, 0, 1, 1)
        self.is_other = QtWidgets.QCheckBox(Form)
        self.is_other.setChecked(True)
        self.is_other.setObjectName("is_other")
        self.gridLayout.addWidget(self.is_other, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.is_anim_key = QtWidgets.QCheckBox(Form)
        self.is_anim_key.setObjectName("is_anim_key")
        self.horizontalLayout.addWidget(self.is_anim_key)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.submit = QtWidgets.QPushButton(Form)
        self.submit.setObjectName("submit")
        self.verticalLayout.addWidget(self.submit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "リファレンス読み込み時にコピーするアトリビュート", None, -1))
        self.is_translate.setText(QtWidgets.QApplication.translate("Form", "Translate", None, -1))
        self.is_rotate.setText(QtWidgets.QApplication.translate("Form", "Rotate", None, -1))
        self.is_scale.setText(QtWidgets.QApplication.translate("Form", "Scale", None, -1))
        self.is_visible.setText(QtWidgets.QApplication.translate("Form", "Visible", None, -1))
        self.is_other.setText(QtWidgets.QApplication.translate("Form", "OtherAttribute", None, -1))
        self.is_anim_key.setText(QtWidgets.QApplication.translate("Form", "アニメーションキーがあれば、アニメーションをコピー", None, -1))
        self.submit.setText(QtWidgets.QApplication.translate("Form", "リファレンスを複製！", None, -1))

