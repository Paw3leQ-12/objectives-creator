from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication([])

with open("style.qss", "r") as styleSheet:
    app.setStyleSheet(styleSheet.read())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Objectives creator")
        self.setMinimumHeight(400)
        self.setMinimumWidth(600)

window = MainWindow()
window.show()
app.exec()