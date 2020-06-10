# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
import shablon


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = shablon.Ui_MainForm()
        self.ui.setupUi(self)

        self.MAXLEN = 30    # Максимальная длина
        # Обнуляем выражение в label
        self.clear()

        # Привязка к кнопках 0-9
        self.ui.btn1.clicked.connect(lambda _, symbol="1": self.add_symbol(symbol))
        self.ui.btn2.clicked.connect(lambda _, symbol="2": self.add_symbol(symbol))
        self.ui.btn3.clicked.connect(lambda _, symbol="3": self.add_symbol(symbol))
        self.ui.btn4.clicked.connect(lambda _, symbol="4": self.add_symbol(symbol))
        self.ui.btn5.clicked.connect(lambda _, symbol="5": self.add_symbol(symbol))
        self.ui.btn6.clicked.connect(lambda _, symbol="6": self.add_symbol(symbol))
        self.ui.btn7.clicked.connect(lambda _, symbol="7": self.add_symbol(symbol))
        self.ui.btn8.clicked.connect(lambda _, symbol="8": self.add_symbol(symbol))
        self.ui.btn9.clicked.connect(lambda _, symbol="9": self.add_symbol(symbol))
        self.ui.btn0.clicked.connect(lambda _, symbol="0": self.add_symbol(symbol))
        # Привязка к кнопке '.'
        self.ui.btndot.clicked.connect(self.add_symbol_dot)
        # Привязка к кнопкам '+', '-', '*', '/'
        self.ui.btnplus.clicked.connect(lambda _, symbol="+": self.add_symbol(symbol))
        self.ui.btnminus.clicked.connect(lambda _, symbol="-": self.add_symbol(symbol))
        self.ui.btndelit.clicked.connect(lambda _, symbol="/": self.add_symbol(symbol))
        self.ui.btnumnoz.clicked.connect(lambda _, symbol="×": self.add_symbol(symbol))
        # Привязка к кнопкам '(', ')'
        self.ui.btnleft.clicked.connect(lambda _, symbol="(": self.add_symbol(symbol))
        self.ui.btnright.clicked.connect(lambda _, symbol=")": self.add_symbol(symbol))
        # Привязка к кнопке '^'
        self.ui.btnstepen.clicked.connect(lambda _, symbol="^": self.add_symbol(symbol))
        # Привязка к кнопке 'AC'
        self.ui.btnac.clicked.connect(self.clear)
        # Привязка к кнопке '='
        self.ui.btnequally.clicked.connect(self.to_count)


    def clear(self):
        """ Обнуление label """
        self.ui.out_label.setText("0")

    def add_symbol(self, symbol: str):
        """ Добавление символа в label """
        if len(self.ui.out_label.text()) <= self.MAXLEN:
            current_string = self.ui.out_label.text() if self.ui.out_label.text()[0] != "0" else ""
            new_string = current_string + symbol
            self.ui.out_label.setText(new_string)

    def to_count(self):
        """ Используется на вычисления выражения """
        try:
            expression = self.ui.out_label.text().replace("^","**").replace("×","*")
            count = str(eval(expression))
            self.ui.out_label.setText(count)
        except: # Если появилось исключения во время вычисления..
            self.clear()

    def delete_last_symbol(self):
        """ Удаление последнего символа """
        label_string = self.ui.out_label.text()
        if len(label_string) == 1:
            self.clear()
        else:
            self.ui.out_label.setText(label_string[:-1])

    def add_symbol_dot(self):
        """ Добавление точки
        дает возможность поставить только одну точку """
        label_string = self.ui.out_label.text()
        if label_string[-1] != ".":
            self.add_symbol(".")


    def keyPressEvent(self, e):
        """ Обработка нажатия клавиш """
        if e.key() == QtCore.Qt.Key_D:
            self.clear()
        elif e.key() == QtCore.Qt.Key_1:
            self.add_symbol("1")
        elif e.key() == QtCore.Qt.Key_2:
            self.add_symbol("2")
        elif e.key() == QtCore.Qt.Key_3:
            self.add_symbol("3")
        elif e.key() == QtCore.Qt.Key_4:
            self.add_symbol("4")
        elif e.key() == QtCore.Qt.Key_5:
            self.add_symbol("5")
        elif e.key() == QtCore.Qt.Key_6:
            self.add_symbol("6")
        elif e.key() == QtCore.Qt.Key_7:
            self.add_symbol("7")
        elif e.key() == QtCore.Qt.Key_8:
            self.add_symbol("8")
        elif e.key() == QtCore.Qt.Key_9:
            self.add_symbol("9")
        elif e.key() == QtCore.Qt.Key_0:
            self.add_symbol("0")
        elif e.key() == QtCore.Qt.Key_Asterisk:
            self.add_symbol("×")
        elif e.key() == QtCore.Qt.Key_Plus:
            self.add_symbol("+")
        elif e.key() == QtCore.Qt.Key_Minus:
            self.add_symbol("-")
        elif e.key() == QtCore.Qt.Key_Period:
            self.add_symbol_dot()
        elif e.key() == QtCore.Qt.Key_Slash:
            self.add_symbol("/")
        elif e.key() == QtCore.Qt.Key_Backspace:
            self.delete_last_symbol()
        elif e.key() == QtCore.Qt.Key_ParenLeft:
            self.add_symbol("(")
        elif e.key() == QtCore.Qt.Key_ParenRight:
            self.add_symbol(")")
        elif e.key() == QtCore.Qt.Key_AsciiCircum:
            self.add_symbol("^")
        elif e.key() == QtCore.Qt.Key_Return:
            self.to_count()
        elif e.key() == QtCore.Qt.Key_Escape:
            QtWidgets.qApp.quit()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
