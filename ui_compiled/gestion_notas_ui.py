# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestion_notas.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTableView, QWidget)
from resources import resources_ui

class Ui_gestion_notas(object):
    def setupUi(self, gestion_notas):
        if not gestion_notas.objectName():
            gestion_notas.setObjectName(u"gestion_notas")
        gestion_notas.resize(1111, 621)
        gestion_notas.setMinimumSize(QSize(1111, 621))
        gestion_notas.setMaximumSize(QSize(1111, 621))
        gestion_notas.setStyleSheet(u"background-color: #f5f6fa;\n"
"color: #2d2d2d;")
        self.frameHeader = QFrame(gestion_notas)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setGeometry(QRect(9, 3, 1093, 55))
        self.frameHeader.setMinimumSize(QSize(0, 55))
        self.frameHeader.setMaximumSize(QSize(16777215, 50))
        self.frameHeader.setStyleSheet(u"QFrame{\n"
"		border-radius: 16px;\n"
"		background-color: transparent;\n"
"border: transparent;\n"
"}\n"
"QLabel{\n"
"	background-color: transparent;\n"
"	color: #2d2d2d;\n"
"border: transparent;\n"
"}")
        self.frameHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameHeader.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameHeader)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblAnio_escolar_notas = QLabel(self.frameHeader)
        self.lblAnio_escolar_notas.setObjectName(u"lblAnio_escolar_notas")
        self.lblAnio_escolar_notas.setMinimumSize(QSize(230, 0))
        self.lblAnio_escolar_notas.setMaximumSize(QSize(230, 61))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        font.setBold(True)
        self.lblAnio_escolar_notas.setFont(font)
        self.lblAnio_escolar_notas.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblAnio_escolar_notas.setFrameShape(QFrame.Shape.NoFrame)
        self.lblAnio_escolar_notas.setFrameShadow(QFrame.Shadow.Plain)
        self.lblAnio_escolar_notas.setScaledContents(False)
        self.lblAnio_escolar_notas.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblAnio_escolar_notas.setWordWrap(False)
        self.lblAnio_escolar_notas.setIndent(0)

        self.horizontalLayout.addWidget(self.lblAnio_escolar_notas)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lblTitulo_notas = QLabel(self.frameHeader)
        self.lblTitulo_notas.setObjectName(u"lblTitulo_notas")
        self.lblTitulo_notas.setMinimumSize(QSize(150, 45))
        self.lblTitulo_notas.setMaximumSize(QSize(150, 45))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.lblTitulo_notas.setFont(font1)
        self.lblTitulo_notas.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblTitulo_notas.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_notas.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_notas.setScaledContents(False)
        self.lblTitulo_notas.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_notas.setWordWrap(True)
        self.lblTitulo_notas.setIndent(0)

        self.horizontalLayout.addWidget(self.lblTitulo_notas)

        self.line_2 = QFrame(self.frameHeader)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(3, 45))
        self.line_2.setMaximumSize(QSize(3, 45))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.lblLogo_notas = QLabel(self.frameHeader)
        self.lblLogo_notas.setObjectName(u"lblLogo_notas")
        self.lblLogo_notas.setMinimumSize(QSize(45, 45))
        self.lblLogo_notas.setMaximumSize(QSize(45, 45))
        self.lblLogo_notas.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblLogo_notas.setStyleSheet(u"background-color: transparent;")
        self.lblLogo_notas.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_notas.setScaledContents(True)
        self.lblLogo_notas.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lblLogo_notas)

        self.frameHeader_2 = QFrame(gestion_notas)
        self.frameHeader_2.setObjectName(u"frameHeader_2")
        self.frameHeader_2.setGeometry(QRect(9, 62, 1093, 51))
        self.frameHeader_2.setMinimumSize(QSize(0, 51))
        self.frameHeader_2.setMaximumSize(QSize(16777215, 51))
        self.frameHeader_2.setStyleSheet(u"QFrame{\n"
"		border-radius: 16px;\n"
"		background-color: transparent;\n"
"border: transparent;\n"
"}\n"
"QLabel{\n"
"	background-color: transparent;\n"
"	color: #2d2d2d;\n"
"border: transparent;\n"
"}")
        self.frameHeader_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameHeader_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frameHeader_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lneBuscar_seccion_notas = QLineEdit(self.frameHeader_2)
        self.lneBuscar_seccion_notas.setObjectName(u"lneBuscar_seccion_notas")
        self.lneBuscar_seccion_notas.setMinimumSize(QSize(200, 35))
        self.lneBuscar_seccion_notas.setMaximumSize(QSize(541, 35))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(13)
        self.lneBuscar_seccion_notas.setFont(font2)
        self.lneBuscar_seccion_notas.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneBuscar_seccion_notas.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #848f9d;\n"
