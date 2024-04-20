from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from instr import test_info

app = QApplication([])
main_win = QWidget()
main_win.show()
main_win.setWindowTitle('Тест Руфье')
start_button = QPushButton('Начать')
start_button.text()
text = QLabel('Тест')
text_main = QLabel(test_info)
v_line = QVBoxLayout()
v_line.addWidget(text)
v_line.addWidget(text_main)
v_line.addWidget(start_button, alignment = Qt.AlignCenter)

main_win.setLayout(v_line)
app.exec_()