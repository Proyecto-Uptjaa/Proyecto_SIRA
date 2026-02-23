# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro_emple.ui'
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

class Ui_registro_emple(object):
    def setupUi(self, registro_emple):
        if not registro_emple.objectName():
            registro_emple.setObjectName(u"registro_emple")
        registro_emple.resize(1000, 600)
        registro_emple.setMinimumSize(QSize(1000, 600))
        registro_emple.setMaximumSize(QSize(1000, 600))
        registro_emple.setStyleSheet(u"background-color: #f5f6fa;")
        self.gridLayout = QGridLayout(registro_emple)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(registro_emple)
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
        self.lneCedula_reg_emple = QLineEdit(self.widget)
        self.lneCedula_reg_emple.setObjectName(u"lneCedula_reg_emple")
        self.lneCedula_reg_emple.setGeometry(QRect(200, 40, 200, 31))
        self.lneCedula_reg_emple.setMinimumSize(QSize(200, 30))
        self.lneCedula_reg_emple.setMaximumSize(QSize(200, 50))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(13)
        self.lneCedula_reg_emple.setFont(font)
        self.lneCedula_reg_emple.setStyleSheet(u"")
        self.lneCedula_reg_emple.setMaxLength(9)
        self.lneCedula_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneCedula_reg_emple.setReadOnly(False)
        self.lneCedula_reg_emple.setClearButtonEnabled(True)
        self.lblCedula_registro_estudiante = QLabel(self.widget)
        self.lblCedula_registro_estudiante.setObjectName(u"lblCedula_registro_estudiante")
        self.lblCedula_registro_estudiante.setGeometry(QRect(30, 40, 171, 31))
        self.lblCedula_registro_estudiante.setMinimumSize(QSize(50, 30))
        self.lblCedula_registro_estudiante.setMaximumSize(QSize(16777215, 50))
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
        self.lblTitulo_reg_emple = QLabel(self.widget)
        self.lblTitulo_reg_emple.setObjectName(u"lblTitulo_reg_emple")
        self.lblTitulo_reg_emple.setGeometry(QRect(701, 10, 191, 81))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(19)
        font2.setBold(True)
        self.lblTitulo_reg_emple.setFont(font2)
        self.lblTitulo_reg_emple.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblTitulo_reg_emple.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_reg_emple.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_reg_emple.setScaledContents(False)
        self.lblTitulo_reg_emple.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_reg_emple.setWordWrap(True)
        self.lblTitulo_reg_emple.setIndent(0)
        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(900, 20, 3, 61))
        self.line_2.setMinimumSize(QSize(3, 61))
        self.line_2.setMaximumSize(QSize(3, 61))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblLogo_reg_emple = QLabel(self.widget)
        self.lblLogo_reg_emple.setObjectName(u"lblLogo_reg_emple")
        self.lblLogo_reg_emple.setGeometry(QRect(910, 20, 51, 61))
        self.lblLogo_reg_emple.setMinimumSize(QSize(50, 50))
        self.lblLogo_reg_emple.setMaximumSize(QSize(130, 70))
        self.lblLogo_reg_emple.setStyleSheet(u"background-color: transparent;")
        self.lblLogo_reg_emple.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_reg_emple.setScaledContents(True)
        self.btnGuardar_reg_emple = QPushButton(self.widget)
        self.btnGuardar_reg_emple.setObjectName(u"btnGuardar_reg_emple")
        self.btnGuardar_reg_emple.setGeometry(QRect(841, 510, 120, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGuardar_reg_emple.sizePolicy().hasHeightForWidth())
        self.btnGuardar_reg_emple.setSizePolicy(sizePolicy)
        self.btnGuardar_reg_emple.setMinimumSize(QSize(120, 40))
        self.btnGuardar_reg_emple.setMaximumSize(QSize(120, 60))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.btnGuardar_reg_emple.setFont(font3)
        self.btnGuardar_reg_emple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGuardar_reg_emple.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnGuardar_reg_emple.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/guardar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGuardar_reg_emple.setIcon(icon)
        self.btnGuardar_reg_emple.setIconSize(QSize(20, 20))
        self.btnLimpiar_reg_emple = QPushButton(self.widget)
        self.btnLimpiar_reg_emple.setObjectName(u"btnLimpiar_reg_emple")
        self.btnLimpiar_reg_emple.setGeometry(QRect(680, 530, 141, 31))
        sizePolicy.setHeightForWidth(self.btnLimpiar_reg_emple.sizePolicy().hasHeightForWidth())
        self.btnLimpiar_reg_emple.setSizePolicy(sizePolicy)
        self.btnLimpiar_reg_emple.setMinimumSize(QSize(120, 30))
        self.btnLimpiar_reg_emple.setMaximumSize(QSize(150, 40))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.btnLimpiar_reg_emple.setFont(font4)
        self.btnLimpiar_reg_emple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLimpiar_reg_emple.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnLimpiar_reg_emple.setStyleSheet(u"QPushButton {\n"
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
        self.btnLimpiar_reg_emple.setIcon(icon1)
        self.stackRegistro_emple = QTabWidget(self.widget)
        self.stackRegistro_emple.setObjectName(u"stackRegistro_emple")
        self.stackRegistro_emple.setGeometry(QRect(30, 120, 921, 371))
        font5 = QFont()
        font5.setBold(True)
        self.stackRegistro_emple.setFont(font5)
        self.stackRegistro_emple.setStyleSheet(u"QTabWidget{\n"
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
        self.stackRegistro_emple.setTabShape(QTabWidget.TabShape.Rounded)
        self.stackRegistro_emplePage1 = QWidget()
        self.stackRegistro_emplePage1.setObjectName(u"stackRegistro_emplePage1")
        self.lblStudent_apellido = QLabel(self.stackRegistro_emplePage1)
        self.lblStudent_apellido.setObjectName(u"lblStudent_apellido")
        self.lblStudent_apellido.setGeometry(QRect(10, 20, 81, 30))
        self.lblStudent_apellido.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido.setFont(font1)
        self.lblStudent_apellido.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneApellidos_reg_emple = QLineEdit(self.stackRegistro_emplePage1)
        self.lneApellidos_reg_emple.setObjectName(u"lneApellidos_reg_emple")
        self.lneApellidos_reg_emple.setGeometry(QRect(100, 20, 371, 30))
        self.lneApellidos_reg_emple.setMinimumSize(QSize(350, 30))
        self.lneApellidos_reg_emple.setMaximumSize(QSize(400, 30))
        self.lneApellidos_reg_emple.setFont(font)
        self.lneApellidos_reg_emple.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneApellidos_reg_emple.setStyleSheet(u"")
        self.lneApellidos_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneNombres_reg_emple = QLineEdit(self.stackRegistro_emplePage1)
        self.lneNombres_reg_emple.setObjectName(u"lneNombres_reg_emple")
        self.lneNombres_reg_emple.setGeometry(QRect(100, 60, 371, 30))
        self.lneNombres_reg_emple.setMinimumSize(QSize(350, 30))
        self.lneNombres_reg_emple.setMaximumSize(QSize(400, 30))
        self.lneNombres_reg_emple.setFont(font)
        self.lneNombres_reg_emple.setStyleSheet(u"")
        self.lneNombres_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_nombres = QLabel(self.stackRegistro_emplePage1)
        self.lblStudent_nombres.setObjectName(u"lblStudent_nombres")
        self.lblStudent_nombres.setGeometry(QRect(10, 60, 81, 30))
        self.lblStudent_nombres.setMinimumSize(QSize(0, 30))
        self.lblStudent_nombres.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_nombres.setFont(font1)
        self.lblStudent_nombres.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_nombres.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_fechaNac = QLabel(self.stackRegistro_emplePage1)
        self.lblStudent_fechaNac.setObjectName(u"lblStudent_fechaNac")
        self.lblStudent_fechaNac.setGeometry(QRect(490, 20, 111, 30))
        self.lblStudent_fechaNac.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac.setFont(font1)
        self.lblStudent_fechaNac.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneEdad_reg_emple = QLineEdit(self.stackRegistro_emplePage1)
        self.lneEdad_reg_emple.setObjectName(u"lneEdad_reg_emple")
        self.lneEdad_reg_emple.setGeometry(QRect(840, 20, 61, 30))
        self.lneEdad_reg_emple.setMinimumSize(QSize(50, 30))
        self.lneEdad_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneEdad_reg_emple.setFont(font)
        self.lneEdad_reg_emple.setStyleSheet(u"")
        self.lneEdad_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneEdad_reg_emple.setReadOnly(True)
        self.lblStudent_edad = QLabel(self.stackRegistro_emplePage1)
        self.lblStudent_edad.setObjectName(u"lblStudent_edad")
        self.lblStudent_edad.setGeometry(QRect(770, 20, 61, 30))
        self.lblStudent_edad.setMinimumSize(QSize(0, 30))
        self.lblStudent_edad.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_edad.setFont(font1)
        self.lblStudent_edad.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_edad.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_genero = QLabel(self.stackRegistro_emplePage1)
        self.lblStudent_genero.setObjectName(u"lblStudent_genero")
        self.lblStudent_genero.setGeometry(QRect(770, 60, 61, 30))
        self.lblStudent_genero.setMinimumSize(QSize(0, 30))
        self.lblStudent_genero.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_genero.setFont(font1)
        self.lblStudent_genero.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_genero.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneDir_reg_emple = QLineEdit(self.stackRegistro_emplePage1)
        self.lneDir_reg_emple.setObjectName(u"lneDir_reg_emple")
        self.lneDir_reg_emple.setGeometry(QRect(100, 110, 801, 60))
        self.lneDir_reg_emple.setMinimumSize(QSize(400, 30))
        self.lneDir_reg_emple.setMaximumSize(QSize(900, 60))
        self.lneDir_reg_emple.setFont(font)
        self.lneDir_reg_emple.setStyleSheet(u"")
        self.lneDir_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_dir = QLabel(self.stackRegistro_emplePage1)
        self.lblStudent_dir.setObjectName(u"lblStudent_dir")
        self.lblStudent_dir.setGeometry(QRect(10, 110, 81, 30))
        self.lblStudent_dir.setMinimumSize(QSize(0, 30))
        self.lblStudent_dir.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_dir.setFont(font1)
        self.lblStudent_dir.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_dir.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneNum_reg_emple = QLineEdit(self.stackRegistro_emplePage1)
        self.lneNum_reg_emple.setObjectName(u"lneNum_reg_emple")
        self.lneNum_reg_emple.setGeometry(QRect(150, 190, 291, 30))
        self.lneNum_reg_emple.setMinimumSize(QSize(100, 30))
        self.lneNum_reg_emple.setMaximumSize(QSize(400, 30))
        self.lneNum_reg_emple.setFont(font)
        self.lneNum_reg_emple.setStyleSheet(u"")
        self.lneNum_reg_emple.setMaxLength(12)
        self.lneNum_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_31 = QLabel(self.stackRegistro_emplePage1)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 230, 131, 30))
        self.label_31.setMinimumSize(QSize(0, 30))
        self.label_31.setMaximumSize(QSize(16777215, 30))
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"background-color: transparent;")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_32 = QLabel(self.stackRegistro_emplePage1)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 190, 131, 30))
        self.label_32.setMinimumSize(QSize(0, 30))
        self.label_32.setMaximumSize(QSize(16777215, 30))
        self.label_32.setFont(font1)
        self.label_32.setStyleSheet(u"background-color: transparent;")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneCorreo_reg_emple = QLineEdit(self.stackRegistro_emplePage1)
        self.lneCorreo_reg_emple.setObjectName(u"lneCorreo_reg_emple")
        self.lneCorreo_reg_emple.setGeometry(QRect(150, 230, 291, 30))
        self.lneCorreo_reg_emple.setMinimumSize(QSize(100, 30))
        self.lneCorreo_reg_emple.setMaximumSize(QSize(400, 30))
        self.lneCorreo_reg_emple.setFont(font)
        self.lneCorreo_reg_emple.setStyleSheet(u"")
        self.lneCorreo_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneFechaNac_reg_emple = QDateEdit(self.stackRegistro_emplePage1)
        self.lneFechaNac_reg_emple.setObjectName(u"lneFechaNac_reg_emple")
        self.lneFechaNac_reg_emple.setGeometry(QRect(610, 20, 151, 30))
        self.lneFechaNac_reg_emple.setMinimumSize(QSize(100, 30))
        self.lneFechaNac_reg_emple.setMaximumSize(QSize(151, 30))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(12)
        self.lneFechaNac_reg_emple.setFont(font6)
        self.lneFechaNac_reg_emple.setStyleSheet(u"QDateEdit {\n"
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
"QCalendarWidget {\n"
"            background-color: white;\n"
"        }\n"
"        QCalendarWidget QWidget {\n"
"            background-color: white;\n"
"            color: #2d2d2d;\n"
"        }\n"
"        QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"            background-color: #2980b9;\n"
"            min-height: 30px;\n"
"            max-height: 30px;\n"
"            border-top-left-radius: 8px;\n"
"            border-top-right-radius: 8px;\n"
"            padding: 2px 2px;\n"
"        }\n"
"        QCalendarWidget QToolButton {\n"
"            color: white;\n"
"            background-color: transparent;\n"
"            font"
                        "-weight: bold;\n"
"            font-size: 13px;\n"
"            border: none;\n"
"            border-radius: 5px;\n"
"            padding: 4px 5px;\n"
"            min-height: 28px;\n"
"        }\n"
"        QCalendarWidget QToolButton:hover {\n"
"            background-color: rgba(255,255,255,0.22);\n"
"        }\n"
"        QCalendarWidget QToolButton:pressed {\n"
"            background-color: rgba(255,255,255,0.38);\n"
"        }\n"
"        QCalendarWidget QToolButton#qt_calendar_monthbutton,\n"
"        QCalendarWidget QToolButton#qt_calendar_yearbutton {\n"
"            font-size: 13px;\n"
"            font-weight: bold;\n"
"            padding: 4px 14px;\n"
"        }\n"
"        QCalendarWidget QToolButton::menu-indicator {\n"
"            image: none;\n"
"            width: 0;\n"
"        }\n"
"        QCalendarWidget QMenu {\n"
"            background-color: white;\n"
"            border: 1.5px solid #2980b9;\n"
"            border-radius: 8px;\n"
"            padding: 4px 0px;\n"
"            color"
                        ": #2d2d2d;\n"
"        }\n"
"        QCalendarWidget QMenu::item {\n"
"            padding: 6px 22px;\n"
"            border-radius: 5px;\n"
"            margin: 1px 5px;\n"
"        }\n"
"        QCalendarWidget QMenu::item:selected {\n"
"            background-color: #2980b9;\n"
"            color: white;\n"
"        }\n"
"        QCalendarWidget QSpinBox {\n"
"            background-color: white;\n"
"            border: 1.5px solid #90caf9;\n"
"            border-radius: 5px;\n"
"            color: #2d2d2d;\n"
"            padding: 2px 4px;\n"
"            font-weight: bold;\n"
"            selection-background-color: #2980b9;\n"
"            selection-color: white;\n"
"        }\n"
"        QCalendarWidget QSpinBox::up-button,\n"
"        QCalendarWidget QSpinBox::down-button {\n"
"            background-color: #e3f2fd;\n"
"            border-radius: 3px;\n"
"            width: 14px;\n"
"        }\n"
"        QCalendarWidget QSpinBox::up-button:hover,\n"
"        QCalendarWidget QSpinBox::down-button:hover"
                        " {\n"
"            background-color: #2980b9;\n"
"        }\n"
"        QCalendarWidget QAbstractItemView {\n"
"            background-color: white;\n"
"            alternate-background-color: #f8fbff;\n"
"            color: #2d2d2d;\n"
"            gridline-color: #e8eaf0;\n"
"            selection-background-color: #2980b9;\n"
"            selection-color: white;\n"
"            outline: none;\n"
"            border: none;\n"
"            font-size: 12px;\n"
"        }\n"
"        QCalendarWidget QAbstractItemView:disabled {\n"
"            color: #bbb;\n"
"        }")
        self.lneFechaNac_reg_emple.setCalendarPopup(True)
        self.lblStudent_fechaNac_repre_5 = QLabel(self.stackRegistro_emplePage1)
        self.lblStudent_fechaNac_repre_5.setObjectName(u"lblStudent_fechaNac_repre_5")
        self.lblStudent_fechaNac_repre_5.setGeometry(QRect(460, 190, 41, 30))
        self.lblStudent_fechaNac_repre_5.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_5.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_5.setFont(font1)
        self.lblStudent_fechaNac_repre_5.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneRIF_reg_emple = QLineEdit(self.stackRegistro_emplePage1)
        self.lneRIF_reg_emple.setObjectName(u"lneRIF_reg_emple")
        self.lneRIF_reg_emple.setGeometry(QRect(510, 190, 181, 30))
        self.lneRIF_reg_emple.setMinimumSize(QSize(100, 30))
        self.lneRIF_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneRIF_reg_emple.setFont(font)
        self.lneRIF_reg_emple.setStyleSheet(u"")
        self.lneRIF_reg_emple.setMaxLength(15)
        self.lneRIF_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneCentroV_reg_emple = QLineEdit(self.stackRegistro_emplePage1)
        self.lneCentroV_reg_emple.setObjectName(u"lneCentroV_reg_emple")
        self.lneCentroV_reg_emple.setGeometry(QRect(150, 270, 400, 30))
        self.lneCentroV_reg_emple.setMinimumSize(QSize(400, 30))
        self.lneCentroV_reg_emple.setMaximumSize(QSize(400, 30))
        self.lneCentroV_reg_emple.setFont(font)
        self.lneCentroV_reg_emple.setStyleSheet(u"")
        self.lneCentroV_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_nombres_3 = QLabel(self.stackRegistro_emplePage1)
        self.lblStudent_nombres_3.setObjectName(u"lblStudent_nombres_3")
        self.lblStudent_nombres_3.setGeometry(QRect(10, 270, 131, 30))
        self.lblStudent_nombres_3.setMinimumSize(QSize(0, 30))
        self.lblStudent_nombres_3.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_nombres_3.setFont(font1)
        self.lblStudent_nombres_3.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_nombres_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frseccion_3 = QFrame(self.stackRegistro_emplePage1)
        self.frseccion_3.setObjectName(u"frseccion_3")
        self.frseccion_3.setGeometry(QRect(840, 60, 61, 30))
        self.frseccion_3.setMinimumSize(QSize(50, 30))
        self.frseccion_3.setMaximumSize(QSize(200, 40))
        self.frseccion_3.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #2980b9;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox{\n"
