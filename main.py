from PyQt4 import QtGui
import sys
import time
import socket
import ui
import re
from PyQt4.QtCore import QThread, SIGNAL

class chat_thread(QThread):
    def __init__(self, username, password, server, channel, client_tag):

        print 'chat_thread.__init__()'

        QThread.__init__(self)
        self.username = str(username)
        self.password = str(password)
        self.server = str(server)
        self.channel = str(channel)
        self.client_tag = str(client_tag)
        self.login_attempts = 0
        self.end_flag = 0

    def __del__(self):

        print 'chat_thread.__del__()'

        self.wait()

    def pvpgn_login(self):

        print 'chat_thread.pvpgn_login()\n'

        while True:

            self.connection_status = 0

            try:
                self.buffer_size = 2048
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((self.server, 6112))
                self.s.setblocking(0)
                self.s.settimeout(10)

                self.s.send("\r\n")

                self.s.send(self.username)
                self.s.send("\r\n")

                self.s.send(self.password)
                self.s.send("\r\n")

                total_data = [];
                data = ''
                while True:
                    data = self.s.recv(8192)
                    if 'Joining channel:' in data or 'Login failed.' in data:
                        total_data.append(data)
                        break
                    total_data.append(data)
                    if len(total_data) > 1:
                        # check if end_of_data was split
                        last_pair = total_data[-2] + total_data[-1]
                        if 'Joining channel:' in last_pair:
                            total_data[-2] = last_pair[:last_pair.find('Joining channel:')]
                            total_data.pop()
                            break
                data = ''.join(total_data)

                print 'WarChat DEBUG: chat_thread.pvpgn_login() Output -----'
                print data
                print '--------------------------------------------------'


                if "failed" in data:
                    self.connection_status = 0
                    self.emit(SIGNAL('catch_status_msg(QString, QString)'), 'Login failed', 'red')
                    return

                elif "no bot" in data:
                    self.connection_status = 0
                    self.emit(SIGNAL('catch_status_msg(QString, QString)'), 'Server not supported', 'red')
                    return

                elif "Your unique name:" in data:
                    self.connection_status = 1
                    if self.channel:
                        self.s.send("/join " + self.channel)
                        self.s.send("\r\n")
                        total_data = [];
                        data = ''
                        while True:
                            data = self.s.recv(8192)
                            if 'Joining channel:' in data or 'Login failed.' in data:
                                total_data.append(data)
                                break
                            total_data.append(data)
                            if len(total_data) > 1:
                                # check if end_of_data was split
                                last_pair = total_data[-2] + total_data[-1]
                                if 'Joining channel:' in last_pair:
                                    total_data[-2] = last_pair[:last_pair.find('Joining channel:')]
                                    total_data.pop()
                                    break
                        data = ''.join(total_data)
                    self.emit(SIGNAL('catch_status_msg(QString, QString)'), 'Login success', 'green')
                    self.emit(SIGNAL('catch_textedit_chat(QString, QString)'), data, 'white')
                    return

                else:
                    self.connection_status = 0
                    self.emit(SIGNAL('catch_status_msg(QString, QString)'), 'Received invalid response', 'red')
                    break

            except Exception as e:
                print 'WarChat Debug: chat_thread.pvpgn_login Socket Error -----'
                print e
                print '--------------------------------------------------------'
                self.emit(SIGNAL('catch_status_msg(QString, QString)'), 'No reply from server', 'red')
                self.connection_status = 0
                return

    def loop_chat_recv(self):
        if self.end_flag == 0:
            while True:
                try:

                    data = self.s.recv(8192)
                    if data:
                        self.emit(SIGNAL('catch_textedit_chat(QString, QString)'), data, 'white')
                        print '-----------'
                        print data
                        print '------------'
                        time.sleep(.1)
                except:
                    time.sleep(.1)
                    continue


    def run(self):
            print 'chat_thread.run()'
            self.pvpgn_login()
            if self.connection_status == 1:
                self.emit(SIGNAL('catch_login_success()'))
                self.loop_chat_recv()

