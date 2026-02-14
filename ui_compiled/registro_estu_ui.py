# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro_estu.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QWidget)
from resources import resources_ui

class Ui_registro_estu(object):
    def setupUi(self, registro_estu):
        if not registro_estu.objectName():
            registro_estu.setObjectName(u"registro_estu")
        registro_estu.resize(1000, 600)
        registro_estu.setMinimumSize(QSize(1000, 600))
        registro_estu.setMaximumSize(QSize(1000, 600))
        registro_estu.setStyleSheet(u"background-color: #f5f6fa;")
        self.gridLayout = QGridLayout(registro_estu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(registro_estu)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"background-color: #f5f6fa;\n"
"color: #2d2d2d;\n"
"}\n"
"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 10px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 2px 5px;\n"
"    background-color: white;\n"
"	color: #2d2d2d;\n"
"}")
        self.lneCedula_reg_estu = QLineEdit(self.widget)
        self.lneCedula_reg_estu.setObjectName(u"lneCedula_reg_estu")
        self.lneCedula_reg_estu.setGeometry(QRect(120, 40, 200, 31))
        self.lneCedula_reg_estu.setMinimumSize(QSize(200, 30))
        self.lneCedula_reg_estu.setMaximumSize(QSize(200, 50))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(13)
        self.lneCedula_reg_estu.setFont(font)
        self.lneCedula_reg_estu.setStyleSheet(u"")
        self.lneCedula_reg_estu.setMaxLength(15)
        self.lneCedula_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneCedula_reg_estu.setReadOnly(False)
        self.lneCedula_reg_estu.setClearButtonEnabled(True)
        self.lblCedula_registro_estudiante = QLabel(self.widget)
        self.lblCedula_registro_estudiante.setObjectName(u"lblCedula_registro_estudiante")
        self.lblCedula_registro_estudiante.setGeometry(QRect(20, 30, 91, 50))
        self.lblCedula_registro_estudiante.setMinimumSize(QSize(0, 50))
        self.lblCedula_registro_estudiante.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblCedula_registro_estudiante.setFont(font1)
        self.lblCedula_registro_estudiante.setStyleSheet(u"color: #2d2d2d;\n"
"border: 1px solid transparent;\n"
"border-radius: 10px;\n"
"background-color: transparent;")
        self.lblCedula_registro_estudiante.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblCedula_registro_estudiante.setWordWrap(True)
        self.btnGuardar_reg_estu = QPushButton(self.widget)
        self.btnGuardar_reg_estu.setObjectName(u"btnGuardar_reg_estu")
        self.btnGuardar_reg_estu.setGeometry(QRect(840, 510, 120, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGuardar_reg_estu.sizePolicy().hasHeightForWidth())
        self.btnGuardar_reg_estu.setSizePolicy(sizePolicy)
        self.btnGuardar_reg_estu.setMinimumSize(QSize(120, 40))
        self.btnGuardar_reg_estu.setMaximumSize(QSize(120, 60))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(13)
        font2.setBold(True)
        self.btnGuardar_reg_estu.setFont(font2)
        self.btnGuardar_reg_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGuardar_reg_estu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnGuardar_reg_estu.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/guardar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGuardar_reg_estu.setIcon(icon)
        self.btnGuardar_reg_estu.setIconSize(QSize(20, 20))
        self.btnLimpiar_reg_estu = QPushButton(self.widget)
        self.btnLimpiar_reg_estu.setObjectName(u"btnLimpiar_reg_estu")
        self.btnLimpiar_reg_estu.setGeometry(QRect(679, 530, 141, 31))
        sizePolicy.setHeightForWidth(self.btnLimpiar_reg_estu.sizePolicy().hasHeightForWidth())
        self.btnLimpiar_reg_estu.setSizePolicy(sizePolicy)
        self.btnLimpiar_reg_estu.setMinimumSize(QSize(120, 30))
        self.btnLimpiar_reg_estu.setMaximumSize(QSize(150, 40))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.btnLimpiar_reg_estu.setFont(font3)
        self.btnLimpiar_reg_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLimpiar_reg_estu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnLimpiar_reg_estu.setStyleSheet(u"QPushButton {\n"
"   background-color: white;\n"
"    color: #2980b9;\n"
"    border: 1.5px solid #2980b9;\n"
"    padding: 2px 2px;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #E3F2FD;\n"
"	border: 1.5px solid #0D47A1;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/limpiar_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLimpiar_reg_estu.setIcon(icon1)
        self.btnGenCedula_reg_estu = QPushButton(self.widget)
        self.btnGenCedula_reg_estu.setObjectName(u"btnGenCedula_reg_estu")
        self.btnGenCedula_reg_estu.setGeometry(QRect(330, 40, 141, 30))
        sizePolicy.setHeightForWidth(self.btnGenCedula_reg_estu.sizePolicy().hasHeightForWidth())
        self.btnGenCedula_reg_estu.setSizePolicy(sizePolicy)
        self.btnGenCedula_reg_estu.setMinimumSize(QSize(90, 30))
        self.btnGenCedula_reg_estu.setMaximumSize(QSize(150, 60))
        self.btnGenCedula_reg_estu.setFont(font3)
        self.btnGenCedula_reg_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGenCedula_reg_estu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnGenCedula_reg_estu.setStyleSheet(u" border-radius: 10px;\n"
"background-color: #27ae60;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/generar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGenCedula_reg_estu.setIcon(icon2)
        self.btnGenCedula_reg_estu.setIconSize(QSize(15, 15))
        self.lblTitulo_reg_estu = QLabel(self.widget)
        self.lblTitulo_reg_estu.setObjectName(u"lblTitulo_reg_estu")
        self.lblTitulo_reg_estu.setGeometry(QRect(711, 20, 191, 61))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(19)
        font4.setBold(True)
        self.lblTitulo_reg_estu.setFont(font4)
        self.lblTitulo_reg_estu.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblTitulo_reg_estu.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_reg_estu.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_reg_estu.setScaledContents(False)
        self.lblTitulo_reg_estu.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_reg_estu.setWordWrap(True)
        self.lblTitulo_reg_estu.setIndent(0)
        self.lblLogo_reg_estu = QLabel(self.widget)
        self.lblLogo_reg_estu.setObjectName(u"lblLogo_reg_estu")
        self.lblLogo_reg_estu.setGeometry(QRect(920, 20, 51, 61))
        self.lblLogo_reg_estu.setMinimumSize(QSize(50, 50))
        self.lblLogo_reg_estu.setMaximumSize(QSize(130, 70))
        self.lblLogo_reg_estu.setStyleSheet(u"background-color: transparent;")
        self.lblLogo_reg_estu.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_reg_estu.setScaledContents(True)
        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(910, 20, 3, 61))
        self.line_2.setMinimumSize(QSize(3, 61))
        self.line_2.setMaximumSize(QSize(3, 61))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.stackRegistro_estudiante = QTabWidget(self.widget)
        self.stackRegistro_estudiante.setObjectName(u"stackRegistro_estudiante")
        self.stackRegistro_estudiante.setGeometry(QRect(20, 100, 921, 391))
        font5 = QFont()
        font5.setFamilies([u"Inter Variable"])
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setItalic(False)
        self.stackRegistro_estudiante.setFont(font5)
        self.stackRegistro_estudiante.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.stackRegistro_estudiante.setStyleSheet(u"QTabWidget{\n"
"	background-color: white;\n"
"	color: #2d2d2d;\n"
"	border-radius: 10px;\n"
"}\n"
"QTabWidget::pane { \n"
"    border: 1.2px solid #2980b9;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"    background-color: white;\n"
"    top: -1px; /* Ajuste para que no haya hueco entre pesta\u00f1a y panel */\n"
"}\n"
"QWidget{\n"
"	background-color: transparent;\n"
"		border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"QTabBar::tab {\n"
"    background: #2980b9;\n"
"    color: white;\n"
"    padding: 8px 12px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    margin-right: 1px;\n"
"}\n"
"\n"
"/* Cuando pasas el mouse por encima */\n"
"QTabBar::tab:hover {\n"
"    background: #0D47A1;\n"
"}\n"
"\n"
"/* Cuando la pesta\u00f1a est\u00e1 seleccionada */\n"
"QTabBar::tab:selected {\n"
"    background: #FFFFFF;\n"
"    color: #2980b9;\n"
"	bord"
                        "er: 1.2px solid #2980b9;\n"
"}")
        self.stackRegistro_estudiante.setTabPosition(QTabWidget.TabPosition.North)
        self.stackRegistro_estudiante.setTabShape(QTabWidget.TabShape.Rounded)
        self.stackRegistro_estudiante.setElideMode(Qt.TextElideMode.ElideNone)
        self.stackRegistro_estudiantePage1 = QWidget()
        self.stackRegistro_estudiantePage1.setObjectName(u"stackRegistro_estudiantePage1")
        self.stackRegistro_estudiantePage1.setStyleSheet(u"")
        self.lblStudent_apellido = QLabel(self.stackRegistro_estudiantePage1)
        self.lblStudent_apellido.setObjectName(u"lblStudent_apellido")
        self.lblStudent_apellido.setGeometry(QRect(10, 20, 81, 30))
        self.lblStudent_apellido.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido.setFont(font1)
        self.lblStudent_apellido.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneApellido_reg_estu = QLineEdit(self.stackRegistro_estudiantePage1)
        self.lneApellido_reg_estu.setObjectName(u"lneApellido_reg_estu")
        self.lneApellido_reg_estu.setGeometry(QRect(100, 20, 400, 30))
        self.lneApellido_reg_estu.setMinimumSize(QSize(400, 30))
        self.lneApellido_reg_estu.setMaximumSize(QSize(400, 30))
        self.lneApellido_reg_estu.setFont(font)
        self.lneApellido_reg_estu.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneApellido_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneApellido_reg_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneApellido_reg_estu.setMaxLength(100)
        self.lneApellido_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneNombre_reg_estu = QLineEdit(self.stackRegistro_estudiantePage1)
        self.lneNombre_reg_estu.setObjectName(u"lneNombre_reg_estu")
        self.lneNombre_reg_estu.setGeometry(QRect(100, 60, 400, 30))
        self.lneNombre_reg_estu.setMinimumSize(QSize(400, 30))
        self.lneNombre_reg_estu.setMaximumSize(QSize(400, 30))
        self.lneNombre_reg_estu.setFont(font)
        self.lneNombre_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneNombre_reg_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneNombre_reg_estu.setMaxLength(100)
        self.lneNombre_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_nombres = QLabel(self.stackRegistro_estudiantePage1)
        self.lblStudent_nombres.setObjectName(u"lblStudent_nombres")
        self.lblStudent_nombres.setGeometry(QRect(10, 60, 81, 30))
        self.lblStudent_nombres.setMinimumSize(QSize(0, 30))
        self.lblStudent_nombres.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_nombres.setFont(font1)
        self.lblStudent_nombres.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_nombres.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_lugarNac = QLabel(self.stackRegistro_estudiantePage1)
        self.lblStudent_lugarNac.setObjectName(u"lblStudent_lugarNac")
        self.lblStudent_lugarNac.setGeometry(QRect(510, 60, 91, 30))
        self.lblStudent_lugarNac.setMinimumSize(QSize(0, 30))
        self.lblStudent_lugarNac.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_lugarNac.setFont(font1)
        self.lblStudent_lugarNac.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_lugarNac.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_fechaNac = QLabel(self.stackRegistro_estudiantePage1)
        self.lblStudent_fechaNac.setObjectName(u"lblStudent_fechaNac")
        self.lblStudent_fechaNac.setGeometry(QRect(510, 20, 91, 30))
        self.lblStudent_fechaNac.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac.setFont(font1)
        self.lblStudent_fechaNac.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneCity_reg_estu = QLineEdit(self.stackRegistro_estudiantePage1)
        self.lneCity_reg_estu.setObjectName(u"lneCity_reg_estu")
        self.lneCity_reg_estu.setGeometry(QRect(610, 60, 151, 30))
        self.lneCity_reg_estu.setMinimumSize(QSize(100, 30))
        self.lneCity_reg_estu.setMaximumSize(QSize(300, 30))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(12)
        self.lneCity_reg_estu.setFont(font6)
        self.lneCity_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneCity_reg_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneCity_reg_estu.setMaxLength(50)
        self.lneCity_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneEdad_reg_estu = QLineEdit(self.stackRegistro_estudiantePage1)
        self.lneEdad_reg_estu.setObjectName(u"lneEdad_reg_estu")
        self.lneEdad_reg_estu.setGeometry(QRect(840, 20, 61, 30))
        self.lneEdad_reg_estu.setMinimumSize(QSize(50, 30))
        self.lneEdad_reg_estu.setMaximumSize(QSize(300, 30))
        self.lneEdad_reg_estu.setFont(font)
        self.lneEdad_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneEdad_reg_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneEdad_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneEdad_reg_estu.setReadOnly(True)
        self.lblStudent_edad = QLabel(self.stackRegistro_estudiantePage1)
        self.lblStudent_edad.setObjectName(u"lblStudent_edad")
        self.lblStudent_edad.setGeometry(QRect(770, 20, 61, 30))
        self.lblStudent_edad.setMinimumSize(QSize(0, 30))
        self.lblStudent_edad.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_edad.setFont(font1)
        self.lblStudent_edad.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_edad.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_genero = QLabel(self.stackRegistro_estudiantePage1)
        self.lblStudent_genero.setObjectName(u"lblStudent_genero")
        self.lblStudent_genero.setGeometry(QRect(770, 60, 61, 30))
        self.lblStudent_genero.setMinimumSize(QSize(0, 30))
        self.lblStudent_genero.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_genero.setFont(font1)
        self.lblStudent_genero.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_genero.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneDir_reg_estu = QLineEdit(self.stackRegistro_estudiantePage1)
        self.lneDir_reg_estu.setObjectName(u"lneDir_reg_estu")
        self.lneDir_reg_estu.setGeometry(QRect(100, 110, 801, 60))
        self.lneDir_reg_estu.setMinimumSize(QSize(400, 30))
        self.lneDir_reg_estu.setMaximumSize(QSize(900, 60))
        self.lneDir_reg_estu.setFont(font)
        self.lneDir_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneDir_reg_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneDir_reg_estu.setMaxLength(100)
        self.lneDir_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_dir = QLabel(self.stackRegistro_estudiantePage1)
        self.lblStudent_dir.setObjectName(u"lblStudent_dir")
        self.lblStudent_dir.setGeometry(QRect(10, 110, 81, 30))
        self.lblStudent_dir.setMinimumSize(QSize(0, 30))
        self.lblStudent_dir.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_dir.setFont(font1)
        self.lblStudent_dir.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_dir.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_31 = QLabel(self.stackRegistro_estudiantePage1)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(280, 200, 121, 30))
        self.label_31.setMinimumSize(QSize(0, 30))
        self.label_31.setMaximumSize(QSize(16777215, 30))
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"background-color: transparent;")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_33 = QLabel(self.stackRegistro_estudiantePage1)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(520, 200, 61, 30))
        self.label_33.setMinimumSize(QSize(0, 30))
        self.label_33.setMaximumSize(QSize(16777215, 30))
        self.label_33.setFont(font1)
        self.label_33.setStyleSheet(u"background-color: transparent;")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_34 = QLabel(self.stackRegistro_estudiantePage1)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(700, 200, 61, 30))
        self.label_34.setMinimumSize(QSize(0, 30))
        self.label_34.setMaximumSize(QSize(16777215, 30))
        self.label_34.setFont(font1)
        self.label_34.setStyleSheet(u"background-color: transparent;")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_42 = QLabel(self.stackRegistro_estudiantePage1)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(0, 270, 111, 30))
        self.label_42.setMinimumSize(QSize(0, 30))
        self.label_42.setMaximumSize(QSize(16777215, 30))
        self.label_42.setFont(font1)
        self.label_42.setStyleSheet(u"background-color: transparent;")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneTallaC_reg_estu = QLineEdit(self.stackRegistro_estudiantePage1)
        self.lneTallaC_reg_estu.setObjectName(u"lneTallaC_reg_estu")
        self.lneTallaC_reg_estu.setGeometry(QRect(110, 270, 61, 30))
        self.lneTallaC_reg_estu.setMinimumSize(QSize(50, 30))
        self.lneTallaC_reg_estu.setMaximumSize(QSize(300, 30))
        self.lneTallaC_reg_estu.setFont(font6)
        self.lneTallaC_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneTallaC_reg_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneTallaC_reg_estu.setMaxLength(2)
        self.lneTallaC_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_44 = QLabel(self.stackRegistro_estudiantePage1)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(190, 270, 111, 30))
        self.label_44.setMinimumSize(QSize(0, 30))
        self.label_44.setMaximumSize(QSize(16777215, 30))
        self.label_44.setFont(font1)
        self.label_44.setStyleSheet(u"background-color: transparent;")
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneTallaP_reg_estu = QLineEdit(self.stackRegistro_estudiantePage1)
        self.lneTallaP_reg_estu.setObjectName(u"lneTallaP_reg_estu")
        self.lneTallaP_reg_estu.setGeometry(QRect(310, 270, 61, 30))
        self.lneTallaP_reg_estu.setMinimumSize(QSize(50, 30))
        self.lneTallaP_reg_estu.setMaximumSize(QSize(300, 30))
        self.lneTallaP_reg_estu.setFont(font6)
        self.lneTallaP_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneTallaP_reg_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneTallaP_reg_estu.setMaxLength(2)
        self.lneTallaP_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneTallaZ_reg_estu = QLineEdit(self.stackRegistro_estudiantePage1)
        self.lneTallaZ_reg_estu.setObjectName(u"lneTallaZ_reg_estu")
        self.lneTallaZ_reg_estu.setGeometry(QRect(510, 270, 61, 30))
        self.lneTallaZ_reg_estu.setMinimumSize(QSize(50, 30))
        self.lneTallaZ_reg_estu.setMaximumSize(QSize(300, 30))
        self.lneTallaZ_reg_estu.setFont(font6)
        self.lneTallaZ_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneTallaZ_reg_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneTallaZ_reg_estu.setMaxLength(2)
        self.lneTallaZ_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_49 = QLabel(self.stackRegistro_estudiantePage1)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(390, 270, 111, 30))
        self.label_49.setMinimumSize(QSize(0, 30))
        self.label_49.setMaximumSize(QSize(16777215, 30))
        self.label_49.setFont(font1)
        self.label_49.setStyleSheet(u"background-color: transparent;")
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneFechaNac_reg_estu = QDateEdit(self.stackRegistro_estudiantePage1)
        self.lneFechaNac_reg_estu.setObjectName(u"lneFechaNac_reg_estu")
        self.lneFechaNac_reg_estu.setGeometry(QRect(610, 20, 151, 30))
        self.lneFechaNac_reg_estu.setMinimumSize(QSize(151, 30))
        self.lneFechaNac_reg_estu.setMaximumSize(QSize(151, 30))
        self.lneFechaNac_reg_estu.setFont(font)
        self.lneFechaNac_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneFechaNac_reg_estu.setStyleSheet(u"QDateEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 12px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"/* Vista de d\u00edas (el grid del calendario) */\n"
"QDateEdit QAbstractItemView {\n"
"    background-color: white;\n"
"    color: #2d2d2d;\n"
"    selection-background-color: #2980b9;\n"
"    selection-color: white;\n"
"}\n"
"/* Botones de navegaci\u00f3n (mes anterior/siguiente) y combos de mes/a\u00f1o */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #90caf9;   /* Fondo del encabezado */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: #2d2d2d;              /* Texto de mes y a\u00f1o */\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 4px 8px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #d6eaff;   /* Hover sobre mes/a\u00f1o o flechas */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Hover sobre los d\u00edas */\n"
"QDateEdit"
                        " QAbstractItemView::item:hover {\n"
"    background-color: #2980b9;   /* azul claro */\n"
"    color: #000;\n"
"}\n"
"\n"
"")
        self.lneFechaNac_reg_estu.setProperty(u"showGroupSeparator", False)
        self.lneFechaNac_reg_estu.setCalendarPopup(True)
        self.lneFechaNac_reg_estu.setCurrentSectionIndex(0)
        self.lneFechaNac_reg_estu.setTimeSpec(Qt.TimeSpec.UTC)
        self.lneFechaIng_reg_estu = QDateEdit(self.stackRegistro_estudiantePage1)
        self.lneFechaIng_reg_estu.setObjectName(u"lneFechaIng_reg_estu")
        self.lneFechaIng_reg_estu.setGeometry(QRect(110, 200, 151, 30))
        self.lneFechaIng_reg_estu.setMinimumSize(QSize(151, 30))
        self.lneFechaIng_reg_estu.setMaximumSize(QSize(151, 30))
        self.lneFechaIng_reg_estu.setFont(font)
        self.lneFechaIng_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneFechaIng_reg_estu.setStyleSheet(u"QDateEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 12px;\n"
"    background-color: white;\n"
"}\n"
"/* Vista de d\u00edas (el grid del calendario) */\n"
"QDateEdit QAbstractItemView {\n"
"    background-color: white;\n"
"    color: #2d2d2d;\n"
"    selection-background-color: #2980b9;\n"
"    selection-color: white;\n"
"}\n"
"/* Botones de navegaci\u00f3n (mes anterior/siguiente) y combos de mes/a\u00f1o */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #90caf9;   /* Fondo del encabezado */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: #2d2d2d;              /* Texto de mes y a\u00f1o */\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 4px 8px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #d6eaff;   /* Hover sobre mes/a\u00f1o o flechas */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Hover sobre los d\u00edas */\n"
"QDateEdit QAbs"
                        "tractItemView::item:hover {\n"
"    background-color: #2980b9;   /* azul claro */\n"
"    color: #000;\n"
"}\n"
"")
        self.lneFechaIng_reg_estu.setCalendarPopup(True)
        self.lblStudent_fechaIng = QLabel(self.stackRegistro_estudiantePage1)
        self.lblStudent_fechaIng.setObjectName(u"lblStudent_fechaIng")
        self.lblStudent_fechaIng.setGeometry(QRect(0, 200, 121, 30))
        self.lblStudent_fechaIng.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaIng.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaIng.setFont(font1)
        self.lblStudent_fechaIng.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaIng.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frGrado_reg_estu = QFrame(self.stackRegistro_estudiantePage1)
        self.frGrado_reg_estu.setObjectName(u"frGrado_reg_estu")
        self.frGrado_reg_estu.setGeometry(QRect(580, 200, 101, 30))
        self.frGrado_reg_estu.setMinimumSize(QSize(70, 30))
        self.frGrado_reg_estu.setMaximumSize(QSize(200, 40))
        self.frGrado_reg_estu.setStyleSheet(u"QFrame{\n"
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
        self.frGrado_reg_estu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frGrado_reg_estu.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxGrado_reg_estu = QComboBox(self.frGrado_reg_estu)
        self.cbxGrado_reg_estu.addItem("")
        self.cbxGrado_reg_estu.addItem("")
        self.cbxGrado_reg_estu.addItem("")
        self.cbxGrado_reg_estu.addItem("")
        self.cbxGrado_reg_estu.addItem("")
        self.cbxGrado_reg_estu.addItem("")
        self.cbxGrado_reg_estu.addItem("")
        self.cbxGrado_reg_estu.setObjectName(u"cbxGrado_reg_estu")
        self.cbxGrado_reg_estu.setGeometry(QRect(5, 5, 91, 21))
        self.cbxGrado_reg_estu.setMaximumSize(QSize(180, 30))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(11)
        font7.setBold(True)
        self.cbxGrado_reg_estu.setFont(font7)
        self.cbxGrado_reg_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxGrado_reg_estu.setStyleSheet(u"border: transparent;")
        self.cbxGrado_reg_estu.setIconSize(QSize(5, 5))
        self.frseccion = QFrame(self.stackRegistro_estudiantePage1)
        self.frseccion.setObjectName(u"frseccion")
        self.frseccion.setGeometry(QRect(770, 200, 131, 30))
        self.frseccion.setMinimumSize(QSize(70, 30))
        self.frseccion.setMaximumSize(QSize(200, 40))
        self.frseccion.setStyleSheet(u"QFrame{\n"
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
        self.frseccion.setFrameShape(QFrame.Shape.StyledPanel)
        self.frseccion.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxSeccion_reg_estu = QComboBox(self.frseccion)
        self.cbxSeccion_reg_estu.setObjectName(u"cbxSeccion_reg_estu")
        self.cbxSeccion_reg_estu.setGeometry(QRect(5, 5, 121, 21))
        self.cbxSeccion_reg_estu.setMaximumSize(QSize(180, 30))
        self.cbxSeccion_reg_estu.setFont(font7)
        self.cbxSeccion_reg_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxSeccion_reg_estu.setStyleSheet(u"border: transparent;")
        self.cbxSeccion_reg_estu.setIconSize(QSize(5, 5))
        self.frseccion_2 = QFrame(self.stackRegistro_estudiantePage1)
        self.frseccion_2.setObjectName(u"frseccion_2")
        self.frseccion_2.setGeometry(QRect(840, 60, 61, 30))
        self.frseccion_2.setMinimumSize(QSize(50, 30))
        self.frseccion_2.setMaximumSize(QSize(200, 40))
        self.frseccion_2.setStyleSheet(u"QFrame{\n"
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
        self.frseccion_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frseccion_2.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxGenero_reg_estu = QComboBox(self.frseccion_2)
        self.cbxGenero_reg_estu.addItem("")
        self.cbxGenero_reg_estu.addItem("")
        self.cbxGenero_reg_estu.addItem("")
        self.cbxGenero_reg_estu.setObjectName(u"cbxGenero_reg_estu")
        self.cbxGenero_reg_estu.setGeometry(QRect(5, 5, 50, 21))
        self.cbxGenero_reg_estu.setMaximumSize(QSize(180, 30))
        self.cbxGenero_reg_estu.setFont(font1)
        self.cbxGenero_reg_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxGenero_reg_estu.setStyleSheet(u"border: transparent;")
        self.cbxGenero_reg_estu.setIconSize(QSize(5, 5))
        self.frGrado_reg_estu_2 = QFrame(self.stackRegistro_estudiantePage1)
        self.frGrado_reg_estu_2.setObjectName(u"frGrado_reg_estu_2")
        self.frGrado_reg_estu_2.setGeometry(QRect(410, 200, 101, 30))
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
        self.cbxTipoEdu_reg_estu = QComboBox(self.frGrado_reg_estu_2)
        self.cbxTipoEdu_reg_estu.addItem("")
        self.cbxTipoEdu_reg_estu.addItem("")
        self.cbxTipoEdu_reg_estu.addItem("")
        self.cbxTipoEdu_reg_estu.setObjectName(u"cbxTipoEdu_reg_estu")
        self.cbxTipoEdu_reg_estu.setGeometry(QRect(5, 5, 91, 21))
        self.cbxTipoEdu_reg_estu.setMaximumSize(QSize(180, 30))
        self.cbxTipoEdu_reg_estu.setFont(font7)
        self.cbxTipoEdu_reg_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxTipoEdu_reg_estu.setStyleSheet(u"border: transparent;")
        self.cbxTipoEdu_reg_estu.setIconSize(QSize(5, 5))
        icon3 = QIcon()
        icon3.addFile(u":/icons/personales_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/personales_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.stackRegistro_estudiante.addTab(self.stackRegistro_estudiantePage1, icon3, "")
        self.stackRegistro_estudiantePage2 = QWidget()
        self.stackRegistro_estudiantePage2.setObjectName(u"stackRegistro_estudiantePage2")
        self.lblStudent_nombres_3 = QLabel(self.stackRegistro_estudiantePage2)
        self.lblStudent_nombres_3.setObjectName(u"lblStudent_nombres_3")
        self.lblStudent_nombres_3.setGeometry(QRect(10, 50, 81, 30))
        self.lblStudent_nombres_3.setMinimumSize(QSize(0, 30))
        self.lblStudent_nombres_3.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_nombres_3.setFont(font1)
        self.lblStudent_nombres_3.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_nombres_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_2 = QWidget(self.stackRegistro_estudiantePage2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 90, 921, 261))
        self.widget_2.setStyleSheet(u"background-color: rgb(242, 245, 247);\n"
"border-radius: 10px;\n"
"border: white;\n"
"color: #2d2d2d;")
        self.lblStudent_nombres_2 = QLabel(self.widget_2)
        self.lblStudent_nombres_2.setObjectName(u"lblStudent_nombres_2")
        self.lblStudent_nombres_2.setGeometry(QRect(10, 100, 81, 30))
        self.lblStudent_nombres_2.setMinimumSize(QSize(0, 30))
        self.lblStudent_nombres_2.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_nombres_2.setFont(font1)
        self.lblStudent_nombres_2.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_nombres_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneApellido_reg_estu_repre = QLineEdit(self.widget_2)
        self.lneApellido_reg_estu_repre.setObjectName(u"lneApellido_reg_estu_repre")
        self.lneApellido_reg_estu_repre.setGeometry(QRect(100, 60, 371, 30))
        self.lneApellido_reg_estu_repre.setMinimumSize(QSize(350, 30))
        self.lneApellido_reg_estu_repre.setMaximumSize(QSize(400, 30))
        self.lneApellido_reg_estu_repre.setFont(font)
        self.lneApellido_reg_estu_repre.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneApellido_reg_estu_repre.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 1px 4px;\n"
"    background-color: white;\n"
"}")
        self.lneApellido_reg_estu_repre.setMaxLength(100)
        self.lneApellido_reg_estu_repre.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_repre = QLabel(self.widget_2)
        self.lblStudent_apellido_repre.setObjectName(u"lblStudent_apellido_repre")
        self.lblStudent_apellido_repre.setGeometry(QRect(10, 60, 81, 30))
        self.lblStudent_apellido_repre.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_repre.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_repre.setFont(font1)
        self.lblStudent_apellido_repre.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido_repre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneNombre_reg_estu_repre = QLineEdit(self.widget_2)
        self.lneNombre_reg_estu_repre.setObjectName(u"lneNombre_reg_estu_repre")
        self.lneNombre_reg_estu_repre.setGeometry(QRect(100, 100, 371, 30))
        self.lneNombre_reg_estu_repre.setMinimumSize(QSize(350, 30))
        self.lneNombre_reg_estu_repre.setMaximumSize(QSize(400, 30))
        self.lneNombre_reg_estu_repre.setFont(font)
        self.lneNombre_reg_estu_repre.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneNombre_reg_estu_repre.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneNombre_reg_estu_repre.setMaxLength(100)
        self.lneNombre_reg_estu_repre.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_dir_repre = QLabel(self.widget_2)
        self.lblStudent_dir_repre.setObjectName(u"lblStudent_dir_repre")
        self.lblStudent_dir_repre.setGeometry(QRect(10, 140, 81, 30))
        self.lblStudent_dir_repre.setMinimumSize(QSize(0, 30))
        self.lblStudent_dir_repre.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_dir_repre.setFont(font1)
        self.lblStudent_dir_repre.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_dir_repre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneDir_reg_estu_repre = QLineEdit(self.widget_2)
        self.lneDir_reg_estu_repre.setObjectName(u"lneDir_reg_estu_repre")
        self.lneDir_reg_estu_repre.setGeometry(QRect(100, 140, 801, 31))
        self.lneDir_reg_estu_repre.setMinimumSize(QSize(400, 30))
        self.lneDir_reg_estu_repre.setMaximumSize(QSize(900, 60))
        self.lneDir_reg_estu_repre.setFont(font)
        self.lneDir_reg_estu_repre.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneDir_reg_estu_repre.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneDir_reg_estu_repre.setMaxLength(100)
        self.lneDir_reg_estu_repre.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneEdad_reg_estu_repre = QLineEdit(self.widget_2)
        self.lneEdad_reg_estu_repre.setObjectName(u"lneEdad_reg_estu_repre")
        self.lneEdad_reg_estu_repre.setGeometry(QRect(840, 60, 61, 30))
        self.lneEdad_reg_estu_repre.setMinimumSize(QSize(50, 30))
        self.lneEdad_reg_estu_repre.setMaximumSize(QSize(300, 30))
        self.lneEdad_reg_estu_repre.setFont(font)
        self.lneEdad_reg_estu_repre.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneEdad_reg_estu_repre.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneEdad_reg_estu_repre.setMaxLength(2)
        self.lneEdad_reg_estu_repre.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneEdad_reg_estu_repre.setReadOnly(True)
        self.label_41 = QLabel(self.widget_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(10, 180, 121, 30))
        self.label_41.setMinimumSize(QSize(0, 30))
        self.label_41.setMaximumSize(QSize(16777215, 30))
        self.label_41.setFont(font1)
        self.label_41.setStyleSheet(u"background-color: transparent;")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneNum_reg_estu_repre = QLineEdit(self.widget_2)
        self.lneNum_reg_estu_repre.setObjectName(u"lneNum_reg_estu_repre")
        self.lneNum_reg_estu_repre.setGeometry(QRect(140, 180, 291, 30))
        self.lneNum_reg_estu_repre.setMinimumSize(QSize(100, 30))
        self.lneNum_reg_estu_repre.setMaximumSize(QSize(400, 30))
        self.lneNum_reg_estu_repre.setFont(font)
        self.lneNum_reg_estu_repre.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneNum_reg_estu_repre.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneNum_reg_estu_repre.setMaxLength(12)
        self.lneNum_reg_estu_repre.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_fechaNac_repre = QLabel(self.widget_2)
        self.lblStudent_fechaNac_repre.setObjectName(u"lblStudent_fechaNac_repre")
        self.lblStudent_fechaNac_repre.setGeometry(QRect(500, 100, 91, 30))
        self.lblStudent_fechaNac_repre.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre.setFont(font1)
        self.lblStudent_fechaNac_repre.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_edad_repre = QLabel(self.widget_2)
        self.lblStudent_edad_repre.setObjectName(u"lblStudent_edad_repre")
        self.lblStudent_edad_repre.setGeometry(QRect(770, 60, 61, 30))
        self.lblStudent_edad_repre.setMinimumSize(QSize(0, 30))
        self.lblStudent_edad_repre.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_edad_repre.setFont(font1)
        self.lblStudent_edad_repre.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_edad_repre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneCedula_reg_estu_repre = QLineEdit(self.widget_2)
        self.lneCedula_reg_estu_repre.setObjectName(u"lneCedula_reg_estu_repre")
        self.lneCedula_reg_estu_repre.setGeometry(QRect(600, 60, 151, 30))
        self.lneCedula_reg_estu_repre.setMinimumSize(QSize(100, 30))
        self.lneCedula_reg_estu_repre.setMaximumSize(QSize(300, 30))
        self.lneCedula_reg_estu_repre.setFont(font)
        self.lneCedula_reg_estu_repre.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneCedula_reg_estu_repre.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneCedula_reg_estu_repre.setMaxLength(10)
        self.lneCedula_reg_estu_repre.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneCorreo_reg_estu_repre = QLineEdit(self.widget_2)
        self.lneCorreo_reg_estu_repre.setObjectName(u"lneCorreo_reg_estu_repre")
        self.lneCorreo_reg_estu_repre.setGeometry(QRect(570, 180, 291, 30))
        self.lneCorreo_reg_estu_repre.setMinimumSize(QSize(100, 30))
        self.lneCorreo_reg_estu_repre.setMaximumSize(QSize(400, 30))
        self.lneCorreo_reg_estu_repre.setFont(font)
        self.lneCorreo_reg_estu_repre.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneCorreo_reg_estu_repre.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneCorreo_reg_estu_repre.setMaxLength(100)
        self.lneCorreo_reg_estu_repre.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_38 = QLabel(self.widget_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(450, 180, 111, 30))
        self.label_38.setMinimumSize(QSize(0, 30))
        self.label_38.setMaximumSize(QSize(16777215, 30))
        self.label_38.setFont(font1)
        self.label_38.setStyleSheet(u"background-color: transparent;")
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_genero_repre = QLabel(self.widget_2)
        self.lblStudent_genero_repre.setObjectName(u"lblStudent_genero_repre")
        self.lblStudent_genero_repre.setGeometry(QRect(770, 100, 61, 30))
        self.lblStudent_genero_repre.setMinimumSize(QSize(0, 30))
        self.lblStudent_genero_repre.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_genero_repre.setFont(font1)
        self.lblStudent_genero_repre.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_genero_repre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitulo_registro_estudiante_2 = QLabel(self.widget_2)
        self.lblTitulo_registro_estudiante_2.setObjectName(u"lblTitulo_registro_estudiante_2")
        self.lblTitulo_registro_estudiante_2.setGeometry(QRect(0, 0, 921, 41))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(17)
        font8.setBold(True)
        self.lblTitulo_registro_estudiante_2.setFont(font8)
        self.lblTitulo_registro_estudiante_2.setStyleSheet(u"")
        self.lblTitulo_registro_estudiante_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_fechaNac_repre_4 = QLabel(self.widget_2)
        self.lblStudent_fechaNac_repre_4.setObjectName(u"lblStudent_fechaNac_repre_4")
        self.lblStudent_fechaNac_repre_4.setGeometry(QRect(500, 60, 91, 30))
        self.lblStudent_fechaNac_repre_4.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_4.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_4.setFont(font1)
        self.lblStudent_fechaNac_repre_4.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneFechaNac_reg_estu_repre = QDateEdit(self.widget_2)
        self.lneFechaNac_reg_estu_repre.setObjectName(u"lneFechaNac_reg_estu_repre")
        self.lneFechaNac_reg_estu_repre.setGeometry(QRect(600, 100, 151, 30))
        self.lneFechaNac_reg_estu_repre.setMinimumSize(QSize(151, 30))
        self.lneFechaNac_reg_estu_repre.setMaximumSize(QSize(151, 30))
        self.lneFechaNac_reg_estu_repre.setFont(font)
        self.lneFechaNac_reg_estu_repre.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneFechaNac_reg_estu_repre.setStyleSheet(u"QDateEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 12px;\n"
"    background-color: white;\n"
"}\n"
"/* Vista de d\u00edas (el grid del calendario) */\n"
"QDateEdit QAbstractItemView {\n"
"    background-color: white;\n"
"    color: #2d2d2d;\n"
"    selection-background-color: #2980b9;\n"
"    selection-color: white;\n"
"}\n"
"/* Botones de navegaci\u00f3n (mes anterior/siguiente) y combos de mes/a\u00f1o */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #90caf9;   /* Fondo del encabezado */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: #2d2d2d;              /* Texto de mes y a\u00f1o */\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 4px 8px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #d6eaff;   /* Hover sobre mes/a\u00f1o o flechas */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Hover sobre los d\u00edas */\n"
"QDateEdit QAbs"
                        "tractItemView::item:hover {\n"
"    background-color: #2980b9;   /* azul claro */\n"
"    color: #000;\n"
"}\n"
"")
        self.lneFechaNac_reg_estu_repre.setCalendarPopup(True)
        self.btnConsult_ci_repre = QPushButton(self.widget_2)
        self.btnConsult_ci_repre.setObjectName(u"btnConsult_ci_repre")
        self.btnConsult_ci_repre.setGeometry(QRect(630, 20, 101, 30))
        sizePolicy.setHeightForWidth(self.btnConsult_ci_repre.sizePolicy().hasHeightForWidth())
        self.btnConsult_ci_repre.setSizePolicy(sizePolicy)
        self.btnConsult_ci_repre.setMinimumSize(QSize(60, 30))
        self.btnConsult_ci_repre.setMaximumSize(QSize(300, 60))
        self.btnConsult_ci_repre.setFont(font3)
        self.btnConsult_ci_repre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnConsult_ci_repre.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnConsult_ci_repre.setStyleSheet(u"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 10px;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/buscar_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnConsult_ci_repre.setIcon(icon4)
        self.btnConsult_ci_repre.setIconSize(QSize(15, 15))
        self.frseccion_3 = QFrame(self.widget_2)
        self.frseccion_3.setObjectName(u"frseccion_3")
        self.frseccion_3.setGeometry(QRect(840, 100, 61, 30))
        self.frseccion_3.setMinimumSize(QSize(50, 30))
        self.frseccion_3.setMaximumSize(QSize(200, 40))
        self.frseccion_3.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #2980b9;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox{\n"
"	background-color: white;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frseccion_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frseccion_3.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxGenero_reg_estu_repre = QComboBox(self.frseccion_3)
        self.cbxGenero_reg_estu_repre.addItem("")
        self.cbxGenero_reg_estu_repre.addItem("")
        self.cbxGenero_reg_estu_repre.addItem("")
        self.cbxGenero_reg_estu_repre.setObjectName(u"cbxGenero_reg_estu_repre")
        self.cbxGenero_reg_estu_repre.setGeometry(QRect(5, 5, 51, 21))
        self.cbxGenero_reg_estu_repre.setMaximumSize(QSize(180, 30))
        self.cbxGenero_reg_estu_repre.setFont(font1)
        self.cbxGenero_reg_estu_repre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxGenero_reg_estu_repre.setStyleSheet(u"")
        self.cbxGenero_reg_estu_repre.setIconSize(QSize(5, 5))
        self.lneObser_reg_estu_repre = QLineEdit(self.widget_2)
        self.lneObser_reg_estu_repre.setObjectName(u"lneObser_reg_estu_repre")
        self.lneObser_reg_estu_repre.setGeometry(QRect(130, 220, 771, 31))
        self.lneObser_reg_estu_repre.setMinimumSize(QSize(400, 30))
        self.lneObser_reg_estu_repre.setMaximumSize(QSize(900, 60))
        self.lneObser_reg_estu_repre.setFont(font)
        self.lneObser_reg_estu_repre.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneObser_reg_estu_repre.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneObser_reg_estu_repre.setMaxLength(200)
        self.lneObser_reg_estu_repre.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_dir_repre_2 = QLabel(self.widget_2)
        self.lblStudent_dir_repre_2.setObjectName(u"lblStudent_dir_repre_2")
        self.lblStudent_dir_repre_2.setGeometry(QRect(10, 220, 111, 30))
        self.lblStudent_dir_repre_2.setMinimumSize(QSize(0, 30))
        self.lblStudent_dir_repre_2.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_dir_repre_2.setFont(font1)
        self.lblStudent_dir_repre_2.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_dir_repre_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneMadre_reg_estu = QLineEdit(self.stackRegistro_estudiantePage2)
        self.lneMadre_reg_estu.setObjectName(u"lneMadre_reg_estu")
        self.lneMadre_reg_estu.setGeometry(QRect(90, 10, 281, 30))
        self.lneMadre_reg_estu.setMinimumSize(QSize(150, 30))
        self.lneMadre_reg_estu.setMaximumSize(QSize(400, 30))
        self.lneMadre_reg_estu.setFont(font)
        self.lneMadre_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneMadre_reg_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneMadre_reg_estu.setMaxLength(100)
        self.lneMadre_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneCI_madre_reg_estu = QLineEdit(self.stackRegistro_estudiantePage2)
        self.lneCI_madre_reg_estu.setObjectName(u"lneCI_madre_reg_estu")
        self.lneCI_madre_reg_estu.setGeometry(QRect(510, 10, 151, 30))
        self.lneCI_madre_reg_estu.setMinimumSize(QSize(100, 30))
        self.lneCI_madre_reg_estu.setMaximumSize(QSize(300, 30))
        self.lneCI_madre_reg_estu.setFont(font)
        self.lneCI_madre_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneCI_madre_reg_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneCI_madre_reg_estu.setMaxLength(10)
        self.lneCI_madre_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneCI_padre_reg_estu = QLineEdit(self.stackRegistro_estudiantePage2)
        self.lneCI_padre_reg_estu.setObjectName(u"lneCI_padre_reg_estu")
        self.lneCI_padre_reg_estu.setGeometry(QRect(510, 50, 151, 30))
        self.lneCI_padre_reg_estu.setMinimumSize(QSize(100, 30))
        self.lneCI_padre_reg_estu.setMaximumSize(QSize(300, 30))
        self.lneCI_padre_reg_estu.setFont(font)
        self.lneCI_padre_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneCI_padre_reg_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneCI_padre_reg_estu.setMaxLength(10)
        self.lneCI_padre_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_fechaNac_repre_3 = QLabel(self.stackRegistro_estudiantePage2)
        self.lblStudent_fechaNac_repre_3.setObjectName(u"lblStudent_fechaNac_repre_3")
        self.lblStudent_fechaNac_repre_3.setGeometry(QRect(390, 50, 121, 30))
        self.lblStudent_fechaNac_repre_3.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_3.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_3.setFont(font1)
        self.lblStudent_fechaNac_repre_3.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_fechaNac_repre_2 = QLabel(self.stackRegistro_estudiantePage2)
        self.lblStudent_fechaNac_repre_2.setObjectName(u"lblStudent_fechaNac_repre_2")
        self.lblStudent_fechaNac_repre_2.setGeometry(QRect(390, 10, 121, 30))
        self.lblStudent_fechaNac_repre_2.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_2.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_2.setFont(font1)
        self.lblStudent_fechaNac_repre_2.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lnePadre_reg_estu = QLineEdit(self.stackRegistro_estudiantePage2)
        self.lnePadre_reg_estu.setObjectName(u"lnePadre_reg_estu")
        self.lnePadre_reg_estu.setGeometry(QRect(90, 50, 281, 30))
        self.lnePadre_reg_estu.setMinimumSize(QSize(150, 30))
        self.lnePadre_reg_estu.setMaximumSize(QSize(400, 30))
        self.lnePadre_reg_estu.setFont(font)
        self.lnePadre_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lnePadre_reg_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lnePadre_reg_estu.setMaxLength(100)
        self.lnePadre_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_repre_2 = QLabel(self.stackRegistro_estudiantePage2)
        self.lblStudent_apellido_repre_2.setObjectName(u"lblStudent_apellido_repre_2")
        self.lblStudent_apellido_repre_2.setGeometry(QRect(10, 10, 81, 30))
        self.lblStudent_apellido_repre_2.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_repre_2.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_repre_2.setFont(font1)
        self.lblStudent_apellido_repre_2.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido_repre_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_fechaNac_repre_5 = QLabel(self.stackRegistro_estudiantePage2)
        self.lblStudent_fechaNac_repre_5.setObjectName(u"lblStudent_fechaNac_repre_5")
        self.lblStudent_fechaNac_repre_5.setGeometry(QRect(670, 50, 91, 30))
        self.lblStudent_fechaNac_repre_5.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_5.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_5.setFont(font1)
        self.lblStudent_fechaNac_repre_5.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneOcup_padre_reg_estu = QLineEdit(self.stackRegistro_estudiantePage2)
        self.lneOcup_padre_reg_estu.setObjectName(u"lneOcup_padre_reg_estu")
        self.lneOcup_padre_reg_estu.setGeometry(QRect(760, 50, 151, 30))
        self.lneOcup_padre_reg_estu.setMinimumSize(QSize(100, 30))
        self.lneOcup_padre_reg_estu.setMaximumSize(QSize(300, 30))
        self.lneOcup_padre_reg_estu.setFont(font)
        self.lneOcup_padre_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneOcup_padre_reg_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneOcup_padre_reg_estu.setMaxLength(200)
        self.lneOcup_padre_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneOcup_madre_reg_estu = QLineEdit(self.stackRegistro_estudiantePage2)
        self.lneOcup_madre_reg_estu.setObjectName(u"lneOcup_madre_reg_estu")
        self.lneOcup_madre_reg_estu.setGeometry(QRect(760, 10, 151, 30))
        self.lneOcup_madre_reg_estu.setMinimumSize(QSize(100, 30))
        self.lneOcup_madre_reg_estu.setMaximumSize(QSize(300, 30))
        self.lneOcup_madre_reg_estu.setFont(font)
        self.lneOcup_madre_reg_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneOcup_madre_reg_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneOcup_madre_reg_estu.setMaxLength(200)
        self.lneOcup_madre_reg_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_fechaNac_repre_6 = QLabel(self.stackRegistro_estudiantePage2)
        self.lblStudent_fechaNac_repre_6.setObjectName(u"lblStudent_fechaNac_repre_6")
        self.lblStudent_fechaNac_repre_6.setGeometry(QRect(670, 10, 91, 30))
        self.lblStudent_fechaNac_repre_6.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_6.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_6.setFont(font1)
        self.lblStudent_fechaNac_repre_6.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon5 = QIcon()
        icon5.addFile(u":/icons/padres_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icons/padres_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.stackRegistro_estudiante.addTab(self.stackRegistro_estudiantePage2, icon5, "")
        self.btnEditCedula_reg_estu = QPushButton(self.widget)
        self.btnEditCedula_reg_estu.setObjectName(u"btnEditCedula_reg_estu")
        self.btnEditCedula_reg_estu.setGeometry(QRect(480, 40, 121, 30))
        sizePolicy.setHeightForWidth(self.btnEditCedula_reg_estu.sizePolicy().hasHeightForWidth())
        self.btnEditCedula_reg_estu.setSizePolicy(sizePolicy)
        self.btnEditCedula_reg_estu.setMinimumSize(QSize(90, 30))
        self.btnEditCedula_reg_estu.setMaximumSize(QSize(150, 60))
        self.btnEditCedula_reg_estu.setFont(font3)
        self.btnEditCedula_reg_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEditCedula_reg_estu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnEditCedula_reg_estu.setStyleSheet(u" border-radius: 10px;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/editar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEditCedula_reg_estu.setIcon(icon6)
        self.btnEditCedula_reg_estu.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(registro_estu)

        self.stackRegistro_estudiante.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(registro_estu)
    # setupUi

    def retranslateUi(self, registro_estu):
        registro_estu.setWindowTitle(QCoreApplication.translate("registro_estu", u"Dialog", None))
        self.lneCedula_reg_estu.setInputMask("")
        self.lneCedula_reg_estu.setText("")
        self.lneCedula_reg_estu.setPlaceholderText("")
        self.lblCedula_registro_estudiante.setText(QCoreApplication.translate("registro_estu", u"C\u00e9dula Estudiantil", None))
        self.btnGuardar_reg_estu.setText(QCoreApplication.translate("registro_estu", u"Guardar", None))
        self.btnLimpiar_reg_estu.setText(QCoreApplication.translate("registro_estu", u"Limpiar campos", None))
        self.btnGenCedula_reg_estu.setText(QCoreApplication.translate("registro_estu", u"Generar Cedula", None))
        self.lblTitulo_reg_estu.setText(QCoreApplication.translate("registro_estu", u"Nuevo registro de estudiante", None))
        self.lblLogo_reg_estu.setText("")
        self.lblStudent_apellido.setText(QCoreApplication.translate("registro_estu", u"Apellidos", None))
        self.lneApellido_reg_estu.setText("")
        self.lneApellido_reg_estu.setPlaceholderText("")
        self.lneNombre_reg_estu.setText("")
        self.lneNombre_reg_estu.setPlaceholderText("")
        self.lblStudent_nombres.setText(QCoreApplication.translate("registro_estu", u"Nombres", None))
        self.lblStudent_lugarNac.setText(QCoreApplication.translate("registro_estu", u"Lugar Nac.", None))
        self.lblStudent_fechaNac.setText(QCoreApplication.translate("registro_estu", u"Fecha Nac.", None))
        self.lneCity_reg_estu.setText("")
        self.lneCity_reg_estu.setPlaceholderText("")
        self.lneEdad_reg_estu.setText("")
        self.lneEdad_reg_estu.setPlaceholderText("")
        self.lblStudent_edad.setText(QCoreApplication.translate("registro_estu", u"Edad", None))
        self.lblStudent_genero.setText(QCoreApplication.translate("registro_estu", u"G\u00e9nero", None))
        self.lneDir_reg_estu.setText("")
        self.lneDir_reg_estu.setPlaceholderText("")
        self.lblStudent_dir.setText(QCoreApplication.translate("registro_estu", u"Direcci\u00f3n", None))
        self.label_31.setText(QCoreApplication.translate("registro_estu", u"Tipo educaci\u00f3n", None))
        self.label_33.setText(QCoreApplication.translate("registro_estu", u"Grado", None))
        self.label_34.setText(QCoreApplication.translate("registro_estu", u"Secci\u00f3n", None))
        self.label_42.setText(QCoreApplication.translate("registro_estu", u"Talla Camisa", None))
        self.lneTallaC_reg_estu.setText("")
        self.lneTallaC_reg_estu.setPlaceholderText(QCoreApplication.translate("registro_estu", u"Ej: S", None))
        self.label_44.setText(QCoreApplication.translate("registro_estu", u"Talla Pantal\u00f3n", None))
        self.lneTallaP_reg_estu.setText("")
        self.lneTallaP_reg_estu.setPlaceholderText(QCoreApplication.translate("registro_estu", u"Ej:28", None))
        self.lneTallaZ_reg_estu.setText("")
        self.lneTallaZ_reg_estu.setPlaceholderText(QCoreApplication.translate("registro_estu", u"Ej:30", None))
        self.label_49.setText(QCoreApplication.translate("registro_estu", u"Talla Zapatos", None))
        self.lneFechaNac_reg_estu.setDisplayFormat(QCoreApplication.translate("registro_estu", u"yyyy/M/d", None))
        self.lneFechaIng_reg_estu.setDisplayFormat(QCoreApplication.translate("registro_estu", u"yyyy/M/d", None))
        self.lblStudent_fechaIng.setText(QCoreApplication.translate("registro_estu", u"Fecha Ing.", None))
        self.cbxGrado_reg_estu.setItemText(0, "")
        self.cbxGrado_reg_estu.setItemText(1, QCoreApplication.translate("registro_estu", u"1ro", None))
        self.cbxGrado_reg_estu.setItemText(2, QCoreApplication.translate("registro_estu", u"2do", None))
        self.cbxGrado_reg_estu.setItemText(3, QCoreApplication.translate("registro_estu", u"3ro", None))
        self.cbxGrado_reg_estu.setItemText(4, QCoreApplication.translate("registro_estu", u"4to", None))
        self.cbxGrado_reg_estu.setItemText(5, QCoreApplication.translate("registro_estu", u"5to", None))
        self.cbxGrado_reg_estu.setItemText(6, QCoreApplication.translate("registro_estu", u"6to", None))

        self.cbxGenero_reg_estu.setItemText(0, "")
        self.cbxGenero_reg_estu.setItemText(1, QCoreApplication.translate("registro_estu", u"M", None))
        self.cbxGenero_reg_estu.setItemText(2, QCoreApplication.translate("registro_estu", u"F", None))

        self.cbxTipoEdu_reg_estu.setItemText(0, "")
        self.cbxTipoEdu_reg_estu.setItemText(1, QCoreApplication.translate("registro_estu", u"Inicial", None))
        self.cbxTipoEdu_reg_estu.setItemText(2, QCoreApplication.translate("registro_estu", u"Primaria", None))

        self.stackRegistro_estudiante.setTabText(self.stackRegistro_estudiante.indexOf(self.stackRegistro_estudiantePage1), QCoreApplication.translate("registro_estu", u"Datos personales", None))
        self.lblStudent_nombres_3.setText(QCoreApplication.translate("registro_estu", u"Padre", None))
        self.lblStudent_nombres_2.setText(QCoreApplication.translate("registro_estu", u"Nombres", None))
        self.lneApellido_reg_estu_repre.setText("")
        self.lneApellido_reg_estu_repre.setPlaceholderText("")
        self.lblStudent_apellido_repre.setText(QCoreApplication.translate("registro_estu", u"Apellidos", None))
        self.lneNombre_reg_estu_repre.setText("")
        self.lneNombre_reg_estu_repre.setPlaceholderText("")
        self.lblStudent_dir_repre.setText(QCoreApplication.translate("registro_estu", u"Direcci\u00f3n", None))
        self.lneDir_reg_estu_repre.setText("")
        self.lneDir_reg_estu_repre.setPlaceholderText("")
        self.lneEdad_reg_estu_repre.setText("")
        self.lneEdad_reg_estu_repre.setPlaceholderText("")
        self.label_41.setText(QCoreApplication.translate("registro_estu", u"Num. Contact.", None))
        self.lneNum_reg_estu_repre.setText("")
        self.lneNum_reg_estu_repre.setPlaceholderText("")
        self.lblStudent_fechaNac_repre.setText(QCoreApplication.translate("registro_estu", u"Fecha Nac.", None))
        self.lblStudent_edad_repre.setText(QCoreApplication.translate("registro_estu", u"Edad", None))
        self.lneCedula_reg_estu_repre.setText("")
        self.lneCedula_reg_estu_repre.setPlaceholderText("")
        self.lneCorreo_reg_estu_repre.setText("")
        self.lneCorreo_reg_estu_repre.setPlaceholderText("")
        self.label_38.setText(QCoreApplication.translate("registro_estu", u"Correo Elect.", None))
        self.lblStudent_genero_repre.setText(QCoreApplication.translate("registro_estu", u"G\u00e9nero", None))
        self.lblTitulo_registro_estudiante_2.setText(QCoreApplication.translate("registro_estu", u"Datos representante", None))
        self.lblStudent_fechaNac_repre_4.setText(QCoreApplication.translate("registro_estu", u"Cedula", None))
        self.lneFechaNac_reg_estu_repre.setDisplayFormat(QCoreApplication.translate("registro_estu", u"yyyy/M/d", None))
        self.btnConsult_ci_repre.setText(QCoreApplication.translate("registro_estu", u"Consultar", None))
        self.cbxGenero_reg_estu_repre.setItemText(0, "")
        self.cbxGenero_reg_estu_repre.setItemText(1, QCoreApplication.translate("registro_estu", u"M", None))
        self.cbxGenero_reg_estu_repre.setItemText(2, QCoreApplication.translate("registro_estu", u"F", None))

        self.lneObser_reg_estu_repre.setText("")
        self.lneObser_reg_estu_repre.setPlaceholderText("")
        self.lblStudent_dir_repre_2.setText(QCoreApplication.translate("registro_estu", u"Observaci\u00f3n:", None))
        self.lneMadre_reg_estu.setText("")
        self.lneMadre_reg_estu.setPlaceholderText("")
        self.lneCI_madre_reg_estu.setText("")
        self.lneCI_madre_reg_estu.setPlaceholderText("")
        self.lneCI_padre_reg_estu.setText("")
        self.lneCI_padre_reg_estu.setPlaceholderText("")
        self.lblStudent_fechaNac_repre_3.setText(QCoreApplication.translate("registro_estu", u"Cedula Padre", None))
        self.lblStudent_fechaNac_repre_2.setText(QCoreApplication.translate("registro_estu", u"Cedula Madre", None))
        self.lnePadre_reg_estu.setText("")
        self.lnePadre_reg_estu.setPlaceholderText("")
        self.lblStudent_apellido_repre_2.setText(QCoreApplication.translate("registro_estu", u"Madre", None))
        self.lblStudent_fechaNac_repre_5.setText(QCoreApplication.translate("registro_estu", u"Ocupaci\u00f3n", None))
        self.lneOcup_padre_reg_estu.setText("")
        self.lneOcup_padre_reg_estu.setPlaceholderText("")
        self.lneOcup_madre_reg_estu.setText("")
        self.lneOcup_madre_reg_estu.setPlaceholderText("")
        self.lblStudent_fechaNac_repre_6.setText(QCoreApplication.translate("registro_estu", u"Ocupaci\u00f3n", None))
        self.stackRegistro_estudiante.setTabText(self.stackRegistro_estudiante.indexOf(self.stackRegistro_estudiantePage2), QCoreApplication.translate("registro_estu", u"Padres y Representante", None))
        self.btnEditCedula_reg_estu.setText(QCoreApplication.translate("registro_estu", u"Editar c\u00e9dula", None))
    # retranslateUi

