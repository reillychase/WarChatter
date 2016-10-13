# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warchat.ui'
#
# Created: Thu Oct 13 09:55:54 2016
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
        MainWindow.resize(802, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.scroll_chat = QtGui.QScrollArea(self.verticalLayoutWidget)
        self.scroll_chat.setWidgetResizable(True)
        self.scroll_chat.setObjectName(_fromUtf8("scroll_chat"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 394, 316))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.textedit_chat = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textedit_chat.setGeometry(QtCore.QRect(0, 0, 391, 321))
        self.textedit_chat.setObjectName(_fromUtf8("textedit_chat"))
        self.scroll_chat.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scroll_chat)
        self.scroll_users = QtGui.QScrollArea(self.verticalLayoutWidget)
        self.scroll_users.setWidgetResizable(True)
        self.scroll_users.setObjectName(_fromUtf8("scroll_users"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 393, 316))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.textedit_users = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textedit_users.setGeometry(QtCore.QRect(-10, 0, 401, 321))
        self.textedit_users.setObjectName(_fromUtf8("textedit_users"))
        self.scroll_users.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.addWidget(self.scroll_users)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.input_password = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.input_password.setObjectName(_fromUtf8("input_password"))
        self.verticalLayout.addWidget(self.input_password)
        self.input_username = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.input_username.setObjectName(_fromUtf8("input_username"))
        self.verticalLayout.addWidget(self.input_username)
        self.input_server = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.input_server.setText(_fromUtf8(""))
        self.input_server.setObjectName(_fromUtf8("input_server"))
        self.verticalLayout.addWidget(self.input_server)
        self.button_login = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_login.setObjectName(_fromUtf8("button_login"))
        self.verticalLayout.addWidget(self.button_login)
        self.label_status_msg = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_status_msg.setObjectName(_fromUtf8("label_status_msg"))
        self.verticalLayout.addWidget(self.label_status_msg)
        self.button_logout = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_logout.setObjectName(_fromUtf8("button_logout"))
        self.verticalLayout.addWidget(self.button_logout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.input_prefix = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.input_prefix.setObjectName(_fromUtf8("input_prefix"))
        self.horizontalLayout_4.addWidget(self.input_prefix)
        self.input_msg = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.input_msg.setObjectName(_fromUtf8("input_msg"))
        self.horizontalLayout_4.addWidget(self.input_msg)
        self.button_send = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_send.setObjectName(_fromUtf8("button_send"))
        self.horizontalLayout_4.addWidget(self.button_send)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.input_password.setPlaceholderText(_translate("MainWindow", "Password", None))
        self.input_username.setPlaceholderText(_translate("MainWindow", "Username", None))
        self.input_server.setPlaceholderText(_translate("MainWindow", "Server", None))
        self.button_login.setText(_translate("MainWindow", "Login", None))
        self.label_status_msg.setText(_translate("MainWindow", "Not Connected", None))
        self.button_logout.setText(_translate("MainWindow", "Logout", None))
        self.button_send.setText(_translate("MainWindow", "Send", None))

