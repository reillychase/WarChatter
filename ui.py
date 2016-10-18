# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warchatter.ui'
#
# Created: Fri Oct 14 10:59:57 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(810, 610)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_login = QtGui.QWidget()
        self.page_login.setObjectName(_fromUtf8("page_login"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.page_login)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 791, 541))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_title = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.verticalLayout_6.addWidget(self.label_title)
        self.input_username = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.input_username.setObjectName(_fromUtf8("input_username"))
        self.verticalLayout_6.addWidget(self.input_username)
        self.input_password = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.input_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.input_password.setEchoMode(QtGui.QLineEdit.Password)
        self.input_password.setObjectName(_fromUtf8("input_password"))
        self.verticalLayout_6.addWidget(self.input_password)
        self.input_server = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.input_server.setObjectName(_fromUtf8("input_server"))
        self.verticalLayout_6.addWidget(self.input_server)
        self.input_channel = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.input_channel.setObjectName(_fromUtf8("input_channel"))
        self.verticalLayout_6.addWidget(self.input_channel)
        self.input_client_tag = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.input_client_tag.setObjectName(_fromUtf8("input_client_tag"))
        self.verticalLayout_6.addWidget(self.input_client_tag)
        self.button_login = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.button_login.setObjectName(_fromUtf8("button_login"))
        self.verticalLayout_6.addWidget(self.button_login)
        self.label_status_msg = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_status_msg.setText(_fromUtf8(""))
        self.label_status_msg.setObjectName(_fromUtf8("label_status_msg"))
        self.verticalLayout_6.addWidget(self.label_status_msg)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.page_login)
        self.page_chat = QtGui.QWidget()
        self.page_chat.setObjectName(_fromUtf8("page_chat"))
        self.verticalLayoutWidget = QtGui.QWidget(self.page_chat)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 791, 541))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.button_logout = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_logout.setObjectName(_fromUtf8("button_logout"))
        self.horizontalLayout_2.addWidget(self.button_logout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textedit_users = QtGui.QTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_users.sizePolicy().hasHeightForWidth())
        self.textedit_users.setSizePolicy(sizePolicy)
        self.textedit_users.setMaximumSize(QtCore.QSize(150, 16777215))
        self.textedit_users.setReadOnly(True)
        self.textedit_users.setObjectName(_fromUtf8("textedit_users"))
        self.gridLayout.addWidget(self.textedit_users, 1, 1, 1, 1)
        self.label_channel = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_channel.setText(_fromUtf8(""))
        self.label_channel.setObjectName(_fromUtf8("label_channel"))
        self.gridLayout.addWidget(self.label_channel, 0, 1, 1, 1)
        self.textedit_chat = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.textedit_chat.setAutoFillBackground(False)
        self.textedit_chat.setOpenExternalLinks(True)
        self.textedit_chat.setObjectName(_fromUtf8("textedit_chat"))
        self.gridLayout.addWidget(self.textedit_chat, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.input_msg_prefix = QtGui.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_msg_prefix.sizePolicy().hasHeightForWidth())
        self.input_msg_prefix.setSizePolicy(sizePolicy)
        self.input_msg_prefix.setObjectName(_fromUtf8("input_msg_prefix"))
        self.horizontalLayout_7.addWidget(self.input_msg_prefix)
        self.input_msg = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.input_msg.setObjectName(_fromUtf8("input_msg"))
        self.horizontalLayout_7.addWidget(self.input_msg)
        self.button_send = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_send.setObjectName(_fromUtf8("button_send"))
        self.horizontalLayout_7.addWidget(self.button_send)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.stackedWidget.addWidget(self.page_chat)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/warchatter/warchatter.png\"/></p></body></html>", None))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">PvPGN Login Info</span></p></body></html>", None))
        self.input_username.setPlaceholderText(_translate("MainWindow", "Username", None))
        self.input_password.setPlaceholderText(_translate("MainWindow", "Password", None))
        self.input_server.setText(_translate("MainWindow", "server.war2.ru", None))
        self.input_server.setPlaceholderText(_translate("MainWindow", "Server", None))
        self.input_channel.setText(_translate("MainWindow", "War2BNE", None))
        self.input_channel.setPlaceholderText(_translate("MainWindow", "Channel", None))
        self.input_client_tag.setText(_translate("MainWindow", "W2BN", None))
        self.input_client_tag.setPlaceholderText(_translate("MainWindow", "Game Tag", None))
        self.button_login.setText(_translate("MainWindow", "Login", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/warchatter/warchatter.png\"/></p></body></html>", None))
        self.button_logout.setText(_translate("MainWindow", "Logout", None))
        self.textedit_users.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\" bgcolor=\"#d3d3d3\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textedit_chat.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\" bgcolor=\"#000000\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_send.setText(_translate("MainWindow", "Send", None))

import resources_rc
