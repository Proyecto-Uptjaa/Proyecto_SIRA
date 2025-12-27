# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro_emple.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QDateEdit,
    QDialog, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QWidget)
from resources import resources_ui
from resources import resources_ui

class Ui_registro_emple(object):
    def setupUi(self, registro_emple):
        if not registro_emple.objectName():
            registro_emple.setObjectName(u"registro_emple")
        registro_emple.resize(1000, 600)
        registro_emple.setMinimumSize(QSize(1000, 600))
        registro_emple.setMaximumSize(QSize(1000, 600))
        registro_emple.setStyleSheet(u"background-color: #f5f6fa;")
        self.gridLayout = QGridLayout(registro_emple)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(registro_emple)
        self.widget.setObjectName(u"widget")
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
"    padding: 2px 5px;\n"
"    background-color: white;\n"
"	color: #2d2d2d;\n"
"}")
        self.lneCedula_reg_emple = QLineEdit(self.widget)
        self.lneCedula_reg_emple.setObjectName(u"lneCedula_reg_emple")
        self.lneCedula_reg_emple.setGeometry(QRect(120, 40, 200, 31))
        self.lneCedula_reg_emple.setMinimumSize(QSize(200, 30))
        self.lneCedula_reg_emple.setMaximumSize(QSize(200, 50))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(13)
        self.lneCedula_reg_emple.setFont(font)
        self.lneCedula_reg_emple.setStyleSheet(u"")
        self.lneCedula_reg_emple.setMaxLength(9)
        self.lneCedula_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneCedula_reg_emple.setReadOnly(False)
        self.lneCedula_reg_emple.setClearButtonEnabled(True)
        self.lblCedula_registro_estudiante = QLabel(self.widget)
        self.lblCedula_registro_estudiante.setObjectName(u"lblCedula_registro_estudiante")
        self.lblCedula_registro_estudiante.setGeometry(QRect(30, 40, 81, 31))
        self.lblCedula_registro_estudiante.setMinimumSize(QSize(50, 30))
        self.lblCedula_registro_estudiante.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblCedula_registro_estudiante.setFont(font1)
        self.lblCedula_registro_estudiante.setStyleSheet(u"color: #2d2d2d;\n"
"border: 1px solid transparent;\n"
"border-radius: 10px;\n"
"background-color: transparent;")
        self.lblCedula_registro_estudiante.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblCedula_registro_estudiante.setWordWrap(True)
        self.frameTabla_student = QFrame(self.widget)
        self.frameTabla_student.setObjectName(u"frameTabla_student")
        self.frameTabla_student.setGeometry(QRect(20, 130, 941, 351))
        self.frameTabla_student.setMinimumSize(QSize(900, 311))
        self.frameTabla_student.setMaximumSize(QSize(950, 500))
        self.frameTabla_student.setStyleSheet(u"QFrame#frameTabla_student {\n"
"    border: 1px solid #1565C0;\n"
"    border-radius: 12px;\n"
"    background-color: white;\n"
"}\n"
"")
        self.frameTabla_student.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTabla_student.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameTabla_student)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackRegistro_emple = QStackedWidget(self.frameTabla_student)
        self.stackRegistro_emple.setObjectName(u"stackRegistro_emple")
        self.stackRegistro_emple.setStyleSheet(u"QStackedWidget#stackRegistro_emple{\n"
"background-color: transparent;\n"
"color: #2d2d2d;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 2px 5px;\n"
"    background-color: white;\n"
"}")
        self.personal_data = QWidget()
        self.personal_data.setObjectName(u"personal_data")
        self.lblStudent_apellido = QLabel(self.personal_data)
        self.lblStudent_apellido.setObjectName(u"lblStudent_apellido")
        self.lblStudent_apellido.setGeometry(QRect(10, 10, 81, 30))
        self.lblStudent_apellido.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido.setFont(font1)
        self.lblStudent_apellido.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneApellidos_reg_emple = QLineEdit(self.personal_data)
        self.lneApellidos_reg_emple.setObjectName(u"lneApellidos_reg_emple")
        self.lneApellidos_reg_emple.setGeometry(QRect(100, 10, 400, 30))
        self.lneApellidos_reg_emple.setMinimumSize(QSize(400, 30))
        self.lneApellidos_reg_emple.setMaximumSize(QSize(400, 30))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.lneApellidos_reg_emple.setFont(font2)
        self.lneApellidos_reg_emple.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lneApellidos_reg_emple.setStyleSheet(u"")
        self.lneApellidos_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneNombres_reg_emple = QLineEdit(self.personal_data)
        self.lneNombres_reg_emple.setObjectName(u"lneNombres_reg_emple")
        self.lneNombres_reg_emple.setGeometry(QRect(100, 50, 400, 30))
        self.lneNombres_reg_emple.setMinimumSize(QSize(400, 30))
        self.lneNombres_reg_emple.setMaximumSize(QSize(400, 30))
        self.lneNombres_reg_emple.setFont(font2)
        self.lneNombres_reg_emple.setStyleSheet(u"")
        self.lneNombres_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_nombres = QLabel(self.personal_data)
        self.lblStudent_nombres.setObjectName(u"lblStudent_nombres")
        self.lblStudent_nombres.setGeometry(QRect(10, 50, 81, 30))
        self.lblStudent_nombres.setMinimumSize(QSize(0, 30))
        self.lblStudent_nombres.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_nombres.setFont(font1)
        self.lblStudent_nombres.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_nombres.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_fechaNac = QLabel(self.personal_data)
        self.lblStudent_fechaNac.setObjectName(u"lblStudent_fechaNac")
        self.lblStudent_fechaNac.setGeometry(QRect(510, 10, 91, 30))
        self.lblStudent_fechaNac.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac.setFont(font1)
        self.lblStudent_fechaNac.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneEdad_reg_emple = QLineEdit(self.personal_data)
        self.lneEdad_reg_emple.setObjectName(u"lneEdad_reg_emple")
        self.lneEdad_reg_emple.setGeometry(QRect(840, 10, 61, 30))
        self.lneEdad_reg_emple.setMinimumSize(QSize(50, 30))
        self.lneEdad_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneEdad_reg_emple.setFont(font2)
        self.lneEdad_reg_emple.setStyleSheet(u"")
        self.lneEdad_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneEdad_reg_emple.setReadOnly(True)
        self.lblStudent_edad = QLabel(self.personal_data)
        self.lblStudent_edad.setObjectName(u"lblStudent_edad")
        self.lblStudent_edad.setGeometry(QRect(770, 10, 61, 30))
        self.lblStudent_edad.setMinimumSize(QSize(0, 30))
        self.lblStudent_edad.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_edad.setFont(font1)
        self.lblStudent_edad.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_edad.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneGenero_reg_emple = QLineEdit(self.personal_data)
        self.lneGenero_reg_emple.setObjectName(u"lneGenero_reg_emple")
        self.lneGenero_reg_emple.setGeometry(QRect(840, 50, 61, 30))
        self.lneGenero_reg_emple.setMinimumSize(QSize(50, 30))
        self.lneGenero_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneGenero_reg_emple.setFont(font2)
        self.lneGenero_reg_emple.setStyleSheet(u"")
        self.lneGenero_reg_emple.setMaxLength(1)
        self.lneGenero_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_genero = QLabel(self.personal_data)
        self.lblStudent_genero.setObjectName(u"lblStudent_genero")
        self.lblStudent_genero.setGeometry(QRect(770, 50, 61, 30))
        self.lblStudent_genero.setMinimumSize(QSize(0, 30))
        self.lblStudent_genero.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_genero.setFont(font1)
        self.lblStudent_genero.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_genero.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneDir_reg_emple = QLineEdit(self.personal_data)
        self.lneDir_reg_emple.setObjectName(u"lneDir_reg_emple")
        self.lneDir_reg_emple.setGeometry(QRect(100, 100, 801, 60))
        self.lneDir_reg_emple.setMinimumSize(QSize(400, 30))
        self.lneDir_reg_emple.setMaximumSize(QSize(900, 60))
        self.lneDir_reg_emple.setFont(font2)
        self.lneDir_reg_emple.setStyleSheet(u"")
        self.lneDir_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_dir = QLabel(self.personal_data)
        self.lblStudent_dir.setObjectName(u"lblStudent_dir")
        self.lblStudent_dir.setGeometry(QRect(10, 100, 81, 30))
        self.lblStudent_dir.setMinimumSize(QSize(0, 30))
        self.lblStudent_dir.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_dir.setFont(font1)
        self.lblStudent_dir.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_dir.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneNum_reg_emple = QLineEdit(self.personal_data)
        self.lneNum_reg_emple.setObjectName(u"lneNum_reg_emple")
        self.lneNum_reg_emple.setGeometry(QRect(130, 190, 291, 30))
        self.lneNum_reg_emple.setMinimumSize(QSize(100, 30))
        self.lneNum_reg_emple.setMaximumSize(QSize(400, 30))
        self.lneNum_reg_emple.setFont(font2)
        self.lneNum_reg_emple.setStyleSheet(u"")
        self.lneNum_reg_emple.setMaxLength(12)
        self.lneNum_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_31 = QLabel(self.personal_data)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 230, 111, 30))
        self.label_31.setMinimumSize(QSize(0, 30))
        self.label_31.setMaximumSize(QSize(16777215, 30))
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"background-color: transparent;")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_32 = QLabel(self.personal_data)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 190, 111, 30))
        self.label_32.setMinimumSize(QSize(0, 30))
        self.label_32.setMaximumSize(QSize(16777215, 30))
        self.label_32.setFont(font1)
        self.label_32.setStyleSheet(u"background-color: transparent;")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneCorreo_reg_emple = QLineEdit(self.personal_data)
        self.lneCorreo_reg_emple.setObjectName(u"lneCorreo_reg_emple")
        self.lneCorreo_reg_emple.setGeometry(QRect(130, 230, 291, 30))
        self.lneCorreo_reg_emple.setMinimumSize(QSize(100, 30))
        self.lneCorreo_reg_emple.setMaximumSize(QSize(400, 30))
        self.lneCorreo_reg_emple.setFont(font2)
        self.lneCorreo_reg_emple.setStyleSheet(u"")
        self.lneCorreo_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneFechaNac_reg_emple = QDateEdit(self.personal_data)
        self.lneFechaNac_reg_emple.setObjectName(u"lneFechaNac_reg_emple")
        self.lneFechaNac_reg_emple.setGeometry(QRect(610, 10, 151, 30))
        self.lneFechaNac_reg_emple.setMinimumSize(QSize(151, 30))
        self.lneFechaNac_reg_emple.setMaximumSize(QSize(151, 30))
        self.lneFechaNac_reg_emple.setFont(font2)
        self.lneFechaNac_reg_emple.setStyleSheet(u"QDateEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 12px;\n"
"    background-color: white;\n"
"}\n"
"/* Vista de d\u00edas (el grid del calendario) */\n"
"QDateEdit QAbstractItemView {\n"
"    background-color: white;\n"
"    color: #2d2d2d;\n"
"    selection-background-color: #2980b9;\n"
"    selection-color: white;\n"
"}\n"
"/* Botones de navegaci\u00f3n (mes anterior/siguiente) y combos de mes/a\u00f1o */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #90caf9;   /* Fondo del encabezado */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: #2d2d2d;              /* Texto de mes y a\u00f1o */\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 4px 8px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #d6eaff;   /* Hover sobre mes/a\u00f1o o flechas */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Hover sobre los d\u00edas */\n"
"QDateEdit QAbs"
                        "tractItemView::item:hover {\n"
"    background-color: #2980b9;   /* azul claro */\n"
"    color: #000;\n"
"}\n"
"")
        self.lneFechaNac_reg_emple.setCalendarPopup(True)
        self.lblStudent_fechaNac_repre_5 = QLabel(self.personal_data)
        self.lblStudent_fechaNac_repre_5.setObjectName(u"lblStudent_fechaNac_repre_5")
        self.lblStudent_fechaNac_repre_5.setGeometry(QRect(540, 50, 41, 30))
        self.lblStudent_fechaNac_repre_5.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_5.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_5.setFont(font1)
        self.lblStudent_fechaNac_repre_5.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneRIF_reg_emple = QLineEdit(self.personal_data)
        self.lneRIF_reg_emple.setObjectName(u"lneRIF_reg_emple")
        self.lneRIF_reg_emple.setGeometry(QRect(590, 50, 151, 30))
        self.lneRIF_reg_emple.setMinimumSize(QSize(100, 30))
        self.lneRIF_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneRIF_reg_emple.setFont(font2)
        self.lneRIF_reg_emple.setStyleSheet(u"")
        self.lneRIF_reg_emple.setMaxLength(15)
        self.lneRIF_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneCentroV_reg_emple = QLineEdit(self.personal_data)
        self.lneCentroV_reg_emple.setObjectName(u"lneCentroV_reg_emple")
        self.lneCentroV_reg_emple.setGeometry(QRect(130, 270, 400, 30))
        self.lneCentroV_reg_emple.setMinimumSize(QSize(400, 30))
        self.lneCentroV_reg_emple.setMaximumSize(QSize(400, 30))
        self.lneCentroV_reg_emple.setFont(font2)
        self.lneCentroV_reg_emple.setStyleSheet(u"")
        self.lneCentroV_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_nombres_3 = QLabel(self.personal_data)
        self.lblStudent_nombres_3.setObjectName(u"lblStudent_nombres_3")
        self.lblStudent_nombres_3.setGeometry(QRect(0, 270, 131, 30))
        self.lblStudent_nombres_3.setMinimumSize(QSize(0, 30))
        self.lblStudent_nombres_3.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_nombres_3.setFont(font1)
        self.lblStudent_nombres_3.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_nombres_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackRegistro_emple.addWidget(self.personal_data)
        self.representante = QWidget()
        self.representante.setObjectName(u"representante")
        self.lblTituloemple = QLabel(self.representante)
        self.lblTituloemple.setObjectName(u"lblTituloemple")
        self.lblTituloemple.setGeometry(QRect(310, 0, 351, 41))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(17)
        font3.setBold(True)
        self.lblTituloemple.setFont(font3)
        self.lblTituloemple.setStyleSheet(u"")
        self.lblTituloemple.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneFechaIngreso_reg_emple = QDateEdit(self.representante)
        self.lneFechaIngreso_reg_emple.setObjectName(u"lneFechaIngreso_reg_emple")
        self.lneFechaIngreso_reg_emple.setGeometry(QRect(650, 70, 151, 30))
        self.lneFechaIngreso_reg_emple.setMinimumSize(QSize(151, 30))
        self.lneFechaIngreso_reg_emple.setMaximumSize(QSize(151, 30))
        self.lneFechaIngreso_reg_emple.setFont(font2)
        self.lneFechaIngreso_reg_emple.setStyleSheet(u"QDateEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 3px 12px;\n"
"    background-color: white;\n"
"}\n"
"/* Vista de d\u00edas (el grid del calendario) */\n"
"QDateEdit QAbstractItemView {\n"
"    background-color: white;\n"
"    color: #2d2d2d;\n"
"    selection-background-color: #2980b9;\n"
"    selection-color: white;\n"
"}\n"
"/* Botones de navegaci\u00f3n (mes anterior/siguiente) y combos de mes/a\u00f1o */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #90caf9;   /* Fondo del encabezado */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: #2d2d2d;              /* Texto de mes y a\u00f1o */\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 4px 8px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #d6eaff;   /* Hover sobre mes/a\u00f1o o flechas */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Hover sobre los d\u00edas */\n"
"QDateEdit QAbs"
                        "tractItemView::item:hover {\n"
"    background-color: #2980b9;   /* azul claro */\n"
"    color: #000;\n"
"}\n"
"")
        self.lneFechaIngreso_reg_emple.setCalendarPopup(True)
        self.lblStudent_nombres_2 = QLabel(self.representante)
        self.lblStudent_nombres_2.setObjectName(u"lblStudent_nombres_2")
        self.lblStudent_nombres_2.setGeometry(QRect(10, 120, 81, 30))
        self.lblStudent_nombres_2.setMinimumSize(QSize(0, 30))
        self.lblStudent_nombres_2.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_nombres_2.setFont(font1)
        self.lblStudent_nombres_2.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_nombres_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_fechaNac_repre_4 = QLabel(self.representante)
        self.lblStudent_fechaNac_repre_4.setObjectName(u"lblStudent_fechaNac_repre_4")
        self.lblStudent_fechaNac_repre_4.setGeometry(QRect(520, 120, 121, 30))
        self.lblStudent_fechaNac_repre_4.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_4.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_4.setFont(font1)
        self.lblStudent_fechaNac_repre_4.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_apellido_repre = QLabel(self.representante)
        self.lblStudent_apellido_repre.setObjectName(u"lblStudent_apellido_repre")
        self.lblStudent_apellido_repre.setGeometry(QRect(10, 70, 81, 30))
        self.lblStudent_apellido_repre.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_repre.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_repre.setFont(font1)
        self.lblStudent_apellido_repre.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido_repre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_fechaNac_repre = QLabel(self.representante)
        self.lblStudent_fechaNac_repre.setObjectName(u"lblStudent_fechaNac_repre")
        self.lblStudent_fechaNac_repre.setGeometry(QRect(520, 70, 121, 30))
        self.lblStudent_fechaNac_repre.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre.setFont(font1)
        self.lblStudent_fechaNac_repre.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneCarnet_reg_emple = QLineEdit(self.representante)
        self.lneCarnet_reg_emple.setObjectName(u"lneCarnet_reg_emple")
        self.lneCarnet_reg_emple.setGeometry(QRect(650, 120, 151, 30))
        self.lneCarnet_reg_emple.setMinimumSize(QSize(100, 30))
        self.lneCarnet_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneCarnet_reg_emple.setFont(font2)
        self.lneCarnet_reg_emple.setStyleSheet(u"")
        self.lneCarnet_reg_emple.setMaxLength(15)
        self.lneCarnet_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.frmTitulo_emple = QFrame(self.representante)
        self.frmTitulo_emple.setObjectName(u"frmTitulo_emple")
        self.frmTitulo_emple.setGeometry(QRect(100, 70, 400, 30))
        self.frmTitulo_emple.setMinimumSize(QSize(400, 30))
        self.frmTitulo_emple.setMaximumSize(QSize(400, 30))
        self.frmTitulo_emple.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 2px solid #2980b9;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frmTitulo_emple.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmTitulo_emple.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxTitulo_reg_emple = QComboBox(self.frmTitulo_emple)
        self.cbxTitulo_reg_emple.addItem("")
        self.cbxTitulo_reg_emple.addItem("")
        self.cbxTitulo_reg_emple.addItem("")
        self.cbxTitulo_reg_emple.addItem("")
        self.cbxTitulo_reg_emple.addItem("")
        self.cbxTitulo_reg_emple.setObjectName(u"cbxTitulo_reg_emple")
        self.cbxTitulo_reg_emple.setGeometry(QRect(5, 4, 390, 20))
        self.cbxTitulo_reg_emple.setMinimumSize(QSize(390, 0))
        self.cbxTitulo_reg_emple.setMaximumSize(QSize(390, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.cbxTitulo_reg_emple.setFont(font4)
        self.cbxTitulo_reg_emple.setStyleSheet(u"background-color: white;\n"
"border: transparent;")
        self.cbxTitulo_reg_emple.setIconSize(QSize(10, 10))
        self.lblStudent_fechaNac_repre_6 = QLabel(self.representante)
        self.lblStudent_fechaNac_repre_6.setObjectName(u"lblStudent_fechaNac_repre_6")
        self.lblStudent_fechaNac_repre_6.setGeometry(QRect(-10, 170, 121, 30))
        self.lblStudent_fechaNac_repre_6.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_6.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_6.setFont(font1)
        self.lblStudent_fechaNac_repre_6.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneRAC_reg_emple = QLineEdit(self.representante)
        self.lneRAC_reg_emple.setObjectName(u"lneRAC_reg_emple")
        self.lneRAC_reg_emple.setGeometry(QRect(100, 170, 151, 30))
        self.lneRAC_reg_emple.setMinimumSize(QSize(100, 30))
        self.lneRAC_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneRAC_reg_emple.setFont(font2)
        self.lneRAC_reg_emple.setStyleSheet(u"")
        self.lneRAC_reg_emple.setMaxLength(15)
        self.lneRAC_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblHoras_reg_emple = QLabel(self.representante)
        self.lblHoras_reg_emple.setObjectName(u"lblHoras_reg_emple")
        self.lblHoras_reg_emple.setGeometry(QRect(270, 170, 141, 30))
        self.lblHoras_reg_emple.setMinimumSize(QSize(0, 30))
        self.lblHoras_reg_emple.setMaximumSize(QSize(16777215, 30))
        self.lblHoras_reg_emple.setFont(font1)
        self.lblHoras_reg_emple.setStyleSheet(u"background-color: transparent;")
        self.lblHoras_reg_emple.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneHoras_reg_emple = QLineEdit(self.representante)
        self.lneHoras_reg_emple.setObjectName(u"lneHoras_reg_emple")
        self.lneHoras_reg_emple.setGeometry(QRect(420, 170, 151, 30))
        self.lneHoras_reg_emple.setMinimumSize(QSize(100, 30))
        self.lneHoras_reg_emple.setMaximumSize(QSize(300, 30))
        self.lneHoras_reg_emple.setFont(font2)
        self.lneHoras_reg_emple.setStyleSheet(u"")
        self.lneHoras_reg_emple.setMaxLength(9)
        self.lneHoras_reg_emple.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.frmTitulo_emple_2 = QFrame(self.representante)
        self.frmTitulo_emple_2.setObjectName(u"frmTitulo_emple_2")
        self.frmTitulo_emple_2.setGeometry(QRect(100, 120, 400, 30))
        self.frmTitulo_emple_2.setMinimumSize(QSize(400, 30))
        self.frmTitulo_emple_2.setMaximumSize(QSize(400, 30))
        self.frmTitulo_emple_2.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 2px solid #2980b9;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"")
        self.frmTitulo_emple_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmTitulo_emple_2.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxCargo_reg_emple = QComboBox(self.frmTitulo_emple_2)
        self.cbxCargo_reg_emple.addItem("")
        self.cbxCargo_reg_emple.setObjectName(u"cbxCargo_reg_emple")
        self.cbxCargo_reg_emple.setGeometry(QRect(5, 4, 390, 20))
        self.cbxCargo_reg_emple.setMinimumSize(QSize(390, 0))
        self.cbxCargo_reg_emple.setMaximumSize(QSize(390, 30))
        self.cbxCargo_reg_emple.setFont(font4)
        self.cbxCargo_reg_emple.setStyleSheet(u"background-color: white;\n"
"border: transparent;")
        self.cbxCargo_reg_emple.setIconSize(QSize(10, 10))
        self.stackRegistro_emple.addWidget(self.representante)

        self.horizontalLayout.addWidget(self.stackRegistro_emple)

        self.btnDatosPersonales_reg_emple = QPushButton(self.widget)
        self.pestanas_ficha = QButtonGroup(registro_emple)
        self.pestanas_ficha.setObjectName(u"pestanas_ficha")
        self.pestanas_ficha.addButton(self.btnDatosPersonales_reg_emple)
        self.btnDatosPersonales_reg_emple.setObjectName(u"btnDatosPersonales_reg_emple")
        self.btnDatosPersonales_reg_emple.setGeometry(QRect(30, 90, 131, 45))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDatosPersonales_reg_emple.sizePolicy().hasHeightForWidth())
        self.btnDatosPersonales_reg_emple.setSizePolicy(sizePolicy)
        self.btnDatosPersonales_reg_emple.setMinimumSize(QSize(80, 25))
        self.btnDatosPersonales_reg_emple.setMaximumSize(QSize(200, 45))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.btnDatosPersonales_reg_emple.setFont(font5)
        self.btnDatosPersonales_reg_emple.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnDatosPersonales_reg_emple.setStyleSheet(u"QPushButton {\n"
"   background: #2980b9;\n"
"	color: #FFFFFF;\n"
"    border: 1px solid #2980b9;\n"
"    padding: 2px 10px;\n"
"    border-radius: 10px;\n"
"	text-align: left;\n"
"    padding-left: 12px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #FFFFFF;\n"
"	color: #2980b9;\n"
" \n"
"}")
        self.btnDatosPersonales_reg_emple.setIconSize(QSize(50, 50))
        self.btnDatosPersonales_reg_emple.setCheckable(True)
        self.btnDatosPersonales_reg_emple.setChecked(True)
        self.btnDatosPersonales_reg_emple.setAutoExclusive(False)
        self.btnDatosLaborales_reg_emple = QPushButton(self.widget)
        self.pestanas_ficha.addButton(self.btnDatosLaborales_reg_emple)
        self.btnDatosLaborales_reg_emple.setObjectName(u"btnDatosLaborales_reg_emple")
        self.btnDatosLaborales_reg_emple.setGeometry(QRect(160, 90, 141, 45))
        sizePolicy.setHeightForWidth(self.btnDatosLaborales_reg_emple.sizePolicy().hasHeightForWidth())
        self.btnDatosLaborales_reg_emple.setSizePolicy(sizePolicy)
        self.btnDatosLaborales_reg_emple.setMinimumSize(QSize(80, 25))
        self.btnDatosLaborales_reg_emple.setMaximumSize(QSize(200, 45))
        self.btnDatosLaborales_reg_emple.setFont(font5)
        self.btnDatosLaborales_reg_emple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDatosLaborales_reg_emple.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnDatosLaborales_reg_emple.setStyleSheet(u"QPushButton {\n"
"   background: #2980b9;\n"
"	color: #FFFFFF;\n"
"    border: 1px solid #2980b9;\n"
"    padding: 2px 16px;\n"
"    border-radius: 10px;\n"
"	text-align: left;\n"
"    padding-left: 20px; /* Mueve el \u00edcono a la derecha un poco */\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #FFFFFF;\n"
"	color: #2980b9;\n"
"	min-width: 80px;\n"
"    max-width: 80px;\n"
"    min-height: 18px;\n"
"    max-height: 18px;\n"
"}")
        self.btnDatosLaborales_reg_emple.setIconSize(QSize(50, 50))
        self.btnDatosLaborales_reg_emple.setCheckable(True)
        self.btnDatosLaborales_reg_emple.setChecked(False)
        self.btnDatosLaborales_reg_emple.setAutoExclusive(False)
        self.btnDatosLaborales_reg_emple.setAutoDefault(False)
        self.lblTitulo_logo_estu = QLabel(self.widget)
        self.lblTitulo_logo_estu.setObjectName(u"lblTitulo_logo_estu")
        self.lblTitulo_logo_estu.setGeometry(QRect(701, 10, 191, 81))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(19)
        font6.setBold(True)
        self.lblTitulo_logo_estu.setFont(font6)
        self.lblTitulo_logo_estu.setStyleSheet(u"color: #2d2d2d")
        self.lblTitulo_logo_estu.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_logo_estu.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_logo_estu.setScaledContents(False)
        self.lblTitulo_logo_estu.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_logo_estu.setWordWrap(True)
        self.lblTitulo_logo_estu.setIndent(0)
        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(900, 20, 3, 61))
        self.line_2.setMinimumSize(QSize(3, 61))
        self.line_2.setMaximumSize(QSize(3, 61))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblLogo_estu = QLabel(self.widget)
        self.lblLogo_estu.setObjectName(u"lblLogo_estu")
        self.lblLogo_estu.setGeometry(QRect(910, 20, 51, 61))
        self.lblLogo_estu.setMinimumSize(QSize(50, 50))
        self.lblLogo_estu.setMaximumSize(QSize(130, 70))
        self.lblLogo_estu.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_estu.setScaledContents(True)
        self.btnGuardar_reg_emple = QPushButton(self.widget)
        self.btnGuardar_reg_emple.setObjectName(u"btnGuardar_reg_emple")
        self.btnGuardar_reg_emple.setGeometry(QRect(841, 510, 120, 51))
        sizePolicy.setHeightForWidth(self.btnGuardar_reg_emple.sizePolicy().hasHeightForWidth())
        self.btnGuardar_reg_emple.setSizePolicy(sizePolicy)
        self.btnGuardar_reg_emple.setMinimumSize(QSize(120, 40))
        self.btnGuardar_reg_emple.setMaximumSize(QSize(120, 60))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(13)
        font7.setBold(True)
        self.btnGuardar_reg_emple.setFont(font7)
        self.btnGuardar_reg_emple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGuardar_reg_emple.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnGuardar_reg_emple.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/guardar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGuardar_reg_emple.setIcon(icon)
        self.btnGuardar_reg_emple.setIconSize(QSize(20, 20))
        self.btnLimpiar_reg_emple = QPushButton(self.widget)
        self.btnLimpiar_reg_emple.setObjectName(u"btnLimpiar_reg_emple")
        self.btnLimpiar_reg_emple.setGeometry(QRect(680, 530, 141, 31))
        sizePolicy.setHeightForWidth(self.btnLimpiar_reg_emple.sizePolicy().hasHeightForWidth())
        self.btnLimpiar_reg_emple.setSizePolicy(sizePolicy)
        self.btnLimpiar_reg_emple.setMinimumSize(QSize(120, 30))
        self.btnLimpiar_reg_emple.setMaximumSize(QSize(150, 40))
        self.btnLimpiar_reg_emple.setFont(font5)
        self.btnLimpiar_reg_emple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLimpiar_reg_emple.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnLimpiar_reg_emple.setStyleSheet(u"QPushButton {\n"
"   background-color: white;\n"
"    color: #2980b9;\n"
"    border: 1.5px solid #2980b9;\n"
"    padding: 2px 2px;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #E3F2FD;\n"
"	border: 1.5px solid #0D47A1;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/limpiar_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLimpiar_reg_emple.setIcon(icon1)
        self.lneCedula_reg_emple.raise_()
        self.lblCedula_registro_estudiante.raise_()
        self.btnDatosPersonales_reg_emple.raise_()
        self.btnDatosLaborales_reg_emple.raise_()
        self.frameTabla_student.raise_()
        self.lblTitulo_logo_estu.raise_()
        self.line_2.raise_()
        self.lblLogo_estu.raise_()
        self.btnGuardar_reg_emple.raise_()
        self.btnLimpiar_reg_emple.raise_()

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(registro_emple)

        self.stackRegistro_emple.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(registro_emple)
    # setupUi

    def retranslateUi(self, registro_emple):
        registro_emple.setWindowTitle(QCoreApplication.translate("registro_emple", u"Dialog", None))
        self.lneCedula_reg_emple.setText("")
        self.lneCedula_reg_emple.setPlaceholderText("")
        self.lblCedula_registro_estudiante.setText(QCoreApplication.translate("registro_emple", u"C\u00e9dula", None))
        self.lblStudent_apellido.setText(QCoreApplication.translate("registro_emple", u"Apellidos", None))
        self.lneApellidos_reg_emple.setText("")
        self.lneApellidos_reg_emple.setPlaceholderText("")
        self.lneNombres_reg_emple.setText("")
        self.lneNombres_reg_emple.setPlaceholderText("")
        self.lblStudent_nombres.setText(QCoreApplication.translate("registro_emple", u"Nombres", None))
        self.lblStudent_fechaNac.setText(QCoreApplication.translate("registro_emple", u"Fecha Nac.", None))
        self.lneEdad_reg_emple.setText("")
        self.lneEdad_reg_emple.setPlaceholderText("")
        self.lblStudent_edad.setText(QCoreApplication.translate("registro_emple", u"Edad", None))
        self.lneGenero_reg_emple.setText("")
        self.lneGenero_reg_emple.setPlaceholderText("")
        self.lblStudent_genero.setText(QCoreApplication.translate("registro_emple", u"G\u00e9nero", None))
        self.lneDir_reg_emple.setText("")
        self.lneDir_reg_emple.setPlaceholderText("")
        self.lblStudent_dir.setText(QCoreApplication.translate("registro_emple", u"Direcci\u00f3n", None))
        self.lneNum_reg_emple.setText("")
        self.lneNum_reg_emple.setPlaceholderText("")
        self.label_31.setText(QCoreApplication.translate("registro_emple", u"Correo Elect.", None))
        self.label_32.setText(QCoreApplication.translate("registro_emple", u"Num. Contact.", None))
        self.lneCorreo_reg_emple.setText("")
        self.lneCorreo_reg_emple.setPlaceholderText("")
        self.lneFechaNac_reg_emple.setDisplayFormat(QCoreApplication.translate("registro_emple", u"yyyy/M/d", None))
        self.lblStudent_fechaNac_repre_5.setText(QCoreApplication.translate("registro_emple", u"RIF", None))
        self.lneRIF_reg_emple.setText("")
        self.lneRIF_reg_emple.setPlaceholderText("")
        self.lneCentroV_reg_emple.setText("")
        self.lneCentroV_reg_emple.setPlaceholderText("")
        self.lblStudent_nombres_3.setText(QCoreApplication.translate("registro_emple", u"Centro votaci\u00f3n", None))
        self.lblTituloemple.setText(QCoreApplication.translate("registro_emple", u"Datos laborales", None))
        self.lneFechaIngreso_reg_emple.setDisplayFormat(QCoreApplication.translate("registro_emple", u"yyyy/M/d", None))
        self.lblStudent_nombres_2.setText(QCoreApplication.translate("registro_emple", u"Cargo", None))
        self.lblStudent_fechaNac_repre_4.setText(QCoreApplication.translate("registro_emple", u"Num. Carnet", None))
        self.lblStudent_apellido_repre.setText(QCoreApplication.translate("registro_emple", u"Titulo", None))
        self.lblStudent_fechaNac_repre.setText(QCoreApplication.translate("registro_emple", u"Fecha Ingreso", None))
        self.lneCarnet_reg_emple.setText("")
        self.lneCarnet_reg_emple.setPlaceholderText("")
        self.cbxTitulo_reg_emple.setItemText(0, QCoreApplication.translate("registro_emple", u"Seleccione t\u00edtulo obtenido", None))
        self.cbxTitulo_reg_emple.setItemText(1, QCoreApplication.translate("registro_emple", u"Bachiller", None))
        self.cbxTitulo_reg_emple.setItemText(2, QCoreApplication.translate("registro_emple", u"T.S.U", None))
        self.cbxTitulo_reg_emple.setItemText(3, QCoreApplication.translate("registro_emple", u"Profesional Universitario", None))
        self.cbxTitulo_reg_emple.setItemText(4, QCoreApplication.translate("registro_emple", u"Postgrado", None))

        self.lblStudent_fechaNac_repre_6.setText(QCoreApplication.translate("registro_emple", u"C\u00f3digo RAC", None))
        self.lneRAC_reg_emple.setText("")
        self.lneRAC_reg_emple.setPlaceholderText("")
        self.lblHoras_reg_emple.setText(QCoreApplication.translate("registro_emple", u"Horas acad\u00e9micas", None))
        self.lneHoras_reg_emple.setText("")
        self.lneHoras_reg_emple.setPlaceholderText("")
        self.cbxCargo_reg_emple.setItemText(0, QCoreApplication.translate("registro_emple", u"Seleccione cargo", None))

#if QT_CONFIG(tooltip)
        self.btnDatosPersonales_reg_emple.setToolTip(QCoreApplication.translate("registro_emple", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.btnDatosPersonales_reg_emple.setText(QCoreApplication.translate("registro_emple", u"Datos personales", None))
#if QT_CONFIG(tooltip)
        self.btnDatosLaborales_reg_emple.setToolTip(QCoreApplication.translate("registro_emple", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.btnDatosLaborales_reg_emple.setText(QCoreApplication.translate("registro_emple", u"Datos laborales", None))
        self.lblTitulo_logo_estu.setText(QCoreApplication.translate("registro_emple", u"Nuevo registro de empleado", None))
        self.lblLogo_estu.setText("")
        self.btnGuardar_reg_emple.setText(QCoreApplication.translate("registro_emple", u"Guardar", None))
        self.btnLimpiar_reg_emple.setText(QCoreApplication.translate("registro_emple", u"Limpiar campos", None))
    # retranslateUi

