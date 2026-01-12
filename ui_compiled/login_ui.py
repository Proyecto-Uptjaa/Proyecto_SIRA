# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from resources import resources_ui

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(325, 340)
        login.setMinimumSize(QSize(325, 340))
        login.setMaximumSize(QSize(325, 340))
        login.setStyleSheet(u"background-color: #f5f6fa;\n"
"border-radius: 15px;")
        self.verticalLayout = QVBoxLayout(login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widgetPrincipal = QWidget(login)
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
"}\n"
"QLabel{\n"
"	background-color: transparent;\n"
"}")
        self.lblTitulo_login = QLabel(self.widgetPrincipal)
        self.lblTitulo_login.setObjectName(u"lblTitulo_login")
        self.lblTitulo_login.setEnabled(True)
        self.lblTitulo_login.setGeometry(QRect(20, 30, 161, 61))
        self.lblTitulo_login.setMinimumSize(QSize(100, 21))
        self.lblTitulo_login.setMaximumSize(QSize(325, 120))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(13)
        font.setBold(True)
        self.lblTitulo_login.setFont(font)
        self.lblTitulo_login.setStyleSheet(u"")
        self.lblTitulo_login.setPixmap(QPixmap(u":/logos/SIRA_logo_cut.png"))
        self.lblTitulo_login.setScaledContents(True)
        self.lblTitulo_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitulo_login.setWordWrap(False)
        self.lblLogo_login = QLabel(self.widgetPrincipal)
        self.lblLogo_login.setObjectName(u"lblLogo_login")
        self.lblLogo_login.setGeometry(QRect(200, 20, 71, 80))
        self.lblLogo_login.setMinimumSize(QSize(70, 80))
        self.lblLogo_login.setMaximumSize(QSize(100, 100))
        self.lblLogo_login.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_login.setScaledContents(True)
        self.lblLogo_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblLogo_login.setMargin(0)
        self.inputUser = QLineEdit(self.widgetPrincipal)
        self.inputUser.setObjectName(u"inputUser")
        self.inputUser.setGeometry(QRect(30, 150, 241, 35))
        self.inputUser.setMinimumSize(QSize(200, 35))
        self.inputUser.setMaximumSize(QSize(270, 35))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.inputUser.setFont(font1)
        self.inputUser.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.inputUser.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.inputPassword = QLineEdit(self.widgetPrincipal)
        self.inputPassword.setObjectName(u"inputPassword")
        self.inputPassword.setGeometry(QRect(30, 200, 241, 35))
        self.inputPassword.setMinimumSize(QSize(200, 35))
        self.inputPassword.setMaximumSize(QSize(241, 35))
        self.inputPassword.setFont(font1)
        self.inputPassword.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.inputPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.inputPassword.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnLogin = QPushButton(self.widgetPrincipal)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(50, 250, 200, 35))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLogin.sizePolicy().hasHeightForWidth())
        self.btnLogin.setSizePolicy(sizePolicy)
        self.btnLogin.setMinimumSize(QSize(200, 35))
        self.btnLogin.setMaximumSize(QSize(200, 35))
        self.btnLogin.setFont(font)
        self.btnLogin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLogin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.btnLogin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnLogin.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/icons/login_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLogin.setIcon(icon)
        self.line_2 = QFrame(self.widgetPrincipal)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(190, 20, 3, 80))
        self.line_2.setMinimumSize(QSize(3, 61))
        self.line_2.setMaximumSize(QSize(3, 85))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblTitulo_login_2 = QLabel(self.widgetPrincipal)
        self.lblTitulo_login_2.setObjectName(u"lblTitulo_login_2")
        self.lblTitulo_login_2.setGeometry(QRect(20, 95, 251, 41))
        self.lblTitulo_login_2.setMinimumSize(QSize(100, 21))
        self.lblTitulo_login_2.setMaximumSize(QSize(325, 120))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.lblTitulo_login_2.setFont(font2)
        self.lblTitulo_login_2.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50; \n"
"}")
        self.lblTitulo_login_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitulo_login_2.setWordWrap(True)
        self.lblVersion = QLabel(self.widgetPrincipal)
        self.lblVersion.setObjectName(u"lblVersion")
        self.lblVersion.setGeometry(QRect(50, 300, 201, 21))
        self.lblVersion.setMinimumSize(QSize(100, 21))
        self.lblVersion.setMaximumSize(QSize(325, 120))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(7)
        font3.setBold(True)
        self.lblVersion.setFont(font3)
        self.lblVersion.setStyleSheet(u"QLabel {\n"
"	color: rgb(140, 143, 146);\n"
"}")
        self.lblVersion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblVersion.setWordWrap(True)
        self.lblLogo_login.raise_()
        self.inputUser.raise_()
        self.inputPassword.raise_()
        self.btnLogin.raise_()
        self.lblTitulo_login.raise_()
        self.lblTitulo_login_2.raise_()
        self.line_2.raise_()
        self.lblVersion.raise_()

        self.verticalLayout.addWidget(self.widgetPrincipal)


        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Dialog", None))
        self.lblTitulo_login.setText("")
        self.lblLogo_login.setText("")
        self.inputUser.setPlaceholderText(QCoreApplication.translate("login", u"USUARIO", None))
        self.inputPassword.setPlaceholderText(QCoreApplication.translate("login", u"CONTRASE\u00d1A", None))
        self.btnLogin.setText(QCoreApplication.translate("login", u"Acceder", None))
        self.lblTitulo_login_2.setText(QCoreApplication.translate("login", u"Sistema Interno de Registro Acad\u00e9mico\n"
"E.B. \"Dr. Severiano Hern\u00e1ndez\"", None))
        self.lblVersion.setText(QCoreApplication.translate("login", u"Versi\u00f3n SIRA: v", None))
    # retranslateUi

