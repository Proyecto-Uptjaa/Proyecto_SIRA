# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestion_materias.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)
from resources import resources_ui

class Ui_gestion_materias(object):
    def setupUi(self, gestion_materias):
        if not gestion_materias.objectName():
            gestion_materias.setObjectName(u"gestion_materias")
        gestion_materias.resize(1111, 621)
        gestion_materias.setMinimumSize(QSize(1111, 621))
        gestion_materias.setMaximumSize(QSize(1111, 621))
        gestion_materias.setStyleSheet(u"background-color: #f5f6fa;\n"
"color: #2d2d2d;")
        self.verticalLayout = QVBoxLayout(gestion_materias)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameHeader = QFrame(gestion_materias)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setMinimumSize(QSize(0, 81))
        self.frameHeader.setMaximumSize(QSize(16777215, 81))
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
        self.btnNueva_materia = QPushButton(self.frameHeader)
        self.btnNueva_materia.setObjectName(u"btnNueva_materia")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNueva_materia.sizePolicy().hasHeightForWidth())
        self.btnNueva_materia.setSizePolicy(sizePolicy)
        self.btnNueva_materia.setMinimumSize(QSize(120, 40))
        self.btnNueva_materia.setMaximumSize(QSize(120, 40))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(13)
        font.setBold(True)
        self.btnNueva_materia.setFont(font)
        self.btnNueva_materia.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNueva_materia.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnNueva_materia.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/icons/nuevo_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNueva_materia.setIcon(icon)
        self.btnNueva_materia.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.btnNueva_materia)

        self.btnGestion_areas = QPushButton(self.frameHeader)
        self.btnGestion_areas.setObjectName(u"btnGestion_areas")
        sizePolicy.setHeightForWidth(self.btnGestion_areas.sizePolicy().hasHeightForWidth())
        self.btnGestion_areas.setSizePolicy(sizePolicy)
        self.btnGestion_areas.setMinimumSize(QSize(120, 40))
        self.btnGestion_areas.setMaximumSize(QSize(300, 40))
        self.btnGestion_areas.setFont(font)
        self.btnGestion_areas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGestion_areas.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnGestion_areas.setStyleSheet(u"QPushButton {\n"
"  \n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 5px 5px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/materias_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGestion_areas.setIcon(icon1)
        self.btnGestion_areas.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.btnGestion_areas)

        self.btnActualizar_tabla_materias = QPushButton(self.frameHeader)
        self.btnActualizar_tabla_materias.setObjectName(u"btnActualizar_tabla_materias")
        sizePolicy.setHeightForWidth(self.btnActualizar_tabla_materias.sizePolicy().hasHeightForWidth())
        self.btnActualizar_tabla_materias.setSizePolicy(sizePolicy)
        self.btnActualizar_tabla_materias.setMinimumSize(QSize(120, 30))
        self.btnActualizar_tabla_materias.setMaximumSize(QSize(150, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.btnActualizar_tabla_materias.setFont(font1)
        self.btnActualizar_tabla_materias.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnActualizar_tabla_materias.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnActualizar_tabla_materias.setStyleSheet(u"QPushButton {\n"
"   background-color: white;\n"
"    color: #2980b9;\n"
"    border: 1.5px solid #2980b9;\n"
"    padding: 2px 2px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(213, 234, 255);\n"
"	border: 1.5px solid #2980b9;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/actualizar_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnActualizar_tabla_materias.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btnActualizar_tabla_materias)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lblTitulo_materias = QLabel(self.frameHeader)
        self.lblTitulo_materias.setObjectName(u"lblTitulo_materias")
        self.lblTitulo_materias.setMinimumSize(QSize(150, 0))
        self.lblTitulo_materias.setMaximumSize(QSize(150, 61))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(19)
        font2.setBold(True)
        self.lblTitulo_materias.setFont(font2)
        self.lblTitulo_materias.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblTitulo_materias.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_materias.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_materias.setScaledContents(False)
        self.lblTitulo_materias.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_materias.setWordWrap(True)
        self.lblTitulo_materias.setIndent(0)

        self.horizontalLayout.addWidget(self.lblTitulo_materias)

        self.line_2 = QFrame(self.frameHeader)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(3, 61))
        self.line_2.setMaximumSize(QSize(3, 61))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.lblLogo_materias = QLabel(self.frameHeader)
        self.lblLogo_materias.setObjectName(u"lblLogo_materias")
        self.lblLogo_materias.setMinimumSize(QSize(50, 61))
        self.lblLogo_materias.setMaximumSize(QSize(50, 61))
        self.lblLogo_materias.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblLogo_materias.setStyleSheet(u"background-color: transparent;")
        self.lblLogo_materias.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_materias.setScaledContents(True)
        self.lblLogo_materias.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lblLogo_materias)


        self.verticalLayout.addWidget(self.frameHeader)

        self.frameHeader_2 = QFrame(gestion_materias)
        self.frameHeader_2.setObjectName(u"frameHeader_2")
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
        self.frameFiltro_estu = QFrame(self.frameHeader_2)
        self.frameFiltro_estu.setObjectName(u"frameFiltro_estu")
        self.frameFiltro_estu.setMinimumSize(QSize(147, 35))
        self.frameFiltro_estu.setMaximumSize(QSize(200, 40))
        self.frameFiltro_estu.setStyleSheet(u"QFrame{\n"
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
        self.frameFiltro_estu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameFiltro_estu.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxFiltro_materias = QComboBox(self.frameFiltro_estu)
        self.cbxFiltro_materias.addItem("")
        self.cbxFiltro_materias.addItem("")
        self.cbxFiltro_materias.addItem("")
        self.cbxFiltro_materias.addItem("")
        self.cbxFiltro_materias.addItem("")
        self.cbxFiltro_materias.setObjectName(u"cbxFiltro_materias")
        self.cbxFiltro_materias.setGeometry(QRect(10, 5, 131, 25))
        self.cbxFiltro_materias.setMaximumSize(QSize(180, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.cbxFiltro_materias.setFont(font3)
        self.cbxFiltro_materias.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxFiltro_materias.setStyleSheet(u"QComboBox {\n"
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
        self.cbxFiltro_materias.setIconSize(QSize(5, 5))

        self.horizontalLayout_4.addWidget(self.frameFiltro_estu)

        self.lneBuscar_materias = QLineEdit(self.frameHeader_2)
        self.lneBuscar_materias.setObjectName(u"lneBuscar_materias")
        self.lneBuscar_materias.setMinimumSize(QSize(200, 35))
        self.lneBuscar_materias.setMaximumSize(QSize(541, 35))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(13)
        self.lneBuscar_materias.setFont(font4)
        self.lneBuscar_materias.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneBuscar_materias.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #848f9d;\n"
"	color: #2d2d2d;\n"
"    border-radius: 12px;\n"
"    padding: 1px 5px;\n"
"    background-color: white;\n"
"}")
        self.lneBuscar_materias.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneBuscar_materias.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.lneBuscar_materias)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.lblIcon_conectado_como = QLabel(self.frameHeader_2)
        self.lblIcon_conectado_como.setObjectName(u"lblIcon_conectado_como")
        self.lblIcon_conectado_como.setMinimumSize(QSize(16, 16))
        self.lblIcon_conectado_como.setMaximumSize(QSize(16, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(8)
        font5.setBold(True)
        self.lblIcon_conectado_como.setFont(font5)
        self.lblIcon_conectado_como.setStyleSheet(u"color: #2d2d2d")
        self.lblIcon_conectado_como.setPixmap(QPixmap(u":/icons/usuario-activo.png"))
        self.lblIcon_conectado_como.setScaledContents(True)
        self.lblIcon_conectado_como.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lblIcon_conectado_como)

        self.lblConectado_como = QLabel(self.frameHeader_2)
        self.lblConectado_como.setObjectName(u"lblConectado_como")
        self.lblConectado_como.setMinimumSize(QSize(161, 16))
        self.lblConectado_como.setMaximumSize(QSize(161, 161))
        self.lblConectado_como.setFont(font5)
        self.lblConectado_como.setStyleSheet(u"color: #2d2d2d")
        self.lblConectado_como.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lblConectado_como)


        self.verticalLayout.addWidget(self.frameHeader_2)

        self.frameTabla_materias = QFrame(gestion_materias)
        self.frameTabla_materias.setObjectName(u"frameTabla_materias")
        self.frameTabla_materias.setMinimumSize(QSize(900, 300))
        self.frameTabla_materias.setMaximumSize(QSize(16777215, 401))
        self.frameTabla_materias.setStyleSheet(u"QFrame#frameTabla_materias {\n"
"    border: 1px solid #d5dbdb;\n"
"    border-radius: 12px;\n"
"    background-color: white;\n"
"}")
        self.frameTabla_materias.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTabla_materias.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameTabla_materias)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableW_materias = QTableView(self.frameTabla_materias)
        self.tableW_materias.setObjectName(u"tableW_materias")
        self.tableW_materias.setStyleSheet(u"QTableView {\n"
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
        self.tableW_materias.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableW_materias.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.tableW_materias.setTabKeyNavigation(False)
        self.tableW_materias.setDragDropOverwriteMode(False)
        self.tableW_materias.setAlternatingRowColors(True)
        self.tableW_materias.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableW_materias.setShowGrid(True)
        self.tableW_materias.setSortingEnabled(True)

        self.horizontalLayout_2.addWidget(self.tableW_materias)


        self.verticalLayout.addWidget(self.frameTabla_materias)

        self.frameSaludo_2 = QFrame(gestion_materias)
        self.frameSaludo_2.setObjectName(u"frameSaludo_2")
        self.frameSaludo_2.setMaximumSize(QSize(16777215, 60))
        self.frameSaludo_2.setStyleSheet(u"QFrame{\n"
"		border-radius: 16px;\n"
"		background-color: transparent;\n"
"border: transparent;\n"
"}\n"
"QLabel{\n"
"	background-color: transparent;\n"
"	color: #2d2d2d;\n"
"border: transparent;\n"
"}")
        self.frameSaludo_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameSaludo_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameSaludo_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.chkMostrar_inactivas_materias = QCheckBox(self.frameSaludo_2)
        self.chkMostrar_inactivas_materias.setObjectName(u"chkMostrar_inactivas_materias")
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(12)
        self.chkMostrar_inactivas_materias.setFont(font6)
        self.chkMostrar_inactivas_materias.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chkMostrar_inactivas_materias.setStyleSheet(u"QCheckBox {\n"
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
        self.chkMostrar_inactivas_materias.setIconSize(QSize(20, 20))
        self.chkMostrar_inactivas_materias.setTristate(False)

        self.horizontalLayout_3.addWidget(self.chkMostrar_inactivas_materias)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btnEditar_materia = QPushButton(self.frameSaludo_2)
        self.btnEditar_materia.setObjectName(u"btnEditar_materia")
        sizePolicy.setHeightForWidth(self.btnEditar_materia.sizePolicy().hasHeightForWidth())
        self.btnEditar_materia.setSizePolicy(sizePolicy)
        self.btnEditar_materia.setMinimumSize(QSize(120, 40))
        self.btnEditar_materia.setMaximumSize(QSize(120, 40))
        self.btnEditar_materia.setFont(font)
        self.btnEditar_materia.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEditar_materia.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnEditar_materia.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/edit_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEditar_materia.setIcon(icon3)
        self.btnEditar_materia.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.btnEditar_materia)

        self.btnDesactivar_materia = QPushButton(self.frameSaludo_2)
        self.btnDesactivar_materia.setObjectName(u"btnDesactivar_materia")
        sizePolicy.setHeightForWidth(self.btnDesactivar_materia.sizePolicy().hasHeightForWidth())
        self.btnDesactivar_materia.setSizePolicy(sizePolicy)
        self.btnDesactivar_materia.setMinimumSize(QSize(120, 40))
        self.btnDesactivar_materia.setMaximumSize(QSize(120, 40))
        self.btnDesactivar_materia.setFont(font)
        self.btnDesactivar_materia.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDesactivar_materia.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnDesactivar_materia.setStyleSheet(u"QPushButton {\n"
"  \n"
"	\n"
"	background-color: #e74c3c;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #C0392B\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/cancelar_w2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDesactivar_materia.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.btnDesactivar_materia)


        self.verticalLayout.addWidget(self.frameSaludo_2)


        self.retranslateUi(gestion_materias)

        QMetaObject.connectSlotsByName(gestion_materias)
    # setupUi

    def retranslateUi(self, gestion_materias):
        gestion_materias.setWindowTitle(QCoreApplication.translate("gestion_materias", u"Form", None))
        self.btnNueva_materia.setText(QCoreApplication.translate("gestion_materias", u"Nueva", None))
        self.btnGestion_areas.setText(QCoreApplication.translate("gestion_materias", u"Gestionar \u00c1reas de Aprendizaje", None))
        self.btnActualizar_tabla_materias.setText(QCoreApplication.translate("gestion_materias", u"Actualizar tabla", None))
        self.lblTitulo_materias.setText(QCoreApplication.translate("gestion_materias", u"Gesti\u00f3n de materias", None))
        self.lblLogo_materias.setText("")
        self.cbxFiltro_materias.setItemText(0, QCoreApplication.translate("gestion_materias", u"Todos", None))
        self.cbxFiltro_materias.setItemText(1, QCoreApplication.translate("gestion_materias", u"Nombre", None))
        self.cbxFiltro_materias.setItemText(2, QCoreApplication.translate("gestion_materias", u"Abreviatura", None))
        self.cbxFiltro_materias.setItemText(3, QCoreApplication.translate("gestion_materias", u"Estado", None))
        self.cbxFiltro_materias.setItemText(4, QCoreApplication.translate("gestion_materias", u"Grados", None))

        self.lneBuscar_materias.setPlaceholderText(QCoreApplication.translate("gestion_materias", u"Busqueda por cualquier dato", None))
        self.lblIcon_conectado_como.setText("")
        self.lblConectado_como.setText(QCoreApplication.translate("gestion_materias", u"Conectado como: jorged", None))
        self.chkMostrar_inactivas_materias.setText(QCoreApplication.translate("gestion_materias", u"Mostrar inactivos", None))
        self.btnEditar_materia.setText(QCoreApplication.translate("gestion_materias", u"Editar", None))
        self.btnDesactivar_materia.setText(QCoreApplication.translate("gestion_materias", u"Desactivar", None))
    # retranslateUi

