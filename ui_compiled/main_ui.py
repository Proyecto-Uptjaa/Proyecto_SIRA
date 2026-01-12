# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QButtonGroup,
    QCheckBox, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTableView, QToolButton, QVBoxLayout,
    QWidget)

from utils.animated_stack import AnimatedStack
from resources import resources_ui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 681)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1300, 681))
        MainWindow.setMaximumSize(QSize(1300, 681))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 640))
        self.widget_main = QWidget(self.centralwidget)
        self.widget_main.setObjectName(u"widget_main")
        self.widget_main.setGeometry(QRect(9, 9, 1291, 651))
        self.widget_main.setMaximumSize(QSize(16777215, 681))
        self.widget_main.setStyleSheet(u"QWidget{\n"
"	font-family: \"Segoe UI\";\n"
"	background-color: #f5f6fa;\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.menuFrame = QFrame(self.widget_main)
        self.menuFrame.setObjectName(u"menuFrame")
        self.menuFrame.setGeometry(QRect(10, 10, 161, 621))
        self.menuFrame.setMinimumSize(QSize(72, 590))
        self.menuFrame.setMaximumSize(QSize(200, 650))
        self.menuFrame.setStyleSheet(u"QFrame#menuFrame {\n"
"    border-radius: 16px;\n"
"	background-color: #2c3e50;\n"
"}\n"
"QPushButton {\n"
"   background: transparent;\n"
"    color: #E3F2FD;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 12px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: #0D47A1\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #F7F9FC;\n"
" 	color: #1565C0;\n"
"	\n"
"}")
        self.menuFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.stackBarra_lateral = AnimatedStack(self.menuFrame)
        self.stackBarra_lateral.setObjectName(u"stackBarra_lateral")
        self.stackBarra_lateral.setGeometry(QRect(0, 0, 161, 591))
        self.stackBarra_lateral.setStyleSheet(u"background-color: transparent;")
        self.menu_principal = QWidget()
        self.menu_principal.setObjectName(u"menu_principal")
        self.btnUsuario_home = QToolButton(self.menu_principal)
        self.btnUsuario_home.setObjectName(u"btnUsuario_home")
        self.btnUsuario_home.setGeometry(QRect(10, 543, 141, 41))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnUsuario_home.sizePolicy().hasHeightForWidth())
        self.btnUsuario_home.setSizePolicy(sizePolicy1)
        self.btnUsuario_home.setMinimumSize(QSize(50, 40))
        self.btnUsuario_home.setMaximumSize(QSize(150, 50))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.btnUsuario_home.setFont(font)
        self.btnUsuario_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnUsuario_home.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.btnUsuario_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnUsuario_home.setStyleSheet(u"QToolButton {\n"
"   background: transparent;\n"
"    color: #F3F6FF;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"text-align: left;\n"
"    padding-left: 12px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"/* --- Estilo del men\u00fa desplegable --- */\n"
"QMenu {\n"
"    background-color: white;         /* fondo blanco */\n"
"    color: black;                    /* texto negro */\n"
"    border: 1px solid #c0c0c0;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 5px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #0078d7;       /* azul Windows */\n"
"    color: white;                    /* texto blanco al seleccionar */\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/perfil_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnUsuario_home.setIcon(icon)
        self.btnUsuario_home.setIconSize(QSize(40, 40))
        self.btnUsuario_home.setCheckable(False)
        self.btnUsuario_home.setChecked(False)
        self.btnUsuario_home.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.btnUsuario_home.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.btnUsuario_home.setAutoRaise(False)
        self.btnAdmin = QPushButton(self.menu_principal)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.btnAdmin)
        self.btnAdmin.setObjectName(u"btnAdmin")
        self.btnAdmin.setGeometry(QRect(10, 260, 171, 50))
        sizePolicy1.setHeightForWidth(self.btnAdmin.sizePolicy().hasHeightForWidth())
        self.btnAdmin.setSizePolicy(sizePolicy1)
        self.btnAdmin.setMinimumSize(QSize(80, 50))
        self.btnAdmin.setMaximumSize(QSize(200, 50))
        self.btnAdmin.setFont(font)
        self.btnAdmin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdmin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnAdmin.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 12px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/admin_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/admin_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnAdmin.setIcon(icon1)
        self.btnAdmin.setIconSize(QSize(50, 50))
        self.btnAdmin.setCheckable(False)
        self.btnAdmin.setChecked(False)
        self.btnReportes = QPushButton(self.menu_principal)
        self.buttonGroup.addButton(self.btnReportes)
        self.btnReportes.setObjectName(u"btnReportes")
        self.btnReportes.setGeometry(QRect(10, 200, 171, 50))
        sizePolicy1.setHeightForWidth(self.btnReportes.sizePolicy().hasHeightForWidth())
        self.btnReportes.setSizePolicy(sizePolicy1)
        self.btnReportes.setMinimumSize(QSize(80, 50))
        self.btnReportes.setMaximumSize(QSize(200, 50))
        self.btnReportes.setFont(font)
        self.btnReportes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnReportes.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnReportes.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 12px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/reportes_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/reportes_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnReportes.setIcon(icon2)
        self.btnReportes.setIconSize(QSize(50, 50))
        self.btnReportes.setCheckable(True)
        self.btnReportes.setChecked(False)
        self.btnEmpleados = QPushButton(self.menu_principal)
        self.buttonGroup.addButton(self.btnEmpleados)
        self.btnEmpleados.setObjectName(u"btnEmpleados")
        self.btnEmpleados.setGeometry(QRect(10, 140, 171, 50))
        sizePolicy1.setHeightForWidth(self.btnEmpleados.sizePolicy().hasHeightForWidth())
        self.btnEmpleados.setSizePolicy(sizePolicy1)
        self.btnEmpleados.setMinimumSize(QSize(80, 50))
        self.btnEmpleados.setMaximumSize(QSize(200, 50))
        self.btnEmpleados.setFont(font)
        self.btnEmpleados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEmpleados.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnEmpleados.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 12px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/empleado_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/empleado_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnEmpleados.setIcon(icon3)
        self.btnEmpleados.setIconSize(QSize(50, 50))
        self.btnEmpleados.setCheckable(True)
        self.btnEmpleados.setChecked(False)
        self.btnEstudiantes = QPushButton(self.menu_principal)
        self.buttonGroup.addButton(self.btnEstudiantes)
        self.btnEstudiantes.setObjectName(u"btnEstudiantes")
        self.btnEstudiantes.setGeometry(QRect(10, 80, 171, 50))
        sizePolicy1.setHeightForWidth(self.btnEstudiantes.sizePolicy().hasHeightForWidth())
        self.btnEstudiantes.setSizePolicy(sizePolicy1)
        self.btnEstudiantes.setMinimumSize(QSize(80, 50))
        self.btnEstudiantes.setMaximumSize(QSize(200, 50))
        self.btnEstudiantes.setFont(font)
        self.btnEstudiantes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEstudiantes.setToolTipDuration(-1)
        self.btnEstudiantes.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnEstudiantes.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 12px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/estudiante_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/estudiante_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnEstudiantes.setIcon(icon4)
        self.btnEstudiantes.setIconSize(QSize(50, 50))
        self.btnEstudiantes.setCheckable(False)
        self.btnEstudiantes.setChecked(False)
        self.btnHome = QPushButton(self.menu_principal)
        self.buttonGroup.addButton(self.btnHome)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setGeometry(QRect(10, 20, 171, 50))
        sizePolicy1.setHeightForWidth(self.btnHome.sizePolicy().hasHeightForWidth())
        self.btnHome.setSizePolicy(sizePolicy1)
        self.btnHome.setMinimumSize(QSize(80, 50))
        self.btnHome.setMaximumSize(QSize(200, 50))
        self.btnHome.setFont(font)
        self.btnHome.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnHome.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnHome.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 12px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/home_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icons/home_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnHome.setIcon(icon5)
        self.btnHome.setIconSize(QSize(50, 50))
        self.btnHome.setCheckable(True)
        self.btnHome.setChecked(True)
        self.btnHome.setAutoExclusive(False)
        self.stackBarra_lateral.addWidget(self.menu_principal)
        self.estudiantes = QWidget()
        self.estudiantes.setObjectName(u"estudiantes")
        self.btnGestion_estudiantes = QPushButton(self.estudiantes)
        self.buttonGroup.addButton(self.btnGestion_estudiantes)
        self.btnGestion_estudiantes.setObjectName(u"btnGestion_estudiantes")
        self.btnGestion_estudiantes.setGeometry(QRect(10, 20, 171, 50))
        sizePolicy1.setHeightForWidth(self.btnGestion_estudiantes.sizePolicy().hasHeightForWidth())
        self.btnGestion_estudiantes.setSizePolicy(sizePolicy1)
        self.btnGestion_estudiantes.setMinimumSize(QSize(80, 50))
        self.btnGestion_estudiantes.setMaximumSize(QSize(200, 50))
        self.btnGestion_estudiantes.setFont(font)
        self.btnGestion_estudiantes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGestion_estudiantes.setToolTipDuration(-1)
        self.btnGestion_estudiantes.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnGestion_estudiantes.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 12px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/gestion_estudiantes.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icons/gestion_estudiantes_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnGestion_estudiantes.setIcon(icon6)
        self.btnGestion_estudiantes.setIconSize(QSize(50, 50))
        self.btnGestion_estudiantes.setCheckable(True)
        self.btnGestion_estudiantes.setChecked(False)
        self.btnSecciones = QPushButton(self.estudiantes)
        self.buttonGroup.addButton(self.btnSecciones)
        self.btnSecciones.setObjectName(u"btnSecciones")
        self.btnSecciones.setGeometry(QRect(10, 80, 171, 50))
        sizePolicy1.setHeightForWidth(self.btnSecciones.sizePolicy().hasHeightForWidth())
        self.btnSecciones.setSizePolicy(sizePolicy1)
        self.btnSecciones.setMinimumSize(QSize(80, 50))
        self.btnSecciones.setMaximumSize(QSize(200, 50))
        self.btnSecciones.setFont(font)
        self.btnSecciones.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSecciones.setToolTipDuration(-1)
        self.btnSecciones.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnSecciones.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 12px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/seccion2_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icons/seccion2_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnSecciones.setIcon(icon7)
        self.btnSecciones.setIconSize(QSize(50, 50))
        self.btnSecciones.setCheckable(True)
        self.btnSecciones.setChecked(False)
        self.btnEgresados = QPushButton(self.estudiantes)
        self.buttonGroup.addButton(self.btnEgresados)
        self.btnEgresados.setObjectName(u"btnEgresados")
        self.btnEgresados.setGeometry(QRect(10, 140, 171, 50))
        sizePolicy1.setHeightForWidth(self.btnEgresados.sizePolicy().hasHeightForWidth())
        self.btnEgresados.setSizePolicy(sizePolicy1)
        self.btnEgresados.setMinimumSize(QSize(80, 50))
        self.btnEgresados.setMaximumSize(QSize(200, 50))
        self.btnEgresados.setFont(font)
        self.btnEgresados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEgresados.setToolTipDuration(-1)
        self.btnEgresados.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnEgresados.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 12px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/promocion_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/icons/promocion_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnEgresados.setIcon(icon8)
        self.btnEgresados.setIconSize(QSize(50, 50))
        self.btnEgresados.setCheckable(True)
        self.btnEgresados.setChecked(False)
        self.btnRegresar_estudiantes = QPushButton(self.estudiantes)
        self.btnRegresar_estudiantes.setObjectName(u"btnRegresar_estudiantes")
        self.btnRegresar_estudiantes.setGeometry(QRect(10, 543, 141, 41))
        sizePolicy1.setHeightForWidth(self.btnRegresar_estudiantes.sizePolicy().hasHeightForWidth())
        self.btnRegresar_estudiantes.setSizePolicy(sizePolicy1)
        self.btnRegresar_estudiantes.setMinimumSize(QSize(50, 40))
        self.btnRegresar_estudiantes.setMaximumSize(QSize(200, 50))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.btnRegresar_estudiantes.setFont(font1)
        self.btnRegresar_estudiantes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnRegresar_estudiantes.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnRegresar_estudiantes.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 20px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/regresar_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRegresar_estudiantes.setIcon(icon9)
        self.btnRegresar_estudiantes.setIconSize(QSize(30, 30))
        self.btnRegresar_estudiantes.setCheckable(False)
        self.btnRegresar_estudiantes.setChecked(False)
        self.lineSeparadora_3 = QFrame(self.estudiantes)
        self.lineSeparadora_3.setObjectName(u"lineSeparadora_3")
        self.lineSeparadora_3.setGeometry(QRect(0, 530, 165, 3))
        self.lineSeparadora_3.setMinimumSize(QSize(100, 3))
        self.lineSeparadora_3.setMaximumSize(QSize(560, 3))
        self.lineSeparadora_3.setStyleSheet(u"background-color: #f5f6fa;")
        self.lineSeparadora_3.setFrameShape(QFrame.Shape.HLine)
        self.lineSeparadora_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.stackBarra_lateral.addWidget(self.estudiantes)
        self.menu_admin = QWidget()
        self.menu_admin.setObjectName(u"menu_admin")
        self.btnGestion_usuarios = QPushButton(self.menu_admin)
        self.buttonGroup.addButton(self.btnGestion_usuarios)
        self.btnGestion_usuarios.setObjectName(u"btnGestion_usuarios")
        self.btnGestion_usuarios.setGeometry(QRect(10, 50, 171, 50))
        sizePolicy1.setHeightForWidth(self.btnGestion_usuarios.sizePolicy().hasHeightForWidth())
        self.btnGestion_usuarios.setSizePolicy(sizePolicy1)
        self.btnGestion_usuarios.setMinimumSize(QSize(80, 30))
        self.btnGestion_usuarios.setMaximumSize(QSize(200, 50))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.btnGestion_usuarios.setFont(font2)
        self.btnGestion_usuarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGestion_usuarios.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnGestion_usuarios.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 2px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 20px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/gestion_usuarios_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/icons/gestion_usuarios_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnGestion_usuarios.setIcon(icon10)
        self.btnGestion_usuarios.setIconSize(QSize(18, 18))
        self.btnGestion_usuarios.setCheckable(True)
        self.btnGestion_usuarios.setChecked(False)
        self.btnGestion_usuarios.setAutoExclusive(False)
        self.btnRoles = QPushButton(self.menu_admin)
        self.buttonGroup.addButton(self.btnRoles)
        self.btnRoles.setObjectName(u"btnRoles")
        self.btnRoles.setEnabled(False)
        self.btnRoles.setGeometry(QRect(10, 100, 171, 50))
        sizePolicy1.setHeightForWidth(self.btnRoles.sizePolicy().hasHeightForWidth())
        self.btnRoles.setSizePolicy(sizePolicy1)
        self.btnRoles.setMinimumSize(QSize(80, 30))
        self.btnRoles.setMaximumSize(QSize(200, 50))
        self.btnRoles.setFont(font2)
        self.btnRoles.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnRoles.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnRoles.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 2px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 20px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/permisos_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/icons/permisos_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnRoles.setIcon(icon11)
        self.btnRoles.setIconSize(QSize(18, 18))
        self.btnRoles.setCheckable(True)
        self.btnRoles.setChecked(False)
        self.btnRoles.setAutoExclusive(False)
        self.lblResumenGeneral_2 = QLabel(self.menu_admin)
        self.lblResumenGeneral_2.setObjectName(u"lblResumenGeneral_2")
        self.lblResumenGeneral_2.setGeometry(QRect(0, 20, 161, 31))
        self.lblResumenGeneral_2.setFont(font)
        self.lblResumenGeneral_2.setStyleSheet(u"color: #bdc3c7")
        self.lblResumenGeneral_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblResumenGeneral_3 = QLabel(self.menu_admin)
        self.lblResumenGeneral_3.setObjectName(u"lblResumenGeneral_3")
        self.lblResumenGeneral_3.setGeometry(QRect(0, 160, 161, 31))
        self.lblResumenGeneral_3.setFont(font)
        self.lblResumenGeneral_3.setStyleSheet(u"color: #bdc3c7")
        self.lblResumenGeneral_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnAuditoria = QPushButton(self.menu_admin)
        self.buttonGroup.addButton(self.btnAuditoria)
        self.btnAuditoria.setObjectName(u"btnAuditoria")
        self.btnAuditoria.setGeometry(QRect(10, 190, 171, 50))
        sizePolicy1.setHeightForWidth(self.btnAuditoria.sizePolicy().hasHeightForWidth())
        self.btnAuditoria.setSizePolicy(sizePolicy1)
        self.btnAuditoria.setMinimumSize(QSize(80, 30))
        self.btnAuditoria.setMaximumSize(QSize(200, 50))
        self.btnAuditoria.setFont(font2)
        self.btnAuditoria.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAuditoria.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnAuditoria.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 2px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 20px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/auditoria_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/icons/auditoria_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnAuditoria.setIcon(icon12)
        self.btnAuditoria.setIconSize(QSize(18, 18))
        self.btnAuditoria.setCheckable(True)
        self.btnAuditoria.setChecked(False)
        self.btnAuditoria.setAutoExclusive(False)
        self.lblResumenGeneral_4 = QLabel(self.menu_admin)
        self.lblResumenGeneral_4.setObjectName(u"lblResumenGeneral_4")
        self.lblResumenGeneral_4.setGeometry(QRect(0, 260, 161, 31))
        self.lblResumenGeneral_4.setFont(font)
        self.lblResumenGeneral_4.setStyleSheet(u"color: #bdc3c7")
        self.lblResumenGeneral_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnDatos_institucion = QPushButton(self.menu_admin)
        self.buttonGroup.addButton(self.btnDatos_institucion)
        self.btnDatos_institucion.setObjectName(u"btnDatos_institucion")
        self.btnDatos_institucion.setGeometry(QRect(10, 290, 171, 50))
        sizePolicy1.setHeightForWidth(self.btnDatos_institucion.sizePolicy().hasHeightForWidth())
        self.btnDatos_institucion.setSizePolicy(sizePolicy1)
        self.btnDatos_institucion.setMinimumSize(QSize(80, 30))
        self.btnDatos_institucion.setMaximumSize(QSize(200, 50))
        self.btnDatos_institucion.setFont(font2)
        self.btnDatos_institucion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDatos_institucion.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnDatos_institucion.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 2px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 20px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/datos_institucion_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/icons/datos_institucion_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnDatos_institucion.setIcon(icon13)
        self.btnDatos_institucion.setIconSize(QSize(18, 18))
        self.btnDatos_institucion.setCheckable(True)
        self.btnDatos_institucion.setChecked(False)
        self.btnDatos_institucion.setAutoExclusive(False)
        self.lblResumenGeneral_5 = QLabel(self.menu_admin)
        self.lblResumenGeneral_5.setObjectName(u"lblResumenGeneral_5")
        self.lblResumenGeneral_5.setGeometry(QRect(0, 400, 161, 31))
        self.lblResumenGeneral_5.setFont(font)
        self.lblResumenGeneral_5.setStyleSheet(u"color: #bdc3c7")
        self.lblResumenGeneral_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnCopia_seguridad = QPushButton(self.menu_admin)
        self.buttonGroup.addButton(self.btnCopia_seguridad)
        self.btnCopia_seguridad.setObjectName(u"btnCopia_seguridad")
        self.btnCopia_seguridad.setGeometry(QRect(10, 430, 171, 50))
        sizePolicy1.setHeightForWidth(self.btnCopia_seguridad.sizePolicy().hasHeightForWidth())
        self.btnCopia_seguridad.setSizePolicy(sizePolicy1)
        self.btnCopia_seguridad.setMinimumSize(QSize(80, 30))
        self.btnCopia_seguridad.setMaximumSize(QSize(200, 50))
        self.btnCopia_seguridad.setFont(font2)
        self.btnCopia_seguridad.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCopia_seguridad.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnCopia_seguridad.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 2px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 20px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/copia_seguridad_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon14.addFile(u":/icons/copia_seguridad_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnCopia_seguridad.setIcon(icon14)
        self.btnCopia_seguridad.setIconSize(QSize(18, 18))
        self.btnCopia_seguridad.setCheckable(True)
        self.btnCopia_seguridad.setChecked(False)
        self.btnCopia_seguridad.setAutoExclusive(False)
        self.btnRegresar_admin = QPushButton(self.menu_admin)
        self.btnRegresar_admin.setObjectName(u"btnRegresar_admin")
        self.btnRegresar_admin.setGeometry(QRect(10, 543, 141, 41))
        sizePolicy1.setHeightForWidth(self.btnRegresar_admin.sizePolicy().hasHeightForWidth())
        self.btnRegresar_admin.setSizePolicy(sizePolicy1)
        self.btnRegresar_admin.setMinimumSize(QSize(50, 40))
        self.btnRegresar_admin.setMaximumSize(QSize(200, 50))
        self.btnRegresar_admin.setFont(font1)
        self.btnRegresar_admin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnRegresar_admin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnRegresar_admin.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 20px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        self.btnRegresar_admin.setIcon(icon9)
        self.btnRegresar_admin.setIconSize(QSize(30, 30))
        self.btnRegresar_admin.setCheckable(False)
        self.btnRegresar_admin.setChecked(False)
        self.lineSeparadora_2 = QFrame(self.menu_admin)
        self.lineSeparadora_2.setObjectName(u"lineSeparadora_2")
        self.lineSeparadora_2.setGeometry(QRect(0, 530, 165, 3))
        self.lineSeparadora_2.setMinimumSize(QSize(100, 3))
        self.lineSeparadora_2.setMaximumSize(QSize(560, 3))
        self.lineSeparadora_2.setStyleSheet(u"background-color: #f5f6fa;")
        self.lineSeparadora_2.setFrameShape(QFrame.Shape.HLine)
        self.lineSeparadora_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.btnAnio_escolar = QPushButton(self.menu_admin)
        self.buttonGroup.addButton(self.btnAnio_escolar)
        self.btnAnio_escolar.setObjectName(u"btnAnio_escolar")
        self.btnAnio_escolar.setGeometry(QRect(10, 340, 171, 50))
        sizePolicy1.setHeightForWidth(self.btnAnio_escolar.sizePolicy().hasHeightForWidth())
        self.btnAnio_escolar.setSizePolicy(sizePolicy1)
        self.btnAnio_escolar.setMinimumSize(QSize(80, 30))
        self.btnAnio_escolar.setMaximumSize(QSize(200, 50))
        self.btnAnio_escolar.setFont(font2)
        self.btnAnio_escolar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAnio_escolar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnAnio_escolar.setStyleSheet(u"QPushButton {\n"
"   background: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 2px 16px;\n"
"    border-radius: 15px;\n"
"	text-align: left;\n"
"    padding-left: 20px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(69, 98, 126);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #f5f6fa;\n"
" 	color: #2d2d2d;\n"
"	\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icons/calendario-diario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon15.addFile(u":/icons/calendario-diario (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnAnio_escolar.setIcon(icon15)
        self.btnAnio_escolar.setIconSize(QSize(18, 18))
        self.btnAnio_escolar.setCheckable(True)
        self.btnAnio_escolar.setChecked(False)
        self.btnAnio_escolar.setAutoExclusive(False)
        self.stackBarra_lateral.addWidget(self.menu_admin)
        self.stackMain = AnimatedStack(self.widget_main)
        self.stackMain.setObjectName(u"stackMain")
        self.stackMain.setGeometry(QRect(170, 10, 1111, 621))
        self.stackMain.setStyleSheet(u"background-color: transparent;\n"
"color: #2d2d2d;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.frameSaludo = QFrame(self.home)
        self.frameSaludo.setObjectName(u"frameSaludo")
        self.frameSaludo.setGeometry(QRect(50, 20, 531, 161))
        self.frameSaludo.setStyleSheet(u"QFrame{\n"
"		border-radius: 16px;\n"
"		background-color: #E3F2FD;\n"
"border: 1.2px solid #2C3E50;\n"
"}\n"
"QLabel{\n"
"	background-color: transparent;\n"
"	color: #2d2d2d;\n"
"border: transparent;\n"
"}")
        self.frameSaludo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameSaludo.setFrameShadow(QFrame.Shadow.Raised)
        self.lblSaludo_Icon = QLabel(self.frameSaludo)
        self.lblSaludo_Icon.setObjectName(u"lblSaludo_Icon")
        self.lblSaludo_Icon.setGeometry(QRect(30, 40, 61, 61))
        self.lblSaludo_Icon.setPixmap(QPixmap(u":/icons/welcome_b.png"))
        self.lblSaludo_Icon.setScaledContents(True)
        self.lblBienvenida = QLabel(self.frameSaludo)
        self.lblBienvenida.setObjectName(u"lblBienvenida")
        self.lblBienvenida.setGeometry(QRect(120, 20, 321, 51))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(22)
        font3.setBold(True)
        self.lblBienvenida.setFont(font3)
        self.lblBienvenida.setStyleSheet(u"")
        self.lblBienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblSaludo_Descript = QLabel(self.frameSaludo)
        self.lblSaludo_Descript.setObjectName(u"lblSaludo_Descript")
        self.lblSaludo_Descript.setGeometry(QRect(110, 70, 341, 81))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(14)
        font4.setBold(False)
        self.lblSaludo_Descript.setFont(font4)
        self.lblSaludo_Descript.setStyleSheet(u"")
        self.lblSaludo_Descript.setScaledContents(False)
        self.lblSaludo_Descript.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblSaludo_Descript.setWordWrap(True)
        self.frameAccesosDirectos = QFrame(self.home)
        self.frameAccesosDirectos.setObjectName(u"frameAccesosDirectos")
        self.frameAccesosDirectos.setGeometry(QRect(620, 90, 391, 481))
        self.frameAccesosDirectos.setMinimumSize(QSize(0, 100))
        self.frameAccesosDirectos.setMaximumSize(QSize(16777215, 540))
        self.frameAccesosDirectos.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(234, 239, 245);\n"
"	\n"
"	border-radius: 16px;\n"
"}\n"
"QLabel{\n"
"	color: #333333;\n"
"}")
        self.frameAccesosDirectos.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameAccesosDirectos.setFrameShadow(QFrame.Shadow.Raised)
        self.btnAccesoDirecto_reg_estu = QPushButton(self.frameAccesosDirectos)
        self.btnAccesoDirecto_reg_estu.setObjectName(u"btnAccesoDirecto_reg_estu")
        self.btnAccesoDirecto_reg_estu.setGeometry(QRect(30, 350, 71, 51))
        sizePolicy1.setHeightForWidth(self.btnAccesoDirecto_reg_estu.sizePolicy().hasHeightForWidth())
        self.btnAccesoDirecto_reg_estu.setSizePolicy(sizePolicy1)
        self.btnAccesoDirecto_reg_estu.setMinimumSize(QSize(40, 40))
        self.btnAccesoDirecto_reg_estu.setMaximumSize(QSize(200, 60))
        self.btnAccesoDirecto_reg_estu.setFont(font1)
        self.btnAccesoDirecto_reg_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAccesoDirecto_reg_estu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnAccesoDirecto_reg_estu.setAutoFillBackground(False)
        self.btnAccesoDirecto_reg_estu.setStyleSheet(u"QPushButton {\n"
"   background-color: #2980b9;\n"
"    color: #F3F6FF;\n"
"    border: none;\n"
"    padding: 8px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icons/estudiante_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAccesoDirecto_reg_estu.setIcon(icon16)
        self.btnAccesoDirecto_reg_estu.setIconSize(QSize(24, 24))
        self.lblResumenGeneral_6 = QLabel(self.frameAccesosDirectos)
        self.lblResumenGeneral_6.setObjectName(u"lblResumenGeneral_6")
        self.lblResumenGeneral_6.setGeometry(QRect(10, 410, 111, 51))
        self.lblResumenGeneral_6.setFont(font1)
        self.lblResumenGeneral_6.setStyleSheet(u"color: #2d2d2d")
        self.lblResumenGeneral_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblResumenGeneral_6.setWordWrap(True)
        self.lblResumenGeneral_7 = QLabel(self.frameAccesosDirectos)
        self.lblResumenGeneral_7.setObjectName(u"lblResumenGeneral_7")
        self.lblResumenGeneral_7.setGeometry(QRect(0, 290, 391, 51))
        self.lblResumenGeneral_7.setFont(font3)
        self.lblResumenGeneral_7.setStyleSheet(u"color: #2d2d2d")
        self.lblResumenGeneral_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblResumenGeneral_8 = QLabel(self.frameAccesosDirectos)
        self.lblResumenGeneral_8.setObjectName(u"lblResumenGeneral_8")
        self.lblResumenGeneral_8.setGeometry(QRect(146, 410, 111, 51))
        self.lblResumenGeneral_8.setFont(font1)
        self.lblResumenGeneral_8.setStyleSheet(u"color: #2d2d2d")
        self.lblResumenGeneral_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblResumenGeneral_8.setWordWrap(True)
        self.btnAccesoDirecto_reg_emple = QPushButton(self.frameAccesosDirectos)
        self.btnAccesoDirecto_reg_emple.setObjectName(u"btnAccesoDirecto_reg_emple")
        self.btnAccesoDirecto_reg_emple.setGeometry(QRect(165, 350, 71, 51))
        sizePolicy1.setHeightForWidth(self.btnAccesoDirecto_reg_emple.sizePolicy().hasHeightForWidth())
        self.btnAccesoDirecto_reg_emple.setSizePolicy(sizePolicy1)
        self.btnAccesoDirecto_reg_emple.setMinimumSize(QSize(40, 40))
        self.btnAccesoDirecto_reg_emple.setMaximumSize(QSize(200, 60))
        self.btnAccesoDirecto_reg_emple.setFont(font1)
        self.btnAccesoDirecto_reg_emple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAccesoDirecto_reg_emple.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnAccesoDirecto_reg_emple.setAutoFillBackground(False)
        self.btnAccesoDirecto_reg_emple.setStyleSheet(u"QPushButton {\n"
"   background-color: #2980b9;\n"
"    color: #F3F6FF;\n"
"    border: none;\n"
"    padding: 8px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icons/empleado_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAccesoDirecto_reg_emple.setIcon(icon17)
        self.btnAccesoDirecto_reg_emple.setIconSize(QSize(24, 24))
        self.lblResumenGeneral_9 = QLabel(self.frameAccesosDirectos)
        self.lblResumenGeneral_9.setObjectName(u"lblResumenGeneral_9")
        self.lblResumenGeneral_9.setGeometry(QRect(270, 410, 111, 51))
        self.lblResumenGeneral_9.setFont(font1)
        self.lblResumenGeneral_9.setStyleSheet(u"color: #2d2d2d")
        self.lblResumenGeneral_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblResumenGeneral_9.setWordWrap(True)
        self.btnAccesoDirecto_secciones = QPushButton(self.frameAccesosDirectos)
        self.btnAccesoDirecto_secciones.setObjectName(u"btnAccesoDirecto_secciones")
        self.btnAccesoDirecto_secciones.setGeometry(QRect(290, 350, 71, 51))
        sizePolicy1.setHeightForWidth(self.btnAccesoDirecto_secciones.sizePolicy().hasHeightForWidth())
        self.btnAccesoDirecto_secciones.setSizePolicy(sizePolicy1)
        self.btnAccesoDirecto_secciones.setMinimumSize(QSize(40, 40))
        self.btnAccesoDirecto_secciones.setMaximumSize(QSize(200, 60))
        self.btnAccesoDirecto_secciones.setFont(font1)
        self.btnAccesoDirecto_secciones.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAccesoDirecto_secciones.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnAccesoDirecto_secciones.setAutoFillBackground(False)
        self.btnAccesoDirecto_secciones.setStyleSheet(u"QPushButton {\n"
"   background-color: #2980b9;\n"
"    color: #F3F6FF;\n"
"    border: none;\n"
"    padding: 8px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1;\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/icons/seccion2_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAccesoDirecto_secciones.setIcon(icon18)
        self.btnAccesoDirecto_secciones.setIconSize(QSize(24, 24))
        self.frNotificaciones_home = QFrame(self.frameAccesosDirectos)
        self.frNotificaciones_home.setObjectName(u"frNotificaciones_home")
        self.frNotificaciones_home.setGeometry(QRect(10, 20, 371, 221))
        self.frNotificaciones_home.setStyleSheet(u"QFrame {\n"
"    background-color: #ffffff;\n"
"    border-radius: 16px;\n"
"    border: 1px solid #e0e0e0;\n"
"}")
        self.frNotificaciones_home.setFrameShape(QFrame.Shape.StyledPanel)
        self.frNotificaciones_home.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frNotificaciones_home)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lblTituloNotif_home = QLabel(self.frNotificaciones_home)
        self.lblTituloNotif_home.setObjectName(u"lblTituloNotif_home")
        self.lblTituloNotif_home.setMaximumSize(QSize(351, 40))
        self.lblTituloNotif_home.setFont(font)
        self.lblTituloNotif_home.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblTituloNotif_home.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblTituloNotif_home)

        self.line = QFrame(self.frNotificaciones_home)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 2))
        self.line.setStyleSheet(u"background-color: rgb(234, 239, 245);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.lblNotificaciones_home = QLabel(self.frNotificaciones_home)
        self.lblNotificaciones_home.setObjectName(u"lblNotificaciones_home")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.lblNotificaciones_home.setFont(font5)
        self.lblNotificaciones_home.setStyleSheet(u"QLabel {\n"
"    color: #424242;\n"
"    padding: 10px;\n"
"    line-height: 1.5;\n"
"}")
        self.lblNotificaciones_home.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lblNotificaciones_home.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lblNotificaciones_home)

        self.frMatricula_home = QFrame(self.home)
        self.frMatricula_home.setObjectName(u"frMatricula_home")
        self.frMatricula_home.setGeometry(QRect(50, 310, 250, 111))
        self.frMatricula_home.setMinimumSize(QSize(230, 0))
        self.frMatricula_home.setMaximumSize(QSize(260, 16777215))
        self.frMatricula_home.setStyleSheet(u"QFrame {\n"
"    background-color: #FFFFFF;\n"
"    border: 1.2px solid #D0E3F0;\n"
"    border-radius: 16px;\n"
"}\n"
"QLabel{\n"
"	border: transparent;\n"
"	color: #0B1321;\n"
"}")
        self.frMatricula_home.setFrameShape(QFrame.Shape.StyledPanel)
        self.frMatricula_home.setFrameShadow(QFrame.Shadow.Raised)
        self.lblTarjeta1_icon = QLabel(self.frMatricula_home)
        self.lblTarjeta1_icon.setObjectName(u"lblTarjeta1_icon")
        self.lblTarjeta1_icon.setGeometry(QRect(20, 50, 31, 31))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(1)
        self.lblTarjeta1_icon.setFont(font6)
        self.lblTarjeta1_icon.setPixmap(QPixmap(u":/icons/matricula.png"))
        self.lblTarjeta1_icon.setScaledContents(True)
        self.lblTarjeta1_Titulo = QLabel(self.frMatricula_home)
        self.lblTarjeta1_Titulo.setObjectName(u"lblTarjeta1_Titulo")
        self.lblTarjeta1_Titulo.setGeometry(QRect(40, 10, 171, 31))
        self.lblTarjeta1_Titulo.setFont(font5)
        self.lblTarjeta1_Titulo.setStyleSheet(u"color: #5d6d7e")
        self.lblTarjeta1_Titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTarjeta1_Titulo.setWordWrap(True)
        self.lblMatricula_home = QLabel(self.frMatricula_home)
        self.lblMatricula_home.setObjectName(u"lblMatricula_home")
        self.lblMatricula_home.setGeometry(QRect(70, 40, 111, 51))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(32)
        font7.setBold(True)
        self.lblMatricula_home.setFont(font7)
        self.lblMatricula_home.setStyleSheet(u"color: #2d2d2d")
        self.lblMatricula_home.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblMatricula_home.setWordWrap(True)
        self.lineSeparadora = QFrame(self.home)
        self.lineSeparadora.setObjectName(u"lineSeparadora")
        self.lineSeparadora.setGeometry(QRect(40, 220, 550, 3))
        self.lineSeparadora.setMinimumSize(QSize(550, 3))
        self.lineSeparadora.setMaximumSize(QSize(560, 3))
        self.lineSeparadora.setStyleSheet(u"background-color: #eef1f8;")
        self.lineSeparadora.setFrameShape(QFrame.Shape.HLine)
        self.lineSeparadora.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblResumenGeneral = QLabel(self.home)
        self.lblResumenGeneral.setObjectName(u"lblResumenGeneral")
        self.lblResumenGeneral.setGeometry(QRect(130, 240, 321, 51))
        self.lblResumenGeneral.setFont(font3)
        self.lblResumenGeneral.setStyleSheet(u"color: #2d2d2d")
        self.lblResumenGeneral.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frRepresentantes_home = QFrame(self.home)
        self.frRepresentantes_home.setObjectName(u"frRepresentantes_home")
        self.frRepresentantes_home.setGeometry(QRect(330, 310, 250, 111))
        self.frRepresentantes_home.setMinimumSize(QSize(250, 0))
        self.frRepresentantes_home.setMaximumSize(QSize(250, 16777215))
        self.frRepresentantes_home.setStyleSheet(u"QFrame {\n"
"    background-color: #FFFFFF;\n"
"    border: 1.2px solid #D0E3F0;\n"
"    border-radius: 16px;\n"
"}\n"
"QLabel{\n"
"	border: transparent;\n"
"	color: #0B1321;\n"
"}")
        self.frRepresentantes_home.setFrameShape(QFrame.Shape.StyledPanel)
        self.frRepresentantes_home.setFrameShadow(QFrame.Shadow.Raised)
        self.lblTarjeta1_icon_3 = QLabel(self.frRepresentantes_home)
        self.lblTarjeta1_icon_3.setObjectName(u"lblTarjeta1_icon_3")
        self.lblTarjeta1_icon_3.setGeometry(QRect(20, 50, 31, 31))
        self.lblTarjeta1_icon_3.setFont(font6)
        self.lblTarjeta1_icon_3.setPixmap(QPixmap(u":/icons/representantes.png"))
        self.lblTarjeta1_icon_3.setScaledContents(True)
        self.lblTarjeta1_Titulo_3 = QLabel(self.frRepresentantes_home)
        self.lblTarjeta1_Titulo_3.setObjectName(u"lblTarjeta1_Titulo_3")
        self.lblTarjeta1_Titulo_3.setGeometry(QRect(40, 10, 171, 31))
        self.lblTarjeta1_Titulo_3.setFont(font5)
        self.lblTarjeta1_Titulo_3.setStyleSheet(u"color: #5d6d7e")
        self.lblTarjeta1_Titulo_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTarjeta1_Titulo_3.setWordWrap(True)
        self.lblRepresentantes_home = QLabel(self.frRepresentantes_home)
        self.lblRepresentantes_home.setObjectName(u"lblRepresentantes_home")
        self.lblRepresentantes_home.setGeometry(QRect(70, 40, 111, 51))
        self.lblRepresentantes_home.setFont(font7)
        self.lblRepresentantes_home.setStyleSheet(u"color: #2d2d2d")
        self.lblRepresentantes_home.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblRepresentantes_home.setWordWrap(True)
        self.frTrabajadores_home = QFrame(self.home)
        self.frTrabajadores_home.setObjectName(u"frTrabajadores_home")
        self.frTrabajadores_home.setGeometry(QRect(50, 450, 250, 111))
        self.frTrabajadores_home.setMinimumSize(QSize(250, 0))
        self.frTrabajadores_home.setMaximumSize(QSize(250, 16777215))
        self.frTrabajadores_home.setStyleSheet(u"QFrame {\n"
"    background-color: #FFFFFF;\n"
"    border: 1.2px solid #D0E3F0;\n"
"    border-radius: 16px;\n"
"}\n"
"QLabel{\n"
"	border: transparent;\n"
"	color: #0B1321;\n"
"}")
        self.frTrabajadores_home.setFrameShape(QFrame.Shape.StyledPanel)
        self.frTrabajadores_home.setFrameShadow(QFrame.Shadow.Raised)
        self.lblTarjeta1_icon_4 = QLabel(self.frTrabajadores_home)
        self.lblTarjeta1_icon_4.setObjectName(u"lblTarjeta1_icon_4")
        self.lblTarjeta1_icon_4.setGeometry(QRect(20, 50, 31, 31))
        self.lblTarjeta1_icon_4.setFont(font6)
        self.lblTarjeta1_icon_4.setPixmap(QPixmap(u":/icons/empleados_female.png"))
        self.lblTarjeta1_icon_4.setScaledContents(True)
        self.lblTarjeta1_Titulo_4 = QLabel(self.frTrabajadores_home)
        self.lblTarjeta1_Titulo_4.setObjectName(u"lblTarjeta1_Titulo_4")
        self.lblTarjeta1_Titulo_4.setGeometry(QRect(40, 10, 171, 31))
        self.lblTarjeta1_Titulo_4.setFont(font5)
        self.lblTarjeta1_Titulo_4.setStyleSheet(u"color: #5d6d7e")
        self.lblTarjeta1_Titulo_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTarjeta1_Titulo_4.setWordWrap(True)
        self.lblEmpleados_home = QLabel(self.frTrabajadores_home)
        self.lblEmpleados_home.setObjectName(u"lblEmpleados_home")
        self.lblEmpleados_home.setGeometry(QRect(70, 40, 111, 51))
        self.lblEmpleados_home.setFont(font7)
        self.lblEmpleados_home.setStyleSheet(u"color: #2d2d2d")
        self.lblEmpleados_home.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblEmpleados_home.setWordWrap(True)
        self.frSeccion_home = QFrame(self.home)
        self.frSeccion_home.setObjectName(u"frSeccion_home")
        self.frSeccion_home.setGeometry(QRect(330, 450, 250, 111))
        self.frSeccion_home.setMinimumSize(QSize(250, 0))
        self.frSeccion_home.setMaximumSize(QSize(250, 16777215))
        self.frSeccion_home.setStyleSheet(u"QFrame {\n"
"    background-color: #FFFFFF;\n"
"    border: 1.2px solid #D0E3F0;\n"
"    border-radius: 16px;\n"
"}\n"
"QLabel{\n"
"	border: transparent;\n"
"	color: #0B1321;\n"
"}")
        self.frSeccion_home.setFrameShape(QFrame.Shape.StyledPanel)
        self.frSeccion_home.setFrameShadow(QFrame.Shadow.Raised)
        self.lblTarjeta1_icon_5 = QLabel(self.frSeccion_home)
        self.lblTarjeta1_icon_5.setObjectName(u"lblTarjeta1_icon_5")
        self.lblTarjeta1_icon_5.setGeometry(QRect(20, 50, 31, 31))
        self.lblTarjeta1_icon_5.setFont(font6)
        self.lblTarjeta1_icon_5.setPixmap(QPixmap(u":/icons/seccion.png"))
        self.lblTarjeta1_icon_5.setScaledContents(True)
        self.lblTarjeta1_Titulo_5 = QLabel(self.frSeccion_home)
        self.lblTarjeta1_Titulo_5.setObjectName(u"lblTarjeta1_Titulo_5")
        self.lblTarjeta1_Titulo_5.setGeometry(QRect(40, 10, 181, 31))
        self.lblTarjeta1_Titulo_5.setFont(font5)
        self.lblTarjeta1_Titulo_5.setStyleSheet(u"color: #5d6d7e")
        self.lblTarjeta1_Titulo_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTarjeta1_Titulo_5.setWordWrap(True)
        self.lblSeccion_home = QLabel(self.frSeccion_home)
        self.lblSeccion_home.setObjectName(u"lblSeccion_home")
        self.lblSeccion_home.setGeometry(QRect(30, 30, 211, 71))
        self.lblSeccion_home.setFont(font3)
        self.lblSeccion_home.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblSeccion_home.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblSeccion_home.setWordWrap(True)
        self.lblLogo_dashboard = QLabel(self.home)
        self.lblLogo_dashboard.setObjectName(u"lblLogo_dashboard")
        self.lblLogo_dashboard.setGeometry(QRect(880, 10, 141, 61))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(19)
        font8.setBold(True)
        self.lblLogo_dashboard.setFont(font8)
        self.lblLogo_dashboard.setStyleSheet(u"color: #2d2d2d")
        self.lblLogo_dashboard.setFrameShape(QFrame.Shape.NoFrame)
        self.lblLogo_dashboard.setFrameShadow(QFrame.Shadow.Plain)
        self.lblLogo_dashboard.setPixmap(QPixmap(u":/logos/SIRA_logo_cut.png"))
        self.lblLogo_dashboard.setScaledContents(True)
        self.lblLogo_dashboard.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblLogo_dashboard.setWordWrap(True)
        self.lblLogo_dashboard.setIndent(0)
        self.lblLogo_dashboard_escuela = QLabel(self.home)
        self.lblLogo_dashboard_escuela.setObjectName(u"lblLogo_dashboard_escuela")
        self.lblLogo_dashboard_escuela.setGeometry(QRect(1039, 10, 51, 61))
        self.lblLogo_dashboard_escuela.setMinimumSize(QSize(50, 50))
        self.lblLogo_dashboard_escuela.setMaximumSize(QSize(130, 70))
        self.lblLogo_dashboard_escuela.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_dashboard_escuela.setScaledContents(True)
        self.line_8 = QFrame(self.home)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(1029, 10, 3, 61))
        self.line_8.setMinimumSize(QSize(3, 61))
        self.line_8.setMaximumSize(QSize(3, 61))
        self.line_8.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.stackMain.addWidget(self.home)
        self.gestion_estudiantes = QWidget()
        self.gestion_estudiantes.setObjectName(u"gestion_estudiantes")
        self.stackMain.addWidget(self.gestion_estudiantes)
        self.secciones = QWidget()
        self.secciones.setObjectName(u"secciones")
        self.stackMain.addWidget(self.secciones)
        self.Egresados = QWidget()
        self.Egresados.setObjectName(u"Egresados")
        self.stackMain.addWidget(self.Egresados)
        self.empleados = QWidget()
        self.empleados.setObjectName(u"empleados")
        self.stackMain.addWidget(self.empleados)
        self.estadisticas = QWidget()
        self.estadisticas.setObjectName(u"estadisticas")
        self.frameCriterio = QFrame(self.estadisticas)
        self.frameCriterio.setObjectName(u"frameCriterio")
        self.frameCriterio.setGeometry(QRect(270, 50, 230, 40))
        self.frameCriterio.setMinimumSize(QSize(230, 40))
        self.frameCriterio.setMaximumSize(QSize(230, 40))
        self.frameCriterio.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #2980b9;\n"
"	border-radius: 12px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frameCriterio.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameCriterio.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxCriterio = QComboBox(self.frameCriterio)
        self.cbxCriterio.setObjectName(u"cbxCriterio")
        self.cbxCriterio.setGeometry(QRect(11, 5, 210, 30))
        self.cbxCriterio.setMinimumSize(QSize(210, 30))
        self.cbxCriterio.setMaximumSize(QSize(210, 30))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(11)
        font9.setBold(True)
        self.cbxCriterio.setFont(font9)
        self.cbxCriterio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxCriterio.setStyleSheet(u"")
        self.cbxCriterio.setIconSize(QSize(10, 10))
        self.frameTipoGrafica = QFrame(self.estadisticas)
        self.frameTipoGrafica.setObjectName(u"frameTipoGrafica")
        self.frameTipoGrafica.setGeometry(QRect(520, 50, 230, 40))
        self.frameTipoGrafica.setMinimumSize(QSize(230, 40))
        self.frameTipoGrafica.setMaximumSize(QSize(230, 40))
        self.frameTipoGrafica.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #2980b9;\n"
"	border-radius: 12px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frameTipoGrafica.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTipoGrafica.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxTipoGrafica = QComboBox(self.frameTipoGrafica)
        self.cbxTipoGrafica.setObjectName(u"cbxTipoGrafica")
        self.cbxTipoGrafica.setGeometry(QRect(11, 5, 210, 30))
        self.cbxTipoGrafica.setMinimumSize(QSize(210, 30))
        self.cbxTipoGrafica.setMaximumSize(QSize(210, 30))
        self.cbxTipoGrafica.setFont(font9)
        self.cbxTipoGrafica.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxTipoGrafica.setStyleSheet(u"")
        self.cbxTipoGrafica.setIconSize(QSize(10, 10))
        self.spnMax = QSpinBox(self.estadisticas)
        self.spnMax.setObjectName(u"spnMax")
        self.spnMax.setEnabled(False)
        self.spnMax.setGeometry(QRect(390, 110, 111, 31))
        self.spnMax.setFont(font1)
        self.spnMax.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.spnMax.setStyleSheet(u"QSpinBox{\n"
"	background-color: white;\n"
"	border: 1.5px solid #2980b9;\n"
"	border-radius: 10px;\n"
"}\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center right;\n"
"    width: 20px;\n"
"	height: 25px;\n"
"    image: url(:/icons/flecha_arriba.png);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center left;\n"
"    width: 20px;\n"
"	height: 25px;\n"
"    image: url(:/icons/flecha_abajo.png);\n"
"}")
        self.spnMax.setWrapping(False)
        self.spnMax.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spnMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.spnMax.setMinimum(1)
        self.spnMax.setMaximum(999999)
        self.lblMin = QLabel(self.estadisticas)
        self.lblMin.setObjectName(u"lblMin")
        self.lblMin.setGeometry(QRect(280, 142, 91, 31))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setPointSize(9)
        font10.setBold(True)
        self.lblMin.setFont(font10)
        self.lblMin.setStyleSheet(u"")
        self.lblMin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblMin.setWordWrap(True)
        self.framePoblacion = QFrame(self.estadisticas)
        self.framePoblacion.setObjectName(u"framePoblacion")
        self.framePoblacion.setGeometry(QRect(50, 50, 200, 40))
        self.framePoblacion.setMinimumSize(QSize(200, 30))
        self.framePoblacion.setMaximumSize(QSize(200, 40))
        self.framePoblacion.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #2980b9;\n"
"	border-radius: 12px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.framePoblacion.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePoblacion.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxPoblacion = QComboBox(self.framePoblacion)
        self.cbxPoblacion.addItem("")
        self.cbxPoblacion.addItem("")
        self.cbxPoblacion.addItem("")
        self.cbxPoblacion.addItem("")
        self.cbxPoblacion.addItem("")
        self.cbxPoblacion.setObjectName(u"cbxPoblacion")
        self.cbxPoblacion.setGeometry(QRect(9, 5, 180, 30))
        self.cbxPoblacion.setMaximumSize(QSize(180, 30))
        self.cbxPoblacion.setFont(font9)
        self.cbxPoblacion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxPoblacion.setStyleSheet(u"")
        self.cbxPoblacion.setIconSize(QSize(5, 5))
        self.lblMax = QLabel(self.estadisticas)
        self.lblMax.setObjectName(u"lblMax")
        self.lblMax.setGeometry(QRect(390, 142, 111, 31))
        self.lblMax.setFont(font10)
        self.lblMax.setStyleSheet(u"")
        self.lblMax.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblMax.setWordWrap(True)
        self.spnMin = QSpinBox(self.estadisticas)
        self.spnMin.setObjectName(u"spnMin")
        self.spnMin.setEnabled(False)
        self.spnMin.setGeometry(QRect(270, 110, 111, 31))
        self.spnMin.setFont(font1)
        self.spnMin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.spnMin.setStyleSheet(u"QSpinBox{\n"
"	background-color: white;\n"
"	border: 1.5px solid #2980b9;\n"
"	border-radius: 10px;\n"
"}\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center right;\n"
"    width: 20px;\n"
"	height: 25px;\n"
"    image: url(:/icons/flecha_arriba.png);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center left;\n"
"    width: 20px;\n"
"	height: 25px;\n"
"    image: url(:/icons/flecha_abajo.png);\n"
"}")
        self.spnMin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spnMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.spnMin.setAccelerated(False)
        self.spnMin.setMinimum(1)
        self.spnMin.setMaximum(99999)
        self.btnExportar_reporte = QPushButton(self.estadisticas)
        self.btnExportar_reporte.setObjectName(u"btnExportar_reporte")
        self.btnExportar_reporte.setGeometry(QRect(950, 100, 121, 50))
        sizePolicy1.setHeightForWidth(self.btnExportar_reporte.sizePolicy().hasHeightForWidth())
        self.btnExportar_reporte.setSizePolicy(sizePolicy1)
        self.btnExportar_reporte.setMinimumSize(QSize(81, 50))
        self.btnExportar_reporte.setMaximumSize(QSize(200, 100))
        self.btnExportar_reporte.setFont(font1)
        self.btnExportar_reporte.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnExportar_reporte.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnExportar_reporte.setStyleSheet(u"QPushButton {\n"
"   background-color: #2980b9;\n"
"    color: #F3F6FF;\n"
"    border: none;\n"
"    padding: 8px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1;\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/icons/pdf_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExportar_reporte.setIcon(icon19)
        self.btnExportar_reporte.setIconSize(QSize(70, 70))
        self.btnGenerarGrafica = QPushButton(self.estadisticas)
        self.btnGenerarGrafica.setObjectName(u"btnGenerarGrafica")
        self.btnGenerarGrafica.setGeometry(QRect(770, 50, 91, 41))
        sizePolicy1.setHeightForWidth(self.btnGenerarGrafica.sizePolicy().hasHeightForWidth())
        self.btnGenerarGrafica.setSizePolicy(sizePolicy1)
        self.btnGenerarGrafica.setMinimumSize(QSize(81, 30))
        self.btnGenerarGrafica.setMaximumSize(QSize(200, 100))
        self.btnGenerarGrafica.setFont(font1)
        self.btnGenerarGrafica.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGenerarGrafica.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnGenerarGrafica.setStyleSheet(u"QPushButton {\n"
"   background-color: #2980b9;\n"
"    color: #F3F6FF;\n"
"    border: none;\n"
"    padding: 8px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1;\n"
"}")
        self.btnGenerarGrafica.setIconSize(QSize(70, 70))
        self.lblLogo_emple_2 = QLabel(self.estadisticas)
        self.lblLogo_emple_2.setObjectName(u"lblLogo_emple_2")
        self.lblLogo_emple_2.setGeometry(QRect(1039, 10, 51, 61))
        self.lblLogo_emple_2.setMinimumSize(QSize(50, 50))
        self.lblLogo_emple_2.setMaximumSize(QSize(130, 70))
        self.lblLogo_emple_2.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_emple_2.setScaledContents(True)
        self.line_3 = QFrame(self.estadisticas)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(1029, 10, 3, 61))
        self.line_3.setMinimumSize(QSize(3, 61))
        self.line_3.setMaximumSize(QSize(3, 61))
        self.line_3.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblTitulo_logo_emple_2 = QLabel(self.estadisticas)
        self.lblTitulo_logo_emple_2.setObjectName(u"lblTitulo_logo_emple_2")
        self.lblTitulo_logo_emple_2.setGeometry(QRect(880, 0, 141, 81))
        self.lblTitulo_logo_emple_2.setFont(font8)
        self.lblTitulo_logo_emple_2.setStyleSheet(u"color: #2d2d2d")
        self.lblTitulo_logo_emple_2.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_logo_emple_2.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_logo_emple_2.setScaledContents(False)
        self.lblTitulo_logo_emple_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_logo_emple_2.setWordWrap(True)
        self.lblTitulo_logo_emple_2.setIndent(0)
        self.lblMin_2 = QLabel(self.estadisticas)
        self.lblMin_2.setObjectName(u"lblMin_2")
        self.lblMin_2.setGeometry(QRect(100, 10, 91, 31))
        self.lblMin_2.setFont(font)
        self.lblMin_2.setStyleSheet(u"")
        self.lblMin_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblMin_2.setWordWrap(True)
        self.lblMin_3 = QLabel(self.estadisticas)
        self.lblMin_3.setObjectName(u"lblMin_3")
        self.lblMin_3.setGeometry(QRect(340, 10, 91, 31))
        self.lblMin_3.setFont(font)
        self.lblMin_3.setStyleSheet(u"")
        self.lblMin_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblMin_3.setWordWrap(True)
        self.lblMin_4 = QLabel(self.estadisticas)
        self.lblMin_4.setObjectName(u"lblMin_4")
        self.lblMin_4.setGeometry(QRect(570, 10, 121, 31))
        self.lblMin_4.setFont(font)
        self.lblMin_4.setStyleSheet(u"")
        self.lblMin_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblMin_4.setWordWrap(True)
        self.frGrafica_border = QFrame(self.estadisticas)
        self.frGrafica_border.setObjectName(u"frGrafica_border")
        self.frGrafica_border.setGeometry(QRect(40, 180, 981, 441))
        self.frGrafica_border.setStyleSheet(u"QFrame#frGrafica_border{\n"
"	background-color: white;\n"
"	border: 1.2px solid #2980b9;\n"
"	border-radius: 16px;\n"
"}")
        self.frGrafica_border.setFrameShape(QFrame.Shape.StyledPanel)
        self.frGrafica_border.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frGrafica_border)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frGrafica_reportes = QFrame(self.frGrafica_border)
        self.frGrafica_reportes.setObjectName(u"frGrafica_reportes")
        self.frGrafica_reportes.setStyleSheet(u"background-color: transparent;")
        self.frGrafica_reportes.setFrameShape(QFrame.Shape.StyledPanel)
        self.frGrafica_reportes.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frGrafica_reportes)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_2.addWidget(self.frGrafica_reportes)

        self.frameSeccion_reporte = QFrame(self.estadisticas)
        self.frameSeccion_reporte.setObjectName(u"frameSeccion_reporte")
        self.frameSeccion_reporte.setGeometry(QRect(570, 110, 101, 31))
        self.frameSeccion_reporte.setMinimumSize(QSize(100, 30))
        self.frameSeccion_reporte.setMaximumSize(QSize(230, 40))
        self.frameSeccion_reporte.setStyleSheet(u"QFrame{\n"
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
        self.frameSeccion_reporte.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameSeccion_reporte.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxSeccion_reporte = QComboBox(self.frameSeccion_reporte)
        self.cbxSeccion_reporte.setObjectName(u"cbxSeccion_reporte")
        self.cbxSeccion_reporte.setGeometry(QRect(5, 1, 91, 27))
        self.cbxSeccion_reporte.setMinimumSize(QSize(90, 25))
        self.cbxSeccion_reporte.setMaximumSize(QSize(210, 30))
        self.cbxSeccion_reporte.setFont(font9)
        self.cbxSeccion_reporte.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxSeccion_reporte.setStyleSheet(u"")
        self.cbxSeccion_reporte.setIconSize(QSize(10, 10))
        self.lblSeccion_reporte = QLabel(self.estadisticas)
        self.lblSeccion_reporte.setObjectName(u"lblSeccion_reporte")
        self.lblSeccion_reporte.setGeometry(QRect(510, 110, 61, 31))
        self.lblSeccion_reporte.setFont(font10)
        self.lblSeccion_reporte.setStyleSheet(u"")
        self.lblSeccion_reporte.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblSeccion_reporte.setWordWrap(True)
        self.stackMain.addWidget(self.estadisticas)
        self.admin_gestion_usuarios = QWidget()
        self.admin_gestion_usuarios.setObjectName(u"admin_gestion_usuarios")
        self.btnCrear_usuario = QPushButton(self.admin_gestion_usuarios)
        self.btnCrear_usuario.setObjectName(u"btnCrear_usuario")
        self.btnCrear_usuario.setGeometry(QRect(20, 10, 150, 40))
        sizePolicy1.setHeightForWidth(self.btnCrear_usuario.sizePolicy().hasHeightForWidth())
        self.btnCrear_usuario.setSizePolicy(sizePolicy1)
        self.btnCrear_usuario.setMinimumSize(QSize(120, 40))
        self.btnCrear_usuario.setMaximumSize(QSize(150, 40))
        self.btnCrear_usuario.setFont(font1)
        self.btnCrear_usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCrear_usuario.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnCrear_usuario.setStyleSheet(u"QPushButton {\n"
"   background-color: #2980b9;\n"
"    color: #F3F6FF;\n"
"    border: none;\n"
"    padding: 8px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1;\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u":/icons/new_home_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCrear_usuario.setIcon(icon20)
        self.btnCrear_usuario.setIconSize(QSize(18, 18))
        self.frameTabla_usuarios = QFrame(self.admin_gestion_usuarios)
        self.frameTabla_usuarios.setObjectName(u"frameTabla_usuarios")
        self.frameTabla_usuarios.setGeometry(QRect(20, 80, 900, 511))
        self.frameTabla_usuarios.setMinimumSize(QSize(900, 450))
        self.frameTabla_usuarios.setMaximumSize(QSize(16777215, 550))
        self.frameTabla_usuarios.setStyleSheet(u"QFrame#frameTabla_usuarios {\n"
"    border: 1px solid #d5dbdb;\n"
"    border-radius: 12px;\n"
"    background-color: white;\n"
"}")
        self.frameTabla_usuarios.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTabla_usuarios.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameTabla_usuarios)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableW_usuarios = QTableView(self.frameTabla_usuarios)
        self.tableW_usuarios.setObjectName(u"tableW_usuarios")
        self.tableW_usuarios.setStyleSheet(u"QTableView {\n"
"    background-color: #F7F9FC;\n"
"    gridline-color: #E3E8EF;\n"
"    color: #0B1321;\n"
"    alternate-background-color: #E3F2FD;\n"
"    selection-background-color: #2980b9;\n"
"    selection-color: #FFFFFF;\n"
"    border: 1px solid #CBD5E1;\n"
"}\n"
"\n"
"/* Cabecera horizontal */\n"
"QHeaderView::section {\n"
"    background-color: #ECF0F1;   /* encabezado */\n"
"    color: #2C3E50;              /* azul oscuro */\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"/* Cabecera vertical */\n"
"QHeaderView::section:vertical {\n"
"    background-color: #ECF0F1;\n"
"    color: #2C3E50;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"/* Bot\u00f3n de esquina (arriba a la izquierda) */\n"
"QTableCornerButton::section {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Scrollbar vertical */\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 10px;\n"
"    margin: 2px;\n"
"}"
                        "\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #CBD5E1;\n"
"    border-radius: 4px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #94A3B8;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"    height: 0px;\n"
"}")
        self.tableW_usuarios.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableW_usuarios.setAlternatingRowColors(True)
        self.tableW_usuarios.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableW_usuarios.setShowGrid(True)
        self.tableW_usuarios.setSortingEnabled(True)

        self.horizontalLayout_3.addWidget(self.tableW_usuarios)

        self.btnActualizar_usuario = QPushButton(self.admin_gestion_usuarios)
        self.btnActualizar_usuario.setObjectName(u"btnActualizar_usuario")
        self.btnActualizar_usuario.setGeometry(QRect(180, 10, 191, 40))
        sizePolicy1.setHeightForWidth(self.btnActualizar_usuario.sizePolicy().hasHeightForWidth())
        self.btnActualizar_usuario.setSizePolicy(sizePolicy1)
        self.btnActualizar_usuario.setMinimumSize(QSize(120, 40))
        self.btnActualizar_usuario.setMaximumSize(QSize(200, 40))
        self.btnActualizar_usuario.setFont(font1)
        self.btnActualizar_usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnActualizar_usuario.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnActualizar_usuario.setStyleSheet(u"QPushButton {\n"
"   background-color: #2980b9;\n"
"    color: #F3F6FF;\n"
"    border: none;\n"
"    padding: 8px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1;\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/icons/edit_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnActualizar_usuario.setIcon(icon21)
        self.btnActualizar_usuario.setIconSize(QSize(18, 18))
        self.btnDisable_usuario = QPushButton(self.admin_gestion_usuarios)
        self.btnDisable_usuario.setObjectName(u"btnDisable_usuario")
        self.btnDisable_usuario.setGeometry(QRect(380, 10, 231, 40))
        sizePolicy1.setHeightForWidth(self.btnDisable_usuario.sizePolicy().hasHeightForWidth())
        self.btnDisable_usuario.setSizePolicy(sizePolicy1)
        self.btnDisable_usuario.setMinimumSize(QSize(120, 40))
        self.btnDisable_usuario.setMaximumSize(QSize(250, 40))
        self.btnDisable_usuario.setFont(font1)
        self.btnDisable_usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDisable_usuario.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnDisable_usuario.setStyleSheet(u"QPushButton {\n"
"   background-color: #2980b9;\n"
"    color: #F3F6FF;\n"
"    border: none;\n"
"    padding: 8px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1;\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u":/icons/confirm_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDisable_usuario.setIcon(icon22)
        self.btnDisable_usuario.setIconSize(QSize(18, 18))
        self.lblTitulo_logo_emple_3 = QLabel(self.admin_gestion_usuarios)
        self.lblTitulo_logo_emple_3.setObjectName(u"lblTitulo_logo_emple_3")
        self.lblTitulo_logo_emple_3.setGeometry(QRect(880, 0, 141, 81))
        self.lblTitulo_logo_emple_3.setFont(font8)
        self.lblTitulo_logo_emple_3.setStyleSheet(u"color: #2d2d2d")
        self.lblTitulo_logo_emple_3.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_logo_emple_3.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_logo_emple_3.setScaledContents(False)
        self.lblTitulo_logo_emple_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_logo_emple_3.setWordWrap(True)
        self.lblTitulo_logo_emple_3.setIndent(0)
        self.lblLogo_emple_3 = QLabel(self.admin_gestion_usuarios)
        self.lblLogo_emple_3.setObjectName(u"lblLogo_emple_3")
        self.lblLogo_emple_3.setGeometry(QRect(1039, 10, 51, 61))
        self.lblLogo_emple_3.setMinimumSize(QSize(50, 50))
        self.lblLogo_emple_3.setMaximumSize(QSize(130, 70))
        self.lblLogo_emple_3.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_emple_3.setScaledContents(True)
        self.line_4 = QFrame(self.admin_gestion_usuarios)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(1029, 10, 3, 61))
        self.line_4.setMinimumSize(QSize(3, 61))
        self.line_4.setMaximumSize(QSize(3, 61))
        self.line_4.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblInactivos_usuarios = QLabel(self.admin_gestion_usuarios)
        self.lblInactivos_usuarios.setObjectName(u"lblInactivos_usuarios")
        self.lblInactivos_usuarios.setGeometry(QRect(380, 590, 61, 31))
        font11 = QFont()
        font11.setFamilies([u"Segoe UI"])
        font11.setPointSize(16)
        font11.setBold(True)
        self.lblInactivos_usuarios.setFont(font11)
        self.lblInactivos_usuarios.setStyleSheet(u"")
        self.lblInactivos_usuarios.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblInactivos_usuarios.setWordWrap(True)
        self.lblTarjeta1_Titulo_11 = QLabel(self.admin_gestion_usuarios)
        self.lblTarjeta1_Titulo_11.setObjectName(u"lblTarjeta1_Titulo_11")
        self.lblTarjeta1_Titulo_11.setGeometry(QRect(240, 590, 151, 31))
        self.lblTarjeta1_Titulo_11.setFont(font5)
        self.lblTarjeta1_Titulo_11.setStyleSheet(u"")
        self.lblTarjeta1_Titulo_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTarjeta1_Titulo_11.setWordWrap(True)
        self.chkMostrar_inactivos_user = QCheckBox(self.admin_gestion_usuarios)
        self.chkMostrar_inactivos_user.setObjectName(u"chkMostrar_inactivos_user")
        self.chkMostrar_inactivos_user.setGeometry(QRect(930, 580, 171, 31))
        font12 = QFont()
        font12.setFamilies([u"Segoe UI"])
        font12.setPointSize(12)
        self.chkMostrar_inactivos_user.setFont(font12)
        self.chkMostrar_inactivos_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chkMostrar_inactivos_user.setStyleSheet(u"QCheckBox {\n"
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
        self.chkMostrar_inactivos_user.setIconSize(QSize(20, 20))
        self.chkMostrar_inactivos_user.setTristate(False)
        self.lblTarjeta1_Titulo_12 = QLabel(self.admin_gestion_usuarios)
        self.lblTarjeta1_Titulo_12.setObjectName(u"lblTarjeta1_Titulo_12")
        self.lblTarjeta1_Titulo_12.setGeometry(QRect(20, 590, 141, 31))
        self.lblTarjeta1_Titulo_12.setFont(font5)
        self.lblTarjeta1_Titulo_12.setStyleSheet(u"")
        self.lblTarjeta1_Titulo_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTarjeta1_Titulo_12.setWordWrap(True)
        self.lblActivos_usuarios = QLabel(self.admin_gestion_usuarios)
        self.lblActivos_usuarios.setObjectName(u"lblActivos_usuarios")
        self.lblActivos_usuarios.setGeometry(QRect(150, 590, 61, 31))
        self.lblActivos_usuarios.setFont(font11)
        self.lblActivos_usuarios.setStyleSheet(u"")
        self.lblActivos_usuarios.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblActivos_usuarios.setWordWrap(True)
        self.btnActualizar_tabla_user = QPushButton(self.admin_gestion_usuarios)
        self.btnActualizar_tabla_user.setObjectName(u"btnActualizar_tabla_user")
        self.btnActualizar_tabla_user.setGeometry(QRect(930, 520, 131, 40))
        sizePolicy1.setHeightForWidth(self.btnActualizar_tabla_user.sizePolicy().hasHeightForWidth())
        self.btnActualizar_tabla_user.setSizePolicy(sizePolicy1)
        self.btnActualizar_tabla_user.setMinimumSize(QSize(70, 40))
        self.btnActualizar_tabla_user.setMaximumSize(QSize(150, 40))
        self.btnActualizar_tabla_user.setFont(font)
        self.btnActualizar_tabla_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnActualizar_tabla_user.setMouseTracking(True)
        self.btnActualizar_tabla_user.setTabletTracking(False)
        self.btnActualizar_tabla_user.setAcceptDrops(False)
        self.btnActualizar_tabla_user.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnActualizar_tabla_user.setAutoFillBackground(False)
        self.btnActualizar_tabla_user.setStyleSheet(u"QPushButton {\n"
"   background-color: #2980b9;\n"
"    color: #F3F6FF;\n"
"    border: none;\n"
"    padding: 8px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1;\n"
"}")
        icon23 = QIcon()
        icon23.addFile(u":/icons/actualizar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnActualizar_tabla_user.setIcon(icon23)
        self.btnActualizar_tabla_user.setIconSize(QSize(40, 40))
        self.stackMain.addWidget(self.admin_gestion_usuarios)
        self.auditoria = QWidget()
        self.auditoria.setObjectName(u"auditoria")
        self.frameTabla_auditoria = QFrame(self.auditoria)
        self.frameTabla_auditoria.setObjectName(u"frameTabla_auditoria")
        self.frameTabla_auditoria.setGeometry(QRect(20, 0, 861, 611))
        self.frameTabla_auditoria.setMinimumSize(QSize(800, 450))
        self.frameTabla_auditoria.setMaximumSize(QSize(16777215, 650))
        self.frameTabla_auditoria.setStyleSheet(u"QFrame#frameTabla_auditoria {\n"
"    border: 1px solid #d5dbdb;\n"
"    border-radius: 12px;\n"
"    background-color: white;\n"
"}")
        self.frameTabla_auditoria.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTabla_auditoria.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frameTabla_auditoria)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableW_auditoria = QTableView(self.frameTabla_auditoria)
        self.tableW_auditoria.setObjectName(u"tableW_auditoria")
        self.tableW_auditoria.setStyleSheet(u"QTableView {\n"
"    background-color: #F7F9FC;\n"
"    gridline-color: #E3E8EF;\n"
"    color: #0B1321;\n"
"    alternate-background-color: #E3F2FD;\n"
"    selection-background-color: #2980b9;\n"
"    selection-color: #FFFFFF;\n"
"    border: 1px solid #CBD5E1;\n"
"}\n"
"\n"
"/* Cabecera horizontal */\n"
"QHeaderView::section {\n"
"    background-color: #ECF0F1;   /* encabezado */\n"
"    color: #2C3E50;              /* azul oscuro */\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"/* Cabecera vertical */\n"
"QHeaderView::section:vertical {\n"
"    background-color: #ECF0F1;\n"
"    color: #2C3E50;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"/* Bot\u00f3n de esquina (arriba a la izquierda) */\n"
"QTableCornerButton::section {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Scrollbar vertical */\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 10px;\n"
"    margin: 2px;\n"
"}"
                        "\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #CBD5E1;\n"
"    border-radius: 4px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #94A3B8;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"    height: 0px;\n"
"}")
        self.tableW_auditoria.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableW_auditoria.setAlternatingRowColors(True)
        self.tableW_auditoria.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableW_auditoria.setShowGrid(True)
        self.tableW_auditoria.setSortingEnabled(True)

        self.horizontalLayout_4.addWidget(self.tableW_auditoria)

        self.lblLogo_emple_4 = QLabel(self.auditoria)
        self.lblLogo_emple_4.setObjectName(u"lblLogo_emple_4")
        self.lblLogo_emple_4.setGeometry(QRect(1040, 10, 51, 61))
        self.lblLogo_emple_4.setMinimumSize(QSize(50, 50))
        self.lblLogo_emple_4.setMaximumSize(QSize(130, 70))
        self.lblLogo_emple_4.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_emple_4.setScaledContents(True)
        self.lblTitulo_logo_emple_4 = QLabel(self.auditoria)
        self.lblTitulo_logo_emple_4.setObjectName(u"lblTitulo_logo_emple_4")
        self.lblTitulo_logo_emple_4.setGeometry(QRect(881, 0, 141, 81))
        self.lblTitulo_logo_emple_4.setFont(font8)
        self.lblTitulo_logo_emple_4.setStyleSheet(u"color: #2d2d2d")
        self.lblTitulo_logo_emple_4.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_logo_emple_4.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_logo_emple_4.setScaledContents(False)
        self.lblTitulo_logo_emple_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_logo_emple_4.setWordWrap(True)
        self.lblTitulo_logo_emple_4.setIndent(0)
        self.line_5 = QFrame(self.auditoria)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(1030, 10, 3, 61))
        self.line_5.setMinimumSize(QSize(3, 61))
        self.line_5.setMaximumSize(QSize(3, 61))
        self.line_5.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.btnActualizar_tabla_auditoria = QPushButton(self.auditoria)
        self.btnActualizar_tabla_auditoria.setObjectName(u"btnActualizar_tabla_auditoria")
        self.btnActualizar_tabla_auditoria.setGeometry(QRect(910, 570, 131, 40))
        sizePolicy1.setHeightForWidth(self.btnActualizar_tabla_auditoria.sizePolicy().hasHeightForWidth())
        self.btnActualizar_tabla_auditoria.setSizePolicy(sizePolicy1)
        self.btnActualizar_tabla_auditoria.setMinimumSize(QSize(70, 40))
        self.btnActualizar_tabla_auditoria.setMaximumSize(QSize(150, 40))
        self.btnActualizar_tabla_auditoria.setFont(font)
        self.btnActualizar_tabla_auditoria.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnActualizar_tabla_auditoria.setMouseTracking(True)
        self.btnActualizar_tabla_auditoria.setTabletTracking(False)
        self.btnActualizar_tabla_auditoria.setAcceptDrops(False)
        self.btnActualizar_tabla_auditoria.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnActualizar_tabla_auditoria.setAutoFillBackground(False)
        self.btnActualizar_tabla_auditoria.setStyleSheet(u"QPushButton {\n"
"   background-color: #2980b9;\n"
"    color: #F3F6FF;\n"
"    border: none;\n"
"    padding: 8px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1;\n"
"}")
        self.btnActualizar_tabla_auditoria.setIcon(icon23)
        self.btnActualizar_tabla_auditoria.setIconSize(QSize(40, 40))
        self.stackMain.addWidget(self.auditoria)
        self.datos_institucionales = QWidget()
        self.datos_institucionales.setObjectName(u"datos_institucionales")
        self.btnModificar_institucion = QPushButton(self.datos_institucionales)
        self.btnModificar_institucion.setObjectName(u"btnModificar_institucion")
        self.btnModificar_institucion.setGeometry(QRect(880, 550, 181, 51))
        sizePolicy1.setHeightForWidth(self.btnModificar_institucion.sizePolicy().hasHeightForWidth())
        self.btnModificar_institucion.setSizePolicy(sizePolicy1)
        self.btnModificar_institucion.setMinimumSize(QSize(120, 40))
        self.btnModificar_institucion.setMaximumSize(QSize(200, 60))
        self.btnModificar_institucion.setFont(font1)
        self.btnModificar_institucion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnModificar_institucion.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnModificar_institucion.setStyleSheet(u"QPushButton {\n"
"   background-color: #2980b9;\n"
"    color: #F3F6FF;\n"
"    border: none;\n"
"    padding: 8px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1;\n"
"}")
        self.btnModificar_institucion.setIcon(icon21)
        self.btnModificar_institucion.setIconSize(QSize(18, 18))
        self.line_6 = QFrame(self.datos_institucionales)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(1030, 10, 3, 61))
        self.line_6.setMinimumSize(QSize(3, 61))
        self.line_6.setMaximumSize(QSize(3, 61))
        self.line_6.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblTitulo_logo_emple_5 = QLabel(self.datos_institucionales)
        self.lblTitulo_logo_emple_5.setObjectName(u"lblTitulo_logo_emple_5")
        self.lblTitulo_logo_emple_5.setGeometry(QRect(881, 0, 141, 81))
        self.lblTitulo_logo_emple_5.setFont(font8)
        self.lblTitulo_logo_emple_5.setStyleSheet(u"color: #2d2d2d")
        self.lblTitulo_logo_emple_5.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_logo_emple_5.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_logo_emple_5.setScaledContents(False)
        self.lblTitulo_logo_emple_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_logo_emple_5.setWordWrap(True)
        self.lblTitulo_logo_emple_5.setIndent(0)
        self.lblLogo_emple_5 = QLabel(self.datos_institucionales)
        self.lblLogo_emple_5.setObjectName(u"lblLogo_emple_5")
        self.lblLogo_emple_5.setGeometry(QRect(1040, 10, 51, 61))
        self.lblLogo_emple_5.setMinimumSize(QSize(50, 50))
        self.lblLogo_emple_5.setMaximumSize(QSize(130, 70))
        self.lblLogo_emple_5.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_emple_5.setScaledContents(True)
        self.frameInstitucion = QFrame(self.datos_institucionales)
        self.frameInstitucion.setObjectName(u"frameInstitucion")
        self.frameInstitucion.setGeometry(QRect(30, 20, 821, 591))
        self.frameInstitucion.setMinimumSize(QSize(0, 0))
        self.frameInstitucion.setMaximumSize(QSize(16777215, 650))
        self.frameInstitucion.setStyleSheet(u"QFrame{\n"
"	background-color: #f3f6ff;\n"
"	border: 1.2px solid #6c8393;\n"
"	border-radius: 16px;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 3px;\n"
"    background-color: white;\n"
"}")
        self.frameInstitucion.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameInstitucion.setFrameShadow(QFrame.Shadow.Raised)
        self.lneUltimaActualizacion_admin = QLineEdit(self.frameInstitucion)
        self.lneUltimaActualizacion_admin.setObjectName(u"lneUltimaActualizacion_admin")
        self.lneUltimaActualizacion_admin.setGeometry(QRect(260, 520, 500, 30))
        self.lneUltimaActualizacion_admin.setMinimumSize(QSize(400, 30))
        self.lneUltimaActualizacion_admin.setMaximumSize(QSize(500, 30))
        self.lneUltimaActualizacion_admin.setFont(font12)
        self.lneUltimaActualizacion_admin.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneUltimaActualizacion_admin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneUltimaActualizacion_admin.setStyleSheet(u"")
        self.lneUltimaActualizacion_admin.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneUltimaActualizacion_admin.setReadOnly(True)
        self.lneTlfInstitucion_admin = QLineEdit(self.frameInstitucion)
        self.lneTlfInstitucion_admin.setObjectName(u"lneTlfInstitucion_admin")
        self.lneTlfInstitucion_admin.setGeometry(QRect(260, 320, 500, 30))
        self.lneTlfInstitucion_admin.setMinimumSize(QSize(400, 30))
        self.lneTlfInstitucion_admin.setMaximumSize(QSize(500, 30))
        self.lneTlfInstitucion_admin.setFont(font12)
        self.lneTlfInstitucion_admin.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneTlfInstitucion_admin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneTlfInstitucion_admin.setStyleSheet(u"")
        self.lneTlfInstitucion_admin.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneDirInstitucion_admin = QLineEdit(self.frameInstitucion)
        self.lneDirInstitucion_admin.setObjectName(u"lneDirInstitucion_admin")
        self.lneDirInstitucion_admin.setGeometry(QRect(260, 270, 500, 30))
        self.lneDirInstitucion_admin.setMinimumSize(QSize(400, 30))
        self.lneDirInstitucion_admin.setMaximumSize(QSize(500, 30))
        self.lneDirInstitucion_admin.setFont(font12)
        self.lneDirInstitucion_admin.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneDirInstitucion_admin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneDirInstitucion_admin.setStyleSheet(u"")
        self.lneDirInstitucion_admin.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_3 = QLabel(self.frameInstitucion)
        self.lblStudent_apellido_3.setObjectName(u"lblStudent_apellido_3")
        self.lblStudent_apellido_3.setGeometry(QRect(20, 270, 241, 30))
        self.lblStudent_apellido_3.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_3.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_3.setFont(font)
        self.lblStudent_apellido_3.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_apellido_5 = QLabel(self.frameInstitucion)
        self.lblStudent_apellido_5.setObjectName(u"lblStudent_apellido_5")
        self.lblStudent_apellido_5.setGeometry(QRect(20, 370, 241, 30))
        self.lblStudent_apellido_5.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_5.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_5.setFont(font)
        self.lblStudent_apellido_5.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_apellido = QLabel(self.frameInstitucion)
        self.lblStudent_apellido.setObjectName(u"lblStudent_apellido")
        self.lblStudent_apellido.setGeometry(QRect(20, 20, 241, 30))
        self.lblStudent_apellido.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido.setFont(font)
        self.lblStudent_apellido.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_apellido_7 = QLabel(self.frameInstitucion)
        self.lblStudent_apellido_7.setObjectName(u"lblStudent_apellido_7")
        self.lblStudent_apellido_7.setGeometry(QRect(20, 520, 241, 30))
        self.lblStudent_apellido_7.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_7.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_7.setFont(font)
        self.lblStudent_apellido_7.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneNombreInstitucion_admin = QLineEdit(self.frameInstitucion)
        self.lneNombreInstitucion_admin.setObjectName(u"lneNombreInstitucion_admin")
        self.lneNombreInstitucion_admin.setGeometry(QRect(260, 20, 500, 30))
        self.lneNombreInstitucion_admin.setMinimumSize(QSize(400, 30))
        self.lneNombreInstitucion_admin.setMaximumSize(QSize(500, 30))
        self.lneNombreInstitucion_admin.setFont(font12)
        self.lneNombreInstitucion_admin.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneNombreInstitucion_admin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneNombreInstitucion_admin.setStyleSheet(u"")
        self.lneNombreInstitucion_admin.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_2 = QLabel(self.frameInstitucion)
        self.lblStudent_apellido_2.setObjectName(u"lblStudent_apellido_2")
        self.lblStudent_apellido_2.setGeometry(QRect(20, 70, 241, 30))
        self.lblStudent_apellido_2.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_2.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_2.setFont(font)
        self.lblStudent_apellido_2.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_apellido_4 = QLabel(self.frameInstitucion)
        self.lblStudent_apellido_4.setObjectName(u"lblStudent_apellido_4")
        self.lblStudent_apellido_4.setGeometry(QRect(20, 320, 241, 30))
        self.lblStudent_apellido_4.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_4.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_4.setFont(font)
        self.lblStudent_apellido_4.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneCodigoDEA_admin = QLineEdit(self.frameInstitucion)
        self.lneCodigoDEA_admin.setObjectName(u"lneCodigoDEA_admin")
        self.lneCodigoDEA_admin.setGeometry(QRect(260, 70, 500, 30))
        self.lneCodigoDEA_admin.setMinimumSize(QSize(400, 30))
        self.lneCodigoDEA_admin.setMaximumSize(QSize(500, 30))
        self.lneCodigoDEA_admin.setFont(font12)
        self.lneCodigoDEA_admin.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneCodigoDEA_admin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneCodigoDEA_admin.setStyleSheet(u"")
        self.lneCodigoDEA_admin.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneCorreoInstitucion_admin = QLineEdit(self.frameInstitucion)
        self.lneCorreoInstitucion_admin.setObjectName(u"lneCorreoInstitucion_admin")
        self.lneCorreoInstitucion_admin.setGeometry(QRect(260, 370, 500, 30))
        self.lneCorreoInstitucion_admin.setMinimumSize(QSize(400, 30))
        self.lneCorreoInstitucion_admin.setMaximumSize(QSize(500, 30))
        self.lneCorreoInstitucion_admin.setFont(font12)
        self.lneCorreoInstitucion_admin.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneCorreoInstitucion_admin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneCorreoInstitucion_admin.setStyleSheet(u"")
        self.lneCorreoInstitucion_admin.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_6 = QLabel(self.frameInstitucion)
        self.lblStudent_apellido_6.setObjectName(u"lblStudent_apellido_6")
        self.lblStudent_apellido_6.setGeometry(QRect(20, 420, 241, 30))
        self.lblStudent_apellido_6.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_6.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_6.setFont(font)
        self.lblStudent_apellido_6.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneDirector_institucion = QLineEdit(self.frameInstitucion)
        self.lneDirector_institucion.setObjectName(u"lneDirector_institucion")
        self.lneDirector_institucion.setGeometry(QRect(260, 420, 500, 30))
        self.lneDirector_institucion.setMinimumSize(QSize(400, 30))
        self.lneDirector_institucion.setMaximumSize(QSize(500, 30))
        self.lneDirector_institucion.setFont(font12)
        self.lneDirector_institucion.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneDirector_institucion.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneDirector_institucion.setStyleSheet(u"")
        self.lneDirector_institucion.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_8 = QLabel(self.frameInstitucion)
        self.lblStudent_apellido_8.setObjectName(u"lblStudent_apellido_8")
        self.lblStudent_apellido_8.setGeometry(QRect(20, 470, 241, 30))
        self.lblStudent_apellido_8.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_8.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_8.setFont(font)
        self.lblStudent_apellido_8.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneCedula_director_institucion = QLineEdit(self.frameInstitucion)
        self.lneCedula_director_institucion.setObjectName(u"lneCedula_director_institucion")
        self.lneCedula_director_institucion.setGeometry(QRect(260, 470, 500, 30))
        self.lneCedula_director_institucion.setMinimumSize(QSize(400, 30))
        self.lneCedula_director_institucion.setMaximumSize(QSize(500, 30))
        self.lneCedula_director_institucion.setFont(font12)
        self.lneCedula_director_institucion.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneCedula_director_institucion.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneCedula_director_institucion.setStyleSheet(u"")
        self.lneCedula_director_institucion.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_9 = QLabel(self.frameInstitucion)
        self.lblStudent_apellido_9.setObjectName(u"lblStudent_apellido_9")
        self.lblStudent_apellido_9.setGeometry(QRect(20, 120, 241, 30))
        self.lblStudent_apellido_9.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_9.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_9.setFont(font)
        self.lblStudent_apellido_9.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneCodigoDEP_admin = QLineEdit(self.frameInstitucion)
        self.lneCodigoDEP_admin.setObjectName(u"lneCodigoDEP_admin")
        self.lneCodigoDEP_admin.setGeometry(QRect(260, 120, 500, 30))
        self.lneCodigoDEP_admin.setMinimumSize(QSize(400, 30))
        self.lneCodigoDEP_admin.setMaximumSize(QSize(500, 30))
        self.lneCodigoDEP_admin.setFont(font12)
        self.lneCodigoDEP_admin.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneCodigoDEP_admin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneCodigoDEP_admin.setStyleSheet(u"")
        self.lneCodigoDEP_admin.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneCodigoEST_admin = QLineEdit(self.frameInstitucion)
        self.lneCodigoEST_admin.setObjectName(u"lneCodigoEST_admin")
        self.lneCodigoEST_admin.setGeometry(QRect(260, 170, 500, 30))
        self.lneCodigoEST_admin.setMinimumSize(QSize(400, 30))
        self.lneCodigoEST_admin.setMaximumSize(QSize(500, 30))
        self.lneCodigoEST_admin.setFont(font12)
        self.lneCodigoEST_admin.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneCodigoEST_admin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneCodigoEST_admin.setStyleSheet(u"")
        self.lneCodigoEST_admin.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_10 = QLabel(self.frameInstitucion)
        self.lblStudent_apellido_10.setObjectName(u"lblStudent_apellido_10")
        self.lblStudent_apellido_10.setGeometry(QRect(20, 170, 241, 30))
        self.lblStudent_apellido_10.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_10.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_10.setFont(font)
        self.lblStudent_apellido_10.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_apellido_11 = QLabel(self.frameInstitucion)
        self.lblStudent_apellido_11.setObjectName(u"lblStudent_apellido_11")
        self.lblStudent_apellido_11.setGeometry(QRect(20, 220, 241, 30))
        self.lblStudent_apellido_11.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_11.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_11.setFont(font)
        self.lblStudent_apellido_11.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;\n"
"border: transparent;")
        self.lblStudent_apellido_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneRIF_admin = QLineEdit(self.frameInstitucion)
        self.lneRIF_admin.setObjectName(u"lneRIF_admin")
        self.lneRIF_admin.setGeometry(QRect(260, 220, 500, 30))
        self.lneRIF_admin.setMinimumSize(QSize(400, 30))
        self.lneRIF_admin.setMaximumSize(QSize(500, 30))
        self.lneRIF_admin.setFont(font12)
        self.lneRIF_admin.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneRIF_admin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneRIF_admin.setStyleSheet(u"")
        self.lneRIF_admin.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.stackMain.addWidget(self.datos_institucionales)
        self.Anio_escolar = QWidget()
        self.Anio_escolar.setObjectName(u"Anio_escolar")
        self.stackMain.addWidget(self.Anio_escolar)
        self.copia_seguridad = QWidget()
        self.copia_seguridad.setObjectName(u"copia_seguridad")
        self.line_7 = QFrame(self.copia_seguridad)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(1030, 10, 3, 61))
        self.line_7.setMinimumSize(QSize(3, 61))
        self.line_7.setMaximumSize(QSize(3, 61))
        self.line_7.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblTitulo_logo_emple_6 = QLabel(self.copia_seguridad)
        self.lblTitulo_logo_emple_6.setObjectName(u"lblTitulo_logo_emple_6")
        self.lblTitulo_logo_emple_6.setGeometry(QRect(891, 0, 131, 81))
        self.lblTitulo_logo_emple_6.setFont(font8)
        self.lblTitulo_logo_emple_6.setStyleSheet(u"color: #2d2d2d")
        self.lblTitulo_logo_emple_6.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_logo_emple_6.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_logo_emple_6.setScaledContents(False)
        self.lblTitulo_logo_emple_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_logo_emple_6.setWordWrap(True)
        self.lblTitulo_logo_emple_6.setIndent(0)
        self.lblLogo_emple_6 = QLabel(self.copia_seguridad)
        self.lblLogo_emple_6.setObjectName(u"lblLogo_emple_6")
        self.lblLogo_emple_6.setGeometry(QRect(1040, 10, 51, 61))
        self.lblLogo_emple_6.setMinimumSize(QSize(50, 50))
        self.lblLogo_emple_6.setMaximumSize(QSize(130, 70))
        self.lblLogo_emple_6.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_emple_6.setScaledContents(True)
        self.lblTitulo_logo_emple_7 = QLabel(self.copia_seguridad)
        self.lblTitulo_logo_emple_7.setObjectName(u"lblTitulo_logo_emple_7")
        self.lblTitulo_logo_emple_7.setGeometry(QRect(200, 30, 481, 101))
        font13 = QFont()
        font13.setFamilies([u"Segoe UI"])
        font13.setPointSize(17)
        font13.setBold(True)
        self.lblTitulo_logo_emple_7.setFont(font13)
        self.lblTitulo_logo_emple_7.setStyleSheet(u"color: #2d2d2d")
        self.lblTitulo_logo_emple_7.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_logo_emple_7.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_logo_emple_7.setScaledContents(False)
        self.lblTitulo_logo_emple_7.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.lblTitulo_logo_emple_7.setWordWrap(True)
        self.lblTitulo_logo_emple_7.setIndent(0)
        self.lblTitulo_logo_emple_8 = QLabel(self.copia_seguridad)
        self.lblTitulo_logo_emple_8.setObjectName(u"lblTitulo_logo_emple_8")
        self.lblTitulo_logo_emple_8.setGeometry(QRect(250, 140, 391, 51))
        self.lblTitulo_logo_emple_8.setFont(font5)
        self.lblTitulo_logo_emple_8.setStyleSheet(u"color: #2d2d2d")
        self.lblTitulo_logo_emple_8.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_logo_emple_8.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_logo_emple_8.setScaledContents(False)
        self.lblTitulo_logo_emple_8.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.lblTitulo_logo_emple_8.setWordWrap(True)
        self.lblTitulo_logo_emple_8.setIndent(0)
        self.btnBackup_manual = QPushButton(self.copia_seguridad)
        self.btnBackup_manual.setObjectName(u"btnBackup_manual")
        self.btnBackup_manual.setGeometry(QRect(230, 210, 421, 60))
        sizePolicy1.setHeightForWidth(self.btnBackup_manual.sizePolicy().hasHeightForWidth())
        self.btnBackup_manual.setSizePolicy(sizePolicy1)
        self.btnBackup_manual.setMinimumSize(QSize(120, 40))
        self.btnBackup_manual.setMaximumSize(QSize(500, 60))
        self.btnBackup_manual.setFont(font1)
        self.btnBackup_manual.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBackup_manual.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnBackup_manual.setStyleSheet(u"QPushButton {\n"
"   background-color: #2980b9;\n"
"    color: #F3F6FF;\n"
"    border: none;\n"
"    padding: 8px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1;\n"
"}")
        icon24 = QIcon()
        icon24.addFile(u":/icons/copia_seguridad_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBackup_manual.setIcon(icon24)
        self.btnBackup_manual.setIconSize(QSize(30, 30))
        self.lblUltimo_backup = QLabel(self.copia_seguridad)
        self.lblUltimo_backup.setObjectName(u"lblUltimo_backup")
        self.lblUltimo_backup.setGeometry(QRect(180, 290, 521, 41))
        self.lblUltimo_backup.setFont(font)
        self.lblUltimo_backup.setStyleSheet(u"color: #2d2d2d")
        self.lblUltimo_backup.setFrameShape(QFrame.Shape.NoFrame)
        self.lblUltimo_backup.setFrameShadow(QFrame.Shadow.Plain)
        self.lblUltimo_backup.setScaledContents(False)
        self.lblUltimo_backup.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.lblUltimo_backup.setWordWrap(True)
        self.lblUltimo_backup.setIndent(0)
        self.stackMain.addWidget(self.copia_seguridad)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1300, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackBarra_lateral.setCurrentIndex(0)
        self.stackMain.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnUsuario_home.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.btnAdmin.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.btnReportes.setText(QCoreApplication.translate("MainWindow", u"Reportes", None))
        self.btnEmpleados.setText(QCoreApplication.translate("MainWindow", u"Empleados", None))
        self.btnEstudiantes.setText(QCoreApplication.translate("MainWindow", u"Estudiantes", None))
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
#if QT_CONFIG(tooltip)
        self.btnGestion_estudiantes.setToolTip(QCoreApplication.translate("MainWindow", u"Modulo estudiantes", None))
#endif // QT_CONFIG(tooltip)
        self.btnGestion_estudiantes.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.btnSecciones.setToolTip(QCoreApplication.translate("MainWindow", u"Modulo estudiantes", None))
#endif // QT_CONFIG(tooltip)
        self.btnSecciones.setText(QCoreApplication.translate("MainWindow", u"Secciones", None))
#if QT_CONFIG(tooltip)
        self.btnEgresados.setToolTip(QCoreApplication.translate("MainWindow", u"Modulo estudiantes", None))
#endif // QT_CONFIG(tooltip)
        self.btnEgresados.setText(QCoreApplication.translate("MainWindow", u"Egresados", None))
#if QT_CONFIG(tooltip)
        self.btnRegresar_estudiantes.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.btnRegresar_estudiantes.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
#if QT_CONFIG(tooltip)
        self.btnGestion_usuarios.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btnGestion_usuarios.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de\n"
"usuarios", None))
        self.btnRoles.setText(QCoreApplication.translate("MainWindow", u"Roles y\n"
"permisos", None))
        self.lblResumenGeneral_2.setText(QCoreApplication.translate("MainWindow", u"USUARIOS", None))
        self.lblResumenGeneral_3.setText(QCoreApplication.translate("MainWindow", u"SEGURIDAD", None))
        self.btnAuditoria.setText(QCoreApplication.translate("MainWindow", u"Auditor\u00eda de\n"
"accesos", None))
        self.lblResumenGeneral_4.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
        self.btnDatos_institucion.setText(QCoreApplication.translate("MainWindow", u"Instituci\u00f3n", None))
        self.lblResumenGeneral_5.setText(QCoreApplication.translate("MainWindow", u"MANTENIMIENTO", None))
        self.btnCopia_seguridad.setText(QCoreApplication.translate("MainWindow", u"Copias de\n"
"seguridad", None))
#if QT_CONFIG(tooltip)
        self.btnRegresar_admin.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.btnRegresar_admin.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.btnAnio_escolar.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o escolar", None))
        self.lblSaludo_Icon.setText("")
        self.lblBienvenida.setText(QCoreApplication.translate("MainWindow", u"\u00a1Bienvenido, Usuario1!", None))
        self.lblSaludo_Descript.setText(QCoreApplication.translate("MainWindow", u"Esta es la ventana principal del sistema, en la que ver\u00e1s res\u00famenes breves sobre informacion relevante.", None))
        self.btnAccesoDirecto_reg_estu.setText("")
        self.lblResumenGeneral_6.setText(QCoreApplication.translate("MainWindow", u"Registrar estudiante", None))
        self.lblResumenGeneral_7.setText(QCoreApplication.translate("MainWindow", u"Accesos directos", None))
        self.lblResumenGeneral_8.setText(QCoreApplication.translate("MainWindow", u"Registras empleado", None))
        self.btnAccesoDirecto_reg_emple.setText("")
        self.lblResumenGeneral_9.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de secciones", None))
        self.btnAccesoDirecto_secciones.setText("")
        self.lblTituloNotif_home.setText(QCoreApplication.translate("MainWindow", u"Estado del sistema", None))
        self.lblNotificaciones_home.setText(QCoreApplication.translate("MainWindow", u"Cargando...", None))
        self.lblTarjeta1_icon.setText("")
        self.lblTarjeta1_Titulo.setText(QCoreApplication.translate("MainWindow", u"Total matr\u00edcula estudiantil:", None))
        self.lblMatricula_home.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.lblResumenGeneral.setText(QCoreApplication.translate("MainWindow", u"Resumen general", None))
        self.lblTarjeta1_icon_3.setText("")
        self.lblTarjeta1_Titulo_3.setText(QCoreApplication.translate("MainWindow", u"Total representantes:", None))
        self.lblRepresentantes_home.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.lblTarjeta1_icon_4.setText("")
        self.lblTarjeta1_Titulo_4.setText(QCoreApplication.translate("MainWindow", u"Total trabajadores:", None))
        self.lblEmpleados_home.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lblTarjeta1_icon_5.setText("")
        self.lblTarjeta1_Titulo_5.setText(QCoreApplication.translate("MainWindow", u"Secci\u00f3n con mas estudiantes:", None))
        self.lblSeccion_home.setText(QCoreApplication.translate("MainWindow", u"3er Nivel A", None))
        self.lblLogo_dashboard.setText("")
        self.lblLogo_dashboard_escuela.setText("")
        self.lblMin.setText(QCoreApplication.translate("MainWindow", u"Edad m\u00ednima", None))
        self.cbxPoblacion.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccione poblaci\u00f3n", None))
        self.cbxPoblacion.setItemText(1, QCoreApplication.translate("MainWindow", u"Estudiantes", None))
        self.cbxPoblacion.setItemText(2, QCoreApplication.translate("MainWindow", u"Egresados", None))
        self.cbxPoblacion.setItemText(3, QCoreApplication.translate("MainWindow", u"Secciones", None))
        self.cbxPoblacion.setItemText(4, QCoreApplication.translate("MainWindow", u"Empleados", None))

        self.lblMax.setText(QCoreApplication.translate("MainWindow", u"Edad m\u00e1xima", None))
        self.btnExportar_reporte.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.btnGenerarGrafica.setText(QCoreApplication.translate("MainWindow", u"Generar", None))
        self.lblLogo_emple_2.setText("")
        self.lblTitulo_logo_emple_2.setText(QCoreApplication.translate("MainWindow", u"M\u00f3dulo de reportes", None))
        self.lblMin_2.setText(QCoreApplication.translate("MainWindow", u"Poblaci\u00f3n", None))
        self.lblMin_3.setText(QCoreApplication.translate("MainWindow", u"Criterio", None))
        self.lblMin_4.setText(QCoreApplication.translate("MainWindow", u"Tipo de gr\u00e1fica", None))
        self.lblSeccion_reporte.setText(QCoreApplication.translate("MainWindow", u"Secci\u00f3n:", None))
        self.btnCrear_usuario.setText(QCoreApplication.translate("MainWindow", u"Crear usuario", None))
        self.btnActualizar_usuario.setText(QCoreApplication.translate("MainWindow", u"Actualizar usuario", None))
        self.btnDisable_usuario.setText(QCoreApplication.translate("MainWindow", u"Deshabilitar/Habilitar", None))
        self.lblTitulo_logo_emple_3.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de usuarios", None))
        self.lblLogo_emple_3.setText("")
        self.lblInactivos_usuarios.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.lblTarjeta1_Titulo_11.setText(QCoreApplication.translate("MainWindow", u"Usuarios inactivos:", None))
        self.chkMostrar_inactivos_user.setText(QCoreApplication.translate("MainWindow", u"Mostrar inactivos", None))
        self.lblTarjeta1_Titulo_12.setText(QCoreApplication.translate("MainWindow", u"Usuarios activos:", None))
        self.lblActivos_usuarios.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.btnActualizar_tabla_user.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.lblLogo_emple_4.setText("")
        self.lblTitulo_logo_emple_4.setText(QCoreApplication.translate("MainWindow", u"Auditor\u00eda de accesos", None))
        self.btnActualizar_tabla_auditoria.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnModificar_institucion.setText(QCoreApplication.translate("MainWindow", u"Modificar datos", None))
        self.lblTitulo_logo_emple_5.setText(QCoreApplication.translate("MainWindow", u"Datos de instituci\u00f3n", None))
        self.lblLogo_emple_5.setText("")
        self.lneUltimaActualizacion_admin.setText("")
        self.lneUltimaActualizacion_admin.setPlaceholderText("")
        self.lneTlfInstitucion_admin.setText("")
        self.lneTlfInstitucion_admin.setPlaceholderText("")
        self.lneDirInstitucion_admin.setText("")
        self.lneDirInstitucion_admin.setPlaceholderText("")
        self.lblStudent_apellido_3.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n:", None))
        self.lblStudent_apellido_5.setText(QCoreApplication.translate("MainWindow", u"Correo electr\u00f3nico:", None))
        self.lblStudent_apellido.setText(QCoreApplication.translate("MainWindow", u"Nombre de la instituci\u00f3n:", None))
        self.lblStudent_apellido_7.setText(QCoreApplication.translate("MainWindow", u"Actualizado por \u00faltima vez:", None))
        self.lneNombreInstitucion_admin.setText("")
        self.lneNombreInstitucion_admin.setPlaceholderText("")
        self.lblStudent_apellido_2.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo DEA:", None))
        self.lblStudent_apellido_4.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.lneCodigoDEA_admin.setText("")
        self.lneCodigoDEA_admin.setPlaceholderText("")
        self.lneCorreoInstitucion_admin.setText("")
        self.lneCorreoInstitucion_admin.setPlaceholderText("")
        self.lblStudent_apellido_6.setText(QCoreApplication.translate("MainWindow", u"Nombre Director(a):", None))
        self.lneDirector_institucion.setText("")
        self.lneDirector_institucion.setPlaceholderText("")
        self.lblStudent_apellido_8.setText(QCoreApplication.translate("MainWindow", u"C\u00e9dula Director(a):", None))
        self.lneCedula_director_institucion.setText("")
        self.lneCedula_director_institucion.setPlaceholderText("")
        self.lblStudent_apellido_9.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo dependencia:", None))
        self.lneCodigoDEP_admin.setText("")
        self.lneCodigoDEP_admin.setPlaceholderText("")
        self.lneCodigoEST_admin.setText("")
        self.lneCodigoEST_admin.setPlaceholderText("")
        self.lblStudent_apellido_10.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo estad\u00edstico:", None))
        self.lblStudent_apellido_11.setText(QCoreApplication.translate("MainWindow", u"RIF:", None))
        self.lneRIF_admin.setText("")
        self.lneRIF_admin.setPlaceholderText("")
        self.lblTitulo_logo_emple_6.setText(QCoreApplication.translate("MainWindow", u"Copia de seguridad", None))
        self.lblLogo_emple_6.setText("")
        self.lblTitulo_logo_emple_7.setText(QCoreApplication.translate("MainWindow", u"Desde \u00e9ste m\u00f3dulo puede crear una copia de seguridad de la base de datos manualmente en su dispositivo.", None))
        self.lblTitulo_logo_emple_8.setText(QCoreApplication.translate("MainWindow", u"El sistema est\u00e1 programado para realizar copias de seguridad autom\u00e1ticas en su dispositivo cada 3 d\u00edas.", None))
        self.btnBackup_manual.setText(QCoreApplication.translate("MainWindow", u"Crear copia de seguridad de base de datos", None))
        self.lblUltimo_backup.setText(QCoreApplication.translate("MainWindow", u"lblUltimo_backup", None))
    # retranslateUi

