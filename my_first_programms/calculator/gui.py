from PyQt5 import QtCore, QtGui, QtWidgets
import math

# Create GUI with Qt Designer

bg_r = 'border-radius: 10;'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 230, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet(f"{bg_r}\nbackground-color: rgb(170, 255, 255);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label.setMargin(10)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(70, 310, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(170, 255, 0);")
        self.btn_0.setObjectName("btn_0")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(10, 250, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(170, 255, 0);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(70, 250, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(170, 255, 0);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(130, 250, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(170, 255, 0);")
        self.btn_3.setObjectName("btn_3")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(70, 190, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(170, 255, 0);")
        self.btn_5.setObjectName("btn_5")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(10, 190, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(170, 255, 0);")
        self.btn_4.setObjectName("btn_4")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(130, 190, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(170, 255, 0);")
        self.btn_6.setObjectName("btn_6")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(70, 130, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(170, 255, 0);")
        self.btn_8.setObjectName("btn_8")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(10, 130, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(170, 255, 0);")
        self.btn_7.setObjectName("btn_7")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(130, 130, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet(f"{bg_r};\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(170, 255, 0);")
        self.btn_9.setObjectName("btn_9")
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(130, 310, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dot.setFont(font)
        self.btn_dot.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(170, 170, 255);")
        self.btn_dot.setObjectName("btn_dot")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(10, 310, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_sign.setFont(font)
        self.btn_sign.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(255, 170, 255);")
        self.btn_sign.setObjectName("btn_sign")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(190, 310, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet(f"{bg_r}\ncolor: rgb(255, 255, 255);\nbackground-color: rgb(0, 85, 0);")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(190, 250, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(134, 134, 134);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(190, 190, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(134, 134, 134);")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_mult = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mult.setGeometry(QtCore.QRect(190, 130, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mult.setFont(font)
        self.btn_mult.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(134, 134, 134);")
        self.btn_mult.setObjectName("btn_mult")
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div.setGeometry(QtCore.QRect(190, 70, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_div.setFont(font)
        self.btn_div.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(134, 134, 134);")
        self.btn_div.setObjectName("btn_div")
        self.btn_sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sqrt.setGeometry(QtCore.QRect(130, 70, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_sqrt.setFont(font)
        self.btn_sqrt.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(0, 170, 255);")
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.btn_square = QtWidgets.QPushButton(self.centralwidget)
        self.btn_square.setGeometry(QtCore.QRect(70, 70, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_square.setFont(font)
        self.btn_square.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(0, 170, 255);")
        self.btn_square.setObjectName("btn_square")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(10, 70, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet(f"{bg_r}\nborder-color: rgb(0, 0, 0);\nbackground-color: rgb(255, 0, 0);")
        self.btn_clear.setObjectName("btn_clear")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_func()

    def add_func(self):
        self.btn_0.clicked.connect(lambda: self.write_num(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_num(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_num(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_num(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_num(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_num(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_num(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_num(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_num(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_num(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_num('+'))
        self.btn_minus.clicked.connect(lambda: self.write_num('-'))
        self.btn_mult.clicked.connect(lambda: self.write_num('*'))
        self.btn_div.clicked.connect(lambda: self.write_num('/'))
        self.btn_equal.clicked.connect(self.result)
        self.btn_clear.clicked.connect(self.clear_input)
        self.btn_square.clicked.connect(self.power_two)
        self.btn_sqrt.clicked.connect(self.sqrt_x)
        self.btn_dot.clicked.connect(lambda: self.write_num(self.btn_dot.text()))
        self.btn_sign.clicked.connect(self.ch_sign)

    def ch_sign(self):
        if self.label.text().startswith('-'):
            self.label.setText(self.label.text()[1:])
        else:
            self.label.setText(f'-{self.label.text()}')

    def write_num(self, number):
        self.label.setText(self.label.text() + number)

    def result(self):
        res = eval(self.label.text())
        self.label.setText(str(res)[:11])

    def clear_input(self):
        self.label.setText('')

    def power_two(self):
        res = math.pow(float(self.label.text()), 2)
        self.label.setText(str(res)[:11])

    def sqrt_x(self):
        try:
            res = math.sqrt(float(self.label.text()))
            self.label.setText(str(res)[:11])
        except:
            self.label.setText('')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "First Program"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_sign.setText(_translate("MainWindow", "±"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_mult.setText(_translate("MainWindow", "×"))
        self.btn_div.setText(_translate("MainWindow", "÷"))
        self.btn_sqrt.setText(_translate("MainWindow", "√x"))
        self.btn_square.setText(_translate("MainWindow", "x²"))
        self.btn_clear.setText(_translate("MainWindow", "C"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())