class WarChatter(QtGui.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        print 'WarChat.__init__()'
        # super allows us to access variables, methods etc in the ui.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in ui.py file automatically
        # It sets up layout and widgets that are defined
        self.button_login.clicked.connect(self.login)
        self.button_logout.clicked.connect(self.logout)
        self.button_send.clicked.connect(self.send_msg)
        self.textedit_chat.setReadOnly(True)
        self.textedit_users.setReadOnly(True)
        self.users_in_chan = []
        self.endflag = 0
        self.input_msg.returnPressed.connect(self.send_msg)
        self.input_msg_prefix.returnPressed.connect(self.send_msg)
        self.input_username.returnPressed.connect(self.login)
        self.input_password.returnPressed.connect(self.login)
        self.input_server.returnPressed.connect(self.login)
        self.input_channel.returnPressed.connect(self.login)
        self.input_client_tag.returnPressed.connect(self.login)
        # Gather and assign all the user input:
        self.username = ''
        self.password = ''
        self.server = ''

    def send_msg(self):
        print 'WarChatter.send_msg()'
        # Gather and assign all the user input:
        self.username = self.input_username.text()
        self.msg_prefix = str(self.input_msg_prefix.text())
        self.msg = str(self.input_msg.text())

        if self.msg_prefix:
            self.msg = self.msg_prefix + ' ' + self.msg
        self.input_msg.setText('')
        if re.findall('^/stats$', self.msg):
            print 'stats for myself'
            self.msg = self.msg + ' ' + self.username + ' ' + self.client_tag
            print self.msg
            self.get_thread.s.send(str(self.msg))
            self.get_thread.s.send("\r\n")

        elif re.findall('^/stats (.+?)$', self.msg):
            print 'stats for other'
            self.msg = self.msg + ' ' + self.client_tag
            print self.msg
            self.get_thread.s.send(str(self.msg))
            self.get_thread.s.send("\r\n")

        elif re.findall('^/', self.msg):
            print 'a command was sent'
            self.get_thread.s.send(self.msg)
            self.get_thread.s.send("\r\n")

        else:
            self.get_thread.s.send(self.msg)
            self.get_thread.s.send("\r\n")
            msg = '<span style="color: #00ffff;">&lt;' + self.username + '&gt;</span><span style="color: white;" > ' + self.msg + '</span>'
            self.catch_textedit_chat_2(msg, 'white')

    def logout(self):

        self.end_flag = 1
        self.users_in_chan = []

        self.get_thread.s.send("/logout")
        self.get_thread.s.send("\r\n")
        self.get_thread.s.close()


        self.textedit_chat.setText('')

        self.textedit_chat.setHtml(ui._translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Droid Sans\'; font-size:12pt; font-weight:400; font-style:normal;\" bgcolor=\"#000000\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                              None))
        self.textedit_users.setText('')
        self.textedit_users.setHtml(ui._translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Droid Sans\'; font-size:12pt; font-weight:400; font-style:normal;\" bgcolor=\"#d3d3d3\">\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                               None))
        self.label_status_msg.setText("")
        self.label_status_msg.setStyleSheet('color: light gray')
        self.textedit_chat.setStyleSheet('color: #ffff00')
        self.stackedWidget.setCurrentIndex(0)


    def login(self):
        print 'WarChat.login()'

        # Gather and assign all the user input:
        self.username = self.input_username.text()
        self.password = self.input_password.text()
        self.server = self.input_server.text()
        self.channel = self.input_channel.text()
        self.client_tag = self.input_client_tag.text()
        # Validate user input/check for missing params
        if not self.username or not self.password:
            self.label_status_msg.setText("Username/Password missing")
            self.label_status_msg.setStyleSheet('color: red')
            return

        # Create chat_thread object
        self.get_thread = chat_thread(self.username, self.password, self.server, self.channel, self.client_tag)

        # Setup signals to listen for and connect them to functions
        self.connect(self.get_thread, SIGNAL("catch_status_msg(QString, QString)"), self.catch_status_msg)
        self.connect(self.get_thread, SIGNAL("catch_textedit_chat(QString, QString)"), self.catch_textedit_chat)
        self.connect(self.get_thread, SIGNAL("catch_login_success()"), self.catch_login_success)

        # Start chat_thread
        self.get_thread.start()

        self.label_status_msg.setText("Connecting...")
        self.label_status_msg.setStyleSheet('color: light gray')

    def catch_login_success(self):
        self.stackedWidget.setCurrentIndex(1)

    def catch_status_msg(self, msg, color):

        print 'WarChat.catch_status_msg()'

        self.label_status_msg.setText(msg)
        self.label_status_msg.setStyleSheet('color: ' + color)

    def catch_textedit_chat_2(self, msg, color):
        self.textedit_chat.append(msg)

    def catch_textedit_chat(self, msg, color):

        print 'WarChat.catch_textedit_chat()'

        # This is where all the chatroom data styling and filtering takes place
        msg = str(msg)
        msg = msg.splitlines()
        for line in msg:
            if re.findall('^Joining channel: "(.+)"$', line):
                self.textedit_users.setText('')
                self.textedit_users.setHtml(ui._translate("MainWindow",
                                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:\'Droid Sans\'; font-size:12pt; font-weight:400; font-style:normal;\" bgcolor=\"#d3d3d3\">\n"
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                          None))
                self.users_in_chan[:] = []
                self.channel_name = re.findall('^Joining channel: "(.+)"$', line)[0]
                self.update_textedit_users()
                print re.findall('^Joining channel: (.+)$', line)
                line = '<span style="color: #00ef00;">' + line + '</span>'
                self.textedit_chat.append(line)

            elif re.findall('^\[(.+)\]$', line):
                user_status_msg = re.findall('^\[(.+)\]$', line)


                if 'is here' in user_status_msg[0]:
                    user = re.findall('^\[(.+) is here\]$', line)
                    self.users_in_chan.append(user[0])
                    self.update_textedit_users()

                elif 'enters' in user_status_msg[0]:
                    user = re.findall('^\[(.+) enters\]$', line)
                    self.users_in_chan.append(user[0])
                    self.update_textedit_users()

                elif 'quit' in user_status_msg[0]:
                    user = re.findall('^\[(.+) quit\]$', line)
                    self.users_in_chan.remove(user[0])
                    self.update_textedit_users()

                elif 'leaves' in user_status_msg[0]:
                    user = re.findall('^\[(.+) leaves\]$', line)
                    self.users_in_chan.remove(user[0])
                    self.update_textedit_users()

                elif 'kicked' in user_status_msg[0]:
                    user = re.findall('^\[(.+) has been kicked\]$', line)
                    self.users_in_chan.remove(user[0])
                    self.update_textedit_users()

                elif 'banned' in user_status_msg[0]:
                    user = re.findall('^\[(.+) has been banned\]$', line)
                    self.users_in_chan.remove(user[0])
                    self.update_textedit_users()

            elif re.findall('^ERROR: ', line):
                line = line.replace("ERROR: ", "", 1)
                line = '<span style="color: #ff0000;">' + line + '</span>'
                self.textedit_chat.append(line)

            elif re.findall('^<from (.+?)>', line):
                username = re.findall('^<from (.+?)> ', line)[0]
                line = line.replace("from ", "From:", 1)
                line = '<span style="color: #ffff00;">&lt;From: ' + username + '&gt;</span><span style="color: gray;" > ' + line + '</span>'
                self.textedit_chat.append(line)

            elif re.findall('^<to (.+?)>', line):
                username = re.findall('^<to (.+?)> ', line)[0]
                line = line.replace("to ", "To:", 1)
                line = '<span style="color: #00ffff;">&lt;To: ' + username + '&gt;</span><span style="color: gray;" > ' + line + '</span>'
                self.textedit_chat.append(line)

            elif re.findall('^<(.+?)> ', line):
                username = re.findall('^<(.+?)> ', line)[0]
                line = '<span style="color: #ffff00;">&lt;' + username + '&gt;</span><span style="color: white;" > ' + line + '</span>'
                self.textedit_chat.append(line)

            else:
                self.textedit_chat.setStyleSheet('color: #ffff00')
                self.textedit_chat.append(line)

    def update_textedit_users(self):
        self.textedit_users.setText('')
        self.textedit_users.setHtml(ui._translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Droid Sans\'; font-size:12pt; font-weight:400; font-style:normal;\" bgcolor=\"#d3d3d3\">\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                               None))
        for user in self.users_in_chan:
            self.textedit_users.append(user)
        self.channel_user_count = len(self.users_in_chan)
        self.label_channel.setText(self.channel_name + ' (' + str(self.channel_user_count) + ')')


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = WarChatter()  # Set the form to be WarChatter (ui.py)
    form.show()  # Show the form
    app.exec_()  # Execute the app


if __name__ == '__main__':  # if running this file directly and not importing it
    main()  # run the main function