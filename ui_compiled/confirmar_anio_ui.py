# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmar_anio.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from resources import resources_ui
from resources import resources_ui

class Ui_confirmar_anio(object):
    def setupUi(self, confirmar_anio):
        if not confirmar_anio.objectName():
            confirmar_anio.setObjectName(u"confirmar_anio")
        confirmar_anio.resize(325, 265)
        confirmar_anio.setMinimumSize(QSize(325, 265))
        confirmar_anio.setMaximumSize(QSize(325, 265))
        confirmar_anio.setStyleSheet(u"background-color: #f5f6fa;")
        self.verticalLayout = QVBoxLayout(confirmar_anio)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widgetPrincipal = QWidget(confirmar_anio)
        self.widgetPrincipal.setObjectName(u"widgetPrincipal")
        self.widgetPrincipal.setStyleSheet(u"QWidget{\n"
"	background-color: #F7F9FC;\n"
"color: #2d2d2d;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 12px;\n"
"    padding: 3px 8px;\n"
"    background-color: white;\n"
"	color: #2d2d2d;\n"
"}")
        self.lblTitulo_login = QLabel(self.widgetPrincipal)
        self.lblTitulo_login.setObjectName(u"lblTitulo_login")
        self.lblTitulo_login.setGeometry(QRect(60, 10, 181, 51))
        self.lblTitulo_login.setMinimumSize(QSize(100, 21))
        self.lblTitulo_login.setMaximumSize(QSize(325, 120))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(13)
        font.setBold(True)
        self.lblTitulo_login.setFont(font)
        self.lblTitulo_login.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50; \n"
"}")
        self.lblTitulo_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitulo_login.setWordWrap(True)
        self.btnAperturar = QPushButton(self.widgetPrincipal)
        self.btnAperturar.setObjectName(u"btnAperturar")
        self.btnAperturar.setGeometry(QRect(60, 140, 200, 35))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAperturar.sizePolicy().hasHeightForWidth())
        self.btnAperturar.setSizePolicy(sizePolicy)
        self.btnAperturar.setMinimumSize(QSize(200, 35))
        self.btnAperturar.setMaximumSize(QSize(200, 35))
        self.btnAperturar.setFont(font)
        self.btnAperturar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAperturar.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.btnAperturar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnAperturar.setStyleSheet(u"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 10px;\n"
"    border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/confirm_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAperturar.setIcon(icon)
        self.frameAnio_nuevo = QFrame(self.widgetPrincipal)
        self.frameAnio_nuevo.setObjectName(u"frameAnio_nuevo")
        self.frameAnio_nuevo.setGeometry(QRect(40, 80, 230, 40))
        self.frameAnio_nuevo.setMinimumSize(QSize(230, 40))
        self.frameAnio_nuevo.setMaximumSize(QSize(230, 40))
        self.frameAnio_nuevo.setStyleSheet(u"QFrame{\n"
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
        self.frameAnio_nuevo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameAnio_nuevo.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxAnio_nuevo = QComboBox(self.frameAnio_nuevo)
        self.cbxAnio_nuevo.setObjectName(u"cbxAnio_nuevo")
        self.cbxAnio_nuevo.setGeometry(QRect(11, 5, 210, 30))
        self.cbxAnio_nuevo.setMinimumSize(QSize(210, 30))
        self.cbxAnio_nuevo.setMaximumSize(QSize(210, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.cbxAnio_nuevo.setFont(font1)
        self.cbxAnio_nuevo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxAnio_nuevo.setStyleSheet(u"QComboBox {\n"
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
        self.cbxAnio_nuevo.setIconSize(QSize(10, 10))
        self.btnCancelar = QPushButton(self.widgetPrincipal)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setGeometry(QRect(90, 190, 141, 35))
        sizePolicy.setHeightForWidth(self.btnCancelar.sizePolicy().hasHeightForWidth())
        self.btnCancelar.setSizePolicy(sizePolicy)
        self.btnCancelar.setMinimumSize(QSize(100, 35))
        self.btnCancelar.setMaximumSize(QSize(200, 35))
        self.btnCancelar.setFont(font)
        self.btnCancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCancelar.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.btnCancelar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnCancelar.setStyleSheet(u"QPushButton {\n"
"	background-color: #e74c3c;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 10px;\n"
"    border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/cancelar_w2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCancelar.setIcon(icon1)
        self.btnAperturar.raise_()
        self.lblTitulo_login.raise_()
        self.frameAnio_nuevo.raise_()
        self.btnCancelar.raise_()

        self.verticalLayout.addWidget(self.widgetPrincipal)


        self.retranslateUi(confirmar_anio)

        QMetaObject.connectSlotsByName(confirmar_anio)
    # setupUi

    def retranslateUi(self, confirmar_anio):
        confirmar_anio.setWindowTitle(QCoreApplication.translate("confirmar_anio", u"Dialog", None))
        self.lblTitulo_login.setText(QCoreApplication.translate("confirmar_anio", u"Seleccione el nuevo a\u00f1o escolar", None))
        self.btnAperturar.setText(QCoreApplication.translate("confirmar_anio", u"Aperturar", None))
        self.btnCancelar.setText(QCoreApplication.translate("confirmar_anio", u"Cancelar", None))
    # retranslateUi