"	color: #2d2d2d;\n"
"    border-radius: 12px;\n"
"    padding: 1px 5px;\n"
"    background-color: white;\n"
"}")
        self.lneBuscar_seccion_notas.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneBuscar_seccion_notas.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.lneBuscar_seccion_notas)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.lblIcon_conectado_como = QLabel(self.frameHeader_2)
        self.lblIcon_conectado_como.setObjectName(u"lblIcon_conectado_como")
        self.lblIcon_conectado_como.setMinimumSize(QSize(16, 16))
        self.lblIcon_conectado_como.setMaximumSize(QSize(16, 16))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(8)
        font3.setBold(True)
        self.lblIcon_conectado_como.setFont(font3)
        self.lblIcon_conectado_como.setStyleSheet(u"color: #2d2d2d")
        self.lblIcon_conectado_como.setPixmap(QPixmap(u":/icons/usuario-activo.png"))
        self.lblIcon_conectado_como.setScaledContents(True)
        self.lblIcon_conectado_como.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lblIcon_conectado_como)

        self.lblConectado_como = QLabel(self.frameHeader_2)
        self.lblConectado_como.setObjectName(u"lblConectado_como")
        self.lblConectado_como.setMinimumSize(QSize(161, 16))
        self.lblConectado_como.setMaximumSize(QSize(161, 161))
        self.lblConectado_como.setFont(font3)
        self.lblConectado_como.setStyleSheet(u"color: #2d2d2d")
        self.lblConectado_como.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lblConectado_como)

        self.scrollArea = QScrollArea(gestion_notas)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(9, 119, 1093, 100))
        self.scrollArea.setMinimumSize(QSize(0, 100))
        self.scrollArea.setMaximumSize(QSize(16777215, 100))
        self.scrollArea.setStyleSheet(u"border: transparent;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1093, 100))
        self.widgetSecciones_notas = QWidget(self.scrollAreaWidgetContents)
        self.widgetSecciones_notas.setObjectName(u"widgetSecciones_notas")
        self.widgetSecciones_notas.setGeometry(QRect(10, 10, 1071, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.widgetSecciones_notas)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame = QFrame(gestion_notas)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 225, 1093, 387))
        self.frame.setStyleSheet(u"border: transparent;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frameHeader_3 = QFrame(self.frame)
        self.frameHeader_3.setObjectName(u"frameHeader_3")
        self.frameHeader_3.setGeometry(QRect(0, 0, 1090, 31))
        self.frameHeader_3.setMinimumSize(QSize(0, 31))
        self.frameHeader_3.setMaximumSize(QSize(16777215, 31))
        self.frameHeader_3.setStyleSheet(u"QFrame{\n"
"		border-radius: 16px;\n"
"		background-color: transparent;\n"
"border: transparent;\n"
"}\n"
"QLabel{\n"
"	background-color: transparent;\n"
"	color: #2d2d2d;\n"
"border: transparent;\n"
"}")
        self.frameHeader_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameHeader_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameHeader_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblGrado_notas = QLabel(self.frameHeader_3)
        self.lblGrado_notas.setObjectName(u"lblGrado_notas")
        self.lblGrado_notas.setMinimumSize(QSize(230, 0))
        self.lblGrado_notas.setMaximumSize(QSize(230, 61))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.lblGrado_notas.setFont(font4)
        self.lblGrado_notas.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblGrado_notas.setFrameShape(QFrame.Shape.NoFrame)
        self.lblGrado_notas.setFrameShadow(QFrame.Shadow.Plain)
        self.lblGrado_notas.setScaledContents(False)
        self.lblGrado_notas.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblGrado_notas.setWordWrap(False)
        self.lblGrado_notas.setIndent(0)

        self.horizontalLayout_3.addWidget(self.lblGrado_notas)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.lblDocente_notas = QLabel(self.frameHeader_3)
        self.lblDocente_notas.setObjectName(u"lblDocente_notas")
        self.lblDocente_notas.setMinimumSize(QSize(250, 0))
        self.lblDocente_notas.setMaximumSize(QSize(200, 61))
        self.lblDocente_notas.setFont(font4)
        self.lblDocente_notas.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblDocente_notas.setFrameShape(QFrame.Shape.NoFrame)
        self.lblDocente_notas.setFrameShadow(QFrame.Shadow.Plain)
        self.lblDocente_notas.setScaledContents(False)
        self.lblDocente_notas.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblDocente_notas.setWordWrap(True)
        self.lblDocente_notas.setIndent(0)

        self.horizontalLayout_3.addWidget(self.lblDocente_notas)

        self.frameHeader_4 = QFrame(self.frame)
        self.frameHeader_4.setObjectName(u"frameHeader_4")
        self.frameHeader_4.setGeometry(QRect(0, 30, 1090, 60))
        self.frameHeader_4.setMinimumSize(QSize(0, 60))
        self.frameHeader_4.setMaximumSize(QSize(16777215, 60))
        self.frameHeader_4.setStyleSheet(u"QFrame{\n"
"		border-radius: 16px;\n"
"		background-color: transparent;\n"
"border: transparent;\n"
"}\n"
"QLabel{\n"
"	background-color: transparent;\n"
"	color: #2d2d2d;\n"
"border: transparent;\n"
"}")
        self.frameHeader_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameHeader_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frameHeader_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblTitulo_materias_7 = QLabel(self.frameHeader_4)
        self.lblTitulo_materias_7.setObjectName(u"lblTitulo_materias_7")
        self.lblTitulo_materias_7.setMinimumSize(QSize(60, 0))
        self.lblTitulo_materias_7.setMaximumSize(QSize(70, 61))
        self.lblTitulo_materias_7.setFont(font4)
        self.lblTitulo_materias_7.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblTitulo_materias_7.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_materias_7.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_materias_7.setScaledContents(False)
        self.lblTitulo_materias_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_materias_7.setWordWrap(False)
        self.lblTitulo_materias_7.setIndent(0)

        self.horizontalLayout_5.addWidget(self.lblTitulo_materias_7)

        self.frameMateria_notas = QFrame(self.frameHeader_4)
        self.frameMateria_notas.setObjectName(u"frameMateria_notas")
        self.frameMateria_notas.setMinimumSize(QSize(300, 35))
        self.frameMateria_notas.setMaximumSize(QSize(300, 40))
        self.frameMateria_notas.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #2c3e50;\n"
"	border-radius: 12px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frameMateria_notas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameMateria_notas.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxMateria_notas = QComboBox(self.frameMateria_notas)
        self.cbxMateria_notas.addItem("")
        self.cbxMateria_notas.setObjectName(u"cbxMateria_notas")
        self.cbxMateria_notas.setGeometry(QRect(10, 5, 280, 30))
        self.cbxMateria_notas.setMinimumSize(QSize(280, 0))
        self.cbxMateria_notas.setMaximumSize(QSize(280, 30))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(11)
        font5.setBold(True)
        self.cbxMateria_notas.setFont(font5)
        self.cbxMateria_notas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxMateria_notas.setStyleSheet(u"QComboBox {\n"
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
        self.cbxMateria_notas.setIconSize(QSize(5, 5))

        self.horizontalLayout_5.addWidget(self.frameMateria_notas)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.btnGuardar_notas = QPushButton(self.frameHeader_4)
        self.btnGuardar_notas.setObjectName(u"btnGuardar_notas")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGuardar_notas.sizePolicy().hasHeightForWidth())
        self.btnGuardar_notas.setSizePolicy(sizePolicy)
        self.btnGuardar_notas.setMinimumSize(QSize(120, 40))
        self.btnGuardar_notas.setMaximumSize(QSize(120, 40))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(13)
        font6.setBold(True)
        self.btnGuardar_notas.setFont(font6)
        self.btnGuardar_notas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGuardar_notas.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnGuardar_notas.setStyleSheet(u"QPushButton {\n"
"  \n"
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
        icon.addFile(u":/icons/guardar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGuardar_notas.setIcon(icon)
        self.btnGuardar_notas.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.btnGuardar_notas)

        self.frameTabla_notas = QFrame(self.frame)
        self.frameTabla_notas.setObjectName(u"frameTabla_notas")
        self.frameTabla_notas.setGeometry(QRect(0, 90, 1081, 291))
        self.frameTabla_notas.setMinimumSize(QSize(1000, 150))
        self.frameTabla_notas.setMaximumSize(QSize(1400, 401))
        self.frameTabla_notas.setStyleSheet(u"QFrame#frameTabla_notas {\n"
"    border: 1px solid #d5dbdb;\n"
"    border-radius: 12px;\n"
"    background-color: white;\n"
"}")
        self.frameTabla_notas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTabla_notas.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frameTabla_notas)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tableW_notas = QTableView(self.frameTabla_notas)
        self.tableW_notas.setObjectName(u"tableW_notas")
        self.tableW_notas.setStyleSheet(u"QTableView {\n"
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
        self.tableW_notas.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableW_notas.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.tableW_notas.setTabKeyNavigation(False)
        self.tableW_notas.setDragDropOverwriteMode(False)
        self.tableW_notas.setAlternatingRowColors(True)
        self.tableW_notas.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableW_notas.setShowGrid(True)
        self.tableW_notas.setSortingEnabled(True)

        self.horizontalLayout_6.addWidget(self.tableW_notas)


        self.retranslateUi(gestion_notas)

        QMetaObject.connectSlotsByName(gestion_notas)
    # setupUi

    def retranslateUi(self, gestion_notas):
        gestion_notas.setWindowTitle(QCoreApplication.translate("gestion_notas", u"Form", None))
        self.lblAnio_escolar_notas.setText(QCoreApplication.translate("gestion_notas", u"A\u00f1o escolar: 2025-2026", None))
        self.lblTitulo_notas.setText(QCoreApplication.translate("gestion_notas", u"Gesti\u00f3n de Notas", None))
        self.lblLogo_notas.setText("")
        self.lneBuscar_seccion_notas.setText("")
        self.lneBuscar_seccion_notas.setPlaceholderText(QCoreApplication.translate("gestion_notas", u"Buscar secci\u00f3n...", None))
        self.lblIcon_conectado_como.setText("")
        self.lblConectado_como.setText(QCoreApplication.translate("gestion_notas", u"Conectado como: jorged", None))
        self.lblGrado_notas.setText(QCoreApplication.translate("gestion_notas", u"1er Grado \"A\" - Primaria", None))
        self.lblDocente_notas.setText(QCoreApplication.translate("gestion_notas", u"Docente: Maria Perezsssss", None))
        self.lblTitulo_materias_7.setText(QCoreApplication.translate("gestion_notas", u"Materia:", None))
        self.cbxMateria_notas.setItemText(0, QCoreApplication.translate("gestion_notas", u"Educacion para la salud", None))

        self.btnGuardar_notas.setText(QCoreApplication.translate("gestion_notas", u"Guardar", None))
    # retranslateUi

