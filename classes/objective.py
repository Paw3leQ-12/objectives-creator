from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton

class Objective(QWidget):
    def __init__(self):
        super().__init__()

        buttonDelete = QPushButton()
        buttonDelete.setText("Delete")
        buttonEdit = QPushButton()
        buttonEdit.setText("Edit")
        buttonFinish = QPushButton()
        buttonFinish.setText("Mark as done")
        buttonSet = QPushButton()
        buttonSet.setText("Set as current")

        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.addWidget(buttonDelete)
        layout.addWidget(buttonEdit)
        layout.addWidget(buttonFinish)
        layout.addWidget(buttonSet)
