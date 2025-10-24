from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton

class Objective(QWidget):
    def __init__(self):
        super().__init__()

        buttonDelete = QPushButton()
        buttonDelete.setText("Delete")
        buttonDelete.setProperty("style", "danger")
        buttonEdit = QPushButton()
        buttonEdit.setText("Edit")
        buttonEdit.setProperty("style", "secondary")
        buttonFinish = QPushButton()
        buttonFinish.setText("Mark as done")
        buttonFinish.setProperty("style", "action")
        buttonSet = QPushButton()
        buttonSet.setText("Set as current")
        buttonSet.setProperty("style", "primary")


        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.addWidget(buttonDelete)
        layout.addWidget(buttonEdit)
        layout.addWidget(buttonFinish)
        layout.addWidget(buttonSet)
