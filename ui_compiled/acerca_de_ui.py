# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acerca_de.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)
from resources import resources_ui
from resources import resources_ui
from resources import resources_ui

class Ui_Acerca_de(object):
    def setupUi(self, Acerca_de):
        if not Acerca_de.objectName():
            Acerca_de.setObjectName(u"Acerca_de")
        Acerca_de.resize(500, 500)
        Acerca_de.setMinimumSize(QSize(500, 500))
        Acerca_de.setMaximumSize(QSize(500, 500))
        Acerca_de.setStyleSheet(u"background-color: #f5f6fa;")
        self.gridLayout = QGridLayout(Acerca_de)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Acerca_de)
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
"QLabel{\n"
"	background-color: transparent;\n"
"}")
        self.lblLogo_UPTJAA_acercade = QLabel(self.widget)
        self.lblLogo_UPTJAA_acercade.setObjectName(u"lblLogo_UPTJAA_acercade")
        self.lblLogo_UPTJAA_acercade.setGeometry(QRect(315, 20, 90, 80))
        self.lblLogo_UPTJAA_acercade.setMinimumSize(QSize(90, 80))
        self.lblLogo_UPTJAA_acercade.setMaximumSize(QSize(90, 80))
        self.lblLogo_UPTJAA_acercade.setStyleSheet(u"background-color: transparent;")
        self.lblLogo_UPTJAA_acercade.setPixmap(QPixmap(u":/logos/logo_uptjaa.png"))
        self.lblLogo_UPTJAA_acercade.setScaledContents(True)
        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(305, 20, 3, 80))
        self.line_2.setMinimumSize(QSize(3, 80))
        self.line_2.setMaximumSize(QSize(3, 80))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblTitulo_logo_estu = QLabel(self.widget)
        self.lblTitulo_logo_estu.setObjectName(u"lblTitulo_logo_estu")
        self.lblTitulo_logo_estu.setGeometry(QRect(50, 110, 381, 50))
        self.lblTitulo_logo_estu.setMinimumSize(QSize(381, 50))
        self.lblTitulo_logo_estu.setMaximumSize(QSize(381, 50))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.lblTitulo_logo_estu.setFont(font1)
        self.lblTitulo_logo_estu.setStyleSheet(u"color: #2d2d2d")
        self.lblTitulo_logo_estu.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_logo_estu.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_logo_estu.setScaledContents(False)
        self.lblTitulo_logo_estu.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_logo_estu.setWordWrap(True)
        self.lblTitulo_logo_estu.setIndent(0)
        self.btnCerrar = QPushButton(self.widget)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setGeometry(QRect(350, 430, 120, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCerrar.sizePolicy().hasHeightForWidth())
        self.btnCerrar.setSizePolicy(sizePolicy)
        self.btnCerrar.setMinimumSize(QSize(120, 40))
        self.btnCerrar.setMaximumSize(QSize(120, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(13)
        font2.setBold(True)
        self.btnCerrar.setFont(font2)
        self.btnCerrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCerrar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnCerrar.setStyleSheet(u"QPushButton {\n"
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
        icon = QIcon()
        icon.addFile(u":/icons/regresar_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCerrar.setIcon(icon)
        self.lblCedula_registro_estudiante = QLabel(self.widget)
        self.lblCedula_registro_estudiante.setObjectName(u"lblCedula_registro_estudiante")
        self.lblCedula_registro_estudiante.setGeometry(QRect(60, 150, 371, 111))
        self.lblCedula_registro_estudiante.setMinimumSize(QSize(0, 50))
        self.lblCedula_registro_estudiante.setMaximumSize(QSize(16777215, 200))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.lblCedula_registro_estudiante.setFont(font3)
        self.lblCedula_registro_estudiante.setStyleSheet(u"color: #2d2d2d;\n"
"border: 1px solid transparent;\n"
"border-radius: 10px;\n"
"background-color: transparent;")
        self.lblCedula_registro_estudiante.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.lblCedula_registro_estudiante.setWordWrap(True)
        self.lblLogo_SIRA_acercade = QLabel(self.widget)
        self.lblLogo_SIRA_acercade.setObjectName(u"lblLogo_SIRA_acercade")
        self.lblLogo_SIRA_acercade.setGeometry(QRect(65, 20, 231, 80))
        self.lblLogo_SIRA_acercade.setMinimumSize(QSize(231, 80))
        self.lblLogo_SIRA_acercade.setMaximumSize(QSize(231, 80))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(19)
        font4.setBold(True)
        self.lblLogo_SIRA_acercade.setFont(font4)
        self.lblLogo_SIRA_acercade.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblLogo_SIRA_acercade.setFrameShape(QFrame.Shape.NoFrame)
        self.lblLogo_SIRA_acercade.setFrameShadow(QFrame.Shadow.Plain)
        self.lblLogo_SIRA_acercade.setPixmap(QPixmap(u":/logos/SIRA_logo_cut.png"))
        self.lblLogo_SIRA_acercade.setScaledContents(True)
        self.lblLogo_SIRA_acercade.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblLogo_SIRA_acercade.setWordWrap(True)
        self.lblLogo_SIRA_acercade.setIndent(0)
        self.lblCedula_registro_estudiante_2 = QLabel(self.widget)
        self.lblCedula_registro_estudiante_2.setObjectName(u"lblCedula_registro_estudiante_2")
        self.lblCedula_registro_estudiante_2.setGeometry(QRect(60, 270, 371, 171))
        self.lblCedula_registro_estudiante_2.setMinimumSize(QSize(0, 50))
        self.lblCedula_registro_estudiante_2.setMaximumSize(QSize(16777215, 200))
        self.lblCedula_registro_estudiante_2.setFont(font3)
        self.lblCedula_registro_estudiante_2.setStyleSheet(u"color: #2d2d2d;\n"
"border: 1px solid transparent;\n"
"border-radius: 10px;\n"
"background-color: transparent;")
        self.lblCedula_registro_estudiante_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblCedula_registro_estudiante_2.setWordWrap(True)

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Acerca_de)

        QMetaObject.connectSlotsByName(Acerca_de)
    # setupUi

    def retranslateUi(self, Acerca_de):
        Acerca_de.setWindowTitle(QCoreApplication.translate("Acerca_de", u"Dialog", None))
        self.lblLogo_UPTJAA_acercade.setText("")
        self.lblTitulo_logo_estu.setText(QCoreApplication.translate("Acerca_de", u"Sistema Interno de Registro Acad\u00e9mico", None))
        self.btnCerrar.setText(QCoreApplication.translate("Acerca_de", u"Cerrar", None))
        self.lblCedula_registro_estudiante.setText(QCoreApplication.translate("Acerca_de", u"Sistema dise\u00f1ado e implementado espec\u00edficamente para la E.B. \"Dr. Severiano Rodr\u00edguez\". Este proyecto representa la culminaci\u00f3n del trayecto acad\u00e9mico del grupo de desarrollo para la obtenci\u00f3n del t\u00edtulo de TSU en Inform\u00e1tica, en la Universidad Polit\u00e9cnica Territorial \"Jos\u00e9 Ant\u00f3nio Anzo\u00e1tegui\".", None))
        self.lblLogo_SIRA_acercade.setText("")
        self.lblCedula_registro_estudiante_2.setText(QCoreApplication.translate("Acerca_de", u"Equipo de Desarrollo:\n"
"\n"
"\u25b6 Jim\u00e9nez, Jorge \u2014 C.I: 25.852.090\n"
"\n"
"\u25b6 Gonz\u00e1lez, Jes\u00fas \u2014 C.I: 30.795.827\n"
"\n"
"\u25b6 Malav\u00e9, Carlos \u2014 C.I: 30.953.463\n"
"\n"
"Tutor Acad\u00e9mico: Ing. Nohem\u00ed G\u00fcacheque", None))
    # retranslateUi

