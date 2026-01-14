# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Egresados.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableView, QToolButton,
    QWidget)
from resources import resources_ui

class Ui_Egresados(object):
    def setupUi(self, Egresados):
        if not Egresados.objectName():
            Egresados.setObjectName(u"Egresados")
        Egresados.resize(1111, 621)
        Egresados.setMinimumSize(QSize(1111, 621))
        Egresados.setStyleSheet(u"background-color: #f5f6fa;\n"
"color: #2d2d2d;")
        self.btnExportar_egresados = QToolButton(Egresados)
        self.btnExportar_egresados.setObjectName(u"btnExportar_egresados")
        self.btnExportar_egresados.setGeometry(QRect(160, 10, 120, 40))
        self.btnExportar_egresados.setMinimumSize(QSize(120, 40))
        self.btnExportar_egresados.setMaximumSize(QSize(120, 40))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(13)
        font.setBold(True)
        self.btnExportar_egresados.setFont(font)
        self.btnExportar_egresados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnExportar_egresados.setAutoFillBackground(False)
        self.btnExportar_egresados.setStyleSheet(u"QToolButton {\n"
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
        icon = QIcon()
        icon.addFile(u":/icons/exportar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExportar_egresados.setIcon(icon)
        self.btnExportar_egresados.setIconSize(QSize(20, 20))
        self.btnExportar_egresados.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.btnExportar_egresados.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.frameTabla_egresados = QFrame(Egresados)
        self.frameTabla_egresados.setObjectName(u"frameTabla_egresados")
        self.frameTabla_egresados.setGeometry(QRect(20, 110, 1061, 481))
        self.frameTabla_egresados.setMinimumSize(QSize(900, 450))
        self.frameTabla_egresados.setMaximumSize(QSize(16777215, 500))
        self.frameTabla_egresados.setStyleSheet(u"QFrame#frameTabla_egresados {\n"
"    border: 1px solid #d5dbdb;\n"
"    border-radius: 12px;\n"
"    background-color: white;\n"
"	border-radius: 10px\n"
"}")
        self.frameTabla_egresados.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTabla_egresados.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameTabla_egresados)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableW_egresados = QTableView(self.frameTabla_egresados)
        self.tableW_egresados.setObjectName(u"tableW_egresados")
        self.tableW_egresados.setStyleSheet(u"QTableView {\n"
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
        self.tableW_egresados.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableW_egresados.setAlternatingRowColors(True)
        self.tableW_egresados.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableW_egresados.setShowGrid(True)
        self.tableW_egresados.setSortingEnabled(True)

        self.horizontalLayout.addWidget(self.tableW_egresados)

        self.lblTitulo_egresados = QLabel(Egresados)
        self.lblTitulo_egresados.setObjectName(u"lblTitulo_egresados")
        self.lblTitulo_egresados.setGeometry(QRect(870, 0, 151, 81))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.lblTitulo_egresados.setFont(font1)
        self.lblTitulo_egresados.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblTitulo_egresados.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_egresados.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_egresados.setScaledContents(False)
        self.lblTitulo_egresados.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_egresados.setWordWrap(True)
        self.lblTitulo_egresados.setIndent(0)
        self.btnDetalles_egresados = QPushButton(Egresados)
        self.btnDetalles_egresados.setObjectName(u"btnDetalles_egresados")
        self.btnDetalles_egresados.setGeometry(QRect(20, 10, 120, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDetalles_egresados.sizePolicy().hasHeightForWidth())
        self.btnDetalles_egresados.setSizePolicy(sizePolicy)
        self.btnDetalles_egresados.setMinimumSize(QSize(120, 40))
        self.btnDetalles_egresados.setMaximumSize(QSize(120, 40))
        self.btnDetalles_egresados.setFont(font)
        self.btnDetalles_egresados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDetalles_egresados.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnDetalles_egresados.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/buscar2_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDetalles_egresados.setIcon(icon1)
        self.lneBuscar_egresados = QLineEdit(Egresados)
        self.lneBuscar_egresados.setObjectName(u"lneBuscar_egresados")
        self.lneBuscar_egresados.setGeometry(QRect(150, 60, 341, 35))
        self.lneBuscar_egresados.setMinimumSize(QSize(200, 35))
        self.lneBuscar_egresados.setMaximumSize(QSize(541, 35))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(13)
        self.lneBuscar_egresados.setFont(font2)
        self.lneBuscar_egresados.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneBuscar_egresados.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #848f9d;\n"
"	color: #2d2d2d;\n"
"    border-radius: 10px;\n"
"    padding: 1px 3px;\n"
"    background-color: white;\n"
"}")
        self.lneBuscar_egresados.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneBuscar_egresados.setClearButtonEnabled(True)
        self.lblLogo_egresados = QLabel(Egresados)
        self.lblLogo_egresados.setObjectName(u"lblLogo_egresados")
        self.lblLogo_egresados.setGeometry(QRect(1039, 10, 51, 61))
        self.lblLogo_egresados.setMinimumSize(QSize(50, 50))
        self.lblLogo_egresados.setMaximumSize(QSize(130, 70))
        self.lblLogo_egresados.setStyleSheet(u"background-color: transparent;")
        self.lblLogo_egresados.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_egresados.setScaledContents(True)
        self.frameFiltro_egresados = QFrame(Egresados)
        self.frameFiltro_egresados.setObjectName(u"frameFiltro_egresados")
        self.frameFiltro_egresados.setGeometry(QRect(20, 60, 151, 35))
        self.frameFiltro_egresados.setMinimumSize(QSize(100, 35))
        self.frameFiltro_egresados.setMaximumSize(QSize(200, 40))
        self.frameFiltro_egresados.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #2c3e50;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frameFiltro_egresados.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameFiltro_egresados.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxFiltro_egresados = QComboBox(self.frameFiltro_egresados)
        self.cbxFiltro_egresados.addItem("")
        self.cbxFiltro_egresados.addItem("")
        self.cbxFiltro_egresados.addItem("")
        self.cbxFiltro_egresados.addItem("")
        self.cbxFiltro_egresados.addItem("")
        self.cbxFiltro_egresados.addItem("")
        self.cbxFiltro_egresados.addItem("")
        self.cbxFiltro_egresados.addItem("")
        self.cbxFiltro_egresados.addItem("")
        self.cbxFiltro_egresados.addItem("")
        self.cbxFiltro_egresados.addItem("")
        self.cbxFiltro_egresados.addItem("")
        self.cbxFiltro_egresados.setObjectName(u"cbxFiltro_egresados")
        self.cbxFiltro_egresados.setGeometry(QRect(9, 5, 131, 25))
        self.cbxFiltro_egresados.setMaximumSize(QSize(180, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.cbxFiltro_egresados.setFont(font3)
        self.cbxFiltro_egresados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxFiltro_egresados.setStyleSheet(u"background-color: white;\n"
"border: transparent;")
        self.cbxFiltro_egresados.setIconSize(QSize(5, 5))
        self.line_2 = QFrame(Egresados)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(1029, 10, 3, 61))
        self.line_2.setMinimumSize(QSize(3, 61))
        self.line_2.setMaximumSize(QSize(3, 61))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblTotalRegistros_egresados = QLabel(Egresados)
        self.lblTotalRegistros_egresados.setObjectName(u"lblTotalRegistros_egresados")
        self.lblTotalRegistros_egresados.setGeometry(QRect(120, 590, 61, 31))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.lblTotalRegistros_egresados.setFont(font4)
        self.lblTotalRegistros_egresados.setStyleSheet(u"background-color: transparent;")
        self.lblTotalRegistros_egresados.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTotalRegistros_egresados.setWordWrap(True)
        self.lblTotalRegistros = QLabel(Egresados)
        self.lblTotalRegistros.setObjectName(u"lblTotalRegistros")
        self.lblTotalRegistros.setGeometry(QRect(20, 590, 111, 31))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.lblTotalRegistros.setFont(font5)
        self.lblTotalRegistros.setStyleSheet(u"background-color: transparent;")
        self.lblTotalRegistros.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTotalRegistros.setWordWrap(True)
        self.btnActualizar_db_egresados = QPushButton(Egresados)
        self.btnActualizar_db_egresados.setObjectName(u"btnActualizar_db_egresados")
        self.btnActualizar_db_egresados.setGeometry(QRect(300, 10, 141, 40))
        sizePolicy.setHeightForWidth(self.btnActualizar_db_egresados.sizePolicy().hasHeightForWidth())
        self.btnActualizar_db_egresados.setSizePolicy(sizePolicy)
        self.btnActualizar_db_egresados.setMinimumSize(QSize(120, 30))
        self.btnActualizar_db_egresados.setMaximumSize(QSize(150, 40))
        self.btnActualizar_db_egresados.setFont(font5)
        self.btnActualizar_db_egresados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnActualizar_db_egresados.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnActualizar_db_egresados.setStyleSheet(u"QPushButton {\n"
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
        self.btnActualizar_db_egresados.setIcon(icon2)

        self.retranslateUi(Egresados)

        QMetaObject.connectSlotsByName(Egresados)
    # setupUi

    def retranslateUi(self, Egresados):
        Egresados.setWindowTitle(QCoreApplication.translate("Egresados", u"Form", None))
        self.btnExportar_egresados.setText(QCoreApplication.translate("Egresados", u"Exportar", None))
        self.lblTitulo_egresados.setText(QCoreApplication.translate("Egresados", u"Historial de Egresados", None))
        self.btnDetalles_egresados.setText(QCoreApplication.translate("Egresados", u"Detalles", None))
        self.lneBuscar_egresados.setPlaceholderText(QCoreApplication.translate("Egresados", u"Busqueda por cualquier dato", None))
        self.lblLogo_egresados.setText("")
        self.cbxFiltro_egresados.setItemText(0, QCoreApplication.translate("Egresados", u"Todos", None))
        self.cbxFiltro_egresados.setItemText(1, QCoreApplication.translate("Egresados", u"C\u00e9dula", None))
        self.cbxFiltro_egresados.setItemText(2, QCoreApplication.translate("Egresados", u"Nombres", None))
        self.cbxFiltro_egresados.setItemText(3, QCoreApplication.translate("Egresados", u"Apellidos", None))
        self.cbxFiltro_egresados.setItemText(4, QCoreApplication.translate("Egresados", u"Fecha nac.", None))
        self.cbxFiltro_egresados.setItemText(5, QCoreApplication.translate("Egresados", u"Edad", None))
        self.cbxFiltro_egresados.setItemText(6, QCoreApplication.translate("Egresados", u"Ciudad", None))
        self.cbxFiltro_egresados.setItemText(7, QCoreApplication.translate("Egresados", u"G\u00e9nero", None))
        self.cbxFiltro_egresados.setItemText(8, QCoreApplication.translate("Egresados", u"Direcci\u00f3n", None))
        self.cbxFiltro_egresados.setItemText(9, QCoreApplication.translate("Egresados", u"Ult. Grado", None))
        self.cbxFiltro_egresados.setItemText(10, QCoreApplication.translate("Egresados", u"Ult. Seccion", None))
        self.cbxFiltro_egresados.setItemText(11, QCoreApplication.translate("Egresados", u"Fecha Egreso", None))

        self.lblTotalRegistros_egresados.setText(QCoreApplication.translate("Egresados", u"000", None))
        self.lblTotalRegistros.setText(QCoreApplication.translate("Egresados", u"Total egresados:", None))
        self.btnActualizar_db_egresados.setText(QCoreApplication.translate("Egresados", u"Actualizar tabla", None))
    # retranslateUi

