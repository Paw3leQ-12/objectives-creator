from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from classes.objective import Objective
import json
app = QApplication([])

with open("data/style.qss", "r") as styleSheet:
    app.setStyleSheet(styleSheet.read())

with open("data/objectives.json", "r") as objectives:
    objectives = json.load(objectives)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Objectives creator")
        self.setMinimumHeight(800)
        self.setMinimumWidth(1000)
        layout = QVBoxLayout()
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        for objective in objectives.values():
            layout.addWidget(Objective(objective["title"], objective["description"]))

window = MainWindow()
window.show()
app.exec()