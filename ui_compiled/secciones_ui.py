# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secciones.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
from resources import resources_ui

class Ui_secciones(object):
    def setupUi(self, secciones):
        if not secciones.objectName():
            secciones.setObjectName(u"secciones")
        secciones.resize(1111, 621)
        secciones.setMinimumSize(QSize(1111, 621))
        secciones.setMaximumSize(QSize(1111, 621))
        secciones.setStyleSheet(u"background-color: #f5f6fa;\n"
"color: #2d2d2d;")
        self.lblTitulo_secciones = QLabel(secciones)
        self.lblTitulo_secciones.setObjectName(u"lblTitulo_secciones")
        self.lblTitulo_secciones.setGeometry(QRect(880, 10, 141, 61))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(19)
        font.setBold(True)
        self.lblTitulo_secciones.setFont(font)
        self.lblTitulo_secciones.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblTitulo_secciones.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_secciones.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_secciones.setScaledContents(False)
        self.lblTitulo_secciones.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_secciones.setWordWrap(True)
        self.lblTitulo_secciones.setIndent(0)
        self.lblLogo_secciones = QLabel(secciones)
        self.lblLogo_secciones.setObjectName(u"lblLogo_secciones")
        self.lblLogo_secciones.setGeometry(QRect(1039, 10, 51, 61))
        self.lblLogo_secciones.setMinimumSize(QSize(50, 50))
        self.lblLogo_secciones.setMaximumSize(QSize(130, 70))
        self.lblLogo_secciones.setStyleSheet(u"background-color: transparent;")
        self.lblLogo_secciones.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_secciones.setScaledContents(True)
        self.line_2 = QFrame(secciones)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(1029, 10, 3, 61))
        self.line_2.setMinimumSize(QSize(3, 61))
        self.line_2.setMaximumSize(QSize(3, 61))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.scrollArea_secciones = QScrollArea(secciones)
        self.scrollArea_secciones.setObjectName(u"scrollArea_secciones")
        self.scrollArea_secciones.setGeometry(QRect(50, 100, 1021, 501))
        self.scrollArea_secciones.setStyleSheet(u"")
        self.scrollArea_secciones.setWidgetResizable(True)
        self.widgetContenidoScroll = QWidget()
        self.widgetContenidoScroll.setObjectName(u"widgetContenidoScroll")
        self.widgetContenidoScroll.setGeometry(QRect(0, 0, 1019, 499))
        self.verticalLayout_contenido = QVBoxLayout(self.widgetContenidoScroll)
        self.verticalLayout_contenido.setSpacing(28)
        self.verticalLayout_contenido.setObjectName(u"verticalLayout_contenido")
        self.verticalLayout_contenido.setContentsMargins(20, 20, 20, 20)
        self.scrollArea_secciones.setWidget(self.widgetContenidoScroll)
        self.lneBuscar_seccion = QLineEdit(secciones)
        self.lneBuscar_seccion.setObjectName(u"lneBuscar_seccion")
        self.lneBuscar_seccion.setGeometry(QRect(50, 30, 441, 40))
        self.lneBuscar_seccion.setMinimumSize(QSize(200, 40))
        self.lneBuscar_seccion.setMaximumSize(QSize(541, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(13)
        self.lneBuscar_seccion.setFont(font1)
        self.lneBuscar_seccion.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneBuscar_seccion.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #848f9d;\n"
"	color: #2d2d2d;\n"
"    border-radius: 12px;\n"
"    padding: 1px 3px;\n"
"    background-color: white;\n"
"}")
        self.lneBuscar_seccion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneBuscar_seccion.setClearButtonEnabled(True)
        self.btnCrear_seccion = QPushButton(secciones)
        self.btnCrear_seccion.setObjectName(u"btnCrear_seccion")
        self.btnCrear_seccion.setGeometry(QRect(500, 30, 150, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCrear_seccion.sizePolicy().hasHeightForWidth())
        self.btnCrear_seccion.setSizePolicy(sizePolicy)
        self.btnCrear_seccion.setMinimumSize(QSize(120, 40))
        self.btnCrear_seccion.setMaximumSize(QSize(150, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(13)
        font2.setBold(True)
        self.btnCrear_seccion.setFont(font2)
        self.btnCrear_seccion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCrear_seccion.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnCrear_seccion.setStyleSheet(u"QPushButton {\n"
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
        self.btnCrear_seccion.setIcon(icon)
        self.btnCrear_seccion.setIconSize(QSize(18, 18))
        self.lblIcon_conectado_como = QLabel(secciones)
        self.lblIcon_conectado_como.setObjectName(u"lblIcon_conectado_como")
        self.lblIcon_conectado_como.setGeometry(QRect(920, 75, 16, 16))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(8)
        font3.setBold(True)
        self.lblIcon_conectado_como.setFont(font3)
        self.lblIcon_conectado_como.setStyleSheet(u"color: #2d2d2d")
        self.lblIcon_conectado_como.setPixmap(QPixmap(u":/icons/usuario-activo.png"))
        self.lblIcon_conectado_como.setScaledContents(True)
        self.lblIcon_conectado_como.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblConectado_como = QLabel(secciones)
        self.lblConectado_como.setObjectName(u"lblConectado_como")
        self.lblConectado_como.setGeometry(QRect(940, 75, 161, 16))
        self.lblConectado_como.setFont(font3)
        self.lblConectado_como.setStyleSheet(u"color: #2d2d2d")
        self.lblConectado_como.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(secciones)

        QMetaObject.connectSlotsByName(secciones)
    # setupUi

    def retranslateUi(self, secciones):
        secciones.setWindowTitle(QCoreApplication.translate("secciones", u"Form", None))
        self.lblTitulo_secciones.setText(QCoreApplication.translate("secciones", u"Gesti\u00f3n de secciones", None))
        self.lblLogo_secciones.setText("")
        self.lneBuscar_seccion.setPlaceholderText(QCoreApplication.translate("secciones", u"Busqueda por grado/secci\u00f3n", None))
        self.btnCrear_seccion.setText(QCoreApplication.translate("secciones", u"Crear secci\u00f3n", None))
        self.lblIcon_conectado_como.setText("")
        self.lblConectado_como.setText(QCoreApplication.translate("secciones", u"Conectado como: jorged", None))
    # retranslateUi

