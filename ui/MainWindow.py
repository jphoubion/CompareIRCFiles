# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(5, -1, -1, 0)
        self.lbl_old_file = QLabel(self.centralwidget)
        self.lbl_old_file.setObjectName(u"lbl_old_file")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_old_file.sizePolicy().hasHeightForWidth())
        self.lbl_old_file.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.lbl_old_file.setFont(font)

        self.horizontalLayout.addWidget(self.lbl_old_file)

        self.lbl_old_filename = QLabel(self.centralwidget)
        self.lbl_old_filename.setObjectName(u"lbl_old_filename")
        self.lbl_old_filename.setFont(font)
        self.lbl_old_filename.setFrameShape(QFrame.StyledPanel)

        self.horizontalLayout.addWidget(self.lbl_old_filename)

        self.btn_old_file = QPushButton(self.centralwidget)
        self.btn_old_file.setObjectName(u"btn_old_file")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_old_file.sizePolicy().hasHeightForWidth())
        self.btn_old_file.setSizePolicy(sizePolicy2)
        icon = QIcon()
        iconThemeName = u"document-open"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btn_old_file.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_old_file)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_2.setContentsMargins(5, -1, -1, 0)
        self.lbl_new_file = QLabel(self.centralwidget)
        self.lbl_new_file.setObjectName(u"lbl_new_file")
        sizePolicy1.setHeightForWidth(self.lbl_new_file.sizePolicy().hasHeightForWidth())
        self.lbl_new_file.setSizePolicy(sizePolicy1)
        self.lbl_new_file.setFont(font)

        self.horizontalLayout_2.addWidget(self.lbl_new_file)

        self.lbl_new_filename = QLabel(self.centralwidget)
        self.lbl_new_filename.setObjectName(u"lbl_new_filename")
        self.lbl_new_filename.setFont(font)
        self.lbl_new_filename.setFrameShape(QFrame.StyledPanel)

        self.horizontalLayout_2.addWidget(self.lbl_new_filename)

        self.btn_new_file = QPushButton(self.centralwidget)
        self.btn_new_file.setObjectName(u"btn_new_file")
        sizePolicy2.setHeightForWidth(self.btn_new_file.sizePolicy().hasHeightForWidth())
        self.btn_new_file.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.btn_new_file)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.tw_old_file = QTableWidget(self.centralwidget)
        self.tw_old_file.setObjectName(u"tw_old_file")

        self.gridLayout.addWidget(self.tw_old_file, 3, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.tw_new_file = QTableWidget(self.centralwidget)
        self.tw_new_file.setObjectName(u"tw_new_file")

        self.gridLayout.addWidget(self.tw_new_file, 5, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.tw_result = QTableWidget(self.centralwidget)
        self.tw_result.setObjectName(u"tw_result")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tw_result.sizePolicy().hasHeightForWidth())
        self.tw_result.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.tw_result, 7, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_compare = QPushButton(self.centralwidget)
        self.btn_compare.setObjectName(u"btn_compare")

        self.horizontalLayout_3.addWidget(self.btn_compare)

        self.btn_export = QPushButton(self.centralwidget)
        self.btn_export.setObjectName(u"btn_export")

        self.horizontalLayout_3.addWidget(self.btn_export)

        self.btn_Quit = QPushButton(self.centralwidget)
        self.btn_Quit.setObjectName(u"btn_Quit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_Quit.sizePolicy().hasHeightForWidth())
        self.btn_Quit.setSizePolicy(sizePolicy4)
        self.btn_Quit.setFlat(False)

        self.horizontalLayout_3.addWidget(self.btn_Quit)


        self.gridLayout.addLayout(self.horizontalLayout_3, 8, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"IRCCompareFiles - V 1.0", None))
        self.lbl_old_file.setText(QCoreApplication.translate("MainWindow", u"Ancien fichier :", None))
        self.lbl_old_filename.setText("")
        self.btn_old_file.setText(QCoreApplication.translate("MainWindow", u"S\u00e9lectionner le fichier", None))
        self.lbl_new_file.setText(QCoreApplication.translate("MainWindow", u"Nouveau fichier :", None))
        self.lbl_new_filename.setText("")
        self.btn_new_file.setText(QCoreApplication.translate("MainWindow", u"S\u00e9lectionner le fichier", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fichier actuel :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nouveau fichier :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"R\u00e9sultats :", None))
        self.btn_compare.setText(QCoreApplication.translate("MainWindow", u"Comparer", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"Export vers fichier Excel", None))
        self.btn_Quit.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
    # retranslateUi

