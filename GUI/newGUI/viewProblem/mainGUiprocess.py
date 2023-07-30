from PyQt5 import QtWidgets
from newGUI.UI.MainWindow import Ui_MainWindow


class MainUi(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.main_windows()

    def main_windows(self):
        self.setupUi(self.MainWindow)
        self.show()
        self.label_19.setText("hahahaha")








