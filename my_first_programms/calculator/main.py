from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from random import randint


# Create GUI with python


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('First GUI Program')
        self.setGeometry(300, 200, 350, 200)  # отступы, размер

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('Label text')
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.main_btn = QtWidgets.QPushButton(self)
        self.main_btn.move(50, 50)
        self.main_btn.setText('Push The Button')
        self.main_btn.setFixedWidth(240)
        self.main_btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText('New Text Label')
        self.new_text.move(randint(0,300), randint(0,290))
        self.new_text.adjustSize()
        # print('Button are pressed...')


def main():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
