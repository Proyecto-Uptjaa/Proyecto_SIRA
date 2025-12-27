# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestion_estudiantes.ui'
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

class Ui_gestion_estudiantes(object):
    def setupUi(self, gestion_estudiantes):
        if not gestion_estudiantes.objectName():
            gestion_estudiantes.setObjectName(u"gestion_estudiantes")
        gestion_estudiantes.resize(1111, 621)
        gestion_estudiantes.setMinimumSize(QSize(1111, 621))
        gestion_estudiantes.setStyleSheet(u"background-color: #f5f6fa;\n"
"color: #2d2d2d;")
        self.btnExportar_estu = QToolButton(gestion_estudiantes)
        self.btnExportar_estu.setObjectName(u"btnExportar_estu")
        self.btnExportar_estu.setGeometry(QRect(300, 10, 120, 40))
        self.btnExportar_estu.setMinimumSize(QSize(120, 40))
        self.btnExportar_estu.setMaximumSize(QSize(120, 40))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(13)
        font.setBold(True)
        self.btnExportar_estu.setFont(font)
        self.btnExportar_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnExportar_estu.setAutoFillBackground(False)
        self.btnExportar_estu.setStyleSheet(u"QToolButton {\n"
"   background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 7px;\n"
"    border-radius: 15px;\n"
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
        icon = QIcon()
        icon.addFile(u":/icons/exportar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExportar_estu.setIcon(icon)
        self.btnExportar_estu.setIconSize(QSize(20, 20))
        self.btnExportar_estu.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.btnExportar_estu.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.frameTabla_student = QFrame(gestion_estudiantes)
        self.frameTabla_student.setObjectName(u"frameTabla_student")
        self.frameTabla_student.setGeometry(QRect(20, 110, 1061, 481))
        self.frameTabla_student.setMinimumSize(QSize(900, 450))
        self.frameTabla_student.setMaximumSize(QSize(16777215, 500))
        self.frameTabla_student.setStyleSheet(u"QFrame#frameTabla_student {\n"
"    border: 1px solid #d5dbdb;\n"
"    border-radius: 12px;\n"
"    background-color: white;\n"
"}")
        self.frameTabla_student.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTabla_student.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameTabla_student)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableW_students = QTableView(self.frameTabla_student)
        self.tableW_students.setObjectName(u"tableW_students")
        self.tableW_students.setStyleSheet(u"QTableView {\n"
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
        self.tableW_students.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableW_students.setAlternatingRowColors(True)
        self.tableW_students.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableW_students.setShowGrid(True)
        self.tableW_students.setSortingEnabled(True)

        self.horizontalLayout.addWidget(self.tableW_students)

        self.lblTitulo_logo_estu = QLabel(gestion_estudiantes)
        self.lblTitulo_logo_estu.setObjectName(u"lblTitulo_logo_estu")
        self.lblTitulo_logo_estu.setGeometry(QRect(870, 10, 151, 61))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.lblTitulo_logo_estu.setFont(font1)
        self.lblTitulo_logo_estu.setStyleSheet(u"color: #2d2d2d")
        self.lblTitulo_logo_estu.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_logo_estu.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_logo_estu.setScaledContents(False)
        self.lblTitulo_logo_estu.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_logo_estu.setWordWrap(True)
        self.lblTitulo_logo_estu.setIndent(0)
        self.btnActualizar_db_estu = QPushButton(gestion_estudiantes)
        self.btnActualizar_db_estu.setObjectName(u"btnActualizar_db_estu")
        self.btnActualizar_db_estu.setGeometry(QRect(810, 30, 31, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnActualizar_db_estu.sizePolicy().hasHeightForWidth())
        self.btnActualizar_db_estu.setSizePolicy(sizePolicy)
        self.btnActualizar_db_estu.setMinimumSize(QSize(20, 20))
        self.btnActualizar_db_estu.setMaximumSize(QSize(150, 50))
        font2 = QFont()
        font2.setFamilies([u"Questrial"])
        font2.setBold(True)
        self.btnActualizar_db_estu.setFont(font2)
        self.btnActualizar_db_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnActualizar_db_estu.setMouseTracking(True)
        self.btnActualizar_db_estu.setTabletTracking(False)
        self.btnActualizar_db_estu.setAcceptDrops(False)
        self.btnActualizar_db_estu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnActualizar_db_estu.setAutoFillBackground(False)
        self.btnActualizar_db_estu.setStyleSheet(u"QPushButton {\n"
"   background-color: #7f8c8d;\n"
"    color: #F3F6FF;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"	font-family: \"Questrial\";\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:#5d6d7e;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/actualizar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnActualizar_db_estu.setIcon(icon1)
        self.btnActualizar_db_estu.setIconSize(QSize(60, 60))
        self.chkMostrar_inactivos_estu = QCheckBox(gestion_estudiantes)
        self.chkMostrar_inactivos_estu.setObjectName(u"chkMostrar_inactivos_estu")
        self.chkMostrar_inactivos_estu.setGeometry(QRect(910, 590, 171, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        self.chkMostrar_inactivos_estu.setFont(font3)
        self.chkMostrar_inactivos_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chkMostrar_inactivos_estu.setStyleSheet(u"QCheckBox {\n"
"    spacing: 8px;\n"
"    color: #2d2d2d;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 4px;\n"
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
        self.chkMostrar_inactivos_estu.setIconSize(QSize(20, 20))
        self.chkMostrar_inactivos_estu.setTristate(False)
        self.btnDetalles_students = QPushButton(gestion_estudiantes)
        self.btnDetalles_students.setObjectName(u"btnDetalles_students")
        self.btnDetalles_students.setGeometry(QRect(160, 10, 120, 40))
        sizePolicy.setHeightForWidth(self.btnDetalles_students.sizePolicy().hasHeightForWidth())
        self.btnDetalles_students.setSizePolicy(sizePolicy)
        self.btnDetalles_students.setMinimumSize(QSize(120, 40))
        self.btnDetalles_students.setMaximumSize(QSize(120, 40))
        self.btnDetalles_students.setFont(font)
        self.btnDetalles_students.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDetalles_students.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnDetalles_students.setStyleSheet(u"QPushButton {\n"
"  \n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 8px;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/buscar2_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDetalles_students.setIcon(icon2)
        self.btnEliminar_estudiante = QPushButton(gestion_estudiantes)
        self.btnEliminar_estudiante.setObjectName(u"btnEliminar_estudiante")
        self.btnEliminar_estudiante.setGeometry(QRect(440, 10, 120, 40))
        sizePolicy.setHeightForWidth(self.btnEliminar_estudiante.sizePolicy().hasHeightForWidth())
        self.btnEliminar_estudiante.setSizePolicy(sizePolicy)
        self.btnEliminar_estudiante.setMinimumSize(QSize(120, 40))
        self.btnEliminar_estudiante.setMaximumSize(QSize(120, 40))
        self.btnEliminar_estudiante.setFont(font)
        self.btnEliminar_estudiante.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEliminar_estudiante.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnEliminar_estudiante.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/eliminar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEliminar_estudiante.setIcon(icon3)
        self.lneBuscar_estu = QLineEdit(gestion_estudiantes)
        self.lneBuscar_estu.setObjectName(u"lneBuscar_estu")
        self.lneBuscar_estu.setGeometry(QRect(150, 60, 341, 35))
        self.lneBuscar_estu.setMinimumSize(QSize(200, 35))
        self.lneBuscar_estu.setMaximumSize(QSize(541, 35))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(13)
        self.lneBuscar_estu.setFont(font4)
        self.lneBuscar_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneBuscar_estu.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #848f9d;\n"
"	color: #2d2d2d;\n"
"    border-radius: 12px;\n"
"    padding: 1px 5px;\n"
"    background-color: white;\n"
"}")
        self.lneBuscar_estu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneBuscar_estu.setClearButtonEnabled(True)
        self.lblLogo_estu = QLabel(gestion_estudiantes)
        self.lblLogo_estu.setObjectName(u"lblLogo_estu")
        self.lblLogo_estu.setGeometry(QRect(1039, 10, 51, 61))
        self.lblLogo_estu.setMinimumSize(QSize(50, 50))
        self.lblLogo_estu.setMaximumSize(QSize(130, 70))
        self.lblLogo_estu.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_estu.setScaledContents(True)
        self.frameFiltro_estu = QFrame(gestion_estudiantes)
        self.frameFiltro_estu.setObjectName(u"frameFiltro_estu")
        self.frameFiltro_estu.setGeometry(QRect(20, 60, 151, 35))
        self.frameFiltro_estu.setMinimumSize(QSize(100, 35))
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
        self.cbxFiltro_estu = QComboBox(self.frameFiltro_estu)
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.addItem("")
        self.cbxFiltro_estu.setObjectName(u"cbxFiltro_estu")
        self.cbxFiltro_estu.setGeometry(QRect(9, 5, 131, 25))
        self.cbxFiltro_estu.setMaximumSize(QSize(180, 30))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(11)
        font5.setBold(True)
        self.cbxFiltro_estu.setFont(font5)
        self.cbxFiltro_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxFiltro_estu.setStyleSheet(u"background-color: white;\n"
"border: transparent;")
        self.cbxFiltro_estu.setIconSize(QSize(5, 5))
        self.line_2 = QFrame(gestion_estudiantes)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(1029, 10, 3, 61))
        self.line_2.setMinimumSize(QSize(3, 61))
        self.line_2.setMaximumSize(QSize(3, 61))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.btnNuevo_students = QPushButton(gestion_estudiantes)
        self.btnNuevo_students.setObjectName(u"btnNuevo_students")
        self.btnNuevo_students.setGeometry(QRect(20, 10, 120, 40))
        sizePolicy.setHeightForWidth(self.btnNuevo_students.sizePolicy().hasHeightForWidth())
        self.btnNuevo_students.setSizePolicy(sizePolicy)
        self.btnNuevo_students.setMinimumSize(QSize(120, 40))
        self.btnNuevo_students.setMaximumSize(QSize(120, 40))
        self.btnNuevo_students.setFont(font)
        self.btnNuevo_students.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNuevo_students.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnNuevo_students.setStyleSheet(u"QPushButton {\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/nuevo_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNuevo_students.setIcon(icon4)
        self.btnNuevo_students.setIconSize(QSize(18, 18))
        self.lblInactivos_estu = QLabel(gestion_estudiantes)
        self.lblInactivos_estu.setObjectName(u"lblInactivos_estu")
        self.lblInactivos_estu.setGeometry(QRect(480, 590, 61, 31))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(16)
        font6.setBold(True)
        self.lblInactivos_estu.setFont(font6)
        self.lblInactivos_estu.setStyleSheet(u"background-color: transparent;")
        self.lblInactivos_estu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblInactivos_estu.setWordWrap(True)
        self.lblActivos_estu = QLabel(gestion_estudiantes)
        self.lblActivos_estu.setObjectName(u"lblActivos_estu")
        self.lblActivos_estu.setGeometry(QRect(310, 590, 61, 31))
        self.lblActivos_estu.setFont(font6)
        self.lblActivos_estu.setStyleSheet(u"background-color: transparent;")
        self.lblActivos_estu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblActivos_estu.setWordWrap(True)
        self.lblTarjeta1_Titulo_8 = QLabel(gestion_estudiantes)
        self.lblTarjeta1_Titulo_8.setObjectName(u"lblTarjeta1_Titulo_8")
        self.lblTarjeta1_Titulo_8.setGeometry(QRect(380, 590, 111, 31))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(10)
        font7.setBold(True)
        self.lblTarjeta1_Titulo_8.setFont(font7)
        self.lblTarjeta1_Titulo_8.setStyleSheet(u"background-color: transparent;")
        self.lblTarjeta1_Titulo_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTarjeta1_Titulo_8.setWordWrap(True)
        self.lblTotalRegistros_estu = QLabel(gestion_estudiantes)
        self.lblTotalRegistros_estu.setObjectName(u"lblTotalRegistros_estu")
        self.lblTotalRegistros_estu.setGeometry(QRect(120, 590, 61, 31))
        self.lblTotalRegistros_estu.setFont(font6)
        self.lblTotalRegistros_estu.setStyleSheet(u"background-color: transparent;")
        self.lblTotalRegistros_estu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTotalRegistros_estu.setWordWrap(True)
        self.lblTarjeta1_Titulo_7 = QLabel(gestion_estudiantes)
        self.lblTarjeta1_Titulo_7.setObjectName(u"lblTarjeta1_Titulo_7")
        self.lblTarjeta1_Titulo_7.setGeometry(QRect(210, 590, 111, 31))
        self.lblTarjeta1_Titulo_7.setFont(font7)
        self.lblTarjeta1_Titulo_7.setStyleSheet(u"background-color: transparent;")
        self.lblTarjeta1_Titulo_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTarjeta1_Titulo_7.setWordWrap(True)
        self.lblTotalRegistros = QLabel(gestion_estudiantes)
        self.lblTotalRegistros.setObjectName(u"lblTotalRegistros")
        self.lblTotalRegistros.setGeometry(QRect(20, 590, 111, 31))
        self.lblTotalRegistros.setFont(font7)
        self.lblTotalRegistros.setStyleSheet(u"background-color: transparent;")
        self.lblTotalRegistros.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTotalRegistros.setWordWrap(True)

        self.retranslateUi(gestion_estudiantes)

        QMetaObject.connectSlotsByName(gestion_estudiantes)
    # setupUi

    def retranslateUi(self, gestion_estudiantes):
        gestion_estudiantes.setWindowTitle(QCoreApplication.translate("gestion_estudiantes", u"Form", None))
        self.btnExportar_estu.setText(QCoreApplication.translate("gestion_estudiantes", u"Exportar", None))
        self.lblTitulo_logo_estu.setText(QCoreApplication.translate("gestion_estudiantes", u"M\u00f3dulo de estudiantes", None))
        self.btnActualizar_db_estu.setText("")
        self.chkMostrar_inactivos_estu.setText(QCoreApplication.translate("gestion_estudiantes", u"Mostrar inactivos", None))
        self.btnDetalles_students.setText(QCoreApplication.translate("gestion_estudiantes", u"Detalles", None))
        self.btnEliminar_estudiante.setText(QCoreApplication.translate("gestion_estudiantes", u"Eliminar", None))
        self.lneBuscar_estu.setPlaceholderText(QCoreApplication.translate("gestion_estudiantes", u"Busqueda por cualquier dato", None))
        self.lblLogo_estu.setText("")
        self.cbxFiltro_estu.setItemText(0, QCoreApplication.translate("gestion_estudiantes", u"Todos", None))
        self.cbxFiltro_estu.setItemText(1, QCoreApplication.translate("gestion_estudiantes", u"C\u00e9dula", None))
        self.cbxFiltro_estu.setItemText(2, QCoreApplication.translate("gestion_estudiantes", u"Nombres", None))
        self.cbxFiltro_estu.setItemText(3, QCoreApplication.translate("gestion_estudiantes", u"Apellidos", None))
        self.cbxFiltro_estu.setItemText(4, QCoreApplication.translate("gestion_estudiantes", u"Fecha nac.", None))
        self.cbxFiltro_estu.setItemText(5, QCoreApplication.translate("gestion_estudiantes", u"Edad", None))
        self.cbxFiltro_estu.setItemText(6, QCoreApplication.translate("gestion_estudiantes", u"Ciudad", None))
        self.cbxFiltro_estu.setItemText(7, QCoreApplication.translate("gestion_estudiantes", u"G\u00e9nero", None))
        self.cbxFiltro_estu.setItemText(8, QCoreApplication.translate("gestion_estudiantes", u"Direcci\u00f3n", None))
        self.cbxFiltro_estu.setItemText(9, QCoreApplication.translate("gestion_estudiantes", u"Tipo Educ.", None))
        self.cbxFiltro_estu.setItemText(10, QCoreApplication.translate("gestion_estudiantes", u"Grado", None))
        self.cbxFiltro_estu.setItemText(11, QCoreApplication.translate("gestion_estudiantes", u"Secci\u00f3n", None))
        self.cbxFiltro_estu.setItemText(12, QCoreApplication.translate("gestion_estudiantes", u"Docente", None))
        self.cbxFiltro_estu.setItemText(13, QCoreApplication.translate("gestion_estudiantes", u"TallaC", None))
        self.cbxFiltro_estu.setItemText(14, QCoreApplication.translate("gestion_estudiantes", u"TallaP", None))
        self.cbxFiltro_estu.setItemText(15, QCoreApplication.translate("gestion_estudiantes", u"TallaZ", None))

        self.btnNuevo_students.setText(QCoreApplication.translate("gestion_estudiantes", u"Nuevo", None))
        self.lblInactivos_estu.setText(QCoreApplication.translate("gestion_estudiantes", u"000", None))
        self.lblActivos_estu.setText(QCoreApplication.translate("gestion_estudiantes", u"000", None))
        self.lblTarjeta1_Titulo_8.setText(QCoreApplication.translate("gestion_estudiantes", u"Total inactivos:", None))
        self.lblTotalRegistros_estu.setText(QCoreApplication.translate("gestion_estudiantes", u"000", None))
        self.lblTarjeta1_Titulo_7.setText(QCoreApplication.translate("gestion_estudiantes", u"Total activos:", None))
        self.lblTotalRegistros.setText(QCoreApplication.translate("gestion_estudiantes", u"Total registros:", None))
    # retranslateUi

