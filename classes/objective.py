from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel

class Objective(QWidget):
    def __init__(self, title, description):
        super().__init__()
        objectiveInfo = QLabel(f"<h1 style='margin: 0;'>{title}</h1><p style='margin: 0;'>{description}</p>")

        buttonDelete = QPushButton()
        buttonDelete.setText("Delete")
        buttonDelete.setProperty("style", "danger")
        buttonDelete.setFixedSize(130, 30)

        buttonEdit = QPushButton()
        buttonEdit.setText("Edit")
        buttonEdit.setProperty("style", "secondary")
        buttonEdit.setFixedSize(130, 30)

        buttonFinish = QPushButton()
        buttonFinish.setText("Mark as done")
        buttonFinish.setProperty("style", "action")
        buttonFinish.setFixedSize(130, 30)

        buttonSet = QPushButton()
        buttonSet.setText("Set as current")
        buttonSet.setProperty("style", "primary")
        buttonSet.setFixedSize(130, 30)

        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.addWidget(objectiveInfo)
        layout.addWidget(buttonDelete)
        layout.addWidget(buttonEdit)
        layout.addWidget(buttonFinish)
        layout.addWidget(buttonSet)
