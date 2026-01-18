# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_inicial.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
from resources import resources_ui

class Ui_config_inicial(object):
    def setupUi(self, config_inicial):
        if not config_inicial.objectName():
            config_inicial.setObjectName(u"config_inicial")
        config_inicial.resize(500, 500)
        config_inicial.setMinimumSize(QSize(325, 340))
        config_inicial.setMaximumSize(QSize(500, 500))
        config_inicial.setStyleSheet(u"background-color: #f5f6fa;\n"
"border-radius: 15px;")
        self.verticalLayout = QVBoxLayout(config_inicial)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widgetPrincipal = QWidget(config_inicial)
        self.widgetPrincipal.setObjectName(u"widgetPrincipal")
        self.widgetPrincipal.setStyleSheet(u"QWidget{\n"
"	background-color: #F7F9FC;\n"
"color: #2d2d2d;\n"
"}")
        self.stackedWidget = QStackedWidget(self.widgetPrincipal)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 481, 431))
        self.stackedWidget.setMaximumSize(QSize(481, 431))
        self.stackedWidget.setStyleSheet(u"QStackedWidget{\n"
"background-color: transparent;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 12px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"	color: #2d2d2d;\n"
"}\n"
"QLabel{\n"
"	background-color: transparent;\n"
"}")
        self.Bienvenida = QWidget()
        self.Bienvenida.setObjectName(u"Bienvenida")
        self.lblTitulo = QLabel(self.Bienvenida)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setGeometry(QRect(50, 80, 381, 61))
        self.lblTitulo.setMinimumSize(QSize(150, 21))
        self.lblTitulo.setMaximumSize(QSize(450, 120))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50; \n"
"}")
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.lblTitulo.setWordWrap(True)
        self.lblLogo_SIRA = QLabel(self.Bienvenida)
        self.lblLogo_SIRA.setObjectName(u"lblLogo_SIRA")
        self.lblLogo_SIRA.setEnabled(True)
        self.lblLogo_SIRA.setGeometry(QRect(170, 10, 161, 61))
        self.lblLogo_SIRA.setMinimumSize(QSize(100, 21))
        self.lblLogo_SIRA.setMaximumSize(QSize(325, 120))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.lblLogo_SIRA.setFont(font1)
        self.lblLogo_SIRA.setStyleSheet(u"")
        self.lblLogo_SIRA.setPixmap(QPixmap(u":/logos/SIRA_logo_cut.png"))
        self.lblLogo_SIRA.setScaledContents(True)
        self.lblLogo_SIRA.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblLogo_SIRA.setWordWrap(False)
        self.lblTitulo_3 = QLabel(self.Bienvenida)
        self.lblTitulo_3.setObjectName(u"lblTitulo_3")
        self.lblTitulo_3.setGeometry(QRect(50, 140, 381, 91))
        self.lblTitulo_3.setMinimumSize(QSize(150, 21))
        self.lblTitulo_3.setMaximumSize(QSize(450, 120))
        self.lblTitulo_3.setFont(font)
        self.lblTitulo_3.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50; \n"
"}")
        self.lblTitulo_3.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.lblTitulo_3.setWordWrap(True)
        self.lblTitulo_4 = QLabel(self.Bienvenida)
        self.lblTitulo_4.setObjectName(u"lblTitulo_4")
        self.lblTitulo_4.setGeometry(QRect(50, 240, 381, 51))
        self.lblTitulo_4.setMinimumSize(QSize(150, 21))
        self.lblTitulo_4.setMaximumSize(QSize(450, 250))
        self.lblTitulo_4.setFont(font)
        self.lblTitulo_4.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50; \n"
"}")
        self.lblTitulo_4.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.lblTitulo_4.setWordWrap(True)
        self.lblTitulo_5 = QLabel(self.Bienvenida)
        self.lblTitulo_5.setObjectName(u"lblTitulo_5")
        self.lblTitulo_5.setGeometry(QRect(50, 300, 381, 21))
        self.lblTitulo_5.setMinimumSize(QSize(150, 21))
        self.lblTitulo_5.setMaximumSize(QSize(450, 120))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.lblTitulo_5.setFont(font2)
        self.lblTitulo_5.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50; \n"
