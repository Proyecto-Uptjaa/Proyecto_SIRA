# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'anio_escolar.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)
from resources import resources_ui

class Ui_anio_escolar(object):
    def setupUi(self, anio_escolar):
        if not anio_escolar.objectName():
            anio_escolar.setObjectName(u"anio_escolar")
        anio_escolar.resize(1111, 621)
        anio_escolar.setMinimumSize(QSize(1111, 621))
        anio_escolar.setMaximumSize(QSize(1111, 621))
        anio_escolar.setStyleSheet(u"background-color: #f5f6fa;\n"
"color: #2d2d2d;")
        self.lblTitulo_logo_estu = QLabel(anio_escolar)
        self.lblTitulo_logo_estu.setObjectName(u"lblTitulo_logo_estu")
        self.lblTitulo_logo_estu.setGeometry(QRect(830, 10, 191, 61))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(19)
        font.setBold(True)
        self.lblTitulo_logo_estu.setFont(font)
        self.lblTitulo_logo_estu.setStyleSheet(u"color: #2d2d2d")
        self.lblTitulo_logo_estu.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_logo_estu.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_logo_estu.setScaledContents(False)
        self.lblTitulo_logo_estu.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_logo_estu.setWordWrap(True)
        self.lblTitulo_logo_estu.setIndent(0)
        self.lblLogo_estu = QLabel(anio_escolar)
        self.lblLogo_estu.setObjectName(u"lblLogo_estu")
        self.lblLogo_estu.setGeometry(QRect(1039, 10, 51, 61))
        self.lblLogo_estu.setMinimumSize(QSize(50, 50))
        self.lblLogo_estu.setMaximumSize(QSize(130, 70))
        self.lblLogo_estu.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_estu.setScaledContents(True)
        self.line_2 = QFrame(anio_escolar)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(1029, 10, 3, 61))
        self.line_2.setMinimumSize(QSize(3, 61))
        self.line_2.setMaximumSize(QSize(3, 61))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.btnAperturar_anio = QPushButton(anio_escolar)
        self.btnAperturar_anio.setObjectName(u"btnAperturar_anio")
        self.btnAperturar_anio.setGeometry(QRect(329, 210, 311, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAperturar_anio.sizePolicy().hasHeightForWidth())
        self.btnAperturar_anio.setSizePolicy(sizePolicy)
        self.btnAperturar_anio.setMinimumSize(QSize(120, 40))
        self.btnAperturar_anio.setMaximumSize(QSize(311, 50))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.btnAperturar_anio.setFont(font1)
        self.btnAperturar_anio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAperturar_anio.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnAperturar_anio.setStyleSheet(u"QPushButton {\n"
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
        self.btnAperturar_anio.setIcon(icon)
        self.btnAperturar_anio.setIconSize(QSize(18, 18))
        self.lblTitulo_logo_estu_2 = QLabel(anio_escolar)
        self.lblTitulo_logo_estu_2.setObjectName(u"lblTitulo_logo_estu_2")
        self.lblTitulo_logo_estu_2.setGeometry(QRect(270, 30, 421, 81))
        self.lblTitulo_logo_estu_2.setFont(font)
        self.lblTitulo_logo_estu_2.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblTitulo_logo_estu_2.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_logo_estu_2.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_logo_estu_2.setScaledContents(False)
        self.lblTitulo_logo_estu_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitulo_logo_estu_2.setWordWrap(True)
        self.lblTitulo_logo_estu_2.setIndent(0)
        self.lblTitulo_logo_estu_3 = QLabel(anio_escolar)
        self.lblTitulo_logo_estu_3.setObjectName(u"lblTitulo_logo_estu_3")
        self.lblTitulo_logo_estu_3.setGeometry(QRect(270, 110, 431, 81))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.lblTitulo_logo_estu_3.setFont(font2)
        self.lblTitulo_logo_estu_3.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblTitulo_logo_estu_3.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_logo_estu_3.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_logo_estu_3.setScaledContents(False)
        self.lblTitulo_logo_estu_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitulo_logo_estu_3.setWordWrap(True)
        self.lblTitulo_logo_estu_3.setIndent(0)

        self.retranslateUi(anio_escolar)

        QMetaObject.connectSlotsByName(anio_escolar)
    # setupUi

    def retranslateUi(self, anio_escolar):
        anio_escolar.setWindowTitle(QCoreApplication.translate("anio_escolar", u"Form", None))
        self.lblTitulo_logo_estu.setText(QCoreApplication.translate("anio_escolar", u"Gesti\u00f3n de a\u00f1os escolares", None))
        self.lblLogo_estu.setText("")
        self.btnAperturar_anio.setText(QCoreApplication.translate("anio_escolar", u"Aperturar nuevo a\u00f1o escolar", None))
        self.lblTitulo_logo_estu_2.setText(QCoreApplication.translate("anio_escolar", u"Con \u00e9sta opci\u00f3n puede aperturar un nuevo a\u00f1o escolar", None))
        self.lblTitulo_logo_estu_3.setText(QCoreApplication.translate("anio_escolar", u"\u00c9sta funci\u00f3n es irreversible, y promover\u00e1 autom\u00e1ticamente a todos los estudiantes al siguiente nivel/grado. Asi como duplicar las secciones actualmente existentes para el nuevo per\u00edodo.", None))
    # retranslateUi

