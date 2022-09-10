from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from sys import argv as sys_argv, exit as sys_exit
from screeninfo import get_monitors
from socket import socket

class AmeyChat:
    def __init__(self):
        self.WindowResoltion = (get_monitors()[0].width, get_monitors()[0].height)
        self.AmeyChatApp = QApplication(sys_argv)
        self.AmeyGUIWindow = QMainWindow()
        self.AmeyGUIWindow.setWindowTitle("AmeyChat")
        self.AmeyGUIWindow.setGeometry(int(self.WindowResoltion[0]/4.2666), int(self.WindowResoltion[1]/4.32), int(self.WindowResoltion[0]/2), int(self.WindowResoltion[1]/2))
        
if __name__ == "__main__":
    A = AmeyChat()
    A.AmeyGUIWindow.show()
    print(A.WindowResoltion)
    sys_exit(A.AmeyChatApp.exec_())