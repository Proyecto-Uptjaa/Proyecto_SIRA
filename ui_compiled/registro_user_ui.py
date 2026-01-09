# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro_user.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
from resources import resources_ui
from resources import resources_ui

class Ui_registro_user(object):
    def setupUi(self, registro_user):
        if not registro_user.objectName():
            registro_user.setObjectName(u"registro_user")
        registro_user.resize(330, 470)
        registro_user.setMinimumSize(QSize(330, 470))
        registro_user.setMaximumSize(QSize(330, 470))
        registro_user.setStyleSheet(u"background-color: #f5f6fa;")
        self.verticalLayout = QVBoxLayout(registro_user)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widgetPrincipal = QWidget(registro_user)
        self.widgetPrincipal.setObjectName(u"widgetPrincipal")
        self.widgetPrincipal.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widgetPrincipal.setStyleSheet(u"QWidget{\n"
"	background-color: #F7F9FC;\n"
"	font-family: \"Segoe UI\";\n"
"color: #2d2d2d;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 12px;\n"
"    padding: 2px 8px;\n"
"    background-color: white;\n"
"	color: #2d2d2d;\n"
"}\n"
"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 10px;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widgetPrincipal)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblTitulo_login = QLabel(self.widgetPrincipal)
        self.lblTitulo_login.setObjectName(u"lblTitulo_login")
        self.lblTitulo_login.setMinimumSize(QSize(241, 21))
        self.lblTitulo_login.setMaximumSize(QSize(250, 21))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.lblTitulo_login.setFont(font)
        self.lblTitulo_login.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblTitulo_login.setStyleSheet(u"")
        self.lblTitulo_login.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lblTitulo_login, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lneNombreCompleto_reg_user = QLineEdit(self.widgetPrincipal)
        self.lneNombreCompleto_reg_user.setObjectName(u"lneNombreCompleto_reg_user")
        self.lneNombreCompleto_reg_user.setMinimumSize(QSize(225, 35))
        self.lneNombreCompleto_reg_user.setMaximumSize(QSize(225, 35))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.lneNombreCompleto_reg_user.setFont(font1)
        self.lneNombreCompleto_reg_user.setMouseTracking(True)
        self.lneNombreCompleto_reg_user.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneNombreCompleto_reg_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lneNombreCompleto_reg_user, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lneUsername_reg_user = QLineEdit(self.widgetPrincipal)
        self.lneUsername_reg_user.setObjectName(u"lneUsername_reg_user")
        self.lneUsername_reg_user.setMinimumSize(QSize(225, 35))
        self.lneUsername_reg_user.setMaximumSize(QSize(225, 35))
        self.lneUsername_reg_user.setFont(font1)
        self.lneUsername_reg_user.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneUsername_reg_user.setMaxLength(8)
        self.lneUsername_reg_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lneUsername_reg_user, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lnePass_reg_user = QLineEdit(self.widgetPrincipal)
        self.lnePass_reg_user.setObjectName(u"lnePass_reg_user")
        self.lnePass_reg_user.setMinimumSize(QSize(225, 35))
        self.lnePass_reg_user.setMaximumSize(QSize(225, 35))
        self.lnePass_reg_user.setFont(font1)
        self.lnePass_reg_user.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lnePass_reg_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lnePass_reg_user, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lneRepPass_reg_user = QLineEdit(self.widgetPrincipal)
        self.lneRepPass_reg_user.setObjectName(u"lneRepPass_reg_user")
        self.lneRepPass_reg_user.setMinimumSize(QSize(225, 35))
        self.lneRepPass_reg_user.setMaximumSize(QSize(225, 35))
        self.lneRepPass_reg_user.setFont(font1)
        self.lneRepPass_reg_user.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneRepPass_reg_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lneRepPass_reg_user, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frameRol_login = QFrame(self.widgetPrincipal)
        self.frameRol_login.setObjectName(u"frameRol_login")
        self.frameRol_login.setMinimumSize(QSize(225, 35))
        self.frameRol_login.setMaximumSize(QSize(225, 35))
        self.frameRol_login.setFont(font1)
        self.frameRol_login.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #1e88e5;\n"
"	border-radius: 12px;\n"
"}\n"
"QComboBox{\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frameRol_login.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameRol_login.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxRol_reg_user = QComboBox(self.frameRol_login)
        self.cbxRol_reg_user.addItem("")
        self.cbxRol_reg_user.addItem("")
        self.cbxRol_reg_user.addItem("")
        self.cbxRol_reg_user.setObjectName(u"cbxRol_reg_user")
        self.cbxRol_reg_user.setGeometry(QRect(11, 5, 201, 26))
        self.cbxRol_reg_user.setMinimumSize(QSize(201, 26))
        self.cbxRol_reg_user.setMaximumSize(QSize(201, 26))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(13)
        self.cbxRol_reg_user.setFont(font2)
        self.cbxRol_reg_user.setStyleSheet(u"")
        self.cbxRol_reg_user.setIconSize(QSize(10, 10))

        self.verticalLayout_2.addWidget(self.frameRol_login, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btnRegistrar_user = QPushButton(self.widgetPrincipal)
        self.btnRegistrar_user.setObjectName(u"btnRegistrar_user")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRegistrar_user.sizePolicy().hasHeightForWidth())
        self.btnRegistrar_user.setSizePolicy(sizePolicy)
        self.btnRegistrar_user.setMinimumSize(QSize(200, 35))
        self.btnRegistrar_user.setMaximumSize(QSize(200, 35))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.btnRegistrar_user.setFont(font3)
        self.btnRegistrar_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnRegistrar_user.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnRegistrar_user.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/confirm_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRegistrar_user.setIcon(icon)

        self.verticalLayout_2.addWidget(self.btnRegistrar_user, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btnCancelar_reg_user = QPushButton(self.widgetPrincipal)
        self.btnCancelar_reg_user.setObjectName(u"btnCancelar_reg_user")
        sizePolicy.setHeightForWidth(self.btnCancelar_reg_user.sizePolicy().hasHeightForWidth())
        self.btnCancelar_reg_user.setSizePolicy(sizePolicy)
        self.btnCancelar_reg_user.setMinimumSize(QSize(150, 35))
        self.btnCancelar_reg_user.setMaximumSize(QSize(150, 35))
        self.btnCancelar_reg_user.setFont(font3)
        self.btnCancelar_reg_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCancelar_reg_user.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnCancelar_reg_user.setStyleSheet(u"background-color: #e74c3c;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/cancelar_w2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCancelar_reg_user.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.btnCancelar_reg_user, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.widgetPrincipal)


        self.retranslateUi(registro_user)

        QMetaObject.connectSlotsByName(registro_user)
    # setupUi

    def retranslateUi(self, registro_user):
        registro_user.setWindowTitle(QCoreApplication.translate("registro_user", u"Dialog", None))
        self.lblTitulo_login.setText(QCoreApplication.translate("registro_user", u"Registro de usuario", None))
        self.lneNombreCompleto_reg_user.setText("")
        self.lneNombreCompleto_reg_user.setPlaceholderText(QCoreApplication.translate("registro_user", u"NOMBRE COMPLETO", None))
        self.lneUsername_reg_user.setPlaceholderText(QCoreApplication.translate("registro_user", u"USUARIO", None))
        self.lnePass_reg_user.setPlaceholderText(QCoreApplication.translate("registro_user", u"CONTRASE\u00d1A", None))
        self.lneRepPass_reg_user.setPlaceholderText(QCoreApplication.translate("registro_user", u"REPITA CONTRASE\u00d1A", None))
        self.cbxRol_reg_user.setItemText(0, QCoreApplication.translate("registro_user", u"Seleccione rol", None))
        self.cbxRol_reg_user.setItemText(1, QCoreApplication.translate("registro_user", u"Empleado", None))
        self.cbxRol_reg_user.setItemText(2, QCoreApplication.translate("registro_user", u"Administrador", None))

        self.btnRegistrar_user.setText(QCoreApplication.translate("registro_user", u"Registrar", None))
        self.btnCancelar_reg_user.setText(QCoreApplication.translate("registro_user", u"Cancelar", None))
    # retranslateUi

