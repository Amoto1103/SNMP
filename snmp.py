import os
import time
from multiprocessing import Process
from MainWin_Func import *



def command(com):
    result = os.popen(com)
    res = result.read()
    ##print(res)
    return res.split(' ')[-1]


def getinfo(comm,aa):
    goon = 1
    i = 0
    while goon:
        out = command(comm)
        print(out)
        aa.lineEdit_4.setText(out)
        time.sleep(3) 
        i = i + 1
        if i==10:
            goon = 0   
'''
def getinfo(comm):
    goon = 1
    i = 0
    while goon:
        out = command("snmputil get 192.168.11.133 public .1.3.6.1.2.1.25.2.2.0")
        print(out)
        time.sleep(3) 
        i = i + 1
        if i==10:
            goon = 0   

    

def getCPU():
    goon = 1
    i = 0
    while goon:
        out = command("snmputil get 192.168.11.133 public .1.3.6.1.4.1.2021.11.9.0")
        print(out)
        time.sleep(3) 
        i = i + 1
        if i==10:
            goon = 0   


if __name__ == '__main__':
    p1 = Process(target=getmemory)
    p2 = Process(target=getCPU)

    p1.start()
    p2.start()

    time.sleep(15)
    p1.terminate()
'''