"}")
        self.lblTitulo_5.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.lblTitulo_5.setWordWrap(True)
        self.lblTitulo_6 = QLabel(self.Bienvenida)
        self.lblTitulo_6.setObjectName(u"lblTitulo_6")
        self.lblTitulo_6.setGeometry(QRect(50, 320, 381, 101))
        self.lblTitulo_6.setMinimumSize(QSize(150, 21))
        self.lblTitulo_6.setMaximumSize(QSize(450, 120))
        self.lblTitulo_6.setFont(font)
        self.lblTitulo_6.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50; \n"
"}")
        self.lblTitulo_6.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.lblTitulo_6.setWordWrap(True)
        self.stackedWidget.addWidget(self.Bienvenida)
        self.Usuario = QWidget()
        self.Usuario.setObjectName(u"Usuario")
        self.lblLogo_SIRA_2 = QLabel(self.Usuario)
        self.lblLogo_SIRA_2.setObjectName(u"lblLogo_SIRA_2")
        self.lblLogo_SIRA_2.setEnabled(True)
        self.lblLogo_SIRA_2.setGeometry(QRect(166, 10, 101, 40))
        self.lblLogo_SIRA_2.setMinimumSize(QSize(100, 21))
        self.lblLogo_SIRA_2.setMaximumSize(QSize(325, 120))
        self.lblLogo_SIRA_2.setFont(font1)
        self.lblLogo_SIRA_2.setStyleSheet(u"")
        self.lblLogo_SIRA_2.setPixmap(QPixmap(u":/logos/SIRA_logo_cut.png"))
        self.lblLogo_SIRA_2.setScaledContents(True)
        self.lblLogo_SIRA_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblLogo_SIRA_2.setWordWrap(False)
        self.lblTitulo_2 = QLabel(self.Usuario)
        self.lblTitulo_2.setObjectName(u"lblTitulo_2")
        self.lblTitulo_2.setGeometry(QRect(50, 60, 381, 61))
        self.lblTitulo_2.setMinimumSize(QSize(150, 21))
        self.lblTitulo_2.setMaximumSize(QSize(450, 120))
        self.lblTitulo_2.setFont(font)
        self.lblTitulo_2.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50; \n"
