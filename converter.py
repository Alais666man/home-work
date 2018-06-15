import sys
from urllib.request import urlopen
from lxml import etree

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, \
    QDoubleSpinBox, QPushButton, QVBoxLayout, QAction


class Course(QObject):
    CB_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

    def get(self):
        with urlopen(self.CB_URL) as r:
            tree = etree.parse(r)
            value = tree.xpath('*[@ID="R01235"]/Value')[0].text
            return float(value.replace(',', '.'))


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initUi()
        self._initSignals()
        self._initLayout()

    def _initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.rubLabel = QLabel('Сумма в рублях', self)
        self.usdLabel = QLabel('Сумма в долларах', self)

        self.rubAmountEdit = QDoubleSpinBox(self)
        self.rubAmountEdit.setMaximum(999999999)
        self.usdAmountEdit = QDoubleSpinBox(self)
        self.usdAmountEdit.setMaximum(999999999)

        self.convertBtn = QPushButton('Перевести', self)
        # self.convertBtn.setAutoDefault(True)
        self.eraseBtn = QPushButton('Отчистить', self)

    def initAction(self):
        initAction = QAction(self)
        initAction.setShortcut('Return')
        initAction.triggered.connect(self.convertBtn)
    #
    # def convertButton(self):
    #     return self.convertBtn

    def _initSignals(self):
        self.convertBtn.clicked.connect(self.onClickConvertBtn)
        self.eraseBtn.clicked.connect(self.onClickEraseBtn)


    def _initLayout(self):
        w = QWidget(self)

        self.mainLayout = QVBoxLayout(w)

        self.mainLayout.addWidget(self.rubLabel)
        self.mainLayout.addWidget(self.rubAmountEdit)
        self.mainLayout.addWidget(self.usdLabel)
        self.mainLayout.addWidget(self.usdAmountEdit)
        self.mainLayout.addWidget(self.convertBtn)
        # self.convertBtn.setDisabled(True)
        self.mainLayout.addWidget(self.eraseBtn)

        self.setCentralWidget(w)

    def onClickConvertBtn(self):
        rub = self.rubAmountEdit.value()
        usd = self.usdAmountEdit.value()
        if rub:
            self.usdAmountEdit.setValue(rub / Course().get())

        elif usd:
            self.rubAmountEdit.setValue(usd * Course().get())

    # def returnPressed(self, event):
    #     if event.key() == QtCore.Qt.Key_Return:
    #         self.onClickConvertBtn(event.key)

    def onClickEraseBtn(self):
        rub = self.rubAmountEdit.value()
        usd = self.usdAmountEdit.value()

        if rub or usd:
            self.rubAmountEdit.setValue(0)

            self.usdAmountEdit.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)


    converter = MainWindow()
    converter.show()

    sys.exit(app.exec_())
