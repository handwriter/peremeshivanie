from design import Ui_Form as Design
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
import sys


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open)

    def open(self):
        a = QFileDialog.getOpenFileName()[0]
        chet = []
        nechet = []
        with open(a, 'r') as text:
            count = 0
            for i in text.readlines():
                count += 1
                if count % 2 == 0:
                    chet.append(i.rstrip())
                else:
                    nechet.append(i.rstrip())
        self.plainTextEdit.appendPlainText('\n'.join(nechet))
        self.plainTextEdit.appendPlainText('\n'.join(chet))


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())