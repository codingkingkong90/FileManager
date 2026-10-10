import sys
import os

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel
)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("File Manager")
window.resize(1100, 750)

layout = QVBoxLayout(window)
layout.addWidget(QLabel("PySide6 is working"))

window.show()

sys.exit(app.exec())