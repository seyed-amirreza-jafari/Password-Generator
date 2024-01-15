from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QRadioButton, QCheckBox, QSpinBox, QSlider
from PyQt5 import uic
import sys
import random

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi('password_generator.ui', self)

        self.setWindowTitle('Password Generator')

        self.length_spin = self.findChild(QSpinBox, 'length_spin')
        self.length_slider = self.findChild(QSlider, 'length_slider')
        self.allChars_radioButton = self.findChild(QRadioButton, 'allChars_radioButton')
        self.easy_radioButton = self.findChild(QRadioButton, 'easy_radioButton')
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

        self.length_slider.valueChanged.connect(self.slider_valueChanged)
        self.length_spin.valueChanged.connect(self.spin_valueChanged)

        self.allChars_radioButton.setChecked(True)
        self.allChars_toggled()

        self.allChars_radioButton.toggled.connect(self.allChars_toggled)
        self.easy_radioButton.toggled.connect(self.easy_toggled)

        self.password_generator_button.clicked.connect(self.generate_password)

        self.copy_button.clicked.connect(self.copy)

        self.show()

    def generate_password(self):
        self.password = ''

        lowercases = 'abcdefghijklmnopqrstuvwxyz'
        uppercases = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '{}[]()!?/\_'

        vowels = ''
        vowels_lowercase = 'aeiouy'
        vowels_uppercase = 'AEIOUY'
        constansts = ''
        constansts_lowercase = 'bcdfghjklmnpqrstvwxz'
        constansts_uppercase = 'BCDFGHJKLMNPQRSTVWXZ'

        chars = ''

        if self.allChars_radioButton.isChecked():
            if self.lowercases_checkBox.isChecked():
                chars += lowercases
            if self.uppercases_checkBox.isChecked():
                chars += uppercases
            if self.numbers_checkBox.isChecked():
                chars += numbers
            if self.symbols_checkBox.isChecked():
                chars += symbols
            
        elif self.easy_radioButton.isChecked():
            if self.lowercases_checkBox.isChecked():
                vowels += vowels_lowercase
                constansts += constansts_lowercase
            if self.uppercases_checkBox.isChecked():
                vowels += vowels_uppercase
                constansts += constansts_uppercase

        if self.allChars_radioButton.isChecked():
            for i in range(self.length_spin.value()):
                self.password += random.choice(chars)

        elif self.easy_radioButton.isChecked():
            for j in range(self.length_spin.value()):
                if j % 2 == 1:
                    self.password += random.choice(vowels)
                else:
                    self.password += random.choice(constansts)

        self.password_label.setText(self.password)

    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.clear(mode = clipboard.Clipboard)
        clipboard.setText(self.password_label.text(), mode = clipboard.Clipboard)

    def allChars_toggled(self):
        if self.allChars_radioButton.isChecked():
            self.lowercases_checkBox.setChecked(True)
            self.uppercases_checkBox.setChecked(True)
            self.numbers_checkBox.setCheckable(True)
            self.symbols_checkBox.setCheckable(True)
            self.numbers_checkBox.setChecked(True)
            self.symbols_checkBox.setChecked(True)

            self.length_slider.setMinimum(10)
            self.length_slider.setMaximum(50)
            self.length_slider.setValue(16)

            self.length_spin.setMinimum(10)
            self.length_spin.setMaximum(50)
            self.length_spin.setValue(16)

    def easy_toggled(self):
        if self.easy_radioButton.isChecked():
            self.lowercases_checkBox.setChecked(True)
            self.uppercases_checkBox.setChecked(True)
            self.numbers_checkBox.setChecked(False)
            self.symbols_checkBox.setChecked(False)
            self.numbers_checkBox.setCheckable(False)
            self.symbols_checkBox.setCheckable(False)

            self.length_slider.setMinimum(5)
            self.length_slider.setMaximum(15)
            self.length_slider.setValue(10)

            self.length_spin.setMinimum(5)
            self.length_spin.setMaximum(15)
            self.length_spin.setValue(10)

    def slider_valueChanged(self):
        self.length_spin.setValue(self.length_slider.value())
    
    def spin_valueChanged(self):
        self.length_slider.setValue(self.length_spin.value())

app = QApplication(sys.argv)
Window = UI()
app.exec_()