"}")
        self.lblTitulo_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitulo_2.setWordWrap(True)
        self.line_2 = QFrame(self.Usuario)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(270, 10, 3, 40))
        self.line_2.setMinimumSize(QSize(3, 40))
        self.line_2.setMaximumSize(QSize(3, 80))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblLogo_UPTJAA_acercade = QLabel(self.Usuario)
        self.lblLogo_UPTJAA_acercade.setObjectName(u"lblLogo_UPTJAA_acercade")
        self.lblLogo_UPTJAA_acercade.setGeometry(QRect(279, 10, 45, 40))
        self.lblLogo_UPTJAA_acercade.setMinimumSize(QSize(40, 40))
        self.lblLogo_UPTJAA_acercade.setMaximumSize(QSize(90, 80))
        self.lblLogo_UPTJAA_acercade.setStyleSheet(u"background-color: transparent;")
        self.lblLogo_UPTJAA_acercade.setPixmap(QPixmap(u":/logos/logo_uptjaa.png"))
        self.lblLogo_UPTJAA_acercade.setScaledContents(True)
        self.lneNombreCompleto_admin = QLineEdit(self.Usuario)
        self.lneNombreCompleto_admin.setObjectName(u"lneNombreCompleto_admin")
        self.lneNombreCompleto_admin.setGeometry(QRect(120, 130, 250, 35))
        self.lneNombreCompleto_admin.setMinimumSize(QSize(225, 35))
        self.lneNombreCompleto_admin.setMaximumSize(QSize(300, 35))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        self.lneNombreCompleto_admin.setFont(font3)
        self.lneNombreCompleto_admin.setMouseTracking(True)
        self.lneNombreCompleto_admin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneNombreCompleto_admin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneRepPass_admin = QLineEdit(self.Usuario)
        self.lneRepPass_admin.setObjectName(u"lneRepPass_admin")
        self.lneRepPass_admin.setGeometry(QRect(120, 295, 250, 35))
        self.lneRepPass_admin.setMinimumSize(QSize(225, 35))
        self.lneRepPass_admin.setMaximumSize(QSize(300, 35))
        self.lneRepPass_admin.setFont(font3)
        self.lneRepPass_admin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneRepPass_admin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneUsername_admin = QLineEdit(self.Usuario)
        self.lneUsername_admin.setObjectName(u"lneUsername_admin")
        self.lneUsername_admin.setGeometry(QRect(120, 185, 250, 35))
        self.lneUsername_admin.setMinimumSize(QSize(225, 35))
        self.lneUsername_admin.setMaximumSize(QSize(300, 35))
        self.lneUsername_admin.setFont(font3)
        self.lneUsername_admin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneUsername_admin.setMaxLength(8)
        self.lneUsername_admin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lnePass_admin = QLineEdit(self.Usuario)
        self.lnePass_admin.setObjectName(u"lnePass_admin")
        self.lnePass_admin.setGeometry(QRect(120, 240, 250, 35))
        self.lnePass_admin.setMinimumSize(QSize(225, 35))
        self.lnePass_admin.setMaximumSize(QSize(300, 35))
        self.lnePass_admin.setFont(font3)
        self.lnePass_admin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lnePass_admin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneRol_admin = QLineEdit(self.Usuario)
        self.lneRol_admin.setObjectName(u"lneRol_admin")
        self.lneRol_admin.setGeometry(QRect(120, 350, 250, 35))
        self.lneRol_admin.setMinimumSize(QSize(225, 35))
        self.lneRol_admin.setMaximumSize(QSize(300, 35))
        self.lneRol_admin.setFont(font3)
        self.lneRol_admin.setMouseTracking(False)
        self.lneRol_admin.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lneRol_admin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneRol_admin.setReadOnly(True)
        self.stackedWidget.addWidget(self.Usuario)
        self.institucion = QWidget()
        self.institucion.setObjectName(u"institucion")
        self.lblLogo_SIRA_3 = QLabel(self.institucion)
        self.lblLogo_SIRA_3.setObjectName(u"lblLogo_SIRA_3")
        self.lblLogo_SIRA_3.setEnabled(True)
        self.lblLogo_SIRA_3.setGeometry(QRect(166, 10, 101, 40))
        self.lblLogo_SIRA_3.setMinimumSize(QSize(100, 21))
        self.lblLogo_SIRA_3.setMaximumSize(QSize(325, 120))
        self.lblLogo_SIRA_3.setFont(font1)
        self.lblLogo_SIRA_3.setStyleSheet(u"")
        self.lblLogo_SIRA_3.setPixmap(QPixmap(u":/logos/SIRA_logo_cut.png"))
        self.lblLogo_SIRA_3.setScaledContents(True)
        self.lblLogo_SIRA_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblLogo_SIRA_3.setWordWrap(False)
        self.line_3 = QFrame(self.institucion)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(270, 10, 3, 40))
        self.line_3.setMinimumSize(QSize(3, 40))
        self.line_3.setMaximumSize(QSize(3, 80))
        self.line_3.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblLogo_UPTJAA_acercade_2 = QLabel(self.institucion)
        self.lblLogo_UPTJAA_acercade_2.setObjectName(u"lblLogo_UPTJAA_acercade_2")
        self.lblLogo_UPTJAA_acercade_2.setGeometry(QRect(279, 10, 45, 40))
        self.lblLogo_UPTJAA_acercade_2.setMinimumSize(QSize(40, 40))
        self.lblLogo_UPTJAA_acercade_2.setMaximumSize(QSize(90, 80))
        self.lblLogo_UPTJAA_acercade_2.setStyleSheet(u"background-color: transparent;")
        self.lblLogo_UPTJAA_acercade_2.setPixmap(QPixmap(u":/logos/logo_uptjaa.png"))
        self.lblLogo_UPTJAA_acercade_2.setScaledContents(True)
        self.lblTitulo_7 = QLabel(self.institucion)
        self.lblTitulo_7.setObjectName(u"lblTitulo_7")
        self.lblTitulo_7.setGeometry(QRect(30, 50, 411, 61))
        self.lblTitulo_7.setMinimumSize(QSize(150, 21))
        self.lblTitulo_7.setMaximumSize(QSize(450, 120))
        self.lblTitulo_7.setFont(font)
        self.lblTitulo_7.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50; \n"
