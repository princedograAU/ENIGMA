__author__ = 'Prince Dogra'

import sys
from PyQt4 import QtGui
import serial

def main():

    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())


def sel_Serials():

    #serial connection check
   try:
        global serialPort
        serialPort = serial.Serial()
        ports = list(serial.tools.list_ports.comports())
        for i in ports:
            print(i)

   except:
        print("OMG")




if __name__ == '__main__':
    main()