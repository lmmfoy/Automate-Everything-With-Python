from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from bs4 import BeautifulSoup
import requests

# Function to use x-rates.com to convert currencies
def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[0:-4])
    
    return rate

# Functions here modify widgets - they do not return anything
# Set label as input text
def show_currency():
    input_text = float(text.text())
    # To ge the current selections from the dropdowns
    in_cur = in_combo.currentText()
    target_cur = target_combo.currentText()
    rate = get_currency(in_cur, target_cur)
    output = round(input_text * rate, 2)
    message = f"{input_text} {in_cur} is {output} {target_cur}"
    output_label.setText(str(message))

app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency Converter")

# Vertical layout - can use QHBoxLayout for horizontal
layout = QVBoxLayout()

# Dropdowns for currencies
currencies = ["USD", "EUR", "INR"]
in_combo = QComboBox()
in_combo.addItems(currencies)
layout.addWidget(in_combo)

target_combo = QComboBox()
target_combo.addItems(currencies)
layout.addWidget(target_combo)

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton("Convert")
layout.addWidget(btn)
# {widget}.{signal}({slot}) - don't call slot method, just add
btn.clicked.connect(show_currency)

output_label = QLabel("")
layout.addWidget(output_label)

# Must set this in order to see widgets in layout
window.setLayout(layout)

# Must do this or won't show anything
window.show()
# Start app
app.exec()