"}")
        self.lblTitulo_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitulo_7.setWordWrap(True)
        self.lneNombreInstitucion = QLineEdit(self.institucion)
        self.lneNombreInstitucion.setObjectName(u"lneNombreInstitucion")
        self.lneNombreInstitucion.setGeometry(QRect(40, 140, 391, 35))
        self.lneNombreInstitucion.setMinimumSize(QSize(120, 30))
        self.lneNombreInstitucion.setMaximumSize(QSize(400, 35))
        self.lneNombreInstitucion.setFont(font3)
        self.lneNombreInstitucion.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneNombreInstitucion.setMouseTracking(False)
        self.lneNombreInstitucion.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lneNombreInstitucion.setStyleSheet(u"")
        self.lneNombreInstitucion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneNombreInstitucion.setReadOnly(True)
        self.lblStudent_apellido = QLabel(self.institucion)
        self.lblStudent_apellido.setObjectName(u"lblStudent_apellido")
        self.lblStudent_apellido.setGeometry(QRect(-10, 100, 501, 40))
        self.lblStudent_apellido.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido.setMaximumSize(QSize(16777215, 40))
        self.lblStudent_apellido.setFont(font)
        self.lblStudent_apellido.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_apellido.setWordWrap(True)
        self.lneCodigoDEA = QLineEdit(self.institucion)
        self.lneCodigoDEA.setObjectName(u"lneCodigoDEA")
        self.lneCodigoDEA.setGeometry(QRect(40, 220, 391, 35))
        self.lneCodigoDEA.setMinimumSize(QSize(120, 30))
        self.lneCodigoDEA.setMaximumSize(QSize(400, 35))
        self.lneCodigoDEA.setFont(font3)
        self.lneCodigoDEA.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneCodigoDEA.setMouseTracking(True)
        self.lneCodigoDEA.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneCodigoDEA.setStyleSheet(u"")
        self.lneCodigoDEA.setMaxLength(15)
        self.lneCodigoDEA.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneCodigoDEA.setReadOnly(False)
        self.lblStudent_apellido_2 = QLabel(self.institucion)
        self.lblStudent_apellido_2.setObjectName(u"lblStudent_apellido_2")
        self.lblStudent_apellido_2.setGeometry(QRect(-10, 180, 501, 40))
        self.lblStudent_apellido_2.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_2.setMaximumSize(QSize(16777215, 40))
        self.lblStudent_apellido_2.setFont(font)
        self.lblStudent_apellido_2.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_apellido_2.setWordWrap(True)
        self.lblStudent_apellido_3 = QLabel(self.institucion)
        self.lblStudent_apellido_3.setObjectName(u"lblStudent_apellido_3")
        self.lblStudent_apellido_3.setGeometry(QRect(-10, 260, 501, 40))
        self.lblStudent_apellido_3.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_3.setMaximumSize(QSize(16777215, 40))
        self.lblStudent_apellido_3.setFont(font)
        self.lblStudent_apellido_3.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_apellido_3.setWordWrap(True)
        self.lneDirectorName = QLineEdit(self.institucion)
        self.lneDirectorName.setObjectName(u"lneDirectorName")
        self.lneDirectorName.setGeometry(QRect(40, 300, 391, 35))
        self.lneDirectorName.setMinimumSize(QSize(120, 30))
        self.lneDirectorName.setMaximumSize(QSize(400, 35))
        self.lneDirectorName.setFont(font3)
        self.lneDirectorName.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneDirectorName.setMouseTracking(True)
        self.lneDirectorName.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneDirectorName.setStyleSheet(u"")
        self.lneDirectorName.setMaxLength(200)
        self.lneDirectorName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneDirectorName.setReadOnly(False)
        self.lblStudent_apellido_4 = QLabel(self.institucion)
        self.lblStudent_apellido_4.setObjectName(u"lblStudent_apellido_4")
        self.lblStudent_apellido_4.setGeometry(QRect(-10, 340, 501, 40))
        self.lblStudent_apellido_4.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_4.setMaximumSize(QSize(16777215, 40))
        self.lblStudent_apellido_4.setFont(font)
        self.lblStudent_apellido_4.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_apellido_4.setWordWrap(True)
        self.lneDirectorCI = QLineEdit(self.institucion)
        self.lneDirectorCI.setObjectName(u"lneDirectorCI")
        self.lneDirectorCI.setGeometry(QRect(40, 380, 391, 35))
        self.lneDirectorCI.setMinimumSize(QSize(120, 30))
        self.lneDirectorCI.setMaximumSize(QSize(400, 35))
        self.lneDirectorCI.setFont(font3)
        self.lneDirectorCI.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneDirectorCI.setMouseTracking(True)
        self.lneDirectorCI.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneDirectorCI.setStyleSheet(u"")
        self.lneDirectorCI.setMaxLength(8)
        self.lneDirectorCI.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneDirectorCI.setReadOnly(False)
        self.stackedWidget.addWidget(self.institucion)
        self.licencia = QWidget()
        self.licencia.setObjectName(u"licencia")
        self.lblTitulo_9 = QLabel(self.licencia)
        self.lblTitulo_9.setObjectName(u"lblTitulo_9")
        self.lblTitulo_9.setGeometry(QRect(50, 120, 391, 261))
        self.lblTitulo_9.setMinimumSize(QSize(150, 21))
        self.lblTitulo_9.setMaximumSize(QSize(450, 300))
        self.lblTitulo_9.setFont(font2)
        self.lblTitulo_9.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50; \n"
