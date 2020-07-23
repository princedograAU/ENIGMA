__author__ = 'Prince Dogra, Piyush Sohal'

from random import randint
import sys
import os
import hashlib
import rsa
from rsa.bigfile import *

from PIL import Image
from PyQt4 import QtGui, QtCore

class ImageProcessor:
    '''--------------------------------------------RESIZING IMAGE----------------------------------------------------'''

    def Resizing_Image(self, image):
        x_cod = image.size[0]
        y_cod = image.size[1]
        if x_cod % 8 != 0:
            x_cod -= x_cod % 8
        if y_cod % 8 != 0:
            y_cod -= y_cod % 8

        return image.crop((0, 0, x_cod, y_cod))

'''------------------------------------------------G U I  S E C T I O N----------------------------------------------'''

class Window(QtGui.QMainWindow):

    def ret_Byte(self, stri):
        for i in range(len(stri)):
            temp = '{:08b}'.format(int(ord(stri[i])))
            self.strout += temp

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("ENIGMA-B8")
        self.setFixedSize(700, 560)
        self.move(150, 100)
        self.statusBar().showMessage("ENIGMA-B8")
        self.setStyleSheet('background-color: white;')
        self.statusBar().showMessage("Open image to encrypt or decrypt")
        self.home()

    def home(self):

        # QtGui.QFontDatabase.addApplicationFont("G:\corel images\Fonts\ds_digital\DS-DIGI.TTF")

        tabs = QtGui.QTabWidget(self)
        enctab = QtGui.QWidget()
        dectab = QtGui.QWidget()
        tabs.resize(700, 500)
        tabs.move(0, 0)

        dectab.setStyleSheet('background-color: rgb(222,222,222);')
        enctab.setStyleSheet('background-color: black;')

        # ---------------------------------------Enc Tab Layout elements-------------------------------------------------

        self.encUploadButton = QtGui.QPushButton("Upload Image", self)
        self.encUploadButton.setStyleSheet('background-color: rgb(244,204,0); font-size: 15px;')
        self.encUploadButton.setFixedSize(200, 50)

        global encImgHolder
        encImgHolder = QtGui.QLabel(self)
        encImgHolder.setStyleSheet('background-color: rgb(66,66,66);font-size: 18px;')
        encImgHolder.setFixedSize(410, 400)

        self.encEncryptButton = QtGui.QPushButton("Encrypt Data")
        self.encEncryptButton.setStyleSheet('background-color: rgb(255,80,0); font-size: 15px;')
        self.encEncryptButton.setFixedSize(200, 50)
        self.encEncryptButton.move(150, 150)
        self.encEncryptButton.clicked.connect(self.enc_img)
        self.encEncryptButton.setEnabled(False)

        self.encTextEditor = QtGui.QTextEdit()
        self.encTextEditor.setStyleSheet('background-color: rgb(66,66,66); color: rgb(255,90,0);font-size: 18px;')

        self.encSaveButton = QtGui.QPushButton("Save Image")
        self.encSaveButton.setStyleSheet('background-color: rgb(0,100,255); font-size: 15px;')
        self.encSaveButton.setFixedSize(200, 50)
        self.encSaveButton.clicked.connect(self.enc_save)
        self.encSaveButton.setEnabled(False)

        self.shaLbl = QtGui.QTextEdit(self)
        self.shaLbl.setStyleSheet('background-color: rgb(200,200,200); font-size: 18px;')
        self.shaLbl.setFixedSize(700, 40)
        self.shaLbl.move(0, 500)

        # -----------------------------------adding widgets to enc tab---------------------------------------------------

        encBoxLayout1 = QtGui.QVBoxLayout()
        encBoxLayout2 = QtGui.QVBoxLayout()

        encBoxElementsLayout_1 = QtGui.QHBoxLayout()
        encBoxElementsLayout_1.addWidget(self.encUploadButton)
        encBoxElementsLayout_1.addWidget(self.encEncryptButton)

        encboxElements = QtGui.QHBoxLayout()

        encBoxLayout1.addWidget(encImgHolder)
        encBoxLayout1.addLayout(encBoxElementsLayout_1)

        encBoxLayout2.addWidget(self.encTextEditor)
        encBoxLayout2.addWidget(self.encSaveButton)

        encboxElements.addLayout(encBoxLayout1)
        encboxElements.addLayout(encBoxLayout2)
        # ---------------------------------------ending encryption tab---------------------------------------------------

        # ---------------------------------------decrypt Tab layout elements---------------------------------------------

        self.decUploadButton = QtGui.QPushButton("Upload Image")
        self.decUploadButton.setStyleSheet('background-color: rgb(244,204,0); font-size: 15px;')
        self.decUploadButton.setFixedSize(200, 50)

        global decImgHolder
        decImgHolder = QtGui.QLabel()
        decImgHolder.setStyleSheet('background-color: rgb(202,202,202);font-size: 18px;')
        decImgHolder.setFixedSize(410, 400)

        self.decDecryptButton = QtGui.QPushButton("Decrypt Image")
        self.decDecryptButton.setStyleSheet('background-color: rgb(0,255,150); font-size: 15px;')
        self.decDecryptButton.setFixedSize(200, 50)
        self.decDecryptButton.move(150, 150)
        self.decDecryptButton.clicked.connect(self.dec_fn)
        self.decDecryptButton.setEnabled(False)

        self.decTextEditor = QtGui.QTextEdit()
        self.decTextEditor.setStyleSheet('background-color: rgb(202,202,202); color: rgb(0,150,150);font-size: 18px;')
        self.dec_path = ''

        self.decSaveButton = QtGui.QPushButton("Save Data")
        self.decSaveButton.setStyleSheet('background-color: rgb(0,100,255); font-size: 15px;')
        self.decSaveButton.setFixedSize(150, 50)
        self.decSaveButton.move(150, 150)
        self.decSaveButton.setEnabled(False)
        self.decSaveButton.clicked.connect(self.dec_save)

        self.shaButton = QtGui.QPushButton("SHA")
        self.shaButton.setStyleSheet('background-color: rgb(200, 0, 100); font-size: 15px;')
        self.shaButton.setFixedSize(100, 50)
        self.shaButton.clicked.connect(self.check_SHA)
        self.shaButton.setEnabled(False)

        # ------------------------------------------adding widget to decrypt tab-----------------------------------------

        decboxElements = QtGui.QHBoxLayout()
        decBoxLayout_1 = QtGui.QVBoxLayout()
        decBoxLayout_2 = QtGui.QVBoxLayout()

        decBoxElementsLayout_1 = QtGui.QHBoxLayout()
        decBoxElementsLayout_1.addWidget(self.decUploadButton)
        decBoxElementsLayout_1.addWidget(self.decDecryptButton)

        decBoxElementsLayout_2 = QtGui.QHBoxLayout()
        decBoxElementsLayout_2.addWidget(self.decSaveButton)
        decBoxElementsLayout_2.addWidget(self.shaButton)

        decBoxLayout_1.addWidget(decImgHolder)
        decBoxLayout_1.addLayout(decBoxElementsLayout_1)
        decBoxLayout_2.addWidget(self.decTextEditor)
        decBoxLayout_2.addLayout(decBoxElementsLayout_2)

        decboxElements.addLayout(decBoxLayout_1)
        decboxElements.addLayout(decBoxLayout_2)

        # ---------------------------------------ending encryption tab---------------------------------------------------

        dectab.setLayout(decboxElements)
        enctab.setLayout(encboxElements)

        tabs.addTab(enctab, "Encrypt")
        tabs.addTab(dectab, "Decrypt")

        # ---------------------------------------method Callings---------------------------------------------------------
        self.encUploadButton.clicked.connect(self.encUploadImage)
        self.decUploadButton.clicked.connect(self.decUploadImage)

        self.show()

    def encUploadImage(self):
        #print("Uploading Image for encryption")
        self.shaLbl.setText('')
        self.encTextEditor.setText('')
        try:
            name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
            file = open(name, 'r')
            file.close()
            self.encFileName = os.path.abspath(file.name)
            self.basicImageOperations()
            pixmap = QtGui.QPixmap(self.encFileName)
            #print(self.temp_im.size)
            encImgHolder.setPixmap(
                pixmap.scaled(encImgHolder.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            self.encEncryptButton.setEnabled(True)
            self.encSaveButton.setEnabled(True)
        except Exception as ex:
            print(ex)

    def decUploadImage(self):
        #print("Uploading Image for decryption")
        self.shaLbl.setText('')
        self.decTextEditor.setText('')
        try:
            self.statusBar().showMessage('Loading and Decrypting File')
            self.decFileName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', filter='*.bin')
            private_key_path = QtGui.QFileDialog.getOpenFileName(self, 'Select Private Key', filter='*.pem')
            with open(private_key_path, 'rb') as priv_file:
                keydata = priv_file.read()
            priv_key = rsa.PrivateKey._load_pkcs1_pem(keydata)
            priv_file.close()
            with open(self.decFileName, 'rb') as infile, open('temp.png', 'wb') as outfile:
                decrypt_bigfile(infile, outfile, priv_key)
                outfile.close()
                infile.close()
            pixmap = QtGui.QPixmap('temp.png')
            decImgHolder.setPixmap(
                pixmap.scaled(decImgHolder.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            self.dec_path = 'temp.png'
            self.shaButton.setEnabled(True)
        except Exception as ex:
            self.statusBar().showMessage('Valid Files Not Selected')
            print(ex)

    def basicImageOperations(self):

        # self.statusBar().showMessage("Scaling Image")
        self.image = ImageProcessor()
        im = Image.open(self.encFileName)
        #print(im.size)
        self.temp_im = self.image.Resizing_Image(im)
        im.close()
        self.temp_im.save("test.png")
        self.encFileName = "test.png"

    def enc_img(self):
        self.strout = ''
        self.ret_Byte('ENIGMA')
        #print(len(self.encTextEditor.toPlainText()))
        self.strout += ("{:016b}".format(len(self.encTextEditor.toPlainText())))
        rgbn = randint(0, 2)
        #print(rgbn)
        self.strout += ("{:02b}".format(rgbn))
        self.ret_Byte(str(self.encTextEditor.toPlainText()))
        self.ret_Byte('#ENIGMA')
        #print(self.strout)

        self.px = self.temp_im.load()
        x = 0
        temp = 0
        rgb = [0, 0, 0]
        for i in range(self.temp_im.size[0]):
            for j in range(self.temp_im.size[1]):
                rgb[0] = self.px[i, j][0]
                rgb[1] = self.px[i, j][1]
                rgb[2] = self.px[i, j][2]

                if self.strout[x] == '1' and rgb[temp] % 2 == 0:
                    rgb[temp] += 1
                elif self.strout[x] == '0' and rgb[temp] % 2 != 0:
                    rgb[temp] -= 1

                self.px[i, j] = (rgb[0], rgb[1], rgb[2])

                if x == 66:
                    temp = rgbn
                x += 1
                if x == len(self.strout):
                    break

            if x == len(self.strout):
                break

        self.statusBar().showMessage('Image Encrypted Successfully')
        self.encUploadButton.setEnabled(False)

    def dec_fn(self):
        if self.dec_path != '':
            self.decUploadButton.setEnabled(False)
            self.decTextEditor.clear()
            #print(self.dec_path)
            self.gen_SHA(self.dec_path)
            temp_im2 = Image.open(self.dec_path)
            px = temp_im2.load()
            chrstr = ''
            x = 0
            rng = 0
            chrr = ''
            temp = 0
            len_str = 0
            for i in range(temp_im2.size[0]):
                for j in range(temp_im2.size[1]):
                    if px[i, j][temp] % 2 == 0:
                        chrr += '0'
                    else:
                        chrr += '1'

                    rng += 1

                    if len(chrr) == 48:
                        for k in range(6):
                            chrstr += chr(int(chrr[x:x + 8], 2))
                            x += 8

                        if chrstr == 'ENIGMA':
                            self.statusBar().showMessage('Image is encrypted')
                            x = 0
                        else:
                            self.statusBar().showMessage('Image is not encrypted')
                            return

                    if len(chrr) == 66:
                        temp = int(chrr[-2:], 2)
                        len_str = int(chrr[48:64], 2)
                    elif rng == ((len_str * 8) + 66):
                        x = 1
                        break

                if x == 1:
                    self.statusBar().showMessage('Decryption Complete')
                    break

            #print(chrr)

            x = 66

            #print(len_str)

            chrstr = ''

            for i in range(len_str):
                chrstr += chr(int(chrr[x:x + 8], 2))
                x += 8

            #print(chrstr)
            self.decTextEditor.append(chrstr)
            os.remove('temp.png')

        else:
            QtGui.QMessageBox.information(self, 'Error', 'Image not selected', QtGui.QMessageBox.Ok)
            self.statusBar().showMessage('Image Not Selected')

    def enc_save(self):
        try:
            self.statusBar().showMessage('Saving File')
            file = QtGui.QFileDialog.getSaveFileName(self, 'Save File', filter='*.bin')
            #print(file)
            self.temp_im.save('temp.png')
            public_key_path = QtGui.QFileDialog.getOpenFileName(self, 'Select Public Key', filter='*.pem')
            with open(public_key_path, 'rb') as pub_file:
                keydata = pub_file.read()
            pub_file.close()
            pub_key = rsa.PublicKey._load_pkcs1_pem(keydata)
            with open('temp.png', 'rb') as infile, open(file, 'wb') as outfile:
                encrypt_bigfile(infile, outfile, pub_key)
            outfile.close()
            infile.close()
            os.remove('temp.png')
            os.remove('test.png')
            sha_str = self.gen_SHA(file)
            self.shaLbl.setText('SHA : '+sha_str)
            self.encUploadButton.setEnabled(True)
            self.encEncryptButton.setEnabled(False)
            self.encSaveButton.setEnabled(False)
            self.statusBar().showMessage('File saved successfully')
            self.temp_im.close()
        except Exception as ex:
            self.statusBar().showMessage('Error Occurred')

    def dec_save(self):
        try:
            file = QtGui.QFileDialog.getSaveFileName(self, 'Save File', filter='*.txt')
            save_file = open(file, 'w')
            save_file.write(self.decTextEditor.toPlainText())
            save_file.close()
            self.statusBar().showMessage('File Saved Successfully')
            self.decUploadButton.setEnabled(True)
            self.decDecryptButton.setEnabled(False)
            self.decSaveButton.setEnabled(False)
        except Exception as ex:
            self.statusBar().showMessage('Error Occurred')

    def gen_SHA(self, file_name):
        sha = hashlib.sha256()
        file = open(file_name, 'rb')
        buf = file.read(65536)
        while len(buf) > 0:
            sha.update(buf)
            buf = file.read(65536)
        hash_res = sha.hexdigest()
        hash_res.encode('ascii')
        #print(hash_res)
        file.close()
        return hash_res

    def check_SHA(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter SHA :')
        if ok:
            sha_str = text
            if sha_str == self.gen_SHA(self.decFileName):
                self.statusBar().showMessage('SHA Matched. Image Decrypted')
                self.decDecryptButton.setEnabled(True)
                self.decSaveButton.setEnabled(True)
                self.shaButton.setEnabled(False)
            else:
                self.statusBar().showMessage('SHA Not Matched. Image not Decrypted')
                self.decDecryptButton.setEnabled(False)
                self.decSaveButton.setEnabled(False)

def runGUI():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

'''------------------------------------------------MAIN SECTION------------------------------------------------------'''

runGUI()