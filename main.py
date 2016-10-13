from PyQt4 import QtGui
import sys
import socket
import ui
from PyQt4.QtCore import QThread, SIGNAL

class chat_thread(QThread):
    def __init__(self, username, password, server):

        print 'chat_thread.__init__()'

        QThread.__init__(self)
        self.username = str(username)
        self.password = str(password)
        self.server = str(server)
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

                print 'WARJAMMER DEBUG: chat_thread.pvpgn_login() Output -----'
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
                    self.emit(SIGNAL('catch_status_msg(QString, QString)'), 'Login success', 'green')
                    self.emit(SIGNAL('catch_textedit_chat(QString, QString)'), data, 'light gray')
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
        total_data = [];
        data = ''
        while True:
            try:

                data = self.s.recv(8192)
                if data:
                    self.emit(SIGNAL('catch_textedit_chat(QString, QString)'), data, 'light gray')
                    print '-----------'
                    print data
                    print '------------'
            except:
                continue

    def run(self):
            print 'chat_thread.run()'
            self.pvpgn_login()
            if self.connection_status == 1:
                self.loop_chat_recv()

class WarChat(QtGui.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        print 'WarChat.__init__()'
        # super allows us to access variables, methods etc in the ui.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in ui.py file automatically
        # It sets up layout and widgets that are defined
        self.button_login.clicked.connect(self.login)
        self.button_send.clicked.connect(self.send_msg)
        self.textedit_chat.setReadOnly(True)
        self.textedit_users.setReadOnly(True)

    def send_msg(self):
        self.msg = str(self.input_msg.text())
        self.get_thread.s.send(self.msg)
        self.get_thread.s.send("\r\n")
        self.catch_textedit_chat(self.msg, 'light gray')


    def login(self):
        print 'WarChat.login()'
        # TODO: Hide the login buttons / flip to next page
        # Gather and assign all the user input:
        self.username = self.input_username.text()
        self.password = self.input_password.text()
        self.server = self.input_server.text()

        # Validate user input/check for missing params
        if not self.username or not self.password:
            self.label_status_msg.setText("Username/Password missing")
            self.label_status_msg.setStyleSheet('color: red')
            return

        # Create chat_thread object
        self.get_thread = chat_thread(self.username, self.password, self.server)

        # Setup signals to listen for and connect them to functions
        self.connect(self.get_thread, SIGNAL("catch_status_msg(QString, QString)"), self.catch_status_msg)
        self.connect(self.get_thread, SIGNAL("catch_textedit_chat(QString, QString)"), self.catch_textedit_chat)
        self.connect(self.get_thread, SIGNAL("catch_textedit_users(QString, QString)"), self.catch_textedit_users)

        # Start chat_thread
        self.get_thread.start()

        self.label_status_msg.setText("Connecting...")
        self.label_status_msg.setStyleSheet('color: light gray')

    def catch_status_msg(self, msg, color):

        print 'WarChat.catch_status_msg()'

        self.label_status_msg.setText(msg)
        self.label_status_msg.setStyleSheet('color: ' + color)

    def catch_textedit_chat(self, msg, color):

        print 'WarChat.catch_textedit_chat()'

        self.textedit_chat.append(msg)
        self.textedit_chat.setStyleSheet('color: ' + color)


    def catch_textedit_users(self, msg, color):
        print 'WarChat.catch_textedit_users()'

        self.textedit_users.append(msg)
        self.textedit_users.setStyleSheet('color: ' + color)


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = WarChat()  # Set the form to be WarChat (ui.py)
    form.show()  # Show the form
    app.exec_()  # Execute the app


if __name__ == '__main__':  # if running this file directly and not importing it
    main()  # run the main function