"	background-color: white;\n"
"	border: transparent;\n"
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
        self.cbxGenero_reg_emple = QComboBox(self.frseccion_3)
        self.cbxGenero_reg_emple.addItem("")
        self.cbxGenero_reg_emple.addItem("")
        self.cbxGenero_reg_emple.addItem("")
        self.cbxGenero_reg_emple.setObjectName(u"cbxGenero_reg_emple")
        self.cbxGenero_reg_emple.setGeometry(QRect(5, 5, 51, 21))
        self.cbxGenero_reg_emple.setMaximumSize(QSize(180, 30))
        self.cbxGenero_reg_emple.setFont(font1)
        self.cbxGenero_reg_emple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxGenero_reg_emple.setStyleSheet(u"QComboBox {\n"
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
        self.cbxGenero_reg_emple.setIconSize(QSize(5, 5))
        self.lneLugarNac_reg_emple = QLineEdit(self.stackRegistro_emplePage1)
        self.lneLugarNac_reg_emple.setObjectName(u"lneLugarNac_reg_emple")
        self.lneLugarNac_reg_emple.setGeometry(QRect(610, 60, 151, 30))
        self.lneLugarNac_reg_emple.setMinimumSize(QSize(100, 30))
        self.lneLugarNac_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneLugarNac_reg_emple.setFont(font)
        self.lneLugarNac_reg_emple.setStyleSheet(u"")
        self.lneLugarNac_reg_emple.setMaxLength(100)
        self.lneLugarNac_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblLugar_nac = QLabel(self.stackRegistro_emplePage1)
        self.lblLugar_nac.setObjectName(u"lblLugar_nac")
        self.lblLugar_nac.setGeometry(QRect(490, 60, 111, 30))
        self.lblLugar_nac.setMinimumSize(QSize(0, 30))
        self.lblLugar_nac.setMaximumSize(QSize(16777215, 30))
        self.lblLugar_nac.setFont(font1)
        self.lblLugar_nac.setStyleSheet(u"background-color: transparent;")
        self.lblLugar_nac.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneTallaC_reg_emple = QLineEdit(self.stackRegistro_emplePage1)
        self.lneTallaC_reg_emple.setObjectName(u"lneTallaC_reg_emple")
        self.lneTallaC_reg_emple.setGeometry(QRect(840, 190, 61, 30))
        self.lneTallaC_reg_emple.setMinimumSize(QSize(50, 30))
        self.lneTallaC_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneTallaC_reg_emple.setFont(font6)
        self.lneTallaC_reg_emple.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneTallaC_reg_emple.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneTallaC_reg_emple.setMaxLength(3)
        self.lneTallaC_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_42 = QLabel(self.stackRegistro_emplePage1)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(720, 190, 111, 30))
        self.label_42.setMinimumSize(QSize(0, 30))
        self.label_42.setMaximumSize(QSize(16777215, 30))
        self.label_42.setFont(font1)
        self.label_42.setStyleSheet(u"background-color: transparent;")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneTallaP_reg_emple = QLineEdit(self.stackRegistro_emplePage1)
        self.lneTallaP_reg_emple.setObjectName(u"lneTallaP_reg_emple")
        self.lneTallaP_reg_emple.setGeometry(QRect(840, 230, 61, 30))
        self.lneTallaP_reg_emple.setMinimumSize(QSize(50, 30))
        self.lneTallaP_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneTallaP_reg_emple.setFont(font6)
        self.lneTallaP_reg_emple.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneTallaP_reg_emple.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneTallaP_reg_emple.setMaxLength(2)
        self.lneTallaP_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_44 = QLabel(self.stackRegistro_emplePage1)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(720, 230, 111, 30))
        self.label_44.setMinimumSize(QSize(0, 30))
        self.label_44.setMaximumSize(QSize(16777215, 30))
        self.label_44.setFont(font1)
        self.label_44.setStyleSheet(u"background-color: transparent;")
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneTallaZ_reg_emple = QLineEdit(self.stackRegistro_emplePage1)
        self.lneTallaZ_reg_emple.setObjectName(u"lneTallaZ_reg_emple")
        self.lneTallaZ_reg_emple.setGeometry(QRect(840, 270, 61, 30))
        self.lneTallaZ_reg_emple.setMinimumSize(QSize(50, 30))
        self.lneTallaZ_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneTallaZ_reg_emple.setFont(font6)
        self.lneTallaZ_reg_emple.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneTallaZ_reg_emple.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"}")
        self.lneTallaZ_reg_emple.setMaxLength(2)
        self.lneTallaZ_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_49 = QLabel(self.stackRegistro_emplePage1)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(720, 270, 111, 30))
        self.label_49.setMinimumSize(QSize(0, 30))
        self.label_49.setMaximumSize(QSize(16777215, 30))
        self.label_49.setFont(font1)
        self.label_49.setStyleSheet(u"background-color: transparent;")
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon2 = QIcon()
        icon2.addFile(u":/icons/personales_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/personales_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.stackRegistro_emple.addTab(self.stackRegistro_emplePage1, icon2, "")
        self.stackRegistro_emplePage2 = QWidget()
        self.stackRegistro_emplePage2.setObjectName(u"stackRegistro_emplePage2")
        self.lneFechaIngreso_reg_emple = QDateEdit(self.stackRegistro_emplePage2)
        self.lneFechaIngreso_reg_emple.setObjectName(u"lneFechaIngreso_reg_emple")
        self.lneFechaIngreso_reg_emple.setGeometry(QRect(710, 50, 151, 30))
        self.lneFechaIngreso_reg_emple.setMinimumSize(QSize(151, 30))
        self.lneFechaIngreso_reg_emple.setMaximumSize(QSize(151, 30))
        self.lneFechaIngreso_reg_emple.setFont(font6)
        self.lneFechaIngreso_reg_emple.setStyleSheet(u"QDateEdit {\n"
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
"QCalendarWidget {\n"
"            background-color: white;\n"
"        }\n"
"        QCalendarWidget QWidget {\n"
"            background-color: white;\n"
"            color: #2d2d2d;\n"
"        }\n"
"        QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"            background-color: #2980b9;\n"
"            min-height: 30px;\n"
"            max-height: 30px;\n"
"            border-top-left-radius: 8px;\n"
"            border-top-right-radius: 8px;\n"
"            padding: 2px 2px;\n"
"        }\n"
"        QCalendarWidget QToolButton {\n"
"            color: white;\n"
"            background-color: transparent;\n"
"            font"
                        "-weight: bold;\n"
"            font-size: 13px;\n"
"            border: none;\n"
"            border-radius: 5px;\n"
"            padding: 4px 5px;\n"
"            min-height: 28px;\n"
"        }\n"
"        QCalendarWidget QToolButton:hover {\n"
"            background-color: rgba(255,255,255,0.22);\n"
"        }\n"
"        QCalendarWidget QToolButton:pressed {\n"
"            background-color: rgba(255,255,255,0.38);\n"
"        }\n"
"        QCalendarWidget QToolButton#qt_calendar_monthbutton,\n"
"        QCalendarWidget QToolButton#qt_calendar_yearbutton {\n"
"            font-size: 13px;\n"
"            font-weight: bold;\n"
"            padding: 4px 14px;\n"
"        }\n"
"        QCalendarWidget QToolButton::menu-indicator {\n"
"            image: none;\n"
"            width: 0;\n"
"        }\n"
"        QCalendarWidget QMenu {\n"
"            background-color: white;\n"
"            border: 1.5px solid #2980b9;\n"
"            border-radius: 8px;\n"
"            padding: 4px 0px;\n"
"            color"
                        ": #2d2d2d;\n"
"        }\n"
"        QCalendarWidget QMenu::item {\n"
"            padding: 6px 22px;\n"
"            border-radius: 5px;\n"
"            margin: 1px 5px;\n"
"        }\n"
"        QCalendarWidget QMenu::item:selected {\n"
"            background-color: #2980b9;\n"
"            color: white;\n"
"        }\n"
"        QCalendarWidget QSpinBox {\n"
"            background-color: white;\n"
"            border: 1.5px solid #90caf9;\n"
"            border-radius: 5px;\n"
"            color: #2d2d2d;\n"
"            padding: 2px 4px;\n"
"            font-weight: bold;\n"
"            selection-background-color: #2980b9;\n"
"            selection-color: white;\n"
"        }\n"
"        QCalendarWidget QSpinBox::up-button,\n"
"        QCalendarWidget QSpinBox::down-button {\n"
"            background-color: #e3f2fd;\n"
"            border-radius: 3px;\n"
"            width: 14px;\n"
"        }\n"
"        QCalendarWidget QSpinBox::up-button:hover,\n"
"        QCalendarWidget QSpinBox::down-button:hover"
                        " {\n"
"            background-color: #2980b9;\n"
"        }\n"
"        QCalendarWidget QAbstractItemView {\n"
"            background-color: white;\n"
"            alternate-background-color: #f8fbff;\n"
"            color: #2d2d2d;\n"
"            gridline-color: #e8eaf0;\n"
"            selection-background-color: #2980b9;\n"
"            selection-color: white;\n"
"            outline: none;\n"
"            border: none;\n"
"            font-size: 12px;\n"
"        }\n"
"        QCalendarWidget QAbstractItemView:disabled {\n"
"            color: #bbb;\n"
"        }")
        self.lneFechaIngreso_reg_emple.setCalendarPopup(True)
        self.lblStudent_nombres_2 = QLabel(self.stackRegistro_emplePage2)
        self.lblStudent_nombres_2.setObjectName(u"lblStudent_nombres_2")
        self.lblStudent_nombres_2.setGeometry(QRect(50, 100, 81, 30))
        self.lblStudent_nombres_2.setMinimumSize(QSize(0, 30))
        self.lblStudent_nombres_2.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_nombres_2.setFont(font1)
        self.lblStudent_nombres_2.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_nombres_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_fechaNac_repre_4 = QLabel(self.stackRegistro_emplePage2)
        self.lblStudent_fechaNac_repre_4.setObjectName(u"lblStudent_fechaNac_repre_4")
        self.lblStudent_fechaNac_repre_4.setGeometry(QRect(580, 150, 121, 30))
        self.lblStudent_fechaNac_repre_4.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_4.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_4.setFont(font1)
        self.lblStudent_fechaNac_repre_4.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_apellido_repre = QLabel(self.stackRegistro_emplePage2)
        self.lblStudent_apellido_repre.setObjectName(u"lblStudent_apellido_repre")
        self.lblStudent_apellido_repre.setGeometry(QRect(40, 40, 101, 41))
        self.lblStudent_apellido_repre.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_repre.setMaximumSize(QSize(16777215, 50))
        self.lblStudent_apellido_repre.setFont(font1)
        self.lblStudent_apellido_repre.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido_repre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_fechaNac_repre = QLabel(self.stackRegistro_emplePage2)
        self.lblStudent_fechaNac_repre.setObjectName(u"lblStudent_fechaNac_repre")
        self.lblStudent_fechaNac_repre.setGeometry(QRect(580, 50, 121, 30))
        self.lblStudent_fechaNac_repre.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre.setFont(font1)
        self.lblStudent_fechaNac_repre.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneCarnet_reg_emple = QLineEdit(self.stackRegistro_emplePage2)
        self.lneCarnet_reg_emple.setObjectName(u"lneCarnet_reg_emple")
        self.lneCarnet_reg_emple.setGeometry(QRect(710, 150, 151, 30))
        self.lneCarnet_reg_emple.setMinimumSize(QSize(100, 30))
        self.lneCarnet_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneCarnet_reg_emple.setFont(font)
        self.lneCarnet_reg_emple.setStyleSheet(u"")
        self.lneCarnet_reg_emple.setMaxLength(15)
        self.lneCarnet_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.frmTitulo_emple = QFrame(self.stackRegistro_emplePage2)
        self.frmTitulo_emple.setObjectName(u"frmTitulo_emple")
        self.frmTitulo_emple.setGeometry(QRect(150, 50, 400, 30))
        self.frmTitulo_emple.setMinimumSize(QSize(400, 30))
        self.frmTitulo_emple.setMaximumSize(QSize(400, 30))
        self.frmTitulo_emple.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 2px solid #2980b9;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frmTitulo_emple.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmTitulo_emple.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxNivel_instruccion_reg_emple = QComboBox(self.frmTitulo_emple)
        self.cbxNivel_instruccion_reg_emple.addItem("")
        self.cbxNivel_instruccion_reg_emple.addItem("")
        self.cbxNivel_instruccion_reg_emple.addItem("")
        self.cbxNivel_instruccion_reg_emple.addItem("")
        self.cbxNivel_instruccion_reg_emple.addItem("")
        self.cbxNivel_instruccion_reg_emple.setObjectName(u"cbxNivel_instruccion_reg_emple")
        self.cbxNivel_instruccion_reg_emple.setGeometry(QRect(5, 4, 390, 20))
        self.cbxNivel_instruccion_reg_emple.setMinimumSize(QSize(390, 0))
        self.cbxNivel_instruccion_reg_emple.setMaximumSize(QSize(390, 30))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(12)
        font7.setBold(False)
        self.cbxNivel_instruccion_reg_emple.setFont(font7)
        self.cbxNivel_instruccion_reg_emple.setStyleSheet(u"QComboBox {\n"
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
        self.cbxNivel_instruccion_reg_emple.setIconSize(QSize(10, 10))
        self.lblStudent_fechaNac_repre_6 = QLabel(self.stackRegistro_emplePage2)
        self.lblStudent_fechaNac_repre_6.setObjectName(u"lblStudent_fechaNac_repre_6")
        self.lblStudent_fechaNac_repre_6.setGeometry(QRect(20, 250, 121, 30))
        self.lblStudent_fechaNac_repre_6.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_6.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_6.setFont(font1)
        self.lblStudent_fechaNac_repre_6.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneRAC_reg_emple = QLineEdit(self.stackRegistro_emplePage2)
        self.lneRAC_reg_emple.setObjectName(u"lneRAC_reg_emple")
        self.lneRAC_reg_emple.setGeometry(QRect(130, 250, 151, 30))
        self.lneRAC_reg_emple.setMinimumSize(QSize(100, 30))
        self.lneRAC_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneRAC_reg_emple.setFont(font)
        self.lneRAC_reg_emple.setStyleSheet(u"")
        self.lneRAC_reg_emple.setMaxLength(15)
        self.lneRAC_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblHoras_reg_emple = QLabel(self.stackRegistro_emplePage2)
        self.lblHoras_reg_emple.setObjectName(u"lblHoras_reg_emple")
        self.lblHoras_reg_emple.setGeometry(QRect(290, 250, 151, 30))
        self.lblHoras_reg_emple.setMinimumSize(QSize(0, 30))
        self.lblHoras_reg_emple.setMaximumSize(QSize(16777215, 30))
        self.lblHoras_reg_emple.setFont(font1)
        self.lblHoras_reg_emple.setStyleSheet(u"background-color: transparent;")
        self.lblHoras_reg_emple.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneHoras_aca_reg_emple = QLineEdit(self.stackRegistro_emplePage2)
        self.lneHoras_aca_reg_emple.setObjectName(u"lneHoras_aca_reg_emple")
        self.lneHoras_aca_reg_emple.setGeometry(QRect(450, 250, 101, 30))
        self.lneHoras_aca_reg_emple.setMinimumSize(QSize(50, 30))
        self.lneHoras_aca_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneHoras_aca_reg_emple.setFont(font)
        self.lneHoras_aca_reg_emple.setStyleSheet(u"")
        self.lneHoras_aca_reg_emple.setMaxLength(5)
        self.lneHoras_aca_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.frmTitulo_emple_2 = QFrame(self.stackRegistro_emplePage2)
        self.frmTitulo_emple_2.setObjectName(u"frmTitulo_emple_2")
        self.frmTitulo_emple_2.setGeometry(QRect(150, 100, 400, 30))
        self.frmTitulo_emple_2.setMinimumSize(QSize(400, 30))
        self.frmTitulo_emple_2.setMaximumSize(QSize(400, 30))
        self.frmTitulo_emple_2.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 2px solid #2980b9;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frmTitulo_emple_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmTitulo_emple_2.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxCargo_reg_emple = QComboBox(self.frmTitulo_emple_2)
        self.cbxCargo_reg_emple.addItem("")
        self.cbxCargo_reg_emple.setObjectName(u"cbxCargo_reg_emple")
        self.cbxCargo_reg_emple.setGeometry(QRect(5, 4, 390, 20))
        self.cbxCargo_reg_emple.setMinimumSize(QSize(390, 0))
        self.cbxCargo_reg_emple.setMaximumSize(QSize(390, 30))
        self.cbxCargo_reg_emple.setFont(font7)
        self.cbxCargo_reg_emple.setStyleSheet(u"QComboBox {\n"
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
        self.cbxCargo_reg_emple.setMaxVisibleItems(8)
        self.cbxCargo_reg_emple.setMaxCount(100)
        self.cbxCargo_reg_emple.setIconSize(QSize(10, 10))
        self.lneHoras_adm_reg_emple = QLineEdit(self.stackRegistro_emplePage2)
        self.lneHoras_adm_reg_emple.setObjectName(u"lneHoras_adm_reg_emple")
        self.lneHoras_adm_reg_emple.setGeometry(QRect(760, 250, 101, 30))
        self.lneHoras_adm_reg_emple.setMinimumSize(QSize(60, 30))
        self.lneHoras_adm_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneHoras_adm_reg_emple.setFont(font)
        self.lneHoras_adm_reg_emple.setStyleSheet(u"")
        self.lneHoras_adm_reg_emple.setMaxLength(5)
        self.lneHoras_adm_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblHoras_reg_emple_2 = QLabel(self.stackRegistro_emplePage2)
        self.lblHoras_reg_emple_2.setObjectName(u"lblHoras_reg_emple_2")
        self.lblHoras_reg_emple_2.setGeometry(QRect(570, 250, 181, 30))
        self.lblHoras_reg_emple_2.setMinimumSize(QSize(0, 30))
        self.lblHoras_reg_emple_2.setMaximumSize(QSize(16777215, 30))
        self.lblHoras_reg_emple_2.setFont(font1)
        self.lblHoras_reg_emple_2.setStyleSheet(u"background-color: transparent;")
        self.lblHoras_reg_emple_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblEspecialidad_reg_emple = QLabel(self.stackRegistro_emplePage2)
        self.lblEspecialidad_reg_emple.setObjectName(u"lblEspecialidad_reg_emple")
        self.lblEspecialidad_reg_emple.setGeometry(QRect(40, 200, 101, 30))
        self.lblEspecialidad_reg_emple.setMinimumSize(QSize(0, 30))
        self.lblEspecialidad_reg_emple.setMaximumSize(QSize(16777215, 30))
        self.lblEspecialidad_reg_emple.setFont(font1)
        self.lblEspecialidad_reg_emple.setStyleSheet(u"background-color: transparent;")
        self.lblEspecialidad_reg_emple.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frmTitulo_emple_3 = QFrame(self.stackRegistro_emplePage2)
        self.frmTitulo_emple_3.setObjectName(u"frmTitulo_emple_3")
        self.frmTitulo_emple_3.setGeometry(QRect(150, 200, 400, 30))
        self.frmTitulo_emple_3.setMinimumSize(QSize(400, 30))
        self.frmTitulo_emple_3.setMaximumSize(QSize(400, 30))
        self.frmTitulo_emple_3.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 2px solid #2980b9;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frmTitulo_emple_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmTitulo_emple_3.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxEspecialidad_reg_emple = QComboBox(self.frmTitulo_emple_3)
        self.cbxEspecialidad_reg_emple.addItem("")
        self.cbxEspecialidad_reg_emple.setObjectName(u"cbxEspecialidad_reg_emple")
        self.cbxEspecialidad_reg_emple.setGeometry(QRect(5, 4, 390, 20))
        self.cbxEspecialidad_reg_emple.setMinimumSize(QSize(390, 0))
        self.cbxEspecialidad_reg_emple.setMaximumSize(QSize(390, 30))
        self.cbxEspecialidad_reg_emple.setFont(font7)
        self.cbxEspecialidad_reg_emple.setStyleSheet(u"QComboBox {\n"
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
        self.cbxEspecialidad_reg_emple.setIconSize(QSize(10, 10))
        self.lblHoras_reg_emple_3 = QLabel(self.stackRegistro_emplePage2)
        self.lblHoras_reg_emple_3.setObjectName(u"lblHoras_reg_emple_3")
        self.lblHoras_reg_emple_3.setGeometry(QRect(580, 100, 121, 30))
        self.lblHoras_reg_emple_3.setMinimumSize(QSize(0, 30))
        self.lblHoras_reg_emple_3.setMaximumSize(QSize(16777215, 30))
        self.lblHoras_reg_emple_3.setFont(font1)
        self.lblHoras_reg_emple_3.setStyleSheet(u"background-color: transparent;")
        self.lblHoras_reg_emple_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frmTitulo_emple_4 = QFrame(self.stackRegistro_emplePage2)
        self.frmTitulo_emple_4.setObjectName(u"frmTitulo_emple_4")
        self.frmTitulo_emple_4.setGeometry(QRect(710, 100, 151, 30))
        self.frmTitulo_emple_4.setMinimumSize(QSize(60, 30))
        self.frmTitulo_emple_4.setMaximumSize(QSize(400, 30))
        self.frmTitulo_emple_4.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 2px solid #2980b9;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frmTitulo_emple_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmTitulo_emple_4.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxTipoPersonal_reg_emple = QComboBox(self.frmTitulo_emple_4)
        self.cbxTipoPersonal_reg_emple.setObjectName(u"cbxTipoPersonal_reg_emple")
        self.cbxTipoPersonal_reg_emple.setGeometry(QRect(5, 4, 141, 20))
        self.cbxTipoPersonal_reg_emple.setMinimumSize(QSize(50, 0))
        self.cbxTipoPersonal_reg_emple.setMaximumSize(QSize(390, 30))
        self.cbxTipoPersonal_reg_emple.setFont(font7)
        self.cbxTipoPersonal_reg_emple.setStyleSheet(u"QComboBox {\n"
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
        self.cbxTipoPersonal_reg_emple.setIconSize(QSize(10, 10))
        self.lblStudent_nombres_4 = QLabel(self.stackRegistro_emplePage2)
        self.lblStudent_nombres_4.setObjectName(u"lblStudent_nombres_4")
        self.lblStudent_nombres_4.setGeometry(QRect(50, 150, 81, 30))
        self.lblStudent_nombres_4.setMinimumSize(QSize(0, 30))
        self.lblStudent_nombres_4.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_nombres_4.setFont(font1)
        self.lblStudent_nombres_4.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_nombres_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneProfesion_reg_emple = QLineEdit(self.stackRegistro_emplePage2)
        self.lneProfesion_reg_emple.setObjectName(u"lneProfesion_reg_emple")
        self.lneProfesion_reg_emple.setGeometry(QRect(150, 150, 400, 30))
        self.lneProfesion_reg_emple.setMinimumSize(QSize(350, 30))
        self.lneProfesion_reg_emple.setMaximumSize(QSize(400, 30))
        self.lneProfesion_reg_emple.setFont(font)
        self.lneProfesion_reg_emple.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneProfesion_reg_emple.setStyleSheet(u"")
        self.lneProfesion_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        icon3 = QIcon()
        icon3.addFile(u":/icons/maletin_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/maletin_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.stackRegistro_emple.addTab(self.stackRegistro_emplePage2, icon3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.lneTipo_vivienda = QLineEdit(self.tab)
        self.lneTipo_vivienda.setObjectName(u"lneTipo_vivienda")
        self.lneTipo_vivienda.setGeometry(QRect(200, 60, 400, 30))
        self.lneTipo_vivienda.setMinimumSize(QSize(350, 30))
        self.lneTipo_vivienda.setMaximumSize(QSize(400, 30))
        self.lneTipo_vivienda.setFont(font)
        self.lneTipo_vivienda.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneTipo_vivienda.setStyleSheet(u"")
        self.lneTipo_vivienda.setMaxLength(50)
        self.lneTipo_vivienda.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_2 = QLabel(self.tab)
        self.lblStudent_apellido_2.setObjectName(u"lblStudent_apellido_2")
        self.lblStudent_apellido_2.setGeometry(QRect(50, 60, 141, 30))
        self.lblStudent_apellido_2.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_2.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_2.setFont(font1)
        self.lblStudent_apellido_2.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_apellido_3 = QLabel(self.tab)
        self.lblStudent_apellido_3.setObjectName(u"lblStudent_apellido_3")
        self.lblStudent_apellido_3.setGeometry(QRect(50, 130, 141, 41))
        self.lblStudent_apellido_3.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_3.setMaximumSize(QSize(16777215, 50))
        self.lblStudent_apellido_3.setFont(font1)
        self.lblStudent_apellido_3.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_apellido_3.setWordWrap(True)
        self.lneCondicion_vivienda = QLineEdit(self.tab)
        self.lneCondicion_vivienda.setObjectName(u"lneCondicion_vivienda")
        self.lneCondicion_vivienda.setGeometry(QRect(200, 130, 400, 30))
        self.lneCondicion_vivienda.setMinimumSize(QSize(350, 30))
        self.lneCondicion_vivienda.setMaximumSize(QSize(400, 30))
        self.lneCondicion_vivienda.setFont(font)
        self.lneCondicion_vivienda.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneCondicion_vivienda.setStyleSheet(u"")
        self.lneCondicion_vivienda.setMaxLength(50)
        self.lneCondicion_vivienda.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneMaterial_vivienda = QLineEdit(self.tab)
        self.lneMaterial_vivienda.setObjectName(u"lneMaterial_vivienda")
        self.lneMaterial_vivienda.setGeometry(QRect(200, 200, 400, 30))
        self.lneMaterial_vivienda.setMinimumSize(QSize(350, 30))
        self.lneMaterial_vivienda.setMaximumSize(QSize(400, 30))
        self.lneMaterial_vivienda.setFont(font)
        self.lneMaterial_vivienda.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneMaterial_vivienda.setStyleSheet(u"")
        self.lneMaterial_vivienda.setMaxLength(50)
        self.lneMaterial_vivienda.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_4 = QLabel(self.tab)
        self.lblStudent_apellido_4.setObjectName(u"lblStudent_apellido_4")
        self.lblStudent_apellido_4.setGeometry(QRect(50, 200, 141, 41))
        self.lblStudent_apellido_4.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_4.setMaximumSize(QSize(16777215, 50))
        self.lblStudent_apellido_4.setFont(font1)
        self.lblStudent_apellido_4.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_apellido_4.setWordWrap(True)
        icon4 = QIcon()
        icon4.addFile(u":/icons/vivienda_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/vivienda_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.stackRegistro_emple.addTab(self.tab, icon4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.lblStudent_apellido_5 = QLabel(self.tab_2)
        self.lblStudent_apellido_5.setObjectName(u"lblStudent_apellido_5")
        self.lblStudent_apellido_5.setGeometry(QRect(20, 30, 471, 30))
        self.lblStudent_apellido_5.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_5.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_5.setFont(font1)
        self.lblStudent_apellido_5.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_5.setWordWrap(True)
        self.lneTipo_enfermedad = QLineEdit(self.tab_2)
        self.lneTipo_enfermedad.setObjectName(u"lneTipo_enfermedad")
        self.lneTipo_enfermedad.setGeometry(QRect(500, 30, 391, 30))
        self.lneTipo_enfermedad.setMinimumSize(QSize(350, 30))
        self.lneTipo_enfermedad.setMaximumSize(QSize(400, 30))
        self.lneTipo_enfermedad.setFont(font)
        self.lneTipo_enfermedad.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneTipo_enfermedad.setStyleSheet(u"")
        self.lneTipo_enfermedad.setMaxLength(100)
        self.lneTipo_enfermedad.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneMedicamento = QLineEdit(self.tab_2)
        self.lneMedicamento.setObjectName(u"lneMedicamento")
        self.lneMedicamento.setGeometry(QRect(480, 90, 411, 30))
        self.lneMedicamento.setMinimumSize(QSize(350, 30))
        self.lneMedicamento.setMaximumSize(QSize(500, 30))
        self.lneMedicamento.setFont(font)
        self.lneMedicamento.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneMedicamento.setStyleSheet(u"")
        self.lneMedicamento.setMaxLength(100)
        self.lneMedicamento.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_6 = QLabel(self.tab_2)
        self.lblStudent_apellido_6.setObjectName(u"lblStudent_apellido_6")
        self.lblStudent_apellido_6.setGeometry(QRect(20, 90, 471, 30))
        self.lblStudent_apellido_6.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_6.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_6.setFont(font1)
        self.lblStudent_apellido_6.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneDiscapacidad = QLineEdit(self.tab_2)
        self.lneDiscapacidad.setObjectName(u"lneDiscapacidad")
        self.lneDiscapacidad.setGeometry(QRect(540, 150, 350, 30))
        self.lneDiscapacidad.setMinimumSize(QSize(350, 30))
        self.lneDiscapacidad.setMaximumSize(QSize(400, 30))
        self.lneDiscapacidad.setFont(font)
        self.lneDiscapacidad.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneDiscapacidad.setStyleSheet(u"")
        self.lneDiscapacidad.setMaxLength(50)
        self.lneDiscapacidad.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_7 = QLabel(self.tab_2)
        self.lblStudent_apellido_7.setObjectName(u"lblStudent_apellido_7")
        self.lblStudent_apellido_7.setGeometry(QRect(20, 150, 521, 30))
        self.lblStudent_apellido_7.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_7.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_7.setFont(font1)
        self.lblStudent_apellido_7.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneActividad = QLineEdit(self.tab_2)
        self.lneActividad.setObjectName(u"lneActividad")
        self.lneActividad.setGeometry(QRect(490, 210, 411, 30))
        self.lneActividad.setMinimumSize(QSize(350, 30))
        self.lneActividad.setMaximumSize(QSize(500, 30))
        self.lneActividad.setFont(font)
        self.lneActividad.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneActividad.setStyleSheet(u"")
        self.lneActividad.setMaxLength(100)
        self.lneActividad.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_8 = QLabel(self.tab_2)
        self.lblStudent_apellido_8.setObjectName(u"lblStudent_apellido_8")
        self.lblStudent_apellido_8.setGeometry(QRect(20, 210, 461, 30))
        self.lblStudent_apellido_8.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_8.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_8.setFont(font1)
        self.lblStudent_apellido_8.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneCultural = QLineEdit(self.tab_2)
        self.lneCultural.setObjectName(u"lneCultural")
        self.lneCultural.setGeometry(QRect(560, 260, 331, 30))
        self.lneCultural.setMinimumSize(QSize(300, 30))
        self.lneCultural.setMaximumSize(QSize(500, 30))
        self.lneCultural.setFont(font)
        self.lneCultural.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneCultural.setStyleSheet(u"")
        self.lneCultural.setMaxLength(100)
        self.lneCultural.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_9 = QLabel(self.tab_2)
        self.lblStudent_apellido_9.setObjectName(u"lblStudent_apellido_9")
        self.lblStudent_apellido_9.setGeometry(QRect(20, 270, 531, 30))
        self.lblStudent_apellido_9.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_9.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_9.setFont(font1)
        self.lblStudent_apellido_9.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        icon5 = QIcon()
        icon5.addFile(u":/icons/salud_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icons/salud_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.stackRegistro_emple.addTab(self.tab_2, icon5, "")

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(registro_emple)

        self.stackRegistro_emple.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(registro_emple)
    # setupUi

    def retranslateUi(self, registro_emple):
        registro_emple.setWindowTitle(QCoreApplication.translate("registro_emple", u"Dialog", None))
        self.lneCedula_reg_emple.setText("")
        self.lneCedula_reg_emple.setPlaceholderText(QCoreApplication.translate("registro_emple", u"Ej: 8320675", None))
        self.lblCedula_registro_estudiante.setText(QCoreApplication.translate("registro_emple", u"C\u00e9dula de identidad", None))
        self.lblTitulo_reg_emple.setText(QCoreApplication.translate("registro_emple", u"Nuevo registro de empleado", None))
        self.lblLogo_reg_emple.setText("")
        self.btnGuardar_reg_emple.setText(QCoreApplication.translate("registro_emple", u"Guardar", None))
        self.btnLimpiar_reg_emple.setText(QCoreApplication.translate("registro_emple", u"Limpiar campos", None))
        self.lblStudent_apellido.setText(QCoreApplication.translate("registro_emple", u"Apellidos", None))
        self.lneApellidos_reg_emple.setText("")
        self.lneApellidos_reg_emple.setPlaceholderText("")
        self.lneNombres_reg_emple.setText("")
        self.lneNombres_reg_emple.setPlaceholderText("")
        self.lblStudent_nombres.setText(QCoreApplication.translate("registro_emple", u"Nombres", None))
        self.lblStudent_fechaNac.setText(QCoreApplication.translate("registro_emple", u"Fecha Nac.", None))
        self.lneEdad_reg_emple.setText("")
        self.lneEdad_reg_emple.setPlaceholderText("")
        self.lblStudent_edad.setText(QCoreApplication.translate("registro_emple", u"Edad", None))
        self.lblStudent_genero.setText(QCoreApplication.translate("registro_emple", u"G\u00e9nero", None))
        self.lneDir_reg_emple.setText("")
        self.lneDir_reg_emple.setPlaceholderText("")
        self.lblStudent_dir.setText(QCoreApplication.translate("registro_emple", u"Direcci\u00f3n", None))
        self.lneNum_reg_emple.setText("")
        self.lneNum_reg_emple.setPlaceholderText("")
        self.label_31.setText(QCoreApplication.translate("registro_emple", u"Correo Elect.", None))
        self.label_32.setText(QCoreApplication.translate("registro_emple", u"Num. Contact.", None))
        self.lneCorreo_reg_emple.setText("")
        self.lneCorreo_reg_emple.setPlaceholderText("")
        self.lneFechaNac_reg_emple.setDisplayFormat(QCoreApplication.translate("registro_emple", u"dd-MM-yyyy", None))
        self.lblStudent_fechaNac_repre_5.setText(QCoreApplication.translate("registro_emple", u"RIF", None))
        self.lneRIF_reg_emple.setText("")
        self.lneRIF_reg_emple.setPlaceholderText("")
        self.lneCentroV_reg_emple.setText("")
        self.lneCentroV_reg_emple.setPlaceholderText("")
        self.lblStudent_nombres_3.setText(QCoreApplication.translate("registro_emple", u"Centro votaci\u00f3n", None))
        self.cbxGenero_reg_emple.setItemText(0, "")
        self.cbxGenero_reg_emple.setItemText(1, QCoreApplication.translate("registro_emple", u"M", None))
        self.cbxGenero_reg_emple.setItemText(2, QCoreApplication.translate("registro_emple", u"F", None))

        self.lneLugarNac_reg_emple.setText("")
        self.lneLugarNac_reg_emple.setPlaceholderText("")
        self.lblLugar_nac.setText(QCoreApplication.translate("registro_emple", u"Lugar de Nac.", None))
        self.lneTallaC_reg_emple.setText("")
        self.lneTallaC_reg_emple.setPlaceholderText(QCoreApplication.translate("registro_emple", u"Ej: S", None))
        self.label_42.setText(QCoreApplication.translate("registro_emple", u"Talla Camisa", None))
        self.lneTallaP_reg_emple.setText("")
        self.lneTallaP_reg_emple.setPlaceholderText(QCoreApplication.translate("registro_emple", u"Ej:28", None))
        self.label_44.setText(QCoreApplication.translate("registro_emple", u"Talla Pantal\u00f3n", None))
        self.lneTallaZ_reg_emple.setText("")
        self.lneTallaZ_reg_emple.setPlaceholderText(QCoreApplication.translate("registro_emple", u"Ej:30", None))
        self.label_49.setText(QCoreApplication.translate("registro_emple", u"Talla Zapatos", None))
        self.stackRegistro_emple.setTabText(self.stackRegistro_emple.indexOf(self.stackRegistro_emplePage1), QCoreApplication.translate("registro_emple", u"Datos Personales", None))
        self.lneFechaIngreso_reg_emple.setDisplayFormat(QCoreApplication.translate("registro_emple", u"dd-MM-yyyy", None))
        self.lblStudent_nombres_2.setText(QCoreApplication.translate("registro_emple", u"Cargo", None))
        self.lblStudent_fechaNac_repre_4.setText(QCoreApplication.translate("registro_emple", u"Num. Carnet", None))
        self.lblStudent_apellido_repre.setText(QCoreApplication.translate("registro_emple", u"Nivel\n"
"Instrucci\u00f3n", None))
        self.lblStudent_fechaNac_repre.setText(QCoreApplication.translate("registro_emple", u"Fecha Ingreso", None))
        self.lneCarnet_reg_emple.setText("")
        self.lneCarnet_reg_emple.setPlaceholderText("")
        self.cbxNivel_instruccion_reg_emple.setItemText(0, QCoreApplication.translate("registro_emple", u"Seleccione t\u00edtulo obtenido", None))
        self.cbxNivel_instruccion_reg_emple.setItemText(1, QCoreApplication.translate("registro_emple", u"Bachiller", None))
        self.cbxNivel_instruccion_reg_emple.setItemText(2, QCoreApplication.translate("registro_emple", u"T.S.U", None))
        self.cbxNivel_instruccion_reg_emple.setItemText(3, QCoreApplication.translate("registro_emple", u"Profesional Universitario", None))
        self.cbxNivel_instruccion_reg_emple.setItemText(4, QCoreApplication.translate("registro_emple", u"Postgrado", None))

        self.lblStudent_fechaNac_repre_6.setText(QCoreApplication.translate("registro_emple", u"C\u00f3digo RAC", None))
        self.lneRAC_reg_emple.setText("")
        self.lneRAC_reg_emple.setPlaceholderText("")
        self.lblHoras_reg_emple.setText(QCoreApplication.translate("registro_emple", u"Horas acad\u00e9micas", None))
        self.lneHoras_aca_reg_emple.setText("")
        self.lneHoras_aca_reg_emple.setPlaceholderText(QCoreApplication.translate("registro_emple", u"Ej: 43.33", None))
        self.cbxCargo_reg_emple.setItemText(0, QCoreApplication.translate("registro_emple", u"Seleccione cargo", None))

        self.lneHoras_adm_reg_emple.setText("")
        self.lneHoras_adm_reg_emple.setPlaceholderText(QCoreApplication.translate("registro_emple", u"Ej: 50.00", None))
        self.lblHoras_reg_emple_2.setText(QCoreApplication.translate("registro_emple", u"Horas administrativas", None))
        self.lblEspecialidad_reg_emple.setText(QCoreApplication.translate("registro_emple", u"Especialidad", None))
        self.cbxEspecialidad_reg_emple.setItemText(0, QCoreApplication.translate("registro_emple", u"Opcional...", None))

        self.lblHoras_reg_emple_3.setText(QCoreApplication.translate("registro_emple", u"Tipo personal", None))
        self.lblStudent_nombres_4.setText(QCoreApplication.translate("registro_emple", u"Profesi\u00f3n", None))
        self.lneProfesion_reg_emple.setText("")
        self.lneProfesion_reg_emple.setPlaceholderText("")
        self.stackRegistro_emple.setTabText(self.stackRegistro_emple.indexOf(self.stackRegistro_emplePage2), QCoreApplication.translate("registro_emple", u"Datos Laborales", None))
        self.lneTipo_vivienda.setText("")
        self.lneTipo_vivienda.setPlaceholderText("")
        self.lblStudent_apellido_2.setText(QCoreApplication.translate("registro_emple", u"Tipo de vivienda", None))
        self.lblStudent_apellido_3.setText(QCoreApplication.translate("registro_emple", u"Condici\u00f3n de vivienda", None))
        self.lneCondicion_vivienda.setText("")
        self.lneCondicion_vivienda.setPlaceholderText("")
        self.lneMaterial_vivienda.setText("")
        self.lneMaterial_vivienda.setPlaceholderText("")
        self.lblStudent_apellido_4.setText(QCoreApplication.translate("registro_emple", u"Tipo de material de la vivienda", None))
        self.stackRegistro_emple.setTabText(self.stackRegistro_emple.indexOf(self.tab), QCoreApplication.translate("registro_emple", u"Datos de Vivienda", None))
        self.lblStudent_apellido_5.setText(QCoreApplication.translate("registro_emple", u"\u00bfPadece alguna enfermedad? De ser positivo, indique cual:", None))
        self.lneTipo_enfermedad.setText("")
        self.lneTipo_enfermedad.setPlaceholderText("")
        self.lneMedicamento.setText("")
        self.lneMedicamento.setPlaceholderText("")
        self.lblStudent_apellido_6.setText(QCoreApplication.translate("registro_emple", u"\u00bfRequiere alg\u00fan medicamento? De ser as\u00ed, indique cual:", None))
        self.lneDiscapacidad.setText("")
        self.lneDiscapacidad.setPlaceholderText("")
        self.lblStudent_apellido_7.setText(QCoreApplication.translate("registro_emple", u"\u00bfPosee alguna discapacidad certificada? De ser as\u00ed, indique cual:", None))
        self.lneActividad.setText("")
        self.lneActividad.setPlaceholderText("")
        self.lblStudent_apellido_8.setText(QCoreApplication.translate("registro_emple", u"\u00bfPractica alguna actividad regularmente? Mencione cual:", None))
        self.lneCultural.setText("")
        self.lneCultural.setPlaceholderText("")
        self.lblStudent_apellido_9.setText(QCoreApplication.translate("registro_emple", u"\u00bfPractica alguna actividad cultural regularmente? Mencione cual:", None))
        self.stackRegistro_emple.setTabText(self.stackRegistro_emple.indexOf(self.tab_2), QCoreApplication.translate("registro_emple", u"Datos de Salud", None))
    # retranslateUi

