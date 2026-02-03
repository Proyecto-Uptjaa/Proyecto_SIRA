# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asignar_materias.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)
from resources import resources_ui

class Ui_asignar_materias(object):
    def setupUi(self, asignar_materias):
        if not asignar_materias.objectName():
            asignar_materias.setObjectName(u"asignar_materias")
        asignar_materias.resize(400, 485)
        asignar_materias.setMinimumSize(QSize(330, 485))
        asignar_materias.setMaximumSize(QSize(400, 500))
        asignar_materias.setStyleSheet(u"background-color: #f5f6fa;")
        self.verticalLayout = QVBoxLayout(asignar_materias)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widgetPrincipal = QWidget(asignar_materias)
        self.widgetPrincipal.setObjectName(u"widgetPrincipal")
        self.widgetPrincipal.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widgetPrincipal.setStyleSheet(u"QWidget{\n"
"	background-color: #F7F9FC;\n"
"	font-family: \"Segoe UI\";\n"
"color: #2d2d2d;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 2px 8px;\n"
"    background-color: white;\n"
"	color: #2d2d2d;\n"
"}\n"
"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 10px;\n"
"    border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widgetPrincipal)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lblTitulo_asignar_materia = QLabel(self.widgetPrincipal)
        self.lblTitulo_asignar_materia.setObjectName(u"lblTitulo_asignar_materia")
        self.lblTitulo_asignar_materia.setMinimumSize(QSize(241, 21))
        self.lblTitulo_asignar_materia.setMaximumSize(QSize(250, 21))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.lblTitulo_asignar_materia.setFont(font)
        self.lblTitulo_asignar_materia.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblTitulo_asignar_materia.setStyleSheet(u"")
        self.lblTitulo_asignar_materia.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.lblTitulo_asignar_materia, 0, Qt.AlignmentFlag.AlignHCenter)

        self.scrollArea_asignar_materia = QScrollArea(self.widgetPrincipal)
        self.scrollArea_asignar_materia.setObjectName(u"scrollArea_asignar_materia")
        self.scrollArea_asignar_materia.setMinimumSize(QSize(361, 0))
        self.scrollArea_asignar_materia.setMaximumSize(QSize(361, 330))
        self.scrollArea_asignar_materia.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 359, 328))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_asignar_materia = QWidget(self.scrollAreaWidgetContents)
        self.widget_asignar_materia.setObjectName(u"widget_asignar_materia")
        self.verticalLayout_2 = QVBoxLayout(self.widget_asignar_materia)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.chkAsignar_materia = QCheckBox(self.widget_asignar_materia)
        self.chkAsignar_materia.setObjectName(u"chkAsignar_materia")

        self.verticalLayout_2.addWidget(self.chkAsignar_materia)


        self.verticalLayout_3.addWidget(self.widget_asignar_materia)

        self.scrollArea_asignar_materia.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea_asignar_materia, 0, Qt.AlignmentFlag.AlignHCenter)

        self.chkSelec_todas = QCheckBox(self.widgetPrincipal)
        self.chkSelec_todas.setObjectName(u"chkSelec_todas")
        self.chkSelec_todas.setMinimumSize(QSize(0, 27))
        self.chkSelec_todas.setMaximumSize(QSize(16777215, 27))
        self.chkSelec_todas.setStyleSheet(u"QCheckBox {\n"
"    spacing: 8px;\n"
"    color: #2d2d2d;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 22px;\n"
"    height: 22px;\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 6px;\n"
"    background: #ffffff;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    border: 2px solid #1565C0;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #1565C0;\n"
"    background: #2980b9;  /* mantener blanco para que Qt pinte la palomita */\n"
"}")

        self.verticalLayout_4.addWidget(self.chkSelec_todas)

        self.frame = QFrame(self.widgetPrincipal)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(361, 0))
        self.frame.setMaximumSize(QSize(361, 51))
        self.frame.setStyleSheet(u"border: transparent;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.btnGuardar_asignar_materias = QPushButton(self.frame)
        self.btnGuardar_asignar_materias.setObjectName(u"btnGuardar_asignar_materias")
        self.btnGuardar_asignar_materias.setGeometry(QRect(230, 10, 120, 35))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGuardar_asignar_materias.sizePolicy().hasHeightForWidth())
        self.btnGuardar_asignar_materias.setSizePolicy(sizePolicy)
        self.btnGuardar_asignar_materias.setMinimumSize(QSize(120, 35))
        self.btnGuardar_asignar_materias.setMaximumSize(QSize(120, 35))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.btnGuardar_asignar_materias.setFont(font1)
        self.btnGuardar_asignar_materias.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGuardar_asignar_materias.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnGuardar_asignar_materias.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/confirm_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGuardar_asignar_materias.setIcon(icon)
        self.btnCancelar_asignar_materias = QPushButton(self.frame)
        self.btnCancelar_asignar_materias.setObjectName(u"btnCancelar_asignar_materias")
        self.btnCancelar_asignar_materias.setGeometry(QRect(10, 10, 120, 35))
        sizePolicy.setHeightForWidth(self.btnCancelar_asignar_materias.sizePolicy().hasHeightForWidth())
        self.btnCancelar_asignar_materias.setSizePolicy(sizePolicy)
        self.btnCancelar_asignar_materias.setMinimumSize(QSize(120, 35))
        self.btnCancelar_asignar_materias.setMaximumSize(QSize(120, 35))
        self.btnCancelar_asignar_materias.setFont(font1)
        self.btnCancelar_asignar_materias.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCancelar_asignar_materias.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnCancelar_asignar_materias.setStyleSheet(u"background-color: white;\n"
"color: #2980b9;\n"
"border: 1.5px solid #2980b9;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/cancelar_b2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCancelar_asignar_materias.setIcon(icon1)
        self.btnCancelar_asignar_materias.setIconSize(QSize(18, 18))

        self.verticalLayout_4.addWidget(self.frame)


        self.verticalLayout.addWidget(self.widgetPrincipal)


        self.retranslateUi(asignar_materias)

        QMetaObject.connectSlotsByName(asignar_materias)
    # setupUi

    def retranslateUi(self, asignar_materias):
        asignar_materias.setWindowTitle(QCoreApplication.translate("asignar_materias", u"Dialog", None))
        self.lblTitulo_asignar_materia.setText(QCoreApplication.translate("asignar_materias", u"Asignar materias", None))
        self.chkAsignar_materia.setText(QCoreApplication.translate("asignar_materias", u"CheckBox", None))
        self.chkSelec_todas.setText(QCoreApplication.translate("asignar_materias", u"Seleccionar todas", None))
        self.btnGuardar_asignar_materias.setText(QCoreApplication.translate("asignar_materias", u"Guardar", None))
        self.btnCancelar_asignar_materias.setText(QCoreApplication.translate("asignar_materias", u"Cancelar", None))
    # retranslateUi

