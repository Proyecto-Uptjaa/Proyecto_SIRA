# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crear_seccion.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
from resources import resources_ui

class Ui_crear_seccion(object):
    def setupUi(self, crear_seccion):
        if not crear_seccion.objectName():
            crear_seccion.setObjectName(u"crear_seccion")
        crear_seccion.resize(330, 468)
        crear_seccion.setMinimumSize(QSize(330, 415))
        crear_seccion.setMaximumSize(QSize(330, 468))
        crear_seccion.setStyleSheet(u"background-color: #f5f6fa;")
        self.verticalLayout = QVBoxLayout(crear_seccion)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widgetPrincipal = QWidget(crear_seccion)
        self.widgetPrincipal.setObjectName(u"widgetPrincipal")
        self.widgetPrincipal.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widgetPrincipal.setStyleSheet(u"QWidget{\n"
"	background-color: #F7F9FC;\n"
"	color: #2d2d2d;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 2px 5px;\n"
"    background-color: white;\n"
"	color: #2d2d2d;\n"
"}\n"
"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 4px 6px;\n"
"    border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widgetPrincipal)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblTitulo_login = QLabel(self.widgetPrincipal)
        self.lblTitulo_login.setObjectName(u"lblTitulo_login")
        self.lblTitulo_login.setMinimumSize(QSize(241, 21))
        self.lblTitulo_login.setMaximumSize(QSize(250, 21))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.lblTitulo_login.setFont(font)
        self.lblTitulo_login.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblTitulo_login.setStyleSheet(u"")
        self.lblTitulo_login.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lblTitulo_login, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frameRol_login_4 = QFrame(self.widgetPrincipal)
        self.frameRol_login_4.setObjectName(u"frameRol_login_4")
        self.frameRol_login_4.setMinimumSize(QSize(225, 35))
        self.frameRol_login_4.setMaximumSize(QSize(225, 35))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.frameRol_login_4.setFont(font1)
        self.frameRol_login_4.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #1e88e5;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox{\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frameRol_login_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameRol_login_4.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxNivel_crear_seccion = QComboBox(self.frameRol_login_4)
        self.cbxNivel_crear_seccion.addItem("")
        self.cbxNivel_crear_seccion.addItem("")
        self.cbxNivel_crear_seccion.addItem("")
        self.cbxNivel_crear_seccion.setObjectName(u"cbxNivel_crear_seccion")
        self.cbxNivel_crear_seccion.setGeometry(QRect(11, 5, 201, 26))
        self.cbxNivel_crear_seccion.setMinimumSize(QSize(201, 26))
        self.cbxNivel_crear_seccion.setMaximumSize(QSize(201, 26))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(13)
        self.cbxNivel_crear_seccion.setFont(font2)
        self.cbxNivel_crear_seccion.setStyleSheet(u"")
        self.cbxNivel_crear_seccion.setIconSize(QSize(10, 10))

        self.verticalLayout_2.addWidget(self.frameRol_login_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frameRol_login_2 = QFrame(self.widgetPrincipal)
        self.frameRol_login_2.setObjectName(u"frameRol_login_2")
        self.frameRol_login_2.setMinimumSize(QSize(225, 35))
        self.frameRol_login_2.setMaximumSize(QSize(225, 35))
        self.frameRol_login_2.setFont(font1)
        self.frameRol_login_2.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #1e88e5;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox{\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frameRol_login_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameRol_login_2.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxGrado_crear_seccion = QComboBox(self.frameRol_login_2)
        self.cbxGrado_crear_seccion.addItem("")
        self.cbxGrado_crear_seccion.addItem("")
        self.cbxGrado_crear_seccion.addItem("")
        self.cbxGrado_crear_seccion.addItem("")
        self.cbxGrado_crear_seccion.addItem("")
        self.cbxGrado_crear_seccion.setObjectName(u"cbxGrado_crear_seccion")
        self.cbxGrado_crear_seccion.setGeometry(QRect(11, 5, 201, 26))
        self.cbxGrado_crear_seccion.setMinimumSize(QSize(201, 26))
        self.cbxGrado_crear_seccion.setMaximumSize(QSize(201, 26))
        self.cbxGrado_crear_seccion.setFont(font2)
        self.cbxGrado_crear_seccion.setStyleSheet(u"")
        self.cbxGrado_crear_seccion.setIconSize(QSize(10, 10))

        self.verticalLayout_2.addWidget(self.frameRol_login_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frameRol_login_3 = QFrame(self.widgetPrincipal)
        self.frameRol_login_3.setObjectName(u"frameRol_login_3")
        self.frameRol_login_3.setMinimumSize(QSize(225, 35))
        self.frameRol_login_3.setMaximumSize(QSize(225, 35))
        self.frameRol_login_3.setFont(font1)
        self.frameRol_login_3.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #1e88e5;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox{\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frameRol_login_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameRol_login_3.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxLetra_crear_seccion = QComboBox(self.frameRol_login_3)
        self.cbxLetra_crear_seccion.addItem("")
        self.cbxLetra_crear_seccion.addItem("")
        self.cbxLetra_crear_seccion.addItem("")
        self.cbxLetra_crear_seccion.addItem("")
        self.cbxLetra_crear_seccion.setObjectName(u"cbxLetra_crear_seccion")
        self.cbxLetra_crear_seccion.setGeometry(QRect(11, 5, 201, 26))
        self.cbxLetra_crear_seccion.setMinimumSize(QSize(201, 26))
        self.cbxLetra_crear_seccion.setMaximumSize(QSize(201, 26))
        self.cbxLetra_crear_seccion.setFont(font2)
        self.cbxLetra_crear_seccion.setStyleSheet(u"")
        self.cbxLetra_crear_seccion.setIconSize(QSize(10, 10))

        self.verticalLayout_2.addWidget(self.frameRol_login_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lneSalon_crear_seccion = QLineEdit(self.widgetPrincipal)
        self.lneSalon_crear_seccion.setObjectName(u"lneSalon_crear_seccion")
        self.lneSalon_crear_seccion.setMinimumSize(QSize(225, 35))
        self.lneSalon_crear_seccion.setMaximumSize(QSize(225, 35))
        self.lneSalon_crear_seccion.setFont(font1)
        self.lneSalon_crear_seccion.setMouseTracking(True)
        self.lneSalon_crear_seccion.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneSalon_crear_seccion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lneSalon_crear_seccion, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lneCupo_crear_seccion = QLineEdit(self.widgetPrincipal)
        self.lneCupo_crear_seccion.setObjectName(u"lneCupo_crear_seccion")
        self.lneCupo_crear_seccion.setMinimumSize(QSize(225, 35))
        self.lneCupo_crear_seccion.setMaximumSize(QSize(225, 35))
        self.lneCupo_crear_seccion.setFont(font1)
        self.lneCupo_crear_seccion.setMouseTracking(True)
        self.lneCupo_crear_seccion.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneCupo_crear_seccion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lneCupo_crear_seccion, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btnAsignar_materias = QPushButton(self.widgetPrincipal)
        self.btnAsignar_materias.setObjectName(u"btnAsignar_materias")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAsignar_materias.sizePolicy().hasHeightForWidth())
        self.btnAsignar_materias.setSizePolicy(sizePolicy)
        self.btnAsignar_materias.setMinimumSize(QSize(200, 35))
        self.btnAsignar_materias.setMaximumSize(QSize(225, 35))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.btnAsignar_materias.setFont(font3)
        self.btnAsignar_materias.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAsignar_materias.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnAsignar_materias.setStyleSheet(u"QPushButton:{\n"
"background-color: #2980b9;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/nueva_materia.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAsignar_materias.setIcon(icon)
        self.btnAsignar_materias.setIconSize(QSize(18, 18))

        self.verticalLayout_2.addWidget(self.btnAsignar_materias, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btnCrear_seccion = QPushButton(self.widgetPrincipal)
        self.btnCrear_seccion.setObjectName(u"btnCrear_seccion")
        sizePolicy.setHeightForWidth(self.btnCrear_seccion.sizePolicy().hasHeightForWidth())
        self.btnCrear_seccion.setSizePolicy(sizePolicy)
        self.btnCrear_seccion.setMinimumSize(QSize(200, 35))
        self.btnCrear_seccion.setMaximumSize(QSize(200, 35))
        self.btnCrear_seccion.setFont(font3)
        self.btnCrear_seccion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCrear_seccion.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnCrear_seccion.setStyleSheet(u"QPushButton {\n"
"	background-color: #27ae60;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 6px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 124, 70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/confirm_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCrear_seccion.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.btnCrear_seccion, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btnCancelar_crear_seccion = QPushButton(self.widgetPrincipal)
        self.btnCancelar_crear_seccion.setObjectName(u"btnCancelar_crear_seccion")
        sizePolicy.setHeightForWidth(self.btnCancelar_crear_seccion.sizePolicy().hasHeightForWidth())
        self.btnCancelar_crear_seccion.setSizePolicy(sizePolicy)
        self.btnCancelar_crear_seccion.setMinimumSize(QSize(140, 35))
        self.btnCancelar_crear_seccion.setMaximumSize(QSize(160, 35))
        self.btnCancelar_crear_seccion.setFont(font3)
        self.btnCancelar_crear_seccion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCancelar_crear_seccion.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnCancelar_crear_seccion.setStyleSheet(u"background-color: white;\n"
"color: #2980b9;\n"
"border: 1.5px solid #2980b9;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/cancelar_b2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCancelar_crear_seccion.setIcon(icon2)
        self.btnCancelar_crear_seccion.setIconSize(QSize(18, 18))

        self.verticalLayout_2.addWidget(self.btnCancelar_crear_seccion, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.widgetPrincipal)


        self.retranslateUi(crear_seccion)

        QMetaObject.connectSlotsByName(crear_seccion)
    # setupUi

    def retranslateUi(self, crear_seccion):
        crear_seccion.setWindowTitle(QCoreApplication.translate("crear_seccion", u"Dialog", None))
        self.lblTitulo_login.setText(QCoreApplication.translate("crear_seccion", u"Crear nueva secci\u00f3n", None))
        self.cbxNivel_crear_seccion.setItemText(0, QCoreApplication.translate("crear_seccion", u"Nivel educaci\u00f3n", None))
        self.cbxNivel_crear_seccion.setItemText(1, QCoreApplication.translate("crear_seccion", u"Inicial", None))
        self.cbxNivel_crear_seccion.setItemText(2, QCoreApplication.translate("crear_seccion", u"Primaria", None))

        self.cbxGrado_crear_seccion.setItemText(0, QCoreApplication.translate("crear_seccion", u"Grado", None))
        self.cbxGrado_crear_seccion.setItemText(1, QCoreApplication.translate("crear_seccion", u"1er nivel", None))
        self.cbxGrado_crear_seccion.setItemText(2, QCoreApplication.translate("crear_seccion", u"2do nivel", None))
        self.cbxGrado_crear_seccion.setItemText(3, QCoreApplication.translate("crear_seccion", u"3er nivel", None))
        self.cbxGrado_crear_seccion.setItemText(4, QCoreApplication.translate("crear_seccion", u"1er grado", None))

        self.cbxLetra_crear_seccion.setItemText(0, QCoreApplication.translate("crear_seccion", u"Letra", None))
        self.cbxLetra_crear_seccion.setItemText(1, QCoreApplication.translate("crear_seccion", u"A", None))
        self.cbxLetra_crear_seccion.setItemText(2, QCoreApplication.translate("crear_seccion", u"B", None))
        self.cbxLetra_crear_seccion.setItemText(3, QCoreApplication.translate("crear_seccion", u"C", None))

        self.lneSalon_crear_seccion.setText("")
        self.lneSalon_crear_seccion.setPlaceholderText(QCoreApplication.translate("crear_seccion", u"Sal\u00f3n/Aula", None))
        self.lneCupo_crear_seccion.setText("")
        self.lneCupo_crear_seccion.setPlaceholderText(QCoreApplication.translate("crear_seccion", u"Cupo", None))
        self.btnAsignar_materias.setText(QCoreApplication.translate("crear_seccion", u"Asignar materias", None))
        self.btnCrear_seccion.setText(QCoreApplication.translate("crear_seccion", u"Crear", None))
        self.btnCancelar_crear_seccion.setText(QCoreApplication.translate("crear_seccion", u"Cancelar", None))
    # retranslateUi