"}")
        self.lblTitulo_9.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.lblTitulo_9.setWordWrap(True)
        self.lblLogo_UPTJAA_acercade_4 = QLabel(self.licencia)
        self.lblLogo_UPTJAA_acercade_4.setObjectName(u"lblLogo_UPTJAA_acercade_4")
        self.lblLogo_UPTJAA_acercade_4.setGeometry(QRect(279, 10, 45, 40))
        self.lblLogo_UPTJAA_acercade_4.setMinimumSize(QSize(40, 40))
        self.lblLogo_UPTJAA_acercade_4.setMaximumSize(QSize(90, 80))
        self.lblLogo_UPTJAA_acercade_4.setStyleSheet(u"background-color: transparent;")
        self.lblLogo_UPTJAA_acercade_4.setPixmap(QPixmap(u":/logos/logo_uptjaa.png"))
        self.lblLogo_UPTJAA_acercade_4.setScaledContents(True)
        self.lblLogo_SIRA_5 = QLabel(self.licencia)
        self.lblLogo_SIRA_5.setObjectName(u"lblLogo_SIRA_5")
        self.lblLogo_SIRA_5.setEnabled(True)
        self.lblLogo_SIRA_5.setGeometry(QRect(166, 10, 101, 40))
        self.lblLogo_SIRA_5.setMinimumSize(QSize(100, 21))
        self.lblLogo_SIRA_5.setMaximumSize(QSize(325, 120))
        self.lblLogo_SIRA_5.setFont(font1)
        self.lblLogo_SIRA_5.setStyleSheet(u"")
        self.lblLogo_SIRA_5.setPixmap(QPixmap(u":/logos/SIRA_logo_cut.png"))
        self.lblLogo_SIRA_5.setScaledContents(True)
        self.lblLogo_SIRA_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblLogo_SIRA_5.setWordWrap(False)
        self.line_5 = QFrame(self.licencia)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(270, 10, 3, 40))
        self.line_5.setMinimumSize(QSize(3, 40))
        self.line_5.setMaximumSize(QSize(3, 80))
        self.line_5.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblTitulo_10 = QLabel(self.licencia)
        self.lblTitulo_10.setObjectName(u"lblTitulo_10")
        self.lblTitulo_10.setGeometry(QRect(50, 70, 391, 41))
        self.lblTitulo_10.setMinimumSize(QSize(150, 21))
        self.lblTitulo_10.setMaximumSize(QSize(450, 120))
        self.lblTitulo_10.setFont(font1)
        self.lblTitulo_10.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50; \n"
