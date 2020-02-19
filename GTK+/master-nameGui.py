###################################################################
# Python
# Project Name: HUMAN NUMBER NAME
# ver  1.0
# Developer: ROB GIULIANO  -a.k.a- PG
# Etherium:       0x14996EE0113C46A34b14e4F30197768b174c9486
# Bitcoin:        1HN7eNRiJFWR1JXQdMx2hwVCaANmbhnUrb
# Bitcoin Cash:   qz7h44sqpn8ud2hv04tw2kgr9ayqu94gngm2tedvrt
# Tipeeestream:   https://www.tipeeestream.com/rob-giuliano/donation
#####################################################################


from PyQt5 import QtCore, QtGui, QtWidgets, uic
from pyc import HumanName
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import img_rc
import os
import sys



Ui_MainWindow, QtBaseClass = uic.loadUiType("human_number_name.ui")

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Human_Name_Gui)

    def Human_Name_Gui(self):
        name = str(self.ui.insert_name_box.toPlainText())
        n = HumanName(name)
        chld = n.chalde()
        div = n.divin()
        r = n.pytha()
        jews = n.jewish()
        greek = n.greek()
        varPytha = str(r['sum'])
        self.ui.lineEdit_2.setText(varPytha)
        varChade = str(chld['sum'])
        self.ui.lineEdit_3.setText(varChade)
        varDivin = str(div['sum'])
        self.ui.lineEdit_4.setText(varDivin)
        varJews = str(jews['sum'])
        self.ui.lineEdit_5.setText(varJews)
        varGreek = str(greek['sum'])
        self.ui.lineEdit_6.setText(varGreek)
        self.ui.link_label.setText("<a href= 'https://www.tipeeestream.com/rob-giuliano/donation'><font size='2', fontface = 'Helvetica', 'sans-serif', 'Arial'>Project:-Donate </font></a>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
