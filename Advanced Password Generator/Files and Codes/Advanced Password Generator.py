from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QRadioButton, QCheckBox, QSpinBox, QSlider
from PyQt5 import uic
import sys
import random

class AllUI(QMainWindow):
    def __init__(self):
        super(AllUI, self).__init__()

        uic.loadUi('All_Characters_Pass_Generator.ui', self)

        self.setWindowTitle('Password Generator')

        self.easyUi = EasyUI()

        self.openEasy_button = self.findChild(QPushButton, 'open_easy_button')
        self.length_spin = self.findChild(QSpinBox, 'length_spin')
        self.length_slider = self.findChild(QSlider, 'length_slider')
        self.lowercases_checkBox = self.findChild(QCheckBox, 'lowercases_checkBox')
        self.uppercases_checkBox = self.findChild(QCheckBox, 'uppercases_checkBox')
        self.numbers_checkBox = self.findChild(QCheckBox, 'numbers_checkBox')
        self.symbols_checkBox = self.findChild(QCheckBox, 'symbols_checkBox')
        self.password_generator_button = self.findChild(QPushButton, 'password_generator_button')
        self.copy_button = self.findChild(QPushButton, 'copy_button')
        self.password_label = self.findChild(QLabel, 'password_label')

        self.length_slider.setMinimum(5)
        self.length_slider.setMaximum(50)
        self.length_slider.setValue(16)

        self.length_spin.setMinimum(5)
        self.length_spin.setMaximum(50)
        self.length_spin.setValue(16)

        self.openEasy_button.clicked.connect(self.openEasy)

        self.length_slider.valueChanged.connect(self.slider_valueChanged)
        self.length_spin.valueChanged.connect(self.spin_valueChanged)

        self.lowercases_checkBox.setChecked(True)
        self.uppercases_checkBox.setChecked(True)
        self.numbers_checkBox.setChecked(True)
        self.symbols_checkBox.setChecked(True)

        self.password_generator_button.clicked.connect(self.generate_password)

        self.copy_button.clicked.connect(self.copy)

        self.show()

    def openEasy(self):
        self.easyUi.display()

    def generate_password(self):
        self.password = ''

        lowercases = 'abcdefghijklmnopqrstuvwxyz'
        uppercases = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '{}[]()!?/\_'

        chars = ''

        if self.lowercases_checkBox.isChecked():
            chars += lowercases
        if self.uppercases_checkBox.isChecked():
            chars += uppercases
        if self.numbers_checkBox.isChecked():
            chars += numbers
        if self.symbols_checkBox.isChecked():
            chars += symbols
        if self.lowercases_checkBox.isChecked() == False and self.uppercases_checkBox.isChecked() == False:
            if self.numbers_checkBox.isChecked() == False and self.symbols_checkBox.isChecked() == False:
                chars += lowercases + uppercases + numbers + symbols

        for i in range(self.length_spin.value()):
            self.password += random.choice(chars)

        self.password_label.setText(self.password)

    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.clear(mode = clipboard.Clipboard)
        clipboard.setText(self.password_label.text(), mode = clipboard.Clipboard)

    def slider_valueChanged(self):
        self.length_spin.setValue(self.length_slider.value())
    
    def spin_valueChanged(self):
        self.length_slider.setValue(self.length_spin.value())

class EasyUI(QMainWindow):
    def __init__(self):
        super(EasyUI, self).__init__()

        uic.loadUi('Easy_Reading-Saying_Pass_Generator.ui', self)

        self.setWindowTitle('Password Generator')

        self.length_spin = self.findChild(QSpinBox, 'length_spin')
        self.length_slider = self.findChild(QSlider, 'length_slider')
        self.letters_radioButton = self.findChild(QRadioButton, 'letters_radioButton')
        self.lowercases_checkBox = self.findChild(QCheckBox, 'lowercases_checkBox')
        self.uppercases_checkBox = self.findChild(QCheckBox, 'uppercases_checkBox')
        self.numbers_radioButton = self.findChild(QRadioButton, 'numbers_radioButton')
        self.password_generator_button = self.findChild(QPushButton, 'password_generator_button')
        self.copy_button = self.findChild(QPushButton, 'copy_button')
        self.password_label = self.findChild(QLabel, 'password_label')

        self.length_slider.setMinimum(5)
        self.length_slider.setMaximum(15)
        self.length_slider.setValue(10)

        self.length_spin.setMinimum(5)
        self.length_spin.setMaximum(15)
        self.length_spin.setValue(10)

        self.length_slider.valueChanged.connect(self.slider_valueChanged)
        self.length_spin.valueChanged.connect(self.spin_valueChanged)

        self.letters_radioButton.setChecked(True)
        self.letters_checked()

        self.letters_radioButton.toggled.connect(self.letters_checked)

        self.password_generator_button.clicked.connect(self.generate_password)

        self.copy_button.clicked.connect(self.copy)

    def display(self):
        self.show()

    def generate_password(self):
        self.password = ''

        numbers = '0123456789'

        vowels = ''
        vowels_lowercase = 'aeiouy'
        vowels_uppercase = 'AEIOUY'
        constansts = ''
        constansts_lowercase = 'bcdfghjklmnpqrstvwxz'
        constansts_uppercase = 'BCDFGHJKLMNPQRSTVWXZ'

        if self.lowercases_checkBox.isChecked():
            vowels += vowels_lowercase
            constansts += constansts_lowercase
        if self.uppercases_checkBox.isChecked():
            vowels += vowels_uppercase
            constansts += constansts_uppercase

        if self.numbers_radioButton.isChecked():
            for i in range(self.length_spin.value()):
                self.password += random.choice(numbers)

        elif self.letters_radioButton.isChecked():
            for i in range(self.length_spin.value()):
                if i % 2 == 0:
                    self.password += random.choice(constansts)
                else:
                    self.password += random.choice(vowels)

        self.password_label.setText(self.password)

    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.clear(mode = clipboard.Clipboard)
        clipboard.setText(self.password_label.text(), mode = clipboard.Clipboard)

    def letters_checked(self):
        if self.letters_radioButton.isChecked():
            self.lowercases_checkBox.show()
            self.uppercases_checkBox.show()
            self.lowercases_checkBox.setChecked(True)
            self.uppercases_checkBox.setChecked(True)
        elif self.letters_radioButton.isChecked() is False:
            self.lowercases_checkBox.hide()
            self.uppercases_checkBox.hide()

    def slider_valueChanged(self):
        self.length_spin.setValue(self.length_slider.value())

    def spin_valueChanged(self):
        self.length_slider.setValue(self.length_spin.value())

app = QApplication(sys.argv)
Window = AllUI()
app.exec_()
