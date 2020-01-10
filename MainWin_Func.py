import os
import sys
import time
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox

from Detail import *
from MainWin import *




class father_window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):                           
        super(father_window, self).__init__()
        self.setupUi(self)
        self.more_window = More_Window()

    def execute(self):
        ip = self.lineEdit.text()
        community = self.lineEdit_2.text()
        oid = self.lineEdit_3.text()
        action = self.comboBox.currentText()
        command = "snmputil " + action + ' ' + ip + ' ' + community + ' ' + oid
        result = os.popen(command)
        res = result.read()
        self.textBrowser.setText(res)

    def more(self):
        self.more_window.show()

    def quit(self):
        self.close()

    ##def show1(self):

class More_Window(QtWidgets.QMainWindow, Ui_Detail):
    def __init__(self):                           
        super(More_Window, self).__init__()
        self.setupUi(self) 

    def begin1(self):
        usr_limit = self.lineEdit.text()
        system_limit = self.lineEdit_2.text()
        goon = 1
        i = 0
        while goon:
            result3 = os.popen("snmputil get 192.168.11.133 public .1.3.6.1.4.1.2021.11.11.0")
            result4 = os.popen("snmputil get 192.168.11.133 public .1.3.6.1.4.1.2021.11.9.0")
            result5 = os.popen("snmputil get 192.168.11.133 public .1.3.6.1.4.1.2021.11.10.0")
            result6 = os.popen("snmputil walk 192.168.11.133 public .1.3.6.1.2.1.25.3.3.1.2")
            res3 = result3.read()
            res4 = result4.read()
            res5 = result5.read()
            res6 = result5.read()
            if (int(res4.split(' ')[-1]) > int(usr_limit)):
                reply1 = QMessageBox.warning(self, "警告!", "用户占用CPU已经超过限制！")
            if (int(res5.split(' ')[-1]) > int(system_limit)):
                reply2 = QMessageBox.warning(self, "警告!", "系统占用CPU已经超过限制！")
            self.lineEdit_3.setText(res3.split(' ')[-1])
            self.lineEdit_4.setText(res4.split(' ')[-1])
            self.lineEdit_5.setText(res5.split(' ')[-1])
            if (len(res6) == 0):
                self.lineEdit_6.setText('0')
            QApplication.processEvents()
            time.sleep(3) 
            i = i + 1
            if i==3:
                goon = 0   
    
    def begin2(self):
        used_limit = self.lineEdit_7.text()
        goon = 1
        i = 0
        while goon:
            result8 = os.popen("snmputil get 192.168.11.133 public .1.3.6.1.2.1.25.2.2.0")
            result9 = os.popen("snmputil walk 192.168.11.133 public .1.3.6.1.2.1.25.2.3.1.6")
            res8 = result8.read()
            res9 = result9.read()
            #if (int(res9.split(' ')[-1])/int(res8.split(' ')[-1]) > int(used_limit)):
            reply3 = QMessageBox.warning(self, "警告!", "内存使用已经超过限制！")
            self.lineEdit_8.setText(res8.split(' ')[-1])
            self.lineEdit_9.setText(res9.split('\n')[1].split(' ')[-1])
            QApplication.processEvents()
            time.sleep(3) 
            i = i + 1
            if i==10:
                goon = 0 
    
    def begin3(self):
        used_limit = self.lineEdit_10.text()
        goon = 1
        i = 0
        while goon:
            result11 = os.popen("snmputil get 192.168.11.133 public .1.3.6.1.2.1.25.2.2.0")
            result12 = os.popen("snmputil walk 192.168.11.133 public .1.3.6.1.2.1.25.2.3.1.6")
            res11 = result11.read()
            res12 = result12.read()
            self.lineEdit_11.setText(res11.split(' ')[-1])
            self.lineEdit_12.setText(res12.split(' ')[-1])
            QApplication.processEvents()
            time.sleep(3) 
            i = i + 1
            if i==3:
                goon = 0 
    
    def begin4(self):
        recieved_limit = self.lineEdit_13.text()
        sent_limit = self.lineEdit_14.text()
        goon = 1
        i = 0
        while goon:
            result15 = os.popen("snmputil walk 192.168.11.133 public .1.3.6.1.2.1.25.2.2.1.10")
            result16 = os.popen("snmputil walk 192.168.11.133 public .1.3.6.1.2.1.25.2.2.1.11")
            result17 = os.popen("snmputil walk 192.168.11.133 public .1.3.6.1.2.1.25.2.2.1.6")
            result18 = os.popen("snmputil walk 192.168.11.133 public .1.3.6.1.2.1.25.2.2.1.16")
            result19 = os.popen("snmputil walk 192.168.11.133 public .1.3.6.1.2.1.25.2.2.1.17")
            result20 = os.popen("snmputil walk 192.168.11.133 public .1.3.6.1.2.1.25.2.2.1.6")
            res15 = result15.read()
            res16 = result16.read()
            res17 = result17.read()
            res18 = result18.read()
            res19 = result19.read()
            res20 = result20.read()
            self.lineEdit_15.setText(res15.split(' ')[-1])
            self.lineEdit_16.setText(res16.split(' ')[-1])
            self.lineEdit_17.setText(res17.split(' ')[-1])
            self.lineEdit_18.setText(res18.split(' ')[-1])
            self.lineEdit_19.setText(res19.split(' ')[-1])
            self.lineEdit_20.setText(res20.split(' ')[-1])
            QApplication.processEvents()
            time.sleep(3) 
            i = i + 1
            if i==10:
                goon = 0 
      
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = father_window()
    ex.show()
    
    sys.exit(app.exec_())
