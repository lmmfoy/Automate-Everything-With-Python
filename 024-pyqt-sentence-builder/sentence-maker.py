from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

# Functions here modify widgets - they do not return anything
# Set label as input text
def make_sentence():
    input_text = text.text()
    output_label.setText(input_text.capitalize() + ".")

app = QApplication([])
window = QWidget()
window.setWindowTitle("TITLE")

# Vertical layout - can use QHBoxLayout for horizontal
layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton("Make")
layout.addWidget(btn)
# {widget}.{signal}({slot})
btn.clicked.connect(make_sentence)

output_label = QLabel("")
layout.addWidget(output_label)

# Must set this in order to see widgets in layout
window.setLayout(layout)

# Must do this or won't show anything
window.show()
# Start app
app.exec()