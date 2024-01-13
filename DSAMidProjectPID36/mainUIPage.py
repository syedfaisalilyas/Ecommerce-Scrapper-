import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QProcess

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(903, 582)
        loadUi("mainUIPage.ui", self)

        # Connect all buttons to the same function
        self.SingleColSort.clicked.connect(self.run_script)
        self.MultiColSort.clicked.connect(self.run_script)
        self.SingleColSearch.clicked.connect(self.run_script)
        self.MultiColSearch.clicked.connect(self.run_script)

    def run_script(self):
        sender_button = self.sender()
        try:
            if sender_button == self.SingleColSort:
                script_name = "trial.py"
            elif sender_button == self.MultiColSort:
                script_name = "multiLevel.py"
            elif sender_button == self.SingleColSearch:
                script_name = "singleLevelSearching.py"
            elif sender_button == self.MultiColSearch:
                script_name = "multiLevelSearching.py"
            else:
                return

            # Run the specified Python script using QProcess
            process = QProcess()
            process.start("python", [script_name])
            process.waitForFinished()
        except Exception as e:
            # Handle any exceptions that might occur while running the script
            print("Error:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
