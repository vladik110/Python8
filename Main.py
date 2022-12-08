#!/usr/bin/env python3
# coding=utf-8

import math
import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Сложные табличные вычисления в Python')

        self.setWindowIcon(QtGui.QIcon('images/icon.png'))
        self.label_img.setPixmap(QPixmap('images/tasks.png'))
        self.label_img.setScaledContents(True)

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.exit)

    def fill_random_numbers(self):
        """
        заполняем таблицу случайными числами
        :return: pass
        """
        i = 0

        while i < self.tableWidget.rowCount():
            random_num = randint(-100, 100)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(random_num)))
            i += 1

    def solve(self):

        if validation_of_data(self.tableWidget):
            i = 0
            j = 1

            sum_of_k_i = 0
            pro_of_k_i = 1
            sum_chet_of_k_i = 0

            while i < self.tableWidget.rowCount():

                try:
                    item = self.tableWidget.item(i, 0).text()
                    if (i + 1) % 2 == 0:
                        sum_chet_of_k_i += int(item)
                    else:
                        pro_of_k_i *= int(item)
                    sum_of_k_i += int(item) ** 2
                    if int(item) >= 0:
                        answer = pro_of_k_i - sum_chet_of_k_i
                    else:
                        answer = sum_of_k_i ** (1 / 3)

                    self.tableWidget.setItem(i, j,
                                             QTableWidgetItem(str(format(answer, ".3f"))))
                except Exception:
                    self.tableWidget.setItem(i, j, QTableWidgetItem('none'))

                i += 1

            self.label_error.setText('')
        else:
            self.label_error.setText('Введены некорректные данные!')

    def clear(self):
        self.tableWidget.clearContents()

    def exit(self):
        self.close()


def validation_of_data(table_widget):
    """
    проверяем данные на валидность
    :param table_widget: таблица с числами
    :return: True - данные корректны, False - есть некорректные данные
    """
    i = 0
    while i < table_widget.rowCount():
        try:
            float(table_widget.item(i, 0).text())
            i += 1
        except Exception:
            return False

    return True


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