"}")
        self.lblTitulo_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitulo_10.setWordWrap(True)
        self.chkLicencia = QCheckBox(self.licencia)
        self.chkLicencia.setObjectName(u"chkLicencia")
        self.chkLicencia.setGeometry(QRect(110, 380, 271, 31))
        self.chkLicencia.setFont(font3)
        self.chkLicencia.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chkLicencia.setStyleSheet(u"QCheckBox {\n"
"    spacing: 8px;\n"
"    color: #2d2d2d;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
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
        self.chkLicencia.setIconSize(QSize(20, 20))
        self.chkLicencia.setTristate(False)
        self.stackedWidget.addWidget(self.licencia)
        self.anio_escolar = QWidget()
        self.anio_escolar.setObjectName(u"anio_escolar")
        self.lblLogo_SIRA_4 = QLabel(self.anio_escolar)
        self.lblLogo_SIRA_4.setObjectName(u"lblLogo_SIRA_4")
        self.lblLogo_SIRA_4.setEnabled(True)
        self.lblLogo_SIRA_4.setGeometry(QRect(166, 10, 101, 40))
        self.lblLogo_SIRA_4.setMinimumSize(QSize(100, 21))
        self.lblLogo_SIRA_4.setMaximumSize(QSize(325, 120))
        self.lblLogo_SIRA_4.setFont(font1)
        self.lblLogo_SIRA_4.setStyleSheet(u"")
        self.lblLogo_SIRA_4.setPixmap(QPixmap(u":/logos/SIRA_logo_cut.png"))
        self.lblLogo_SIRA_4.setScaledContents(True)
        self.lblLogo_SIRA_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblLogo_SIRA_4.setWordWrap(False)
        self.line_4 = QFrame(self.anio_escolar)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(270, 10, 3, 40))
        self.line_4.setMinimumSize(QSize(3, 40))
        self.line_4.setMaximumSize(QSize(3, 80))
        self.line_4.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblLogo_UPTJAA_acercade_3 = QLabel(self.anio_escolar)
        self.lblLogo_UPTJAA_acercade_3.setObjectName(u"lblLogo_UPTJAA_acercade_3")
        self.lblLogo_UPTJAA_acercade_3.setGeometry(QRect(279, 10, 45, 40))
        self.lblLogo_UPTJAA_acercade_3.setMinimumSize(QSize(40, 40))
        self.lblLogo_UPTJAA_acercade_3.setMaximumSize(QSize(90, 80))
        self.lblLogo_UPTJAA_acercade_3.setStyleSheet(u"background-color: transparent;")
        self.lblLogo_UPTJAA_acercade_3.setPixmap(QPixmap(u":/logos/logo_uptjaa.png"))
        self.lblLogo_UPTJAA_acercade_3.setScaledContents(True)
        self.lblTitulo_8 = QLabel(self.anio_escolar)
        self.lblTitulo_8.setObjectName(u"lblTitulo_8")
        self.lblTitulo_8.setGeometry(QRect(40, 90, 391, 231))
        self.lblTitulo_8.setMinimumSize(QSize(150, 21))
        self.lblTitulo_8.setMaximumSize(QSize(450, 300))
        self.lblTitulo_8.setFont(font)
        self.lblTitulo_8.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50; \n"
