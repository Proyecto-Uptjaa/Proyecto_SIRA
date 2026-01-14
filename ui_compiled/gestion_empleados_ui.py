# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestion_empleados.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableView,
    QToolButton, QWidget)
from resources import resources_ui

class Ui_gestion_empleados(object):
    def setupUi(self, gestion_empleados):
        if not gestion_empleados.objectName():
            gestion_empleados.setObjectName(u"gestion_empleados")
        gestion_empleados.resize(1111, 621)
        gestion_empleados.setMinimumSize(QSize(1111, 621))
        gestion_empleados.setStyleSheet(u"background-color: #f5f6fa;\n"
"color: #2d2d2d;")
        self.lblTitulo_emple = QLabel(gestion_empleados)
        self.lblTitulo_emple.setObjectName(u"lblTitulo_emple")
        self.lblTitulo_emple.setGeometry(QRect(880, 0, 141, 81))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(19)
        font.setBold(True)
        self.lblTitulo_emple.setFont(font)
        self.lblTitulo_emple.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblTitulo_emple.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_emple.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_emple.setScaledContents(False)
        self.lblTitulo_emple.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_emple.setWordWrap(True)
        self.lblTitulo_emple.setIndent(0)
        self.btnEliminar_emple = QPushButton(gestion_empleados)
        self.btnEliminar_emple.setObjectName(u"btnEliminar_emple")
        self.btnEliminar_emple.setGeometry(QRect(440, 10, 120, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEliminar_emple.sizePolicy().hasHeightForWidth())
        self.btnEliminar_emple.setSizePolicy(sizePolicy)
        self.btnEliminar_emple.setMinimumSize(QSize(120, 40))
        self.btnEliminar_emple.setMaximumSize(QSize(120, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.btnEliminar_emple.setFont(font1)
        self.btnEliminar_emple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEliminar_emple.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnEliminar_emple.setStyleSheet(u"QPushButton {\n"
"  \n"
"	\n"
"	background-color: #e74c3c;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #C0392B\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/delete_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEliminar_emple.setIcon(icon)
        self.lneBuscar_emple = QLineEdit(gestion_empleados)
        self.lneBuscar_emple.setObjectName(u"lneBuscar_emple")
        self.lneBuscar_emple.setGeometry(QRect(150, 60, 341, 35))
        self.lneBuscar_emple.setMinimumSize(QSize(200, 35))
        self.lneBuscar_emple.setMaximumSize(QSize(541, 35))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(13)
        self.lneBuscar_emple.setFont(font2)
        self.lneBuscar_emple.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneBuscar_emple.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #848f9d;\n"
"	color: #2d2d2d;\n"
"    border-radius: 12px;\n"
"    padding: 1px 5px;\n"
"    background-color: white;\n"
"}")
        self.lneBuscar_emple.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneBuscar_emple.setClearButtonEnabled(True)
        self.lblLogo_emple = QLabel(gestion_empleados)
        self.lblLogo_emple.setObjectName(u"lblLogo_emple")
        self.lblLogo_emple.setGeometry(QRect(1039, 10, 51, 61))
        self.lblLogo_emple.setMinimumSize(QSize(50, 50))
        self.lblLogo_emple.setMaximumSize(QSize(130, 70))
        self.lblLogo_emple.setStyleSheet(u"background-color: transparent;")
        self.lblLogo_emple.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_emple.setScaledContents(True)
        self.chkMostrar_inactivos_emple = QCheckBox(gestion_empleados)
        self.chkMostrar_inactivos_emple.setObjectName(u"chkMostrar_inactivos_emple")
        self.chkMostrar_inactivos_emple.setGeometry(QRect(910, 590, 161, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        self.chkMostrar_inactivos_emple.setFont(font3)
        self.chkMostrar_inactivos_emple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chkMostrar_inactivos_emple.setStyleSheet(u"QCheckBox {\n"
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
        self.chkMostrar_inactivos_emple.setIconSize(QSize(20, 20))
        self.chkMostrar_inactivos_emple.setTristate(False)
        self.btnNuevo_emple = QPushButton(gestion_empleados)
        self.btnNuevo_emple.setObjectName(u"btnNuevo_emple")
        self.btnNuevo_emple.setGeometry(QRect(20, 10, 120, 40))
        sizePolicy.setHeightForWidth(self.btnNuevo_emple.sizePolicy().hasHeightForWidth())
        self.btnNuevo_emple.setSizePolicy(sizePolicy)
        self.btnNuevo_emple.setMinimumSize(QSize(120, 40))
        self.btnNuevo_emple.setMaximumSize(QSize(120, 40))
        self.btnNuevo_emple.setFont(font1)
        self.btnNuevo_emple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNuevo_emple.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnNuevo_emple.setStyleSheet(u"QPushButton {\n"
"  \n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 10px;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/nuevo_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNuevo_emple.setIcon(icon1)
        self.btnNuevo_emple.setIconSize(QSize(18, 18))
        self.line = QFrame(gestion_empleados)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(1029, 10, 3, 61))
        self.line.setMinimumSize(QSize(3, 61))
        self.line.setMaximumSize(QSize(3, 61))
        self.line.setStyleSheet(u"background-color: #2d2d2d;")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.btnExportar_emple = QToolButton(gestion_empleados)
        self.btnExportar_emple.setObjectName(u"btnExportar_emple")
        self.btnExportar_emple.setGeometry(QRect(300, 10, 120, 40))
        self.btnExportar_emple.setMinimumSize(QSize(120, 40))
        self.btnExportar_emple.setMaximumSize(QSize(120, 40))
        self.btnExportar_emple.setFont(font1)
        self.btnExportar_emple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnExportar_emple.setAutoFillBackground(False)
        self.btnExportar_emple.setStyleSheet(u"QToolButton {\n"
"   background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 7px;\n"
"    border-radius: 14px;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: #0D47A1;\n"
"}\n"
"\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/exportar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExportar_emple.setIcon(icon2)
        self.btnExportar_emple.setIconSize(QSize(20, 20))
        self.btnExportar_emple.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.btnExportar_emple.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.frameTabla_emple = QFrame(gestion_empleados)
        self.frameTabla_emple.setObjectName(u"frameTabla_emple")
        self.frameTabla_emple.setGeometry(QRect(20, 110, 1061, 481))
        self.frameTabla_emple.setMinimumSize(QSize(900, 450))
        self.frameTabla_emple.setMaximumSize(QSize(16777215, 500))
        self.frameTabla_emple.setStyleSheet(u"QFrame#frameTabla_emple {\n"
"    border: 1px solid #d5dbdb;\n"
"    border-radius: 12px;\n"
"    background-color: white;\n"
"}")
        self.frameTabla_emple.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTabla_emple.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameTabla_emple)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableW_emple = QTableView(self.frameTabla_emple)
        self.tableW_emple.setObjectName(u"tableW_emple")
        self.tableW_emple.setStyleSheet(u"QTableView {\n"
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
        self.tableW_emple.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableW_emple.setAlternatingRowColors(True)
        self.tableW_emple.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableW_emple.setShowGrid(True)
        self.tableW_emple.setSortingEnabled(True)

        self.horizontalLayout_2.addWidget(self.tableW_emple)

        self.btnDetalles_emple = QPushButton(gestion_empleados)
        self.btnDetalles_emple.setObjectName(u"btnDetalles_emple")
        self.btnDetalles_emple.setGeometry(QRect(160, 10, 120, 40))
        sizePolicy.setHeightForWidth(self.btnDetalles_emple.sizePolicy().hasHeightForWidth())
        self.btnDetalles_emple.setSizePolicy(sizePolicy)
        self.btnDetalles_emple.setMinimumSize(QSize(120, 40))
        self.btnDetalles_emple.setMaximumSize(QSize(120, 40))
        self.btnDetalles_emple.setFont(font1)
        self.btnDetalles_emple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDetalles_emple.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnDetalles_emple.setStyleSheet(u"QPushButton {\n"
"  \n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 8px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/buscar2_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDetalles_emple.setIcon(icon3)
        self.frameFiltro_estu_4 = QFrame(gestion_empleados)
        self.frameFiltro_estu_4.setObjectName(u"frameFiltro_estu_4")
        self.frameFiltro_estu_4.setGeometry(QRect(20, 60, 151, 35))
        self.frameFiltro_estu_4.setMinimumSize(QSize(100, 35))
        self.frameFiltro_estu_4.setMaximumSize(QSize(200, 40))
        self.frameFiltro_estu_4.setStyleSheet(u"QFrame{\n"
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
        self.frameFiltro_estu_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameFiltro_estu_4.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxFiltro_emple = QComboBox(self.frameFiltro_estu_4)
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.addItem("")
        self.cbxFiltro_emple.setObjectName(u"cbxFiltro_emple")
        self.cbxFiltro_emple.setGeometry(QRect(10, 5, 131, 25))
        self.cbxFiltro_emple.setMaximumSize(QSize(180, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.cbxFiltro_emple.setFont(font4)
        self.cbxFiltro_emple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxFiltro_emple.setStyleSheet(u"background-color: white;\n"
"border: transparent;")
        self.cbxFiltro_emple.setIconSize(QSize(5, 5))
        self.lblActivos_emple = QLabel(gestion_empleados)
        self.lblActivos_emple.setObjectName(u"lblActivos_emple")
        self.lblActivos_emple.setGeometry(QRect(300, 590, 61, 31))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(16)
        font5.setBold(True)
        self.lblActivos_emple.setFont(font5)
        self.lblActivos_emple.setStyleSheet(u"background-color: transparent;")
        self.lblActivos_emple.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblActivos_emple.setWordWrap(True)
        self.lblInactivos_emple = QLabel(gestion_empleados)
        self.lblInactivos_emple.setObjectName(u"lblInactivos_emple")
        self.lblInactivos_emple.setGeometry(QRect(480, 590, 61, 31))
        self.lblInactivos_emple.setFont(font5)
        self.lblInactivos_emple.setStyleSheet(u"background-color: transparent;")
        self.lblInactivos_emple.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblInactivos_emple.setWordWrap(True)
        self.lblTarjeta1_Titulo_9 = QLabel(gestion_empleados)
        self.lblTarjeta1_Titulo_9.setObjectName(u"lblTarjeta1_Titulo_9")
        self.lblTarjeta1_Titulo_9.setGeometry(QRect(200, 590, 111, 31))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.lblTarjeta1_Titulo_9.setFont(font6)
        self.lblTarjeta1_Titulo_9.setStyleSheet(u"background-color: transparent;")
        self.lblTarjeta1_Titulo_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTarjeta1_Titulo_9.setWordWrap(True)
        self.lblTarjeta1_Titulo_10 = QLabel(gestion_empleados)
        self.lblTarjeta1_Titulo_10.setObjectName(u"lblTarjeta1_Titulo_10")
        self.lblTarjeta1_Titulo_10.setGeometry(QRect(380, 590, 111, 31))
        self.lblTarjeta1_Titulo_10.setFont(font6)
        self.lblTarjeta1_Titulo_10.setStyleSheet(u"background-color: transparent;")
        self.lblTarjeta1_Titulo_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTarjeta1_Titulo_10.setWordWrap(True)
        self.lblTotalRegistros_emple = QLabel(gestion_empleados)
        self.lblTotalRegistros_emple.setObjectName(u"lblTotalRegistros_emple")
        self.lblTotalRegistros_emple.setGeometry(QRect(120, 590, 61, 31))
        self.lblTotalRegistros_emple.setFont(font5)
        self.lblTotalRegistros_emple.setStyleSheet(u"background-color: transparent;")
        self.lblTotalRegistros_emple.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTotalRegistros_emple.setWordWrap(True)
        self.lblTotalRegistros_2 = QLabel(gestion_empleados)
        self.lblTotalRegistros_2.setObjectName(u"lblTotalRegistros_2")
        self.lblTotalRegistros_2.setGeometry(QRect(20, 590, 111, 31))
        self.lblTotalRegistros_2.setFont(font6)
        self.lblTotalRegistros_2.setStyleSheet(u"background-color: transparent;")
        self.lblTotalRegistros_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTotalRegistros_2.setWordWrap(True)
        self.btnActualizar_db_emple = QPushButton(gestion_empleados)
        self.btnActualizar_db_emple.setObjectName(u"btnActualizar_db_emple")
        self.btnActualizar_db_emple.setGeometry(QRect(580, 10, 141, 40))
        sizePolicy.setHeightForWidth(self.btnActualizar_db_emple.sizePolicy().hasHeightForWidth())
        self.btnActualizar_db_emple.setSizePolicy(sizePolicy)
        self.btnActualizar_db_emple.setMinimumSize(QSize(120, 30))
        self.btnActualizar_db_emple.setMaximumSize(QSize(150, 40))
        self.btnActualizar_db_emple.setFont(font6)
        self.btnActualizar_db_emple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnActualizar_db_emple.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnActualizar_db_emple.setStyleSheet(u"QPushButton {\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/actualizar_b.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnActualizar_db_emple.setIcon(icon4)

        self.retranslateUi(gestion_empleados)

        QMetaObject.connectSlotsByName(gestion_empleados)
    # setupUi

    def retranslateUi(self, gestion_empleados):
        gestion_empleados.setWindowTitle(QCoreApplication.translate("gestion_empleados", u"Form", None))
        self.lblTitulo_emple.setText(QCoreApplication.translate("gestion_empleados", u"M\u00f3dulo de empleados", None))
        self.btnEliminar_emple.setText(QCoreApplication.translate("gestion_empleados", u"Eliminar", None))
        self.lneBuscar_emple.setPlaceholderText(QCoreApplication.translate("gestion_empleados", u"Busqueda por cualquier dato", None))
        self.lblLogo_emple.setText("")
        self.chkMostrar_inactivos_emple.setText(QCoreApplication.translate("gestion_empleados", u"Mostrar inactivos", None))
        self.btnNuevo_emple.setText(QCoreApplication.translate("gestion_empleados", u"Nuevo", None))
        self.btnExportar_emple.setText(QCoreApplication.translate("gestion_empleados", u"Exportar", None))
        self.btnDetalles_emple.setText(QCoreApplication.translate("gestion_empleados", u"Detalles", None))
        self.cbxFiltro_emple.setItemText(0, QCoreApplication.translate("gestion_empleados", u"Todos", None))
        self.cbxFiltro_emple.setItemText(1, QCoreApplication.translate("gestion_empleados", u"C\u00e9dula", None))
        self.cbxFiltro_emple.setItemText(2, QCoreApplication.translate("gestion_empleados", u"Nombres", None))
        self.cbxFiltro_emple.setItemText(3, QCoreApplication.translate("gestion_empleados", u"Apellidos", None))
        self.cbxFiltro_emple.setItemText(4, QCoreApplication.translate("gestion_empleados", u"Fecha nac.", None))
        self.cbxFiltro_emple.setItemText(5, QCoreApplication.translate("gestion_empleados", u"Edad", None))
        self.cbxFiltro_emple.setItemText(6, QCoreApplication.translate("gestion_empleados", u"G\u00e9nero", None))
        self.cbxFiltro_emple.setItemText(7, QCoreApplication.translate("gestion_empleados", u"Direcci\u00f3n", None))
        self.cbxFiltro_emple.setItemText(8, QCoreApplication.translate("gestion_empleados", u"Tel\u00e9fono", None))
        self.cbxFiltro_emple.setItemText(9, QCoreApplication.translate("gestion_empleados", u"Correo", None))
        self.cbxFiltro_emple.setItemText(10, QCoreApplication.translate("gestion_empleados", u"Titulo", None))
        self.cbxFiltro_emple.setItemText(11, QCoreApplication.translate("gestion_empleados", u"Cargo", None))
        self.cbxFiltro_emple.setItemText(12, QCoreApplication.translate("gestion_empleados", u"Fecha Ingreso", None))
        self.cbxFiltro_emple.setItemText(13, QCoreApplication.translate("gestion_empleados", u"Num. Carnet", None))
        self.cbxFiltro_emple.setItemText(14, QCoreApplication.translate("gestion_empleados", u"RIF", None))
        self.cbxFiltro_emple.setItemText(15, QCoreApplication.translate("gestion_empleados", u"Codigo RAC", None))

        self.lblActivos_emple.setText(QCoreApplication.translate("gestion_empleados", u"000", None))
        self.lblInactivos_emple.setText(QCoreApplication.translate("gestion_empleados", u"000", None))
        self.lblTarjeta1_Titulo_9.setText(QCoreApplication.translate("gestion_empleados", u"Total activos:", None))
        self.lblTarjeta1_Titulo_10.setText(QCoreApplication.translate("gestion_empleados", u"Total inactivos:", None))
        self.lblTotalRegistros_emple.setText(QCoreApplication.translate("gestion_empleados", u"000", None))
        self.lblTotalRegistros_2.setText(QCoreApplication.translate("gestion_empleados", u"Total registros:", None))
        self.btnActualizar_db_emple.setText(QCoreApplication.translate("gestion_empleados", u"Actualizar tabla", None))
    # retranslateUi

