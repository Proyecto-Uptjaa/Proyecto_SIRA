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
from resources import resources_ui

class Ui_detalle_seccion(object):
    def setupUi(self, detalle_seccion):
        if not detalle_seccion.objectName():
            detalle_seccion.setObjectName(u"detalle_seccion")
        detalle_seccion.resize(636, 650)
        detalle_seccion.setMinimumSize(QSize(636, 650))
        detalle_seccion.setMaximumSize(QSize(636, 650))
        detalle_seccion.setStyleSheet(u"background-color: #f5f6fa;")
        self.gridLayout = QGridLayout(detalle_seccion)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(detalle_seccion)
        self.widget.setObjectName(u"widget")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"QWidget{\n"
"font-family: \"Segoe UI\";\n"
"background-color: #f5f6fa;\n"
"color: #2d2d2d;\n"
"}\n"
"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 10px;\n"
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
        self.btnMover_estudiante.setGeometry(QRect(419, 570, 171, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMover_estudiante.sizePolicy().hasHeightForWidth())
        self.btnMover_estudiante.setSizePolicy(sizePolicy)
        self.btnMover_estudiante.setMinimumSize(QSize(120, 40))
        self.btnMover_estudiante.setMaximumSize(QSize(200, 60))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.btnMover_estudiante.setFont(font1)
        self.btnMover_estudiante.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMover_estudiante.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnMover_estudiante.setStyleSheet(u"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 10px;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        self.btnMover_estudiante.setIconSize(QSize(20, 20))
        self.lblLogo_estu = QLabel(self.widget)
        self.lblLogo_estu.setObjectName(u"lblLogo_estu")
        self.lblLogo_estu.setGeometry(QRect(560, 10, 50, 61))
        self.lblLogo_estu.setMinimumSize(QSize(50, 50))
        self.lblLogo_estu.setMaximumSize(QSize(130, 70))
        self.lblLogo_estu.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_estu.setScaledContents(True)
        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(549, 10, 3, 61))
        self.line_2.setMinimumSize(QSize(3, 61))
        self.line_2.setMaximumSize(QSize(3, 61))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblTitulo_detalle_seccion = QLabel(self.widget)
        self.lblTitulo_detalle_seccion.setObjectName(u"lblTitulo_detalle_seccion")
        self.lblTitulo_detalle_seccion.setGeometry(QRect(411, 10, 131, 61))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(19)
        font2.setBold(True)
        self.lblTitulo_detalle_seccion.setFont(font2)
        self.lblTitulo_detalle_seccion.setStyleSheet(u"color: #2d2d2d")
        self.lblTitulo_detalle_seccion.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_detalle_seccion.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_detalle_seccion.setScaledContents(False)
        self.lblTitulo_detalle_seccion.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_detalle_seccion.setWordWrap(True)
        self.lblTitulo_detalle_seccion.setIndent(0)
        self.frameTabla_seccion = QFrame(self.widget)
        self.frameTabla_seccion.setObjectName(u"frameTabla_seccion")
        self.frameTabla_seccion.setGeometry(QRect(20, 130, 571, 431))
        self.frameTabla_seccion.setMinimumSize(QSize(550, 300))
        self.frameTabla_seccion.setMaximumSize(QSize(950, 500))
        self.frameTabla_seccion.setStyleSheet(u"QFrame#frameTabla_seccion {\n"
"    border: 1px solid #d5dbdb;\n"
"    border-radius: 12px;\n"
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
        self.frameFiltro_estu.setGeometry(QRect(20, 90, 151, 35))
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
        self.cbxFiltro_detalle_seccion.setStyleSheet(u"background-color: white;\n"
"border: transparent;")
        self.cbxFiltro_detalle_seccion.setIconSize(QSize(5, 5))
        self.lneBuscar_detalle_seccion = QLineEdit(self.widget)
        self.lneBuscar_detalle_seccion.setObjectName(u"lneBuscar_detalle_seccion")
        self.lneBuscar_detalle_seccion.setGeometry(QRect(150, 90, 331, 35))
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
"    padding: 1px 9px;\n"
"    background-color: white;\n"
"}")
        self.lneBuscar_detalle_seccion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneBuscar_detalle_seccion.setClearButtonEnabled(True)
        self.lneDocente_seccion = QLineEdit(self.widget)
        self.lneDocente_seccion.setObjectName(u"lneDocente_seccion")
        self.lneDocente_seccion.setGeometry(QRect(100, 20, 251, 31))
        self.lneDocente_seccion.setMinimumSize(QSize(200, 30))
        self.lneDocente_seccion.setMaximumSize(QSize(300, 50))
        self.lneDocente_seccion.setFont(font)
        self.lneDocente_seccion.setStyleSheet(u"")
        self.lneDocente_seccion.setMaxLength(15)
        self.lneDocente_seccion.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneDocente_seccion.setReadOnly(True)
        self.lneDocente_seccion.setClearButtonEnabled(True)
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
        self.btnDesactivar_seccion.setGeometry(QRect(219, 580, 191, 40))
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
"    padding: 8px 8px;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #C0392B\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/eliminar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDesactivar_seccion.setIcon(icon)
        self.lblTarjeta1_Titulo_7 = QLabel(self.widget)
        self.lblTarjeta1_Titulo_7.setObjectName(u"lblTarjeta1_Titulo_7")
        self.lblTarjeta1_Titulo_7.setGeometry(QRect(20, 570, 111, 31))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.lblTarjeta1_Titulo_7.setFont(font6)
        self.lblTarjeta1_Titulo_7.setStyleSheet(u"")
        self.lblTarjeta1_Titulo_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTarjeta1_Titulo_7.setWordWrap(True)
        self.lblActivos_seccion = QLabel(self.widget)
        self.lblActivos_seccion.setObjectName(u"lblActivos_seccion")
        self.lblActivos_seccion.setGeometry(QRect(120, 570, 61, 31))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(16)
        font7.setBold(True)
        self.lblActivos_seccion.setFont(font7)
        self.lblActivos_seccion.setStyleSheet(u"")
        self.lblActivos_seccion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblActivos_seccion.setWordWrap(True)
        self.btnMover_seccion_2 = QPushButton(self.widget)
        self.btnMover_seccion_2.setObjectName(u"btnMover_seccion_2")
        self.btnMover_seccion_2.setGeometry(QRect(360, 20, 30, 30))
        sizePolicy.setHeightForWidth(self.btnMover_seccion_2.sizePolicy().hasHeightForWidth())
        self.btnMover_seccion_2.setSizePolicy(sizePolicy)
        self.btnMover_seccion_2.setMinimumSize(QSize(30, 30))
        self.btnMover_seccion_2.setMaximumSize(QSize(30, 30))
        self.btnMover_seccion_2.setFont(font1)
        self.btnMover_seccion_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMover_seccion_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnMover_seccion_2.setStyleSheet(u"QPushButton {\n"
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
        icon1.addFile(u":/icons/edit_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMover_seccion_2.setIcon(icon1)
        self.btnMover_seccion_2.setIconSize(QSize(20, 20))
        self.btnMover_estudiante.raise_()
        self.lblLogo_estu.raise_()
        self.line_2.raise_()
        self.lblTitulo_detalle_seccion.raise_()
        self.frameTabla_seccion.raise_()
        self.lneBuscar_detalle_seccion.raise_()
        self.frameFiltro_estu.raise_()
        self.lneDocente_seccion.raise_()
        self.lblCedula_registro_estudiante.raise_()
        self.btnDesactivar_seccion.raise_()
        self.lblTarjeta1_Titulo_7.raise_()
        self.lblActivos_seccion.raise_()
        self.btnMover_seccion_2.raise_()

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(detalle_seccion)

        QMetaObject.connectSlotsByName(detalle_seccion)
    # setupUi

    def retranslateUi(self, detalle_seccion):
        detalle_seccion.setWindowTitle(QCoreApplication.translate("detalle_seccion", u"Dialog", None))
        self.btnMover_estudiante.setText(QCoreApplication.translate("detalle_seccion", u"Mover estudiante", None))
        self.lblLogo_estu.setText("")
        self.lblTitulo_detalle_seccion.setText(QCoreApplication.translate("detalle_seccion", u"Seccion X", None))
        self.cbxFiltro_detalle_seccion.setItemText(0, QCoreApplication.translate("detalle_seccion", u"Todos", None))
        self.cbxFiltro_detalle_seccion.setItemText(1, QCoreApplication.translate("detalle_seccion", u"C\u00e9dula", None))
        self.cbxFiltro_detalle_seccion.setItemText(2, QCoreApplication.translate("detalle_seccion", u"Nombres", None))
        self.cbxFiltro_detalle_seccion.setItemText(3, QCoreApplication.translate("detalle_seccion", u"Apellidos", None))
        self.cbxFiltro_detalle_seccion.setItemText(4, QCoreApplication.translate("detalle_seccion", u"Edad", None))
        self.cbxFiltro_detalle_seccion.setItemText(5, QCoreApplication.translate("detalle_seccion", u"G\u00e9nero", None))

        self.lneBuscar_detalle_seccion.setPlaceholderText(QCoreApplication.translate("detalle_seccion", u"Busqueda por cualquier dato", None))
        self.lneDocente_seccion.setText("")
        self.lneDocente_seccion.setPlaceholderText("")
        self.lblCedula_registro_estudiante.setText(QCoreApplication.translate("detalle_seccion", u"Docente", None))
        self.btnDesactivar_seccion.setText(QCoreApplication.translate("detalle_seccion", u"Desactivar secci\u00f3n", None))
        self.lblTarjeta1_Titulo_7.setText(QCoreApplication.translate("detalle_seccion", u"Total activos:", None))
        self.lblActivos_seccion.setText(QCoreApplication.translate("detalle_seccion", u"000", None))
        self.btnMover_seccion_2.setText("")
    # retranslateUi