"}")
        self.lblTitulo_8.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.lblTitulo_8.setWordWrap(True)
        self.stackedWidget.addWidget(self.anio_escolar)
        self.btnSiguiente = QPushButton(self.widgetPrincipal)
        self.btnSiguiente.setObjectName(u"btnSiguiente")
        self.btnSiguiente.setGeometry(QRect(340, 440, 131, 35))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSiguiente.sizePolicy().hasHeightForWidth())
        self.btnSiguiente.setSizePolicy(sizePolicy)
        self.btnSiguiente.setMinimumSize(QSize(120, 35))
        self.btnSiguiente.setMaximumSize(QSize(200, 35))
        self.btnSiguiente.setFont(font1)
        self.btnSiguiente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSiguiente.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.btnSiguiente.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnSiguiente.setStyleSheet(u"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 10px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/siguiente.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSiguiente.setIcon(icon)
        self.btnSiguiente.setIconSize(QSize(20, 20))
        self.btnAtras = QPushButton(self.widgetPrincipal)
        self.btnAtras.setObjectName(u"btnAtras")
        self.btnAtras.setGeometry(QRect(210, 440, 120, 35))
        sizePolicy.setHeightForWidth(self.btnAtras.sizePolicy().hasHeightForWidth())
        self.btnAtras.setSizePolicy(sizePolicy)
        self.btnAtras.setMinimumSize(QSize(120, 35))
        self.btnAtras.setMaximumSize(QSize(120, 35))
        self.btnAtras.setFont(font1)
        self.btnAtras.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAtras.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnAtras.setStyleSheet(u"QPushButton {\n"
"  \n"
"	\n"
"	background-color: #e74c3c;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #C0392B\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/regresar_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAtras.setIcon(icon1)

        self.verticalLayout.addWidget(self.widgetPrincipal)


        self.retranslateUi(config_inicial)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(config_inicial)
    # setupUi

    def retranslateUi(self, config_inicial):
        config_inicial.setWindowTitle(QCoreApplication.translate("config_inicial", u"Dialog", None))
        self.lblTitulo.setText(QCoreApplication.translate("config_inicial", u"Bienvenido a la configuraci\u00f3n inicial de SIRA (Sistema Interno de Registro Acad\u00e9mico).", None))
        self.lblLogo_SIRA.setText("")
        self.lblTitulo_3.setText(QCoreApplication.translate("config_inicial", u"\u00c9sta configuraci\u00f3n solo se muestra la primera vez que se inicia el sistema. Se le solicitar\u00e1n datos del usuario administrador y datos de la instituci\u00f3n.", None))
        self.lblTitulo_4.setText(QCoreApplication.translate("config_inicial", u"SIRA ha sido desarrollado como proyecto de grado por:", None))
        self.lblTitulo_5.setText(QCoreApplication.translate("config_inicial", u"\u25b6 Jorge Jim\u00e9nez  |  \u25b6 Jes\u00fas Gonz\u00e1lez  |  \u25b6 Carlos Malav\u00e9", None))
        self.lblTitulo_6.setText(QCoreApplication.translate("config_inicial", u"\n"
"Estudiantes de Inform\u00e1tica en la Universidad Polit\u00e9cnica Territorial Jos\u00e9 Ant\u00f3nio Anzo\u00e1tegui (UPTJAA).", None))
        self.lblLogo_SIRA_2.setText("")
        self.lblTitulo_2.setText(QCoreApplication.translate("config_inicial", u"Ingrese los datos del Administrador principal del sistema:", None))
        self.lblLogo_UPTJAA_acercade.setText("")
        self.lneNombreCompleto_admin.setText("")
        self.lneNombreCompleto_admin.setPlaceholderText(QCoreApplication.translate("config_inicial", u"NOMBRE COMPLETO", None))
        self.lneRepPass_admin.setPlaceholderText(QCoreApplication.translate("config_inicial", u"REPITA CONTRASE\u00d1A", None))
        self.lneUsername_admin.setPlaceholderText(QCoreApplication.translate("config_inicial", u"USUARIO", None))
        self.lnePass_admin.setPlaceholderText(QCoreApplication.translate("config_inicial", u"CONTRASE\u00d1A", None))
        self.lneRol_admin.setPlaceholderText(QCoreApplication.translate("config_inicial", u"ROL: ADMINISTRADOR", None))
        self.lblLogo_SIRA_3.setText("")
        self.lblLogo_UPTJAA_acercade_2.setText("")
        self.lblTitulo_7.setText(QCoreApplication.translate("config_inicial", u"Ingrese los datos del Administrador del sistema:", None))
        self.lneNombreInstitucion.setText(QCoreApplication.translate("config_inicial", u"Escuela Bolivariana \"Dr. Severiano Hern\u00e1ndez\"", None))
        self.lneNombreInstitucion.setPlaceholderText("")
        self.lblStudent_apellido.setText(QCoreApplication.translate("config_inicial", u"Nombre de la instituci\u00f3n:", None))
        self.lneCodigoDEA.setText("")
        self.lneCodigoDEA.setPlaceholderText(QCoreApplication.translate("config_inicial", u"Ej: OD03140321", None))
        self.lblStudent_apellido_2.setText(QCoreApplication.translate("config_inicial", u"C\u00f3digo DEA:", None))
        self.lblStudent_apellido_3.setText(QCoreApplication.translate("config_inicial", u"Nombre Director(a):", None))
        self.lneDirectorName.setText("")
        self.lneDirectorName.setPlaceholderText(QCoreApplication.translate("config_inicial", u"Ej: Pedro Rond\u00f3n", None))
        self.lblStudent_apellido_4.setText(QCoreApplication.translate("config_inicial", u"C\u00e9dula Director(a):", None))
        self.lneDirectorCI.setText("")
        self.lneDirectorCI.setPlaceholderText(QCoreApplication.translate("config_inicial", u"Ej: 8674264", None))
        self.lblTitulo_9.setText(QCoreApplication.translate("config_inicial", u"Este sistema se distribuye bajo la Licencia MIT. Esto significa que tienes permiso para usar, copiar, modificar, fusionar, publicar y distribuir el software sin restricciones, siempre y cuando se cumplan las siguientes condiciones:\n"
"\n"
"   \u25b6 Aviso de Copyright: Se debe incluir el aviso de derechos de autor original en todas las copias o partes sustanciales del software.\n"
"\n"
"   \u25b6 Sin Garant\u00eda: El software se proporciona \"tal cual\", sin garant\u00edas de ning\u00fan tipo. Los autores no se hacen responsables de reclamaciones o da\u00f1os derivados del uso del sistema.", None))
        self.lblLogo_UPTJAA_acercade_4.setText("")
        self.lblLogo_SIRA_5.setText("")
        self.lblTitulo_10.setText(QCoreApplication.translate("config_inicial", u"Aviso de licencia MIT: Software libre y abierto", None))
        self.chkLicencia.setText(QCoreApplication.translate("config_inicial", u"Acepto los terminos de licencia.", u"0"))
        self.lblLogo_SIRA_4.setText("")
        self.lblLogo_UPTJAA_acercade_3.setText("")
        self.lblTitulo_8.setText(QCoreApplication.translate("config_inicial", u"Presione en \"Confirmar\" para iniciar el sistema con los datos previamente ingresados.\n"
"\n"
"Una vez iniciado el sistema, se recomienda entrar al m\u00f3dulo de Administraci\u00f3n, para terminar de ingresar otros datos institucionales.\n"
"\n"
"El a\u00f1o escolar en curso se crea autom\u00e1ticamente tomando en cuenta la fecha actual del computador.", None))
        self.btnSiguiente.setText(QCoreApplication.translate("config_inicial", u"Siguiente", None))
        self.btnAtras.setText(QCoreApplication.translate("config_inicial", u"Atras", None))
    # retranslateUi

