# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'actualizar_user.ui'
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

class Ui_actualizar_user(object):
    def setupUi(self, actualizar_user):
        if not actualizar_user.objectName():
            actualizar_user.setObjectName(u"actualizar_user")
        actualizar_user.resize(330, 470)
        actualizar_user.setMinimumSize(QSize(330, 470))
        actualizar_user.setMaximumSize(QSize(330, 470))
        self.verticalLayout = QVBoxLayout(actualizar_user)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widgetPrincipal = QWidget(actualizar_user)
        self.widgetPrincipal.setObjectName(u"widgetPrincipal")
        self.widgetPrincipal.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widgetPrincipal.setStyleSheet(u"QWidget{\n"
"	background-color: #F7F9FC;\n"
"	font-family: \"Segoe UI\";\n"
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
"    border-radius: 15px;\n"
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
        self.lblTitulo_login.setStyleSheet(u"color: #0b1321")
        self.lblTitulo_login.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lblTitulo_login, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lneNombreCompleto_actu_user = QLineEdit(self.widgetPrincipal)
        self.lneNombreCompleto_actu_user.setObjectName(u"lneNombreCompleto_actu_user")
        self.lneNombreCompleto_actu_user.setMinimumSize(QSize(225, 35))
        self.lneNombreCompleto_actu_user.setMaximumSize(QSize(225, 35))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.lneNombreCompleto_actu_user.setFont(font1)
        self.lneNombreCompleto_actu_user.setMouseTracking(True)
        self.lneNombreCompleto_actu_user.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneNombreCompleto_actu_user.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneNombreCompleto_actu_user.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.lneNombreCompleto_actu_user, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lneUsername_actu_user = QLineEdit(self.widgetPrincipal)
        self.lneUsername_actu_user.setObjectName(u"lneUsername_actu_user")
        self.lneUsername_actu_user.setMinimumSize(QSize(225, 35))
        self.lneUsername_actu_user.setMaximumSize(QSize(225, 35))
        self.lneUsername_actu_user.setFont(font1)
        self.lneUsername_actu_user.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneUsername_actu_user.setMaxLength(8)
        self.lneUsername_actu_user.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneUsername_actu_user.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.lneUsername_actu_user, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lnePass_actu_user = QLineEdit(self.widgetPrincipal)
        self.lnePass_actu_user.setObjectName(u"lnePass_actu_user")
        self.lnePass_actu_user.setMinimumSize(QSize(225, 35))
        self.lnePass_actu_user.setMaximumSize(QSize(225, 35))
        self.lnePass_actu_user.setFont(font1)
        self.lnePass_actu_user.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lnePass_actu_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lnePass_actu_user, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lneRepPass_actu_user = QLineEdit(self.widgetPrincipal)
        self.lneRepPass_actu_user.setObjectName(u"lneRepPass_actu_user")
        self.lneRepPass_actu_user.setMinimumSize(QSize(225, 35))
        self.lneRepPass_actu_user.setMaximumSize(QSize(225, 35))
        self.lneRepPass_actu_user.setFont(font1)
        self.lneRepPass_actu_user.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneRepPass_actu_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lneRepPass_actu_user, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frameRol_login = QFrame(self.widgetPrincipal)
        self.frameRol_login.setObjectName(u"frameRol_login")
        self.frameRol_login.setMinimumSize(QSize(225, 35))
        self.frameRol_login.setMaximumSize(QSize(225, 35))
        self.frameRol_login.setFont(font1)
        self.frameRol_login.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #1e88e5;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox{\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frameRol_login.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameRol_login.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxRol_actu_user = QComboBox(self.frameRol_login)
        self.cbxRol_actu_user.addItem("")
        self.cbxRol_actu_user.addItem("")
        self.cbxRol_actu_user.addItem("")
        self.cbxRol_actu_user.setObjectName(u"cbxRol_actu_user")
        self.cbxRol_actu_user.setGeometry(QRect(11, 5, 201, 26))
        self.cbxRol_actu_user.setMinimumSize(QSize(201, 26))
        self.cbxRol_actu_user.setMaximumSize(QSize(201, 26))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        self.cbxRol_actu_user.setFont(font2)
        self.cbxRol_actu_user.setStyleSheet(u"")
        self.cbxRol_actu_user.setIconSize(QSize(10, 10))

        self.verticalLayout_2.addWidget(self.frameRol_login, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btnActualizar_user = QPushButton(self.widgetPrincipal)
        self.btnActualizar_user.setObjectName(u"btnActualizar_user")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnActualizar_user.sizePolicy().hasHeightForWidth())
        self.btnActualizar_user.setSizePolicy(sizePolicy)
        self.btnActualizar_user.setMinimumSize(QSize(200, 35))
        self.btnActualizar_user.setMaximumSize(QSize(200, 35))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.btnActualizar_user.setFont(font3)
        self.btnActualizar_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnActualizar_user.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnActualizar_user.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/confirm_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnActualizar_user.setIcon(icon)

        self.verticalLayout_2.addWidget(self.btnActualizar_user, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btnCancelar_actu_user = QPushButton(self.widgetPrincipal)
        self.btnCancelar_actu_user.setObjectName(u"btnCancelar_actu_user")
        sizePolicy.setHeightForWidth(self.btnCancelar_actu_user.sizePolicy().hasHeightForWidth())
        self.btnCancelar_actu_user.setSizePolicy(sizePolicy)
        self.btnCancelar_actu_user.setMinimumSize(QSize(150, 35))
        self.btnCancelar_actu_user.setMaximumSize(QSize(150, 35))
        self.btnCancelar_actu_user.setFont(font3)
        self.btnCancelar_actu_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCancelar_actu_user.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnCancelar_actu_user.setStyleSheet(u"background-color: #e74c3c;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/cancelar_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCancelar_actu_user.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.btnCancelar_actu_user, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.widgetPrincipal)


        self.retranslateUi(actualizar_user)

        QMetaObject.connectSlotsByName(actualizar_user)
    # setupUi

    def retranslateUi(self, actualizar_user):
        actualizar_user.setWindowTitle(QCoreApplication.translate("actualizar_user", u"Dialog", None))
        self.lblTitulo_login.setText(QCoreApplication.translate("actualizar_user", u"Actualizar datos de usuario", None))
        self.lneNombreCompleto_actu_user.setText("")
        self.lneNombreCompleto_actu_user.setPlaceholderText(QCoreApplication.translate("actualizar_user", u"NOMBRE COMPLETO", None))
        self.lneUsername_actu_user.setPlaceholderText(QCoreApplication.translate("actualizar_user", u"USUARIO", None))
        self.lnePass_actu_user.setPlaceholderText(QCoreApplication.translate("actualizar_user", u"NUEVA CONTRASE\u00d1A", None))
        self.lneRepPass_actu_user.setPlaceholderText(QCoreApplication.translate("actualizar_user", u"REPITA CONTRASE\u00d1A", None))
        self.cbxRol_actu_user.setItemText(0, QCoreApplication.translate("actualizar_user", u"Seleccione rol", None))
        self.cbxRol_actu_user.setItemText(1, QCoreApplication.translate("actualizar_user", u"empleado", None))
        self.cbxRol_actu_user.setItemText(2, QCoreApplication.translate("actualizar_user", u"admin", None))

        self.btnActualizar_user.setText(QCoreApplication.translate("actualizar_user", u"Actualizar", None))
        self.btnCancelar_actu_user.setText(QCoreApplication.translate("actualizar_user", u"Cancelar", None))
    # retranslateUi

