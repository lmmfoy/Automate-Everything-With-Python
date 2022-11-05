from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path

def open_files():
    # Making filenames global (against best practices)
    global filenames
    # QFileDialog returns 2 variables: list of filenames (absolute paths), and extra information about dialogue action (don't need this currently)
    filenames, _ = QFileDialog.getOpenFileNames(window, "Select files")
    # Show file names
    message.setText("\n".join(filenames))

def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, "wb") as file:
            # Overrriding anything file had inside
            file.write(b"")
        path.unlink()
    message.setText("Files destroyed")

app = QApplication([])
window = QWidget()
window.setWindowTitle("File Destroyer")
layout = QVBoxLayout()

description = QLabel('Select files you want to destroy. The files will be <font color="red">permanently</font> deleted')
layout.addWidget(description)

open_btn = QPushButton("Open Files")
# Pop up label when hover over button (important for icons)
open_btn.setToolTip("Open File")
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

destroy_btn = QPushButton("Destroy Files")
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

message = QLabel("")
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()