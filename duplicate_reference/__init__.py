# -*- coding: utf-8 -*-

import os.path

import pymel.core as pm
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

from PySide2 import QtCore, QtGui, QtWidgets

import ui.main_ui as main_ui

DEFAULT_ATTR = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']


class MainUI(MayaQWidgetBaseMixin, QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        super(MainUI, self).__init__(*args, **kwargs)

        self.ui = main_ui.Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle(u"duplicate_reference_tool v1.0")

        self.ui.submit.clicked.connect(self.submit)

    def get_copy_attr(self):

        copy_attr = []

        if self.ui.is_translate.isChecked():
            copy_attr += ['tx', 'ty', 'tz']
        if self.ui.is_rotate.isChecked():
            copy_attr += ['rx', 'ry', 'rz']
        if self.ui.is_scale.isChecked():
            copy_attr += ['sx', 'sy', 'sz']
        if self.ui.is_visible.isChecked():
            copy_attr += ['v']
        if self.ui.is_other.isChecked():
            copy_attr += ['<other_attr>']
        return copy_attr

    def submit(self):

        copy_attr = self.get_copy_attr()
        dubplicate_reference(copy_attr, self.ui.is_anim_key.isChecked())


def dubplicate_reference(copy_attrs=DEFAULT_ATTR,
                         copy_anim=False):
    """
    選択しているリファレンスノードを複製する    
    """

    sel_node = pm.ls(sl=True)

    load_reference = []
    for i in sel_node:
        ref_node = i.referenceFile()
        if i.referenceFile() not in load_reference:
            load_reference.append(ref_node)

    for ref in load_reference:

        path   = ref.path
        bn     = os.path.splitext(os.path.basename(path))[0]
        to_ref = pm.createReference(path, ns=bn)
        to_ns  = to_ref.namespace

        for n in ref.nodes():
            if n.type() == "transform":
                to_pynode = pm.PyNode(n.name().replace(ref.namespace + ":", to_ns + ":"))
                for attr in n.listAttr():
                    # コピーするアトリビュートかチェックする
                    # Keyを指定できて、かつLockがかかっていないアトリビュートをコピーする
                    if attr.isKeyable() and attr.isLocked() is False:
                        attr_name = attr.plugAttr()
                        # copy_attrsで指定したアトリビュートのみコピーする
                        if attr_name not in copy_attrs and '<other_attr>' not in copy_attrs:
                            continue
                        # constraintがあったらなにもしない
                        if len(attr.connections(scn=True, type="constraint")) != 0:
                            continue
                        to_pynode.attr(attr_name).set(attr.get())
                        # AnimationNodeが刺さってたらKeyをコピーする
                        if copy_anim:
                            if len(attr.connections(scn=True, type="animCurve")) != 0:
                                pm.copyKey(n, attribute=attr.plugAttr())
                                pm.pasteKey(to_pynode, attribute=attr_name)


if __name__ == "__main__":
    a = MainUI()
    a.show()
