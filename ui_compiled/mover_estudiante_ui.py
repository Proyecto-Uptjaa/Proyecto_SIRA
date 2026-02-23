# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mover_estudiante.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QLabel, QSizePolicy,
    QWidget)

class Ui_mover_estudiante(object):
    def setupUi(self, mover_estudiante):
        if not mover_estudiante.objectName():
            mover_estudiante.setObjectName(u"mover_estudiante")
        mover_estudiante.resize(300, 145)
        mover_estudiante.setMinimumSize(QSize(300, 145))
        mover_estudiante.setMaximumSize(QSize(300, 145))
        mover_estudiante.setStyleSheet(u"background-color: #f5f6fa;\n"
"color: #2d2d2d;")
        self.buttonBox = QDialogButtonBox(mover_estudiante)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(40, 100, 191, 32))
        self.buttonBox.setStyleSheet(u"color: #2d2d2d;")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.frGrado_reg_estu_2 = QFrame(mover_estudiante)
        self.frGrado_reg_estu_2.setObjectName(u"frGrado_reg_estu_2")
        self.frGrado_reg_estu_2.setGeometry(QRect(70, 50, 151, 30))
        self.frGrado_reg_estu_2.setMinimumSize(QSize(70, 30))
        self.frGrado_reg_estu_2.setMaximumSize(QSize(200, 40))
        self.frGrado_reg_estu_2.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #2980b9;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frGrado_reg_estu_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frGrado_reg_estu_2.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxMover_estudiante = QComboBox(self.frGrado_reg_estu_2)
        self.cbxMover_estudiante.addItem("")
        self.cbxMover_estudiante.addItem("")
        self.cbxMover_estudiante.addItem("")
        self.cbxMover_estudiante.setObjectName(u"cbxMover_estudiante")
        self.cbxMover_estudiante.setGeometry(QRect(5, 5, 141, 21))
        self.cbxMover_estudiante.setMaximumSize(QSize(180, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(True)
        self.cbxMover_estudiante.setFont(font)
        self.cbxMover_estudiante.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxMover_estudiante.setStyleSheet(u"QComboBox {\n"
"			combobox-popup: 0;\n"
"            border-radius: 10px;\n"
"            padding: 2px 8px;\n"
"            background-color: white;\n"
"            color: #2d2d2d;\n"
"   \n"
"        }\n"
"        QComboBox:hover {\n"
"            border-color: #0D47A1;\n"
"        }\n"
"        \n"
"        QComboBox QAbstractItemView {\n"
"            background-color: white;\n"
"            border: 1.5px solid #2980b9;\n"
"            border-radius: 8px;\n"
"            color: #2d2d2d;\n"
"            outline: none;\n"
"            padding: 4px 0px;\n"
"        }\n"
"        QComboBox QAbstractItemView::item {\n"
"            min-height: 20px;\n"
"            padding: 3px 5px;\n"
"        }\n"
"        QComboBox QAbstractItemView::item:selected {\n"
"            background-color: #2980b9;\n"
"            color: white;\n"
"        }\n"
"        QComboBox QAbstractItemView QScrollBar:vertical {\n"
"            border: none;\n"
"            background: #f0f7ff;\n"
"            width: 7px;\n"
"            bor"
                        "der-radius: 3px;\n"
"            margin: 4px 2px;\n"
"        }\n"
"        QComboBox QAbstractItemView QScrollBar::handle:vertical {\n"
"            background: #2980b9;\n"
"            border-radius: 3px;\n"
"            min-height: 20px;\n"
"        }\n"
"        QComboBox QAbstractItemView QScrollBar::add-line:vertical,\n"
"        QComboBox QAbstractItemView QScrollBar::sub-line:vertical {\n"
"            height: 0px;\n"
"        }")
        self.cbxMover_estudiante.setIconSize(QSize(5, 5))
        self.lblStudent_dir = QLabel(mover_estudiante)
        self.lblStudent_dir.setObjectName(u"lblStudent_dir")
        self.lblStudent_dir.setGeometry(QRect(20, 10, 261, 30))
        self.lblStudent_dir.setMinimumSize(QSize(0, 30))
        self.lblStudent_dir.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblStudent_dir.setFont(font1)
        self.lblStudent_dir.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_dir.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(mover_estudiante)
        self.buttonBox.accepted.connect(mover_estudiante.accept)
        self.buttonBox.rejected.connect(mover_estudiante.reject)

        QMetaObject.connectSlotsByName(mover_estudiante)
    # setupUi

    def retranslateUi(self, mover_estudiante):
        mover_estudiante.setWindowTitle(QCoreApplication.translate("mover_estudiante", u"Dialog", None))
        self.cbxMover_estudiante.setItemText(0, "")
        self.cbxMover_estudiante.setItemText(1, QCoreApplication.translate("mover_estudiante", u"Inicial", None))
        self.cbxMover_estudiante.setItemText(2, QCoreApplication.translate("mover_estudiante", u"Primaria", None))

        self.lblStudent_dir.setText(QCoreApplication.translate("mover_estudiante", u"Seleccione la secci\u00f3n de destino", None))
    # retranslateUi

