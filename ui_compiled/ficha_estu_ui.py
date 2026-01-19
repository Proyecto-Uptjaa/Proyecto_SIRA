# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ficha_estu.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QComboBox,
    QDateEdit, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QTableView,
    QToolButton, QWidget)
from resources import resources_ui
from resources import resources_ui
from resources import resources_ui

class Ui_ficha_estu(object):
    def setupUi(self, ficha_estu):
        if not ficha_estu.objectName():
            ficha_estu.setObjectName(u"ficha_estu")
        ficha_estu.resize(1000, 600)
        ficha_estu.setMinimumSize(QSize(1000, 600))
        ficha_estu.setMaximumSize(QSize(1000, 600))
        ficha_estu.setStyleSheet(u"background-color: #f5f6fa;")
        self.gridLayout = QGridLayout(ficha_estu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(ficha_estu)
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
"    padding: 2px 3px;\n"
"    background-color: white;\n"
"	color: #2d2d2d;\n"
"}")
        self.lneCedula_ficha_estu = QLineEdit(self.widget)
        self.lneCedula_ficha_estu.setObjectName(u"lneCedula_ficha_estu")
        self.lneCedula_ficha_estu.setGeometry(QRect(120, 40, 200, 30))
        self.lneCedula_ficha_estu.setMinimumSize(QSize(200, 30))
        self.lneCedula_ficha_estu.setMaximumSize(QSize(200, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.lneCedula_ficha_estu.setFont(font1)
        self.lneCedula_ficha_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneCedula_ficha_estu.setStyleSheet(u"")
        self.lneCedula_ficha_estu.setMaxLength(15)
        self.lneCedula_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneCedula_ficha_estu.setClearButtonEnabled(True)
        self.frameTabla_student = QFrame(self.widget)
        self.frameTabla_student.setObjectName(u"frameTabla_student")
        self.frameTabla_student.setGeometry(QRect(20, 130, 941, 371))
        self.frameTabla_student.setMinimumSize(QSize(900, 311))
        self.frameTabla_student.setMaximumSize(QSize(950, 500))
        self.frameTabla_student.setStyleSheet(u"QFrame#frameTabla_student {\n"
"    border: 1px solid #2980b9;\n"
"    border-radius: 12px;\n"
"    background-color: white;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"    background-color: white;\n"
"}")
        self.frameTabla_student.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTabla_student.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameTabla_student)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackFicha_estu = QStackedWidget(self.frameTabla_student)
        self.stackFicha_estu.setObjectName(u"stackFicha_estu")
        self.stackFicha_estu.setStyleSheet(u"QStackedWidget#stackFicha_estu{\n"
"background-color: transparent;\n"
"color: #2d2d2d;}\n"
"\n"
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
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.lblStudent_apellido.setFont(font2)
        self.lblStudent_apellido.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneApellido_ficha_estu = QLineEdit(self.personal_data)
        self.lneApellido_ficha_estu.setObjectName(u"lneApellido_ficha_estu")
        self.lneApellido_ficha_estu.setGeometry(QRect(100, 10, 400, 30))
        self.lneApellido_ficha_estu.setMinimumSize(QSize(400, 30))
        self.lneApellido_ficha_estu.setMaximumSize(QSize(400, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(13)
        self.lneApellido_ficha_estu.setFont(font3)
        self.lneApellido_ficha_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneApellido_ficha_estu.setStyleSheet(u"")
        self.lneApellido_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneNombre_ficha_estu = QLineEdit(self.personal_data)
        self.lneNombre_ficha_estu.setObjectName(u"lneNombre_ficha_estu")
        self.lneNombre_ficha_estu.setGeometry(QRect(100, 50, 400, 30))
        self.lneNombre_ficha_estu.setMinimumSize(QSize(400, 30))
        self.lneNombre_ficha_estu.setMaximumSize(QSize(400, 30))
        self.lneNombre_ficha_estu.setFont(font3)
        self.lneNombre_ficha_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneNombre_ficha_estu.setStyleSheet(u"")
        self.lneNombre_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_nombres = QLabel(self.personal_data)
        self.lblStudent_nombres.setObjectName(u"lblStudent_nombres")
        self.lblStudent_nombres.setGeometry(QRect(10, 50, 81, 30))
        self.lblStudent_nombres.setMinimumSize(QSize(0, 30))
        self.lblStudent_nombres.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_nombres.setFont(font2)
        self.lblStudent_nombres.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_nombres.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_lugarNac = QLabel(self.personal_data)
        self.lblStudent_lugarNac.setObjectName(u"lblStudent_lugarNac")
        self.lblStudent_lugarNac.setGeometry(QRect(510, 50, 91, 30))
        self.lblStudent_lugarNac.setMinimumSize(QSize(0, 30))
        self.lblStudent_lugarNac.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_lugarNac.setFont(font2)
        self.lblStudent_lugarNac.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_lugarNac.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_fechaNac = QLabel(self.personal_data)
        self.lblStudent_fechaNac.setObjectName(u"lblStudent_fechaNac")
        self.lblStudent_fechaNac.setGeometry(QRect(510, 10, 91, 30))
        self.lblStudent_fechaNac.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac.setFont(font2)
        self.lblStudent_fechaNac.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneCity_ficha_estu = QLineEdit(self.personal_data)
        self.lneCity_ficha_estu.setObjectName(u"lneCity_ficha_estu")
        self.lneCity_ficha_estu.setGeometry(QRect(610, 50, 151, 30))
        self.lneCity_ficha_estu.setMinimumSize(QSize(100, 30))
        self.lneCity_ficha_estu.setMaximumSize(QSize(300, 30))
        self.lneCity_ficha_estu.setFont(font3)
        self.lneCity_ficha_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneCity_ficha_estu.setStyleSheet(u"")
        self.lneCity_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneEdad_ficha_estu = QLineEdit(self.personal_data)
        self.lneEdad_ficha_estu.setObjectName(u"lneEdad_ficha_estu")
        self.lneEdad_ficha_estu.setGeometry(QRect(840, 10, 61, 30))
        self.lneEdad_ficha_estu.setMinimumSize(QSize(50, 30))
        self.lneEdad_ficha_estu.setMaximumSize(QSize(300, 30))
        self.lneEdad_ficha_estu.setFont(font3)
        self.lneEdad_ficha_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneEdad_ficha_estu.setStyleSheet(u"")
        self.lneEdad_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneEdad_ficha_estu.setReadOnly(True)
        self.lblStudent_edad = QLabel(self.personal_data)
        self.lblStudent_edad.setObjectName(u"lblStudent_edad")
        self.lblStudent_edad.setGeometry(QRect(770, 10, 61, 30))
        self.lblStudent_edad.setMinimumSize(QSize(0, 30))
        self.lblStudent_edad.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_edad.setFont(font2)
        self.lblStudent_edad.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_edad.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_genero = QLabel(self.personal_data)
        self.lblStudent_genero.setObjectName(u"lblStudent_genero")
        self.lblStudent_genero.setGeometry(QRect(770, 50, 61, 30))
        self.lblStudent_genero.setMinimumSize(QSize(0, 30))
        self.lblStudent_genero.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_genero.setFont(font2)
        self.lblStudent_genero.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_genero.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneDir_ficha_estu = QLineEdit(self.personal_data)
        self.lneDir_ficha_estu.setObjectName(u"lneDir_ficha_estu")
        self.lneDir_ficha_estu.setGeometry(QRect(100, 100, 801, 60))
        self.lneDir_ficha_estu.setMinimumSize(QSize(400, 30))
        self.lneDir_ficha_estu.setMaximumSize(QSize(900, 60))
        self.lneDir_ficha_estu.setFont(font3)
        self.lneDir_ficha_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneDir_ficha_estu.setStyleSheet(u"")
        self.lneDir_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_dir = QLabel(self.personal_data)
        self.lblStudent_dir.setObjectName(u"lblStudent_dir")
        self.lblStudent_dir.setGeometry(QRect(10, 100, 81, 30))
        self.lblStudent_dir.setMinimumSize(QSize(0, 30))
        self.lblStudent_dir.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_dir.setFont(font2)
        self.lblStudent_dir.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_dir.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblGrado = QLabel(self.personal_data)
        self.lblGrado.setObjectName(u"lblGrado")
        self.lblGrado.setGeometry(QRect(510, 190, 61, 30))
        self.lblGrado.setMinimumSize(QSize(0, 30))
        self.lblGrado.setMaximumSize(QSize(16777215, 30))
        self.lblGrado.setFont(font2)
        self.lblGrado.setStyleSheet(u"background-color: transparent;")
        self.lblGrado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblSeccion = QLabel(self.personal_data)
        self.lblSeccion.setObjectName(u"lblSeccion")
        self.lblSeccion.setGeometry(QRect(690, 190, 61, 30))
        self.lblSeccion.setMinimumSize(QSize(0, 30))
        self.lblSeccion.setMaximumSize(QSize(16777215, 30))
        self.lblSeccion.setFont(font2)
        self.lblSeccion.setStyleSheet(u"background-color: transparent;")
        self.lblSeccion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneDocente_ficha_estu = QLineEdit(self.personal_data)
        self.lneDocente_ficha_estu.setObjectName(u"lneDocente_ficha_estu")
        self.lneDocente_ficha_estu.setGeometry(QRect(100, 240, 351, 30))
        self.lneDocente_ficha_estu.setMinimumSize(QSize(100, 30))
        self.lneDocente_ficha_estu.setMaximumSize(QSize(400, 30))
        self.lneDocente_ficha_estu.setFont(font3)
        self.lneDocente_ficha_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneDocente_ficha_estu.setStyleSheet(u"")
        self.lneDocente_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_35 = QLabel(self.personal_data)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 240, 81, 30))
        self.label_35.setMinimumSize(QSize(0, 30))
        self.label_35.setMaximumSize(QSize(16777215, 30))
        self.label_35.setFont(font2)
        self.label_35.setStyleSheet(u"background-color: transparent;")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_42 = QLabel(self.personal_data)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(10, 280, 101, 30))
        self.label_42.setMinimumSize(QSize(0, 30))
        self.label_42.setMaximumSize(QSize(16777215, 30))
        self.label_42.setFont(font2)
        self.label_42.setStyleSheet(u"background-color: transparent;")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneTallaC_ficha_estu = QLineEdit(self.personal_data)
        self.lneTallaC_ficha_estu.setObjectName(u"lneTallaC_ficha_estu")
        self.lneTallaC_ficha_estu.setGeometry(QRect(120, 280, 61, 30))
        self.lneTallaC_ficha_estu.setMinimumSize(QSize(50, 30))
        self.lneTallaC_ficha_estu.setMaximumSize(QSize(300, 30))
        self.lneTallaC_ficha_estu.setFont(font3)
        self.lneTallaC_ficha_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneTallaC_ficha_estu.setStyleSheet(u"")
        self.lneTallaC_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_44 = QLabel(self.personal_data)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(190, 280, 111, 30))
        self.label_44.setMinimumSize(QSize(0, 30))
        self.label_44.setMaximumSize(QSize(16777215, 30))
        self.label_44.setFont(font2)
        self.label_44.setStyleSheet(u"background-color: transparent;")
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneTallaP_ficha_estu = QLineEdit(self.personal_data)
        self.lneTallaP_ficha_estu.setObjectName(u"lneTallaP_ficha_estu")
        self.lneTallaP_ficha_estu.setGeometry(QRect(310, 280, 61, 30))
        self.lneTallaP_ficha_estu.setMinimumSize(QSize(50, 30))
        self.lneTallaP_ficha_estu.setMaximumSize(QSize(300, 30))
        self.lneTallaP_ficha_estu.setFont(font3)
        self.lneTallaP_ficha_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneTallaP_ficha_estu.setStyleSheet(u"")
        self.lneTallaP_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneTallaZ_ficha_estu = QLineEdit(self.personal_data)
        self.lneTallaZ_ficha_estu.setObjectName(u"lneTallaZ_ficha_estu")
        self.lneTallaZ_ficha_estu.setGeometry(QRect(510, 280, 61, 30))
        self.lneTallaZ_ficha_estu.setMinimumSize(QSize(50, 30))
        self.lneTallaZ_ficha_estu.setMaximumSize(QSize(300, 30))
        self.lneTallaZ_ficha_estu.setFont(font3)
        self.lneTallaZ_ficha_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneTallaZ_ficha_estu.setStyleSheet(u"")
        self.lneTallaZ_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_49 = QLabel(self.personal_data)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(390, 280, 111, 30))
        self.label_49.setMinimumSize(QSize(0, 30))
        self.label_49.setMaximumSize(QSize(16777215, 30))
        self.label_49.setFont(font2)
        self.label_49.setStyleSheet(u"background-color: transparent;")
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneFechaNac_ficha_estu = QDateEdit(self.personal_data)
        self.lneFechaNac_ficha_estu.setObjectName(u"lneFechaNac_ficha_estu")
        self.lneFechaNac_ficha_estu.setGeometry(QRect(610, 10, 151, 30))
        self.lneFechaNac_ficha_estu.setMinimumSize(QSize(151, 30))
        self.lneFechaNac_ficha_estu.setMaximumSize(QSize(151, 30))
        self.lneFechaNac_ficha_estu.setFont(font3)
        self.lneFechaNac_ficha_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneFechaNac_ficha_estu.setStyleSheet(u"QDateEdit {\n"
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
        self.lneFechaNac_ficha_estu.setCalendarPopup(True)
        self.frseccion = QFrame(self.personal_data)
        self.frseccion.setObjectName(u"frseccion")
        self.frseccion.setGeometry(QRect(760, 190, 71, 30))
        self.frseccion.setMinimumSize(QSize(70, 30))
        self.frseccion.setMaximumSize(QSize(200, 40))
        self.frseccion.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #2980b9;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.frseccion.setFrameShape(QFrame.Shape.StyledPanel)
        self.frseccion.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxSeccion_ficha_estu = QComboBox(self.frseccion)
        self.cbxSeccion_ficha_estu.addItem("")
        self.cbxSeccion_ficha_estu.addItem("")
        self.cbxSeccion_ficha_estu.addItem("")
        self.cbxSeccion_ficha_estu.setObjectName(u"cbxSeccion_ficha_estu")
        self.cbxSeccion_ficha_estu.setGeometry(QRect(5, 5, 60, 21))
        self.cbxSeccion_ficha_estu.setMaximumSize(QSize(180, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.cbxSeccion_ficha_estu.setFont(font4)
        self.cbxSeccion_ficha_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxSeccion_ficha_estu.setStyleSheet(u"QComboBox {\n"
"   \n"
"    border-radius: 10px;           /* Esquinas redondeadas del combobox */\n"
"    padding: 3px 8px;              /* Espaciado interno (arriba/abajo 4px, lados 8px) */\n"
"    background-color: white;       /* Fondo blanco del combobox cerrado */\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"   \n"
"    border-radius: 5px;            /* Esquinas redondeadas del men\u00fa desplegable */\n"
"    background-color: white;       /* Fondo blanco de la lista desplegable */\n"
"    color: #2d2d2d;                   /* Color de texto gris oscuro para los \u00edtems */\n"
"    selection-background-color: #2980b9; /* Fondo azul para el \u00edtem seleccionado */\n"
"    selection-color: white;        /* Texto blanco para el \u00edtem seleccionado */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 4px 8px;              /* Espaciado interno de cada \u00edtem de la lista */\n"
"}\n"
"")
        self.cbxSeccion_ficha_estu.setIconSize(QSize(5, 5))
        self.frGrado_reg_estu = QFrame(self.personal_data)
        self.frGrado_reg_estu.setObjectName(u"frGrado_reg_estu")
        self.frGrado_reg_estu.setGeometry(QRect(570, 190, 101, 30))
        self.frGrado_reg_estu.setMinimumSize(QSize(70, 30))
        self.frGrado_reg_estu.setMaximumSize(QSize(200, 40))
        self.frGrado_reg_estu.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 1.5px solid #2980b9;\n"
"	border-radius: 10px;\n"
"}\n"
"QComboBox{\n"
"	background-color: white;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    color: #2d2d2d;\n"
"}\n"
"")
        self.frGrado_reg_estu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frGrado_reg_estu.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxGrado_ficha_estu = QComboBox(self.frGrado_reg_estu)
        self.cbxGrado_ficha_estu.addItem("")
        self.cbxGrado_ficha_estu.addItem("")
        self.cbxGrado_ficha_estu.addItem("")
        self.cbxGrado_ficha_estu.addItem("")
        self.cbxGrado_ficha_estu.addItem("")
        self.cbxGrado_ficha_estu.addItem("")
        self.cbxGrado_ficha_estu.addItem("")
        self.cbxGrado_ficha_estu.setObjectName(u"cbxGrado_ficha_estu")
        self.cbxGrado_ficha_estu.setGeometry(QRect(5, 5, 91, 21))
        self.cbxGrado_ficha_estu.setMaximumSize(QSize(180, 30))
        self.cbxGrado_ficha_estu.setFont(font4)
        self.cbxGrado_ficha_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxGrado_ficha_estu.setStyleSheet(u"background-color: white;\n"
"border: transparent;")
        self.cbxGrado_ficha_estu.setIconSize(QSize(5, 5))
        self.frseccion_2 = QFrame(self.personal_data)
        self.frseccion_2.setObjectName(u"frseccion_2")
        self.frseccion_2.setGeometry(QRect(840, 50, 61, 30))
        self.frseccion_2.setMinimumSize(QSize(50, 30))
        self.frseccion_2.setMaximumSize(QSize(200, 40))
        self.frseccion_2.setStyleSheet(u"QFrame{\n"
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
        self.frseccion_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frseccion_2.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxGenero_ficha_estu = QComboBox(self.frseccion_2)
        self.cbxGenero_ficha_estu.addItem("")
        self.cbxGenero_ficha_estu.addItem("")
        self.cbxGenero_ficha_estu.addItem("")
        self.cbxGenero_ficha_estu.setObjectName(u"cbxGenero_ficha_estu")
        self.cbxGenero_ficha_estu.setGeometry(QRect(5, 5, 51, 21))
        self.cbxGenero_ficha_estu.setMaximumSize(QSize(180, 30))
        self.cbxGenero_ficha_estu.setFont(font4)
        self.cbxGenero_ficha_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxGenero_ficha_estu.setStyleSheet(u"background-color: white;\n"
"border: transparent;")
        self.cbxGenero_ficha_estu.setIconSize(QSize(5, 5))
        self.lblStudent_fechaIng = QLabel(self.personal_data)
        self.lblStudent_fechaIng.setObjectName(u"lblStudent_fechaIng")
        self.lblStudent_fechaIng.setGeometry(QRect(0, 190, 101, 30))
        self.lblStudent_fechaIng.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaIng.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaIng.setFont(font2)
        self.lblStudent_fechaIng.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaIng.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneFechaIng_ficha_estu = QDateEdit(self.personal_data)
        self.lneFechaIng_ficha_estu.setObjectName(u"lneFechaIng_ficha_estu")
        self.lneFechaIng_ficha_estu.setGeometry(QRect(100, 190, 151, 30))
        self.lneFechaIng_ficha_estu.setMinimumSize(QSize(151, 30))
        self.lneFechaIng_ficha_estu.setMaximumSize(QSize(151, 30))
        self.lneFechaIng_ficha_estu.setFont(font3)
        self.lneFechaIng_ficha_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneFechaIng_ficha_estu.setStyleSheet(u"QDateEdit {\n"
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
        self.lneFechaIng_ficha_estu.setCalendarPopup(True)
        self.frTipoEdu_reg_estu = QFrame(self.personal_data)
        self.frTipoEdu_reg_estu.setObjectName(u"frTipoEdu_reg_estu")
        self.frTipoEdu_reg_estu.setGeometry(QRect(400, 190, 101, 30))
        self.frTipoEdu_reg_estu.setMinimumSize(QSize(70, 30))
        self.frTipoEdu_reg_estu.setMaximumSize(QSize(200, 40))
        self.frTipoEdu_reg_estu.setStyleSheet(u"QFrame{\n"
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
        self.frTipoEdu_reg_estu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frTipoEdu_reg_estu.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxTipoEdu_ficha_estu = QComboBox(self.frTipoEdu_reg_estu)
        self.cbxTipoEdu_ficha_estu.addItem("")
        self.cbxTipoEdu_ficha_estu.addItem("")
        self.cbxTipoEdu_ficha_estu.addItem("")
        self.cbxTipoEdu_ficha_estu.setObjectName(u"cbxTipoEdu_ficha_estu")
        self.cbxTipoEdu_ficha_estu.setGeometry(QRect(5, 5, 91, 21))
        self.cbxTipoEdu_ficha_estu.setMaximumSize(QSize(180, 30))
        self.cbxTipoEdu_ficha_estu.setFont(font4)
        self.cbxTipoEdu_ficha_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxTipoEdu_ficha_estu.setStyleSheet(u"background-color: white;\n"
"border: transparent;")
        self.cbxTipoEdu_ficha_estu.setIconSize(QSize(5, 5))
        self.lblTipoEdu = QLabel(self.personal_data)
        self.lblTipoEdu.setObjectName(u"lblTipoEdu")
        self.lblTipoEdu.setGeometry(QRect(270, 190, 121, 30))
        self.lblTipoEdu.setMinimumSize(QSize(0, 30))
        self.lblTipoEdu.setMaximumSize(QSize(16777215, 30))
        self.lblTipoEdu.setFont(font2)
        self.lblTipoEdu.setStyleSheet(u"background-color: transparent;")
        self.lblTipoEdu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneEstatus_egresado = QLineEdit(self.personal_data)
        self.lneEstatus_egresado.setObjectName(u"lneEstatus_egresado")
        self.lneEstatus_egresado.setGeometry(QRect(340, 190, 151, 30))
        self.lneEstatus_egresado.setMinimumSize(QSize(50, 30))
        self.lneEstatus_egresado.setMaximumSize(QSize(300, 30))
        self.lneEstatus_egresado.setFont(font3)
        self.lneEstatus_egresado.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneEstatus_egresado.setStyleSheet(u"")
        self.lneEstatus_egresado.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblEstatus = QLabel(self.personal_data)
        self.lblEstatus.setObjectName(u"lblEstatus")
        self.lblEstatus.setGeometry(QRect(260, 190, 71, 30))
        self.lblEstatus.setMinimumSize(QSize(0, 30))
        self.lblEstatus.setMaximumSize(QSize(16777215, 30))
        self.lblEstatus.setFont(font2)
        self.lblEstatus.setStyleSheet(u"background-color: transparent;")
        self.lblEstatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneUltimoGrado = QLineEdit(self.personal_data)
        self.lneUltimoGrado.setObjectName(u"lneUltimoGrado")
        self.lneUltimoGrado.setGeometry(QRect(620, 190, 71, 30))
        self.lneUltimoGrado.setMinimumSize(QSize(50, 30))
        self.lneUltimoGrado.setMaximumSize(QSize(300, 30))
        self.lneUltimoGrado.setFont(font3)
        self.lneUltimoGrado.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneUltimoGrado.setStyleSheet(u"")
        self.lneUltimoGrado.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblUltimoGrado = QLabel(self.personal_data)
        self.lblUltimoGrado.setObjectName(u"lblUltimoGrado")
        self.lblUltimoGrado.setGeometry(QRect(500, 190, 111, 30))
        self.lblUltimoGrado.setMinimumSize(QSize(0, 30))
        self.lblUltimoGrado.setMaximumSize(QSize(16777215, 30))
        self.lblUltimoGrado.setFont(font2)
        self.lblUltimoGrado.setStyleSheet(u"background-color: transparent;")
        self.lblUltimoGrado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneAnioEgreso = QLineEdit(self.personal_data)
        self.lneAnioEgreso.setObjectName(u"lneAnioEgreso")
        self.lneAnioEgreso.setGeometry(QRect(800, 190, 101, 30))
        self.lneAnioEgreso.setMinimumSize(QSize(50, 30))
        self.lneAnioEgreso.setMaximumSize(QSize(300, 30))
        self.lneAnioEgreso.setFont(font1)
        self.lneAnioEgreso.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneAnioEgreso.setStyleSheet(u"")
        self.lneAnioEgreso.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblAnioEgreso = QLabel(self.personal_data)
        self.lblAnioEgreso.setObjectName(u"lblAnioEgreso")
        self.lblAnioEgreso.setGeometry(QRect(700, 190, 101, 30))
        self.lblAnioEgreso.setMinimumSize(QSize(0, 30))
        self.lblAnioEgreso.setMaximumSize(QSize(16777215, 30))
        self.lblAnioEgreso.setFont(font2)
        self.lblAnioEgreso.setStyleSheet(u"background-color: transparent;")
        self.lblAnioEgreso.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackFicha_estu.addWidget(self.personal_data)
        self.representante = QWidget()
        self.representante.setObjectName(u"representante")
        self.lneMadre_ficha_estu = QLineEdit(self.representante)
        self.lneMadre_ficha_estu.setObjectName(u"lneMadre_ficha_estu")
        self.lneMadre_ficha_estu.setGeometry(QRect(90, 10, 281, 30))
        self.lneMadre_ficha_estu.setMinimumSize(QSize(150, 30))
        self.lneMadre_ficha_estu.setMaximumSize(QSize(400, 30))
        self.lneMadre_ficha_estu.setFont(font1)
        self.lneMadre_ficha_estu.setStyleSheet(u"")
        self.lneMadre_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_repre_2 = QLabel(self.representante)
        self.lblStudent_apellido_repre_2.setObjectName(u"lblStudent_apellido_repre_2")
        self.lblStudent_apellido_repre_2.setGeometry(QRect(10, 10, 81, 30))
        self.lblStudent_apellido_repre_2.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_repre_2.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_repre_2.setFont(font2)
        self.lblStudent_apellido_repre_2.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido_repre_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lnePadre_ficha_estu = QLineEdit(self.representante)
        self.lnePadre_ficha_estu.setObjectName(u"lnePadre_ficha_estu")
        self.lnePadre_ficha_estu.setGeometry(QRect(90, 50, 281, 30))
        self.lnePadre_ficha_estu.setMinimumSize(QSize(150, 30))
        self.lnePadre_ficha_estu.setMaximumSize(QSize(400, 30))
        self.lnePadre_ficha_estu.setFont(font1)
        self.lnePadre_ficha_estu.setStyleSheet(u"")
        self.lnePadre_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_nombres_3 = QLabel(self.representante)
        self.lblStudent_nombres_3.setObjectName(u"lblStudent_nombres_3")
        self.lblStudent_nombres_3.setGeometry(QRect(10, 50, 81, 30))
        self.lblStudent_nombres_3.setMinimumSize(QSize(0, 30))
        self.lblStudent_nombres_3.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_nombres_3.setFont(font2)
        self.lblStudent_nombres_3.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_nombres_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_fechaNac_repre_2 = QLabel(self.representante)
        self.lblStudent_fechaNac_repre_2.setObjectName(u"lblStudent_fechaNac_repre_2")
        self.lblStudent_fechaNac_repre_2.setGeometry(QRect(380, 10, 121, 30))
        self.lblStudent_fechaNac_repre_2.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_2.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_2.setFont(font2)
        self.lblStudent_fechaNac_repre_2.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneCedula_madre_ficha_estu = QLineEdit(self.representante)
        self.lneCedula_madre_ficha_estu.setObjectName(u"lneCedula_madre_ficha_estu")
        self.lneCedula_madre_ficha_estu.setGeometry(QRect(500, 10, 151, 30))
        self.lneCedula_madre_ficha_estu.setMinimumSize(QSize(100, 30))
        self.lneCedula_madre_ficha_estu.setMaximumSize(QSize(300, 30))
        self.lneCedula_madre_ficha_estu.setFont(font1)
        self.lneCedula_madre_ficha_estu.setStyleSheet(u"")
        self.lneCedula_madre_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneCedula_padre_ficha_estu = QLineEdit(self.representante)
        self.lneCedula_padre_ficha_estu.setObjectName(u"lneCedula_padre_ficha_estu")
        self.lneCedula_padre_ficha_estu.setGeometry(QRect(500, 50, 151, 30))
        self.lneCedula_padre_ficha_estu.setMinimumSize(QSize(100, 30))
        self.lneCedula_padre_ficha_estu.setMaximumSize(QSize(300, 30))
        self.lneCedula_padre_ficha_estu.setFont(font1)
        self.lneCedula_padre_ficha_estu.setStyleSheet(u"")
        self.lneCedula_padre_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_fechaNac_repre_3 = QLabel(self.representante)
        self.lblStudent_fechaNac_repre_3.setObjectName(u"lblStudent_fechaNac_repre_3")
        self.lblStudent_fechaNac_repre_3.setGeometry(QRect(380, 50, 121, 30))
        self.lblStudent_fechaNac_repre_3.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_3.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_3.setFont(font2)
        self.lblStudent_fechaNac_repre_3.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widgetDatosRepre = QWidget(self.representante)
        self.widgetDatosRepre.setObjectName(u"widgetDatosRepre")
        self.widgetDatosRepre.setGeometry(QRect(0, 90, 921, 261))
        self.widgetDatosRepre.setStyleSheet(u"QWidget#widgetDatosRepre{\n"
"background-color: rgb(242, 245, 247);\n"
"border-radius: 10px;\n"
"border: white;\n"
"color: #2d2d2d;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 10px;\n"
"    padding: 2px 5px;\n"
"    background-color: white;\n"
"}")
        self.lblStudent_nombres_2 = QLabel(self.widgetDatosRepre)
        self.lblStudent_nombres_2.setObjectName(u"lblStudent_nombres_2")
        self.lblStudent_nombres_2.setGeometry(QRect(10, 100, 81, 30))
        self.lblStudent_nombres_2.setMinimumSize(QSize(0, 30))
        self.lblStudent_nombres_2.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_nombres_2.setFont(font2)
        self.lblStudent_nombres_2.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_nombres_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneApellidos_repre_ficha_estu = QLineEdit(self.widgetDatosRepre)
        self.lneApellidos_repre_ficha_estu.setObjectName(u"lneApellidos_repre_ficha_estu")
        self.lneApellidos_repre_ficha_estu.setGeometry(QRect(100, 60, 400, 30))
        self.lneApellidos_repre_ficha_estu.setMinimumSize(QSize(400, 30))
        self.lneApellidos_repre_ficha_estu.setMaximumSize(QSize(400, 30))
        self.lneApellidos_repre_ficha_estu.setFont(font1)
        self.lneApellidos_repre_ficha_estu.setStyleSheet(u"")
        self.lneApellidos_repre_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_apellido_repre = QLabel(self.widgetDatosRepre)
        self.lblStudent_apellido_repre.setObjectName(u"lblStudent_apellido_repre")
        self.lblStudent_apellido_repre.setGeometry(QRect(10, 60, 81, 30))
        self.lblStudent_apellido_repre.setMinimumSize(QSize(0, 30))
        self.lblStudent_apellido_repre.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_apellido_repre.setFont(font2)
        self.lblStudent_apellido_repre.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_apellido_repre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneNombres_repre_ficha_estu = QLineEdit(self.widgetDatosRepre)
        self.lneNombres_repre_ficha_estu.setObjectName(u"lneNombres_repre_ficha_estu")
        self.lneNombres_repre_ficha_estu.setGeometry(QRect(100, 100, 400, 30))
        self.lneNombres_repre_ficha_estu.setMinimumSize(QSize(400, 30))
        self.lneNombres_repre_ficha_estu.setMaximumSize(QSize(400, 30))
        self.lneNombres_repre_ficha_estu.setFont(font1)
        self.lneNombres_repre_ficha_estu.setStyleSheet(u"")
        self.lneNombres_repre_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_dir_repre = QLabel(self.widgetDatosRepre)
        self.lblStudent_dir_repre.setObjectName(u"lblStudent_dir_repre")
        self.lblStudent_dir_repre.setGeometry(QRect(10, 140, 81, 30))
        self.lblStudent_dir_repre.setMinimumSize(QSize(0, 30))
        self.lblStudent_dir_repre.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_dir_repre.setFont(font2)
        self.lblStudent_dir_repre.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_dir_repre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneDir_repre_ficha_estu = QLineEdit(self.widgetDatosRepre)
        self.lneDir_repre_ficha_estu.setObjectName(u"lneDir_repre_ficha_estu")
        self.lneDir_repre_ficha_estu.setGeometry(QRect(100, 140, 801, 31))
        self.lneDir_repre_ficha_estu.setMinimumSize(QSize(400, 30))
        self.lneDir_repre_ficha_estu.setMaximumSize(QSize(900, 60))
        self.lneDir_repre_ficha_estu.setFont(font1)
        self.lneDir_repre_ficha_estu.setStyleSheet(u"")
        self.lneDir_repre_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneEdad_repre_ficha_estu = QLineEdit(self.widgetDatosRepre)
        self.lneEdad_repre_ficha_estu.setObjectName(u"lneEdad_repre_ficha_estu")
        self.lneEdad_repre_ficha_estu.setGeometry(QRect(850, 60, 61, 30))
        self.lneEdad_repre_ficha_estu.setMinimumSize(QSize(50, 30))
        self.lneEdad_repre_ficha_estu.setMaximumSize(QSize(300, 30))
        self.lneEdad_repre_ficha_estu.setFont(font1)
        self.lneEdad_repre_ficha_estu.setStyleSheet(u"")
        self.lneEdad_repre_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneEdad_repre_ficha_estu.setReadOnly(True)
        self.label_41 = QLabel(self.widgetDatosRepre)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(10, 180, 111, 30))
        self.label_41.setMinimumSize(QSize(0, 30))
        self.label_41.setMaximumSize(QSize(16777215, 30))
        self.label_41.setFont(font2)
        self.label_41.setStyleSheet(u"background-color: transparent;")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneNum_repre_ficha_estu = QLineEdit(self.widgetDatosRepre)
        self.lneNum_repre_ficha_estu.setObjectName(u"lneNum_repre_ficha_estu")
        self.lneNum_repre_ficha_estu.setGeometry(QRect(130, 180, 291, 30))
        self.lneNum_repre_ficha_estu.setMinimumSize(QSize(100, 30))
        self.lneNum_repre_ficha_estu.setMaximumSize(QSize(400, 30))
        self.lneNum_repre_ficha_estu.setFont(font1)
        self.lneNum_repre_ficha_estu.setStyleSheet(u"")
        self.lneNum_repre_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_fechaNac_repre = QLabel(self.widgetDatosRepre)
        self.lblStudent_fechaNac_repre.setObjectName(u"lblStudent_fechaNac_repre")
        self.lblStudent_fechaNac_repre.setGeometry(QRect(520, 100, 91, 30))
        self.lblStudent_fechaNac_repre.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre.setFont(font2)
        self.lblStudent_fechaNac_repre.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_edad_repre = QLabel(self.widgetDatosRepre)
        self.lblStudent_edad_repre.setObjectName(u"lblStudent_edad_repre")
        self.lblStudent_edad_repre.setGeometry(QRect(780, 60, 61, 30))
        self.lblStudent_edad_repre.setMinimumSize(QSize(0, 30))
        self.lblStudent_edad_repre.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_edad_repre.setFont(font2)
        self.lblStudent_edad_repre.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_edad_repre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneCedula_repre_ficha_estu = QLineEdit(self.widgetDatosRepre)
        self.lneCedula_repre_ficha_estu.setObjectName(u"lneCedula_repre_ficha_estu")
        self.lneCedula_repre_ficha_estu.setGeometry(QRect(620, 60, 151, 30))
        self.lneCedula_repre_ficha_estu.setMinimumSize(QSize(100, 30))
        self.lneCedula_repre_ficha_estu.setMaximumSize(QSize(300, 30))
        self.lneCedula_repre_ficha_estu.setFont(font1)
        self.lneCedula_repre_ficha_estu.setStyleSheet(u"")
        self.lneCedula_repre_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneCorreo_repre_ficha_estu = QLineEdit(self.widgetDatosRepre)
        self.lneCorreo_repre_ficha_estu.setObjectName(u"lneCorreo_repre_ficha_estu")
        self.lneCorreo_repre_ficha_estu.setGeometry(QRect(570, 180, 291, 30))
        self.lneCorreo_repre_ficha_estu.setMinimumSize(QSize(100, 30))
        self.lneCorreo_repre_ficha_estu.setMaximumSize(QSize(400, 30))
        self.lneCorreo_repre_ficha_estu.setFont(font1)
        self.lneCorreo_repre_ficha_estu.setStyleSheet(u"")
        self.lneCorreo_repre_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_38 = QLabel(self.widgetDatosRepre)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(450, 180, 111, 30))
        self.label_38.setMinimumSize(QSize(0, 30))
        self.label_38.setMaximumSize(QSize(16777215, 30))
        self.label_38.setFont(font2)
        self.label_38.setStyleSheet(u"background-color: transparent;")
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_genero_repre = QLabel(self.widgetDatosRepre)
        self.lblStudent_genero_repre.setObjectName(u"lblStudent_genero_repre")
        self.lblStudent_genero_repre.setGeometry(QRect(780, 100, 61, 30))
        self.lblStudent_genero_repre.setMinimumSize(QSize(0, 30))
        self.lblStudent_genero_repre.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_genero_repre.setFont(font2)
        self.lblStudent_genero_repre.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_genero_repre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitulo_registro_estudiante_2 = QLabel(self.widgetDatosRepre)
        self.lblTitulo_registro_estudiante_2.setObjectName(u"lblTitulo_registro_estudiante_2")
        self.lblTitulo_registro_estudiante_2.setGeometry(QRect(320, 0, 351, 41))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(17)
        font5.setBold(True)
        self.lblTitulo_registro_estudiante_2.setFont(font5)
        self.lblTitulo_registro_estudiante_2.setStyleSheet(u"")
        self.lblTitulo_registro_estudiante_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_fechaNac_repre_4 = QLabel(self.widgetDatosRepre)
        self.lblStudent_fechaNac_repre_4.setObjectName(u"lblStudent_fechaNac_repre_4")
        self.lblStudent_fechaNac_repre_4.setGeometry(QRect(520, 60, 91, 30))
        self.lblStudent_fechaNac_repre_4.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_4.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_4.setFont(font2)
        self.lblStudent_fechaNac_repre_4.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneFechaNac_repre_ficha_estu = QDateEdit(self.widgetDatosRepre)
        self.lneFechaNac_repre_ficha_estu.setObjectName(u"lneFechaNac_repre_ficha_estu")
        self.lneFechaNac_repre_ficha_estu.setGeometry(QRect(620, 100, 151, 30))
        self.lneFechaNac_repre_ficha_estu.setMinimumSize(QSize(151, 30))
        self.lneFechaNac_repre_ficha_estu.setMaximumSize(QSize(151, 30))
        self.lneFechaNac_repre_ficha_estu.setFont(font1)
        self.lneFechaNac_repre_ficha_estu.setStyleSheet(u"QDateEdit {\n"
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
        self.lneFechaNac_repre_ficha_estu.setCalendarPopup(True)
        self.frseccion_3 = QFrame(self.widgetDatosRepre)
        self.frseccion_3.setObjectName(u"frseccion_3")
        self.frseccion_3.setGeometry(QRect(850, 100, 61, 30))
        self.frseccion_3.setMinimumSize(QSize(50, 30))
        self.frseccion_3.setMaximumSize(QSize(200, 40))
        self.frseccion_3.setStyleSheet(u"QFrame{\n"
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
        self.frseccion_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frseccion_3.setFrameShadow(QFrame.Shadow.Raised)
        self.cbxGenero_repre_ficha_estu = QComboBox(self.frseccion_3)
        self.cbxGenero_repre_ficha_estu.addItem("")
        self.cbxGenero_repre_ficha_estu.addItem("")
        self.cbxGenero_repre_ficha_estu.addItem("")
        self.cbxGenero_repre_ficha_estu.setObjectName(u"cbxGenero_repre_ficha_estu")
        self.cbxGenero_repre_ficha_estu.setGeometry(QRect(5, 5, 51, 21))
        self.cbxGenero_repre_ficha_estu.setMaximumSize(QSize(180, 30))
        self.cbxGenero_repre_ficha_estu.setFont(font4)
        self.cbxGenero_repre_ficha_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbxGenero_repre_ficha_estu.setStyleSheet(u"background-color: white")
        self.cbxGenero_repre_ficha_estu.setIconSize(QSize(5, 5))
        self.lblStudent_dir_repre_2 = QLabel(self.widgetDatosRepre)
        self.lblStudent_dir_repre_2.setObjectName(u"lblStudent_dir_repre_2")
        self.lblStudent_dir_repre_2.setGeometry(QRect(10, 220, 101, 30))
        self.lblStudent_dir_repre_2.setMinimumSize(QSize(0, 30))
        self.lblStudent_dir_repre_2.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_dir_repre_2.setFont(font2)
        self.lblStudent_dir_repre_2.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_dir_repre_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lneObser_ficha_estu_repre = QLineEdit(self.widgetDatosRepre)
        self.lneObser_ficha_estu_repre.setObjectName(u"lneObser_ficha_estu_repre")
        self.lneObser_ficha_estu_repre.setGeometry(QRect(120, 220, 781, 31))
        self.lneObser_ficha_estu_repre.setMinimumSize(QSize(400, 30))
        self.lneObser_ficha_estu_repre.setMaximumSize(QSize(900, 60))
        self.lneObser_ficha_estu_repre.setFont(font)
        self.lneObser_ficha_estu_repre.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneObser_ficha_estu_repre.setStyleSheet(u"")
        self.lneObser_ficha_estu_repre.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneOcup_madre_ficha_estu = QLineEdit(self.representante)
        self.lneOcup_madre_ficha_estu.setObjectName(u"lneOcup_madre_ficha_estu")
        self.lneOcup_madre_ficha_estu.setGeometry(QRect(750, 10, 151, 30))
        self.lneOcup_madre_ficha_estu.setMinimumSize(QSize(100, 30))
        self.lneOcup_madre_ficha_estu.setMaximumSize(QSize(300, 30))
        self.lneOcup_madre_ficha_estu.setFont(font)
        self.lneOcup_madre_ficha_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneOcup_madre_ficha_estu.setStyleSheet(u"")
        self.lneOcup_madre_ficha_estu.setMaxLength(10)
        self.lneOcup_madre_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lneOcup_padre_ficha_estu = QLineEdit(self.representante)
        self.lneOcup_padre_ficha_estu.setObjectName(u"lneOcup_padre_ficha_estu")
        self.lneOcup_padre_ficha_estu.setGeometry(QRect(750, 50, 151, 30))
        self.lneOcup_padre_ficha_estu.setMinimumSize(QSize(100, 30))
        self.lneOcup_padre_ficha_estu.setMaximumSize(QSize(300, 30))
        self.lneOcup_padre_ficha_estu.setFont(font)
        self.lneOcup_padre_ficha_estu.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lneOcup_padre_ficha_estu.setStyleSheet(u"")
        self.lneOcup_padre_ficha_estu.setMaxLength(10)
        self.lneOcup_padre_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblStudent_fechaNac_repre_6 = QLabel(self.representante)
        self.lblStudent_fechaNac_repre_6.setObjectName(u"lblStudent_fechaNac_repre_6")
        self.lblStudent_fechaNac_repre_6.setGeometry(QRect(660, 10, 91, 30))
        self.lblStudent_fechaNac_repre_6.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_6.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_6.setFont(font2)
        self.lblStudent_fechaNac_repre_6.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStudent_fechaNac_repre_5 = QLabel(self.representante)
        self.lblStudent_fechaNac_repre_5.setObjectName(u"lblStudent_fechaNac_repre_5")
        self.lblStudent_fechaNac_repre_5.setGeometry(QRect(660, 50, 91, 30))
        self.lblStudent_fechaNac_repre_5.setMinimumSize(QSize(0, 30))
        self.lblStudent_fechaNac_repre_5.setMaximumSize(QSize(16777215, 30))
        self.lblStudent_fechaNac_repre_5.setFont(font2)
        self.lblStudent_fechaNac_repre_5.setStyleSheet(u"background-color: transparent;")
        self.lblStudent_fechaNac_repre_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackFicha_estu.addWidget(self.representante)
        self.historial = QWidget()
        self.historial.setObjectName(u"historial")
        self.frameTabla_historial = QFrame(self.historial)
        self.frameTabla_historial.setObjectName(u"frameTabla_historial")
        self.frameTabla_historial.setGeometry(QRect(0, 10, 921, 341))
        self.frameTabla_historial.setMinimumSize(QSize(300, 200))
        self.frameTabla_historial.setMaximumSize(QSize(16777215, 500))
        self.frameTabla_historial.setStyleSheet(u"QFrame#frameTabla_historial {\n"
"    border: 1px solid #d5dbdb;\n"
"    border-radius: 12px;\n"
"    background-color: white;\n"
"}")
        self.frameTabla_historial.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTabla_historial.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameTabla_historial)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableW_historial = QTableView(self.frameTabla_historial)
        self.tableW_historial.setObjectName(u"tableW_historial")
        self.tableW_historial.setStyleSheet(u"QTableView {\n"
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
        self.tableW_historial.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableW_historial.setAlternatingRowColors(True)
        self.tableW_historial.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableW_historial.setShowGrid(True)
        self.tableW_historial.setSortingEnabled(True)

        self.horizontalLayout_3.addWidget(self.tableW_historial)

        self.stackFicha_estu.addWidget(self.historial)

        self.horizontalLayout.addWidget(self.stackFicha_estu)

        self.btnStudentDatos_ficha = QPushButton(self.widget)
        self.pestanas_ficha = QButtonGroup(ficha_estu)
        self.pestanas_ficha.setObjectName(u"pestanas_ficha")
        self.pestanas_ficha.addButton(self.btnStudentDatos_ficha)
        self.btnStudentDatos_ficha.setObjectName(u"btnStudentDatos_ficha")
        self.btnStudentDatos_ficha.setGeometry(QRect(30, 90, 141, 45))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStudentDatos_ficha.sizePolicy().hasHeightForWidth())
        self.btnStudentDatos_ficha.setSizePolicy(sizePolicy)
        self.btnStudentDatos_ficha.setMinimumSize(QSize(80, 25))
        self.btnStudentDatos_ficha.setMaximumSize(QSize(200, 45))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.btnStudentDatos_ficha.setFont(font6)
        self.btnStudentDatos_ficha.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnStudentDatos_ficha.setStyleSheet(u"QPushButton {\n"
"   background: #2980b9;\n"
"	color: #FFFFFF;\n"
"    border: 1px solid #2980b9;\n"
"    padding: 2px 16px;\n"
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
        self.btnStudentDatos_ficha.setIconSize(QSize(50, 50))
        self.btnStudentDatos_ficha.setCheckable(True)
        self.btnStudentDatos_ficha.setChecked(True)
        self.btnStudentDatos_ficha.setAutoExclusive(False)
        self.btnRepre_ficha = QPushButton(self.widget)
        self.pestanas_ficha.addButton(self.btnRepre_ficha)
        self.btnRepre_ficha.setObjectName(u"btnRepre_ficha")
        self.btnRepre_ficha.setGeometry(QRect(170, 90, 161, 45))
        sizePolicy.setHeightForWidth(self.btnRepre_ficha.sizePolicy().hasHeightForWidth())
        self.btnRepre_ficha.setSizePolicy(sizePolicy)
        self.btnRepre_ficha.setMinimumSize(QSize(80, 25))
        self.btnRepre_ficha.setMaximumSize(QSize(200, 45))
        self.btnRepre_ficha.setFont(font6)
        self.btnRepre_ficha.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnRepre_ficha.setStyleSheet(u"QPushButton {\n"
"   background: #2980b9;\n"
"	color: #FFFFFF;\n"
"    border: 1px solid #2980b9;\n"
"    padding: 2px 8px;\n"
"    border-radius: 10px;\n"
"	text-align: left;\n"
"    padding-left: 12px; /* Mueve el \u00edcono a la derecha un poco */\n"
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
        self.btnRepre_ficha.setIconSize(QSize(50, 50))
        self.btnRepre_ficha.setCheckable(True)
        self.btnRepre_ficha.setChecked(False)
        self.btnRepre_ficha.setAutoExclusive(False)
        self.btnModificar_ficha_estu = QPushButton(self.widget)
        self.btnModificar_ficha_estu.setObjectName(u"btnModificar_ficha_estu")
        self.btnModificar_ficha_estu.setGeometry(QRect(840, 510, 120, 50))
        sizePolicy.setHeightForWidth(self.btnModificar_ficha_estu.sizePolicy().hasHeightForWidth())
        self.btnModificar_ficha_estu.setSizePolicy(sizePolicy)
        self.btnModificar_ficha_estu.setMinimumSize(QSize(120, 40))
        self.btnModificar_ficha_estu.setMaximumSize(QSize(120, 60))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(13)
        font7.setBold(True)
        self.btnModificar_ficha_estu.setFont(font7)
        self.btnModificar_ficha_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnModificar_ficha_estu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnModificar_ficha_estu.setStyleSheet(u"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 10px;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        self.btnModificar_ficha_estu.setIconSize(QSize(20, 20))
        self.btnExportar_ficha_estu = QToolButton(self.widget)
        self.btnExportar_ficha_estu.setObjectName(u"btnExportar_ficha_estu")
        self.btnExportar_ficha_estu.setGeometry(QRect(700, 510, 134, 50))
        self.btnExportar_ficha_estu.setFont(font4)
        self.btnExportar_ficha_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnExportar_ficha_estu.setAutoFillBackground(False)
        self.btnExportar_ficha_estu.setStyleSheet(u"QToolButton {\n"
"   background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 7px;\n"
"    border-radius: 15px;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: #0D47A1;\n"
"}\n"
"\n"
"/* --- Estilo del men\u00fa desplegable --- */\n"
"QMenu {\n"
"    background-color: white;         /* fondo blanco */\n"
"    color: black;                    /* texto negro */\n"
"    border: 1px solid #c0c0c0;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 5px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #0078d7;       /* azul Windows */\n"
"    color: white;                    /* texto blanco al seleccionar */\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/pdf_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExportar_ficha_estu.setIcon(icon)
        self.btnExportar_ficha_estu.setIconSize(QSize(20, 20))
        self.btnExportar_ficha_estu.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.btnExportar_ficha_estu.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.contenedorSwitch = QFrame(self.widget)
        self.contenedorSwitch.setObjectName(u"contenedorSwitch")
        self.contenedorSwitch.setGeometry(QRect(330, 30, 67, 51))
        self.contenedorSwitch.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedorSwitch.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contenedorSwitch)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblLogo_ficha_estu = QLabel(self.widget)
        self.lblLogo_ficha_estu.setObjectName(u"lblLogo_ficha_estu")
        self.lblLogo_ficha_estu.setGeometry(QRect(919, 20, 51, 61))
        self.lblLogo_ficha_estu.setMinimumSize(QSize(50, 50))
        self.lblLogo_ficha_estu.setMaximumSize(QSize(130, 70))
        self.lblLogo_ficha_estu.setStyleSheet(u"background-color: transparent;")
        self.lblLogo_ficha_estu.setPixmap(QPixmap(u":/logos/logo_escuela_sinFondo.png"))
        self.lblLogo_ficha_estu.setScaledContents(True)
        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(909, 20, 3, 61))
        self.line_2.setMinimumSize(QSize(3, 61))
        self.line_2.setMaximumSize(QSize(3, 61))
        self.line_2.setStyleSheet(u"background-color: #2d2d2d;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblTitulo_ficha_estu = QLabel(self.widget)
        self.lblTitulo_ficha_estu.setObjectName(u"lblTitulo_ficha_estu")
        self.lblTitulo_ficha_estu.setGeometry(QRect(760, 20, 141, 61))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(19)
        font8.setBold(True)
        self.lblTitulo_ficha_estu.setFont(font8)
        self.lblTitulo_ficha_estu.setStyleSheet(u"color: #2d2d2d;\n"
"background-color: transparent;")
        self.lblTitulo_ficha_estu.setFrameShape(QFrame.Shape.NoFrame)
        self.lblTitulo_ficha_estu.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitulo_ficha_estu.setScaledContents(False)
        self.lblTitulo_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTitulo_ficha_estu.setWordWrap(True)
        self.lblTitulo_ficha_estu.setIndent(0)
        self.btnEliminar_ficha_estu = QPushButton(self.widget)
        self.btnEliminar_ficha_estu.setObjectName(u"btnEliminar_ficha_estu")
        self.btnEliminar_ficha_estu.setGeometry(QRect(320, 520, 120, 40))
        sizePolicy.setHeightForWidth(self.btnEliminar_ficha_estu.sizePolicy().hasHeightForWidth())
        self.btnEliminar_ficha_estu.setSizePolicy(sizePolicy)
        self.btnEliminar_ficha_estu.setMinimumSize(QSize(120, 30))
        self.btnEliminar_ficha_estu.setMaximumSize(QSize(120, 40))
        self.btnEliminar_ficha_estu.setFont(font7)
        self.btnEliminar_ficha_estu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEliminar_ficha_estu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnEliminar_ficha_estu.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/delete_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEliminar_ficha_estu.setIcon(icon1)
        self.lblCedula_registro_estudiante = QLabel(self.widget)
        self.lblCedula_registro_estudiante.setObjectName(u"lblCedula_registro_estudiante")
        self.lblCedula_registro_estudiante.setGeometry(QRect(20, 30, 91, 50))
        self.lblCedula_registro_estudiante.setMinimumSize(QSize(0, 50))
        self.lblCedula_registro_estudiante.setMaximumSize(QSize(16777215, 30))
        self.lblCedula_registro_estudiante.setFont(font2)
        self.lblCedula_registro_estudiante.setStyleSheet(u"color: #2d2d2d;\n"
"border: 1px solid transparent;\n"
"border-radius: 10px;\n"
"background-color: transparent;")
        self.lblCedula_registro_estudiante.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblCedula_registro_estudiante.setWordWrap(True)
        self.lblEstado_ficha_estu = QLabel(self.widget)
        self.lblEstado_ficha_estu.setObjectName(u"lblEstado_ficha_estu")
        self.lblEstado_ficha_estu.setGeometry(QRect(400, 30, 121, 51))
        self.lblEstado_ficha_estu.setFont(font2)
        self.lblEstado_ficha_estu.setStyleSheet(u"color: #2d2d2d")
        self.lblEstado_ficha_estu.setFrameShape(QFrame.Shape.NoFrame)
        self.lblEstado_ficha_estu.setFrameShadow(QFrame.Shadow.Plain)
        self.lblEstado_ficha_estu.setScaledContents(False)
        self.lblEstado_ficha_estu.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblEstado_ficha_estu.setWordWrap(True)
        self.lblEstado_ficha_estu.setIndent(0)
        self.btnHistorial_estu = QPushButton(self.widget)
        self.pestanas_ficha.addButton(self.btnHistorial_estu)
        self.btnHistorial_estu.setObjectName(u"btnHistorial_estu")
        self.btnHistorial_estu.setGeometry(QRect(330, 90, 161, 45))
        sizePolicy.setHeightForWidth(self.btnHistorial_estu.sizePolicy().hasHeightForWidth())
        self.btnHistorial_estu.setSizePolicy(sizePolicy)
        self.btnHistorial_estu.setMinimumSize(QSize(80, 25))
        self.btnHistorial_estu.setMaximumSize(QSize(200, 45))
        self.btnHistorial_estu.setFont(font6)
        self.btnHistorial_estu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnHistorial_estu.setStyleSheet(u"QPushButton {\n"
"   background: #2980b9;\n"
"	color: #FFFFFF;\n"
"    border: 1px solid #2980b9;\n"
"    padding: 2px 8px;\n"
"    border-radius: 10px;\n"
"	text-align: left;\n"
"    padding-left: 12px; /* Mueve el \u00edcono a la derecha un poco */\n"
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
        self.btnHistorial_estu.setIconSize(QSize(50, 50))
        self.btnHistorial_estu.setCheckable(True)
        self.btnHistorial_estu.setChecked(False)
        self.btnHistorial_estu.setAutoExclusive(False)
        self.btnDevolver_grado = QPushButton(self.widget)
        self.btnDevolver_grado.setObjectName(u"btnDevolver_grado")
        self.btnDevolver_grado.setGeometry(QRect(449, 510, 241, 50))
        sizePolicy.setHeightForWidth(self.btnDevolver_grado.sizePolicy().hasHeightForWidth())
        self.btnDevolver_grado.setSizePolicy(sizePolicy)
        self.btnDevolver_grado.setMinimumSize(QSize(120, 40))
        self.btnDevolver_grado.setMaximumSize(QSize(300, 60))
        self.btnDevolver_grado.setFont(font7)
        self.btnDevolver_grado.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDevolver_grado.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnDevolver_grado.setStyleSheet(u"QPushButton {\n"
"	background-color: #2980b9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 8px 10px;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0D47A1\n"
"}")
        self.btnDevolver_grado.setIconSize(QSize(20, 20))
        self.btnHistorial_estu.raise_()
        self.lneCedula_ficha_estu.raise_()
        self.btnStudentDatos_ficha.raise_()
        self.btnRepre_ficha.raise_()
        self.frameTabla_student.raise_()
        self.btnModificar_ficha_estu.raise_()
        self.btnExportar_ficha_estu.raise_()
        self.contenedorSwitch.raise_()
        self.lblLogo_ficha_estu.raise_()
        self.line_2.raise_()
        self.lblTitulo_ficha_estu.raise_()
        self.btnEliminar_ficha_estu.raise_()
        self.lblCedula_registro_estudiante.raise_()
        self.lblEstado_ficha_estu.raise_()
        self.btnDevolver_grado.raise_()

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(ficha_estu)

        self.stackFicha_estu.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(ficha_estu)
    # setupUi

    def retranslateUi(self, ficha_estu):
        ficha_estu.setWindowTitle(QCoreApplication.translate("ficha_estu", u"Dialog", None))
        self.lneCedula_ficha_estu.setText("")
        self.lneCedula_ficha_estu.setPlaceholderText(QCoreApplication.translate("ficha_estu", u"Ingrese cedula estudiantil...", None))
        self.lblStudent_apellido.setText(QCoreApplication.translate("ficha_estu", u"Apellidos", None))
        self.lneApellido_ficha_estu.setText("")
        self.lneApellido_ficha_estu.setPlaceholderText("")
        self.lneNombre_ficha_estu.setText("")
        self.lneNombre_ficha_estu.setPlaceholderText("")
        self.lblStudent_nombres.setText(QCoreApplication.translate("ficha_estu", u"Nombres", None))
        self.lblStudent_lugarNac.setText(QCoreApplication.translate("ficha_estu", u"Lugar Nac.", None))
        self.lblStudent_fechaNac.setText(QCoreApplication.translate("ficha_estu", u"Fecha Nac.", None))
        self.lneCity_ficha_estu.setText("")
        self.lneCity_ficha_estu.setPlaceholderText("")
        self.lneEdad_ficha_estu.setText("")
        self.lneEdad_ficha_estu.setPlaceholderText("")
        self.lblStudent_edad.setText(QCoreApplication.translate("ficha_estu", u"Edad", None))
        self.lblStudent_genero.setText(QCoreApplication.translate("ficha_estu", u"G\u00e9nero", None))
        self.lneDir_ficha_estu.setText("")
        self.lneDir_ficha_estu.setPlaceholderText("")
        self.lblStudent_dir.setText(QCoreApplication.translate("ficha_estu", u"Direcci\u00f3n", None))
        self.lblGrado.setText(QCoreApplication.translate("ficha_estu", u"Grado", None))
        self.lblSeccion.setText(QCoreApplication.translate("ficha_estu", u"Secci\u00f3n", None))
        self.lneDocente_ficha_estu.setText("")
        self.lneDocente_ficha_estu.setPlaceholderText("")
        self.label_35.setText(QCoreApplication.translate("ficha_estu", u"Docente", None))
        self.label_42.setText(QCoreApplication.translate("ficha_estu", u"Talla Camisa", None))
        self.lneTallaC_ficha_estu.setText("")
        self.lneTallaC_ficha_estu.setPlaceholderText("")
        self.label_44.setText(QCoreApplication.translate("ficha_estu", u"Talla Pantal\u00f3n", None))
        self.lneTallaP_ficha_estu.setText("")
        self.lneTallaP_ficha_estu.setPlaceholderText("")
        self.lneTallaZ_ficha_estu.setText("")
        self.lneTallaZ_ficha_estu.setPlaceholderText("")
        self.label_49.setText(QCoreApplication.translate("ficha_estu", u"Talla Zapatos", None))
        self.lneFechaNac_ficha_estu.setDisplayFormat(QCoreApplication.translate("ficha_estu", u"yyyy/M/d", None))
        self.cbxSeccion_ficha_estu.setItemText(0, QCoreApplication.translate("ficha_estu", u"A", None))
        self.cbxSeccion_ficha_estu.setItemText(1, QCoreApplication.translate("ficha_estu", u"B", None))
        self.cbxSeccion_ficha_estu.setItemText(2, QCoreApplication.translate("ficha_estu", u"C", None))

        self.cbxGrado_ficha_estu.setItemText(0, "")
        self.cbxGrado_ficha_estu.setItemText(1, QCoreApplication.translate("ficha_estu", u"1ero", None))
        self.cbxGrado_ficha_estu.setItemText(2, QCoreApplication.translate("ficha_estu", u"2do", None))
        self.cbxGrado_ficha_estu.setItemText(3, QCoreApplication.translate("ficha_estu", u"3ro", None))
        self.cbxGrado_ficha_estu.setItemText(4, QCoreApplication.translate("ficha_estu", u"4to", None))
        self.cbxGrado_ficha_estu.setItemText(5, QCoreApplication.translate("ficha_estu", u"5to", None))
        self.cbxGrado_ficha_estu.setItemText(6, QCoreApplication.translate("ficha_estu", u"6to", None))

        self.cbxGenero_ficha_estu.setItemText(0, "")
        self.cbxGenero_ficha_estu.setItemText(1, QCoreApplication.translate("ficha_estu", u"M", None))
        self.cbxGenero_ficha_estu.setItemText(2, QCoreApplication.translate("ficha_estu", u"F", None))

        self.lblStudent_fechaIng.setText(QCoreApplication.translate("ficha_estu", u"Fecha Ing.", None))
        self.lneFechaIng_ficha_estu.setDisplayFormat(QCoreApplication.translate("ficha_estu", u"yyyy/M/d", None))
        self.cbxTipoEdu_ficha_estu.setItemText(0, "")
        self.cbxTipoEdu_ficha_estu.setItemText(1, QCoreApplication.translate("ficha_estu", u"Inicial", None))
        self.cbxTipoEdu_ficha_estu.setItemText(2, QCoreApplication.translate("ficha_estu", u"Primaria", None))

        self.lblTipoEdu.setText(QCoreApplication.translate("ficha_estu", u"Tipo educaci\u00f3n", None))
        self.lneEstatus_egresado.setText("")
        self.lneEstatus_egresado.setPlaceholderText("")
        self.lblEstatus.setText(QCoreApplication.translate("ficha_estu", u"Estatus", None))
        self.lneUltimoGrado.setText("")
        self.lneUltimoGrado.setPlaceholderText("")
        self.lblUltimoGrado.setText(QCoreApplication.translate("ficha_estu", u"Ultimo grado", None))
        self.lneAnioEgreso.setText("")
        self.lneAnioEgreso.setPlaceholderText("")
        self.lblAnioEgreso.setText(QCoreApplication.translate("ficha_estu", u"A\u00f1o egreso:", None))
        self.lneMadre_ficha_estu.setText("")
        self.lneMadre_ficha_estu.setPlaceholderText("")
        self.lblStudent_apellido_repre_2.setText(QCoreApplication.translate("ficha_estu", u"Madre", None))
        self.lnePadre_ficha_estu.setText("")
        self.lnePadre_ficha_estu.setPlaceholderText("")
        self.lblStudent_nombres_3.setText(QCoreApplication.translate("ficha_estu", u"Padre", None))
        self.lblStudent_fechaNac_repre_2.setText(QCoreApplication.translate("ficha_estu", u"Cedula Madre", None))
        self.lneCedula_madre_ficha_estu.setText("")
        self.lneCedula_madre_ficha_estu.setPlaceholderText("")
        self.lneCedula_padre_ficha_estu.setText("")
        self.lneCedula_padre_ficha_estu.setPlaceholderText("")
        self.lblStudent_fechaNac_repre_3.setText(QCoreApplication.translate("ficha_estu", u"Cedula Padre", None))
        self.lblStudent_nombres_2.setText(QCoreApplication.translate("ficha_estu", u"Nombres", None))
        self.lneApellidos_repre_ficha_estu.setText("")
        self.lneApellidos_repre_ficha_estu.setPlaceholderText("")
        self.lblStudent_apellido_repre.setText(QCoreApplication.translate("ficha_estu", u"Apellidos", None))
        self.lneNombres_repre_ficha_estu.setText("")
        self.lneNombres_repre_ficha_estu.setPlaceholderText("")
        self.lblStudent_dir_repre.setText(QCoreApplication.translate("ficha_estu", u"Direcci\u00f3n", None))
        self.lneDir_repre_ficha_estu.setText("")
        self.lneDir_repre_ficha_estu.setPlaceholderText("")
        self.lneEdad_repre_ficha_estu.setText("")
        self.lneEdad_repre_ficha_estu.setPlaceholderText("")
        self.label_41.setText(QCoreApplication.translate("ficha_estu", u"Num. Contact.", None))
        self.lneNum_repre_ficha_estu.setText("")
        self.lneNum_repre_ficha_estu.setPlaceholderText("")
        self.lblStudent_fechaNac_repre.setText(QCoreApplication.translate("ficha_estu", u"Fecha Nac.", None))
        self.lblStudent_edad_repre.setText(QCoreApplication.translate("ficha_estu", u"Edad", None))
        self.lneCedula_repre_ficha_estu.setText("")
        self.lneCedula_repre_ficha_estu.setPlaceholderText("")
        self.lneCorreo_repre_ficha_estu.setText("")
        self.lneCorreo_repre_ficha_estu.setPlaceholderText("")
        self.label_38.setText(QCoreApplication.translate("ficha_estu", u"Correo Elect.", None))
        self.lblStudent_genero_repre.setText(QCoreApplication.translate("ficha_estu", u"G\u00e9nero", None))
        self.lblTitulo_registro_estudiante_2.setText(QCoreApplication.translate("ficha_estu", u"Datos representante", None))
        self.lblStudent_fechaNac_repre_4.setText(QCoreApplication.translate("ficha_estu", u"Cedula", None))
        self.lneFechaNac_repre_ficha_estu.setDisplayFormat(QCoreApplication.translate("ficha_estu", u"yyyy/M/d", None))
        self.cbxGenero_repre_ficha_estu.setItemText(0, "")
        self.cbxGenero_repre_ficha_estu.setItemText(1, QCoreApplication.translate("ficha_estu", u"M", None))
        self.cbxGenero_repre_ficha_estu.setItemText(2, QCoreApplication.translate("ficha_estu", u"F", None))

        self.lblStudent_dir_repre_2.setText(QCoreApplication.translate("ficha_estu", u"Observaci\u00f3n:", None))
        self.lneObser_ficha_estu_repre.setText("")
        self.lneObser_ficha_estu_repre.setPlaceholderText("")
        self.lneOcup_madre_ficha_estu.setText("")
        self.lneOcup_madre_ficha_estu.setPlaceholderText("")
        self.lneOcup_padre_ficha_estu.setText("")
        self.lneOcup_padre_ficha_estu.setPlaceholderText("")
        self.lblStudent_fechaNac_repre_6.setText(QCoreApplication.translate("ficha_estu", u"Ocupaci\u00f3n", None))
        self.lblStudent_fechaNac_repre_5.setText(QCoreApplication.translate("ficha_estu", u"Ocupaci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.btnStudentDatos_ficha.setToolTip(QCoreApplication.translate("ficha_estu", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.btnStudentDatos_ficha.setText(QCoreApplication.translate("ficha_estu", u"Datos personales", None))
#if QT_CONFIG(tooltip)
        self.btnRepre_ficha.setToolTip(QCoreApplication.translate("ficha_estu", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.btnRepre_ficha.setText(QCoreApplication.translate("ficha_estu", u"Datos Representante", None))
        self.btnModificar_ficha_estu.setText(QCoreApplication.translate("ficha_estu", u"Modificar", None))
        self.btnExportar_ficha_estu.setText(QCoreApplication.translate("ficha_estu", u"Generar PDF", None))
        self.lblLogo_ficha_estu.setText("")
        self.lblTitulo_ficha_estu.setText(QCoreApplication.translate("ficha_estu", u"Ficha de estudiante", None))
        self.btnEliminar_ficha_estu.setText(QCoreApplication.translate("ficha_estu", u"Eliminar", None))
        self.lblCedula_registro_estudiante.setText(QCoreApplication.translate("ficha_estu", u"C\u00e9dula Estudiantil", None))
        self.lblEstado_ficha_estu.setText(QCoreApplication.translate("ficha_estu", u"Activo/Inactivo", None))
#if QT_CONFIG(tooltip)
        self.btnHistorial_estu.setToolTip(QCoreApplication.translate("ficha_estu", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.btnHistorial_estu.setText(QCoreApplication.translate("ficha_estu", u"Historial acad\u00e9mico", None))
        self.btnDevolver_grado.setText(QCoreApplication.translate("ficha_estu", u"Devolver a grado anterior", None))
    # retranslateUi

