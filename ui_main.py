# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainYVYVKO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys, os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1154, 636)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 40))
        self.top_frame.setMaximumSize(QSize(16777215, 40))
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggle_frame = QFrame(self.top_frame)
        self.toggle_frame.setObjectName(u"toggle_frame")
        self.toggle_frame.setMinimumSize(QSize(100, 40))
        self.toggle_frame.setMaximumSize(QSize(100, 40))
        self.toggle_frame.setStyleSheet(u"")
        self.toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.toggle_frame.setFrameShadow(QFrame.Raised)
        self.toggle_btn = QPushButton(self.toggle_frame)
        self.toggle_btn.setObjectName(u"toggle_btn")
        self.toggle_btn.setGeometry(QRect(0, 0, 100, 40))
        self.toggle_btn.setMaximumSize(QSize(150, 40))
        self.toggle_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggle_btn.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:0px solid;\n"
"}")
        icon = QIcon()
        icon.addFile(resource_path("menu-button.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.toggle_btn.setIcon(icon)
        self.toggle_btn.setIconSize(QSize(50, 50))
        self.toggle_btn.setAutoDefault(False)
        self.toggle_btn.setFlat(True)

        self.horizontalLayout_2.addWidget(self.toggle_frame)

        self.top_space = QFrame(self.top_frame)
        self.top_space.setObjectName(u"top_space")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_space.sizePolicy().hasHeightForWidth())
        self.top_space.setSizePolicy(sizePolicy)
        self.top_space.setMaximumSize(QSize(16777215, 40))
        self.top_space.setFrameShape(QFrame.StyledPanel)
        self.top_space.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.top_space)


        self.verticalLayout.addWidget(self.top_frame)

        self.content_frame = QFrame(self.centralwidget)
        self.content_frame.setObjectName(u"content_frame")
        sizePolicy.setHeightForWidth(self.content_frame.sizePolicy().hasHeightForWidth())
        self.content_frame.setSizePolicy(sizePolicy)
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.content_frame)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMinimumSize(QSize(0, 0))
        self.sidebar.setMaximumSize(QSize(0, 16777215))
        self.sidebar.setStyleSheet(u"")
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.enc_btn = QPushButton(self.sidebar)
        self.enc_btn.setObjectName(u"enc_btn")
        self.enc_btn.setGeometry(QRect(10, 220, 131, 41))
        self.enc_btn.setStyleSheet(u"QPushButton:hover{\n"
"	border:0px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.var_enc_btn = QPushButton(self.sidebar)
        self.var_enc_btn.setObjectName(u"var_enc_btn")
        self.var_enc_btn.setGeometry(QRect(10, 300, 131, 41))
        self.var_enc_btn.setStyleSheet(u"QPushButton:hover{\n"
"	border:0px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.select_btn = QPushButton(self.sidebar)
        self.select_btn.setObjectName(u"select_btn")
        self.select_btn.setGeometry(QRect(10, 70, 131, 41))
        self.select_btn.setStyleSheet(u"QPushButton:hover{\n"
"	border:0px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.save_btn = QPushButton(self.sidebar)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(10, 380, 131, 41))
        self.save_btn.setStyleSheet(u"QPushButton:hover{\n"
"	border:0px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.about = QPushButton(self.sidebar)
        self.about.setObjectName(u"about")
        self.about.setGeometry(QRect(10, 460, 131, 41))
        self.about.setStyleSheet(u"QPushButton:hover{\n"
"	border:0px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.org_btn = QPushButton(self.sidebar)
        self.org_btn.setObjectName(u"org_btn")
        self.org_btn.setGeometry(QRect(10, 150, 131, 41))
        self.org_btn.setStyleSheet(u"QPushButton:hover{\n"
"	border:0px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.sidebar)

        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        sizePolicy1.setHeightForWidth(self.page1.sizePolicy().hasHeightForWidth())
        self.page1.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.page1)
        self.gridLayout.setSpacing(21)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(21, 0, 21, 21)
        self.org_loc = QLabel(self.page1)
        self.org_loc.setObjectName(u"org_loc")
        self.org_loc.setMaximumSize(QSize(16777215, 40))
        self.org_loc.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")

        self.gridLayout.addWidget(self.org_loc, 0, 0, 1, 1)

        self.browse = QPushButton(self.page1)
        self.browse.setObjectName(u"browse")
        self.browse.setMaximumSize(QSize(160, 40))
        self.browse.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 0);\n"
"}")

        self.gridLayout.addWidget(self.browse, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_3 = QVBoxLayout(self.page2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.copy_btn = QPushButton(self.page2)
        self.copy_btn.setObjectName(u"copy_btn")
        self.copy_btn.setStyleSheet(u"QPushButton:hover{\n"
"	border:0px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.copy_btn, 0, Qt.AlignRight)

        self.code_here = QTextBrowser(self.page2)
        self.code_here.setObjectName(u"code_here")
        self.code_here.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_3.addWidget(self.code_here)

        self.stackedWidget.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.verticalLayout_5 = QVBoxLayout(self.page3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.copy_btn_2 = QPushButton(self.page3)
        self.copy_btn_2.setObjectName(u"copy_btn_2")
        self.copy_btn_2.setStyleSheet(u"QPushButton:hover{\n"
"	border:0px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_5.addWidget(self.copy_btn_2, 0, Qt.AlignRight)

        self.emj_code_here = QTextBrowser(self.page3)
        self.emj_code_here.setObjectName(u"emj_code_here")
        self.emj_code_here.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_5.addWidget(self.emj_code_here)

        self.stackedWidget.addWidget(self.page3)
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.verticalLayout_6 = QVBoxLayout(self.page4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.copy_btn_3 = QPushButton(self.page4)
        self.copy_btn_3.setObjectName(u"copy_btn_3")
        self.copy_btn_3.setStyleSheet(u"QPushButton:hover{\n"
"	border:0px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.copy_btn_3, 0, Qt.AlignRight)

        self.var_code_here = QTextBrowser(self.page4)
        self.var_code_here.setObjectName(u"var_code_here")
        self.var_code_here.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.var_code_here)

        self.stackedWidget.addWidget(self.page4)
        self.page5 = QWidget()
        self.page5.setObjectName(u"page5")
        self.gridLayout_2 = QGridLayout(self.page5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.save_emj = QPushButton(self.page5)
        self.save_emj.setObjectName(u"save_emj")
        self.save_emj.setMinimumSize(QSize(0, 0))
        self.save_emj.setMaximumSize(QSize(150, 40))
        self.save_emj.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 0);\n"
"}")

        self.gridLayout_2.addWidget(self.save_emj, 0, 1, 1, 1)

        self.save_loc_emj = QLabel(self.page5)
        self.save_loc_emj.setObjectName(u"save_loc_emj")
        self.save_loc_emj.setMaximumSize(QSize(16777215, 40))
        self.save_loc_emj.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;")

        self.gridLayout_2.addWidget(self.save_loc_emj, 0, 0, 1, 1)

        self.save_var = QPushButton(self.page5)
        self.save_var.setObjectName(u"save_var")
        self.save_var.setMinimumSize(QSize(0, 40))
        self.save_var.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 0);\n"
"}")

        self.gridLayout_2.addWidget(self.save_var, 1, 1, 1, 1)

        self.save_var_2 = QLabel(self.page5)
        self.save_var_2.setObjectName(u"save_var_2")
        self.save_var_2.setMinimumSize(QSize(0, 40))
        self.save_var_2.setMaximumSize(QSize(16777215, 40))
        self.save_var_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;")

        self.gridLayout_2.addWidget(self.save_var_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page5)
        self.page6 = QWidget()
        self.page6.setObjectName(u"page6")
        self.verticalLayout_4 = QVBoxLayout(self.page6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.page6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setCursor(QCursor(Qt.BlankCursor))
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.page6)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addWidget(self.content_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggle_btn.setText("")
        self.enc_btn.setText(QCoreApplication.translate("MainWindow", u"Emoji Encrypted Code", None))
        self.var_enc_btn.setText(QCoreApplication.translate("MainWindow", u"VAR Encrypted Code", None))
        self.select_btn.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save Encrypted Code", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.org_btn.setText(QCoreApplication.translate("MainWindow", u"Original Code", None))
        self.org_loc.setText("")
        self.browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.copy_btn.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.copy_btn_2.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.copy_btn_3.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.save_emj.setText(QCoreApplication.translate("MainWindow", u"Save Emoji Code", None))
        self.save_loc_emj.setText("")
        self.save_var.setText(QCoreApplication.translate("MainWindow", u"Save Var Code", None))
        self.save_var_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; text-decoration: underline;\">ABOUT</span><br/></p><p align=\"center\"><span style=\" font-size:14pt;\">This app helps developer to Encrypt their python code.</span></p><p align=\"center\"><br/><br/></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; text-decoration: underline;\">Developers</span><span style=\" font-size:26pt; font-weight:600;\"><br/></span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:26pt; font-style:italic;\">Inderjeet Singh (22BTC35118)</span></p><p align=\"center\"><span style=\" font-size:26pt; font-style:italic;\">Nishant Pratap Savita (22BTC35142)</span></p><p align=\"center\"><span style=\" font-size:26pt; font-style:italic;\">Gunjan</span></p><p align=\"center\"><br/></p></body></html>", None))
    # retranslateUi

