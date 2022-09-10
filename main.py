from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout
from sys import argv as sys_argv, exit as sys_exit
from screeninfo import get_monitors
from socket import socket

class AmeyChat:
    def __init__(self):
        self.WindowResoltion = (int(get_monitors()[0].width/2), int(get_monitors()[0].height/2))
        self.AmeyChatApp = QApplication(sys_argv)
        self.AmeyGUIWindow = QMainWindow()
        self.AmeyGUIWindow.setWindowTitle("AmeyChat")
        self.AmeyGUIWindow.setGeometry(int(get_monitors()[0].width/4.2666), int(get_monitors()[0].height/4.32), self.WindowResoltion[0], self.WindowResoltion[1])
        
    def mainChatInterface(self):
        mainWidget = QVBoxLayout()
        self.ChatTextBox = QLineEdit(self.AmeyGUIWindow)
        self.ChatTextBox.move(100, 100)
        self.ChatTextBox.resize(100, 100)
        mainWidget.addWidget(self.ChatTextBox)
        self.AmeyGUIWindow.setLayout(mainWidget)
if __name__ == "__main__":
    A = AmeyChat()
    A.AmeyGUIWindow.show()
    sys_exit(A.AmeyChatApp.exec_())