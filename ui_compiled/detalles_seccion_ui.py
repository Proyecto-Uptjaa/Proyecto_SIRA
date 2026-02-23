# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detalles_seccion.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableView, QWidget)
from resources import resources_ui

class Ui_detalle_seccion(object):
    def setupUi(self, detalle_seccion):
        if not detalle_seccion.objectName():
            detalle_seccion.setObjectName(u"detalle_seccion")
        detalle_seccion.resize(636, 595)
        detalle_seccion.setMinimumSize(QSize(636, 595))
        detalle_seccion.setMaximumSize(QSize(636, 595))
        detalle_seccion.setStyleSheet(u"background-color: #f5f6fa;")
        self.gridLayout = QGridLayout(detalle_seccion)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(detalle_seccion)
        self.widget.setObjectName(u"widget")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"QWidget{\n"
"background-color: #f5f6fa;\n"
"color: #2d2d2d;\n"
"}\n"
"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 3px 3px;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 2px 10px;\n"
"    background-color: white;\n"
"	color: #2d2d2d;\n"
"}")
        self.btnMover_estudiante = QPushButton(self.widget)
        self.btnMover_estudiante.setObjectName(u"btnMover_estudiante")
        self.btnMover_estudiante.setGeometry(QRect(440, 530, 150, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMover_estudiante.sizePolicy().hasHeightForWidth())
        self.btnMover_estudiante.setSizePolicy(sizePolicy)
        self.btnMover_estudiante.setMinimumSize(QSize(120, 40))
        self.btnMover_estudiante.setMaximumSize(QSize(200, 60))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.btnMover_estudiante.setFont(font1)
        self.btnMover_estudiante.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMover_estudiante.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnMover_estudiante.setStyleSheet(u"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 6px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/mover_estu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMover_estudiante.setIcon(icon)
        self.btnMover_estudiante.setIconSize(QSize(18, 18))
        self.lblLogo_detalle_seccion = QLabel(self.widget)
        self.lblLogo_detalle_seccion.setObjectName(u"lblLogo_detalle_seccion")
        self.lblLogo_detalle_seccion.setGeometry(QRect(560, 0, 45, 51))
        self.lblLogo_detalle_seccion.setMinimumSize(QSize(40, 50))
        self.lblLogo_detalle_seccion.setMaximumSize(QSize(130, 70))
        self.lblLogo_detalle_seccion.setStyleSheet(u"background-color: transparent;")
        self.lblLogo_detalle_seccion.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_detalle_seccion.setScaledContents(True)
        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(549, 0, 3, 51))
        self.line_2.setMinimumSize(QSize(3, 51))
        self.line_2.setMaximumSize(QSize(3, 61))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblTitulo_detalle_seccion = QLabel(self.widget)
        self.lblTitulo_detalle_seccion.setObjectName(u"lblTitulo_detalle_seccion")
        self.lblTitulo_detalle_seccion.setGeometry(QRect(411, 0, 131, 51))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.lblTitulo_detalle_seccion.setFont(font2)
        self.lblTitulo_detalle_seccion.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblTitulo_detalle_seccion.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_detalle_seccion.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_detalle_seccion.setScaledContents(False)
        self.lblTitulo_detalle_seccion.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_detalle_seccion.setWordWrap(True)
        self.lblTitulo_detalle_seccion.setIndent(0)
        self.frameTabla_seccion = QFrame(self.widget)
        self.frameTabla_seccion.setObjectName(u"frameTabla_seccion")
        self.frameTabla_seccion.setGeometry(QRect(20, 110, 571, 411))
        self.frameTabla_seccion.setMinimumSize(QSize(550, 300))
        self.frameTabla_seccion.setMaximumSize(QSize(950, 500))
        self.frameTabla_seccion.setStyleSheet(u"QFrame#frameTabla_seccion {\n"
"    border: 1px solid #d5dbdb;\n"
"    border-radius: 16px;\n"
"    background-color: white;\n"
"}")
        self.frameTabla_seccion.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTabla_seccion.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameTabla_seccion)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableW_seccion = QTableView(self.frameTabla_seccion)
        self.tableW_seccion.setObjectName(u"tableW_seccion")
        self.tableW_seccion.setStyleSheet(u"QTableView {\n"
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
        self.tableW_seccion.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableW_seccion.setAlternatingRowColors(True)
        self.tableW_seccion.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableW_seccion.setShowGrid(True)
        self.tableW_seccion.setSortingEnabled(True)

        self.horizontalLayout.addWidget(self.tableW_seccion)

        self.frameFiltro_estu = QFrame(self.widget)
        self.frameFiltro_estu.setObjectName(u"frameFiltro_estu")
        self.frameFiltro_estu.setGeometry(QRect(20, 70, 151, 35))
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
        self.cbxFiltro_detalle_seccion = QComboBox(self.frameFiltro_estu)
        self.cbxFiltro_detalle_seccion.addItem("")
        self.cbxFiltro_detalle_seccion.addItem("")
        self.cbxFiltro_detalle_seccion.addItem("")
        self.cbxFiltro_detalle_seccion.addItem("")
        self.cbxFiltro_detalle_seccion.addItem("")
        self.cbxFiltro_detalle_seccion.addItem("")
        self.cbxFiltro_detalle_seccion.setObjectName(u"cbxFiltro_detalle_seccion")
        self.cbxFiltro_detalle_seccion.setGeometry(QRect(9, 5, 131, 25))
        self.cbxFiltro_detalle_seccion.setMaximumSize(QSize(180, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.cbxFiltro_detalle_seccion.setFont(font3)
        self.cbxFiltro_detalle_seccion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxFiltro_detalle_seccion.setStyleSheet(u"QComboBox {\n"
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
        self.cbxFiltro_detalle_seccion.setIconSize(QSize(5, 5))
        self.lneBuscar_detalle_seccion = QLineEdit(self.widget)
        self.lneBuscar_detalle_seccion.setObjectName(u"lneBuscar_detalle_seccion")
        self.lneBuscar_detalle_seccion.setGeometry(QRect(150, 70, 331, 35))
        self.lneBuscar_detalle_seccion.setMinimumSize(QSize(200, 35))
        self.lneBuscar_detalle_seccion.setMaximumSize(QSize(541, 35))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(13)
        self.lneBuscar_detalle_seccion.setFont(font4)
        self.lneBuscar_detalle_seccion.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneBuscar_detalle_seccion.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #848f9d;\n"
"	color: #2d2d2d;\n"
"    border-radius: 12px;\n"
"    padding: 1px 5px;\n"
"    background-color: white;\n"
"}")
        self.lneBuscar_detalle_seccion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneBuscar_detalle_seccion.setClearButtonEnabled(True)
        self.lblCedula_registro_estudiante = QLabel(self.widget)
        self.lblCedula_registro_estudiante.setObjectName(u"lblCedula_registro_estudiante")
        self.lblCedula_registro_estudiante.setGeometry(QRect(10, 10, 91, 50))
        self.lblCedula_registro_estudiante.setMinimumSize(QSize(0, 50))
        self.lblCedula_registro_estudiante.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.lblCedula_registro_estudiante.setFont(font5)
        self.lblCedula_registro_estudiante.setStyleSheet(u"color: #2d2d2d;\n"
"border: 1px solid transparent;\n"
"border-radius: 10px;\n"
"background-color: transparent;")
        self.lblCedula_registro_estudiante.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblCedula_registro_estudiante.setWordWrap(True)
        self.btnDesactivar_seccion = QPushButton(self.widget)
        self.btnDesactivar_seccion.setObjectName(u"btnDesactivar_seccion")
        self.btnDesactivar_seccion.setGeometry(QRect(20, 530, 131, 40))
        sizePolicy.setHeightForWidth(self.btnDesactivar_seccion.sizePolicy().hasHeightForWidth())
        self.btnDesactivar_seccion.setSizePolicy(sizePolicy)
        self.btnDesactivar_seccion.setMinimumSize(QSize(120, 40))
        self.btnDesactivar_seccion.setMaximumSize(QSize(200, 40))
        self.btnDesactivar_seccion.setFont(font1)
        self.btnDesactivar_seccion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDesactivar_seccion.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnDesactivar_seccion.setStyleSheet(u"QPushButton {\n"
"	background-color: #e74c3c;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 3px 3px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #C0392B\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/cancelar_w2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDesactivar_seccion.setIcon(icon1)
        self.btnDesactivar_seccion.setIconSize(QSize(18, 18))
        self.lblTarjeta1_Titulo_7 = QLabel(self.widget)
        self.lblTarjeta1_Titulo_7.setObjectName(u"lblTarjeta1_Titulo_7")
        self.lblTarjeta1_Titulo_7.setGeometry(QRect(480, 70, 71, 31))
        self.lblTarjeta1_Titulo_7.setFont(font1)
        self.lblTarjeta1_Titulo_7.setStyleSheet(u"background-color: transparent;")
        self.lblTarjeta1_Titulo_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTarjeta1_Titulo_7.setWordWrap(True)
        self.lblActivos_seccion = QLabel(self.widget)
        self.lblActivos_seccion.setObjectName(u"lblActivos_seccion")
        self.lblActivos_seccion.setGeometry(QRect(540, 70, 61, 31))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(16)
        font6.setBold(True)
        self.lblActivos_seccion.setFont(font6)
        self.lblActivos_seccion.setStyleSheet(u"")
        self.lblActivos_seccion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblActivos_seccion.setWordWrap(True)
        self.btnCambiar_docente = QPushButton(self.widget)
        self.btnCambiar_docente.setObjectName(u"btnCambiar_docente")
        self.btnCambiar_docente.setGeometry(QRect(370, 20, 30, 30))
        sizePolicy.setHeightForWidth(self.btnCambiar_docente.sizePolicy().hasHeightForWidth())
        self.btnCambiar_docente.setSizePolicy(sizePolicy)
        self.btnCambiar_docente.setMinimumSize(QSize(30, 30))
        self.btnCambiar_docente.setMaximumSize(QSize(30, 30))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(13)
        font7.setBold(True)
        self.btnCambiar_docente.setFont(font7)
        self.btnCambiar_docente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCambiar_docente.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnCambiar_docente.setStyleSheet(u"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 10px;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/edit_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCambiar_docente.setIcon(icon2)
        self.btnCambiar_docente.setIconSize(QSize(20, 20))
        self.frameDocente_seccion = QFrame(self.widget)
        self.frameDocente_seccion.setObjectName(u"frameDocente_seccion")
        self.frameDocente_seccion.setGeometry(QRect(110, 20, 251, 30))
        self.frameDocente_seccion.setMinimumSize(QSize(251, 30))
        self.frameDocente_seccion.setMaximumSize(QSize(251, 30))
        self.frameDocente_seccion.setStyleSheet(u"QFrame{\n"
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
        self.frameDocente_seccion.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameDocente_seccion.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxDocente_seccion = QComboBox(self.frameDocente_seccion)
        self.cbxDocente_seccion.setObjectName(u"cbxDocente_seccion")
        self.cbxDocente_seccion.setGeometry(QRect(5, 3, 240, 23))
        self.cbxDocente_seccion.setMaximumSize(QSize(249, 28))
        self.cbxDocente_seccion.setFont(font3)
        self.cbxDocente_seccion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxDocente_seccion.setStyleSheet(u"QComboBox {\n"
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
        self.cbxDocente_seccion.setIconSize(QSize(5, 5))
        self.btnExportar_listado = QPushButton(self.widget)
        self.btnExportar_listado.setObjectName(u"btnExportar_listado")
        self.btnExportar_listado.setGeometry(QRect(160, 530, 110, 40))
        sizePolicy.setHeightForWidth(self.btnExportar_listado.sizePolicy().hasHeightForWidth())
        self.btnExportar_listado.setSizePolicy(sizePolicy)
        self.btnExportar_listado.setMinimumSize(QSize(100, 40))
        self.btnExportar_listado.setMaximumSize(QSize(200, 60))
        self.btnExportar_listado.setFont(font1)
        self.btnExportar_listado.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnExportar_listado.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnExportar_listado.setStyleSheet(u"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 6px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/pdf_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExportar_listado.setIcon(icon3)
        self.btnExportar_listado.setIconSize(QSize(18, 18))
        self.btnGestionar_materias = QPushButton(self.widget)
        self.btnGestionar_materias.setObjectName(u"btnGestionar_materias")
        self.btnGestionar_materias.setGeometry(QRect(280, 530, 151, 40))
        sizePolicy.setHeightForWidth(self.btnGestionar_materias.sizePolicy().hasHeightForWidth())
        self.btnGestionar_materias.setSizePolicy(sizePolicy)
        self.btnGestionar_materias.setMinimumSize(QSize(130, 35))
        self.btnGestionar_materias.setMaximumSize(QSize(225, 40))
        self.btnGestionar_materias.setFont(font1)
        self.btnGestionar_materias.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGestionar_materias.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnGestionar_materias.setStyleSheet(u"QPushButton {\n"
"	background-color: #27ae60;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 6px 6px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 124, 70);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/materias_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGestionar_materias.setIcon(icon4)
        self.btnGestionar_materias.setIconSize(QSize(16, 16))
        self.btnMover_estudiante.raise_()
        self.lblLogo_detalle_seccion.raise_()
        self.line_2.raise_()
        self.lblTitulo_detalle_seccion.raise_()
        self.frameTabla_seccion.raise_()
        self.lneBuscar_detalle_seccion.raise_()
        self.frameFiltro_estu.raise_()
        self.lblCedula_registro_estudiante.raise_()
        self.btnDesactivar_seccion.raise_()
        self.lblTarjeta1_Titulo_7.raise_()
        self.lblActivos_seccion.raise_()
        self.btnCambiar_docente.raise_()
        self.frameDocente_seccion.raise_()
        self.btnExportar_listado.raise_()
        self.btnGestionar_materias.raise_()

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(detalle_seccion)

        QMetaObject.connectSlotsByName(detalle_seccion)
    # setupUi

    def retranslateUi(self, detalle_seccion):
        detalle_seccion.setWindowTitle(QCoreApplication.translate("detalle_seccion", u"Dialog", None))
        self.btnMover_estudiante.setText(QCoreApplication.translate("detalle_seccion", u"Mover estudiante", None))
        self.lblLogo_detalle_seccion.setText("")
        self.lblTitulo_detalle_seccion.setText(QCoreApplication.translate("detalle_seccion", u"Seccion X", None))
        self.cbxFiltro_detalle_seccion.setItemText(0, QCoreApplication.translate("detalle_seccion", u"Todos", None))
        self.cbxFiltro_detalle_seccion.setItemText(1, QCoreApplication.translate("detalle_seccion", u"C\u00e9dula", None))
        self.cbxFiltro_detalle_seccion.setItemText(2, QCoreApplication.translate("detalle_seccion", u"Nombres", None))
        self.cbxFiltro_detalle_seccion.setItemText(3, QCoreApplication.translate("detalle_seccion", u"Apellidos", None))
        self.cbxFiltro_detalle_seccion.setItemText(4, QCoreApplication.translate("detalle_seccion", u"Edad", None))
        self.cbxFiltro_detalle_seccion.setItemText(5, QCoreApplication.translate("detalle_seccion", u"G\u00e9nero", None))

        self.lneBuscar_detalle_seccion.setPlaceholderText(QCoreApplication.translate("detalle_seccion", u"Busqueda por cualquier dato", None))
        self.lblCedula_registro_estudiante.setText(QCoreApplication.translate("detalle_seccion", u"Docente", None))
        self.btnDesactivar_seccion.setText(QCoreApplication.translate("detalle_seccion", u"Desact. secci\u00f3n", None))
        self.lblTarjeta1_Titulo_7.setText(QCoreApplication.translate("detalle_seccion", u"Total activos:", None))
        self.lblActivos_seccion.setText(QCoreApplication.translate("detalle_seccion", u"000", None))
        self.btnCambiar_docente.setText("")
        self.btnExportar_listado.setText(QCoreApplication.translate("detalle_seccion", u"Listado PDF", None))
        self.btnGestionar_materias.setText(QCoreApplication.translate("detalle_seccion", u"Gestionar materias", None))
    # retranslateUi

