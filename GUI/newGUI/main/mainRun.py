from PyQt5.QtWidgets import QWidget,QApplication
import sys
from newGUI.viewProblem import mainGUiprocess


if __name__ == '__main__':

    app = QApplication(sys.argv)
    gui = mainGUiprocess.MainUi()
    gui.main_windows()
    sys.exit(app.exec_())


