import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class Udit2(QDialog):
    def __init__(self):
        super(Udit2, self).__init__()
        loadUi('Udit2.ui', self)
        self.setWindowTitle('Login ui')
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.label1.setText('Welcome : '+self.lineEdit.text())
        self.label2_2.setText('Birthday :'+self.lineEdit2.text())
        self.label2.setText('Working : '+self.lineEdit3.text())



app = QApplication(sys.argv)
widget=Udit2()
widget.show()
sys.exit(app.exec())
