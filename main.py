# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 10:48:58 2020

@author: egod
"""
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QFileDialog, QLabel, QSlider
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore

from PIL import Image

class FaceMerge(QWidget):
    def __init__(self):
        super().__init__()
        # img path stored to use when merge
        self.img1 = 'data/png/1.png'
        self.img2 = 'data/png/1.png'
        # default img
        self.defaultpix = QPixmap('data/png/1.png')
        self.defaultpix=self.scalePixmap(self.defaultpix)
        
        self.initUI()
        
    def initUI(self):
        # frame setting
        self.setGeometry(300,300,570,200)
        self.setFixedSize(570, 200)
        self.setWindowTitle('Emotion Merge')
        self.setWindowIcon(QIcon('imgs/icon.png'))
        
        # root vertical box
        vbox = QVBoxLayout()
        
        
        # up horizontal box for images
        hboxUp = QHBoxLayout()
        
        # slider
        self.sli = QSlider(QtCore.Qt.Vertical)
        self.sli.setFixedHeight(100)
        self.sli.setMinimum(10)
        self.sli.setMaximum(90)
        self.sli.setValue(50)
        self.sli.valueChanged.connect(self.updateUpAndDown)
        
        # labels
        lb1 = QLabel()
        lb1.setFixedSize(100,100)
        #lb1.setAlignment(QtCore.Qt.AlignCenter)
        lb1.setStyleSheet('border: 2px solid black')
        lb1.setPixmap(self.defaultpix)
        self.lb1 = lb1
        
        lbplus = QLabel('+')
        lbplus.setStyleSheet('font-size:100px')
        lbplus.setAlignment(QtCore.Qt.AlignCenter)
        lbplus.setFixedSize(100,100)
        
        
        lb2 = QLabel()
        lb2.setFixedSize(100,100)
        #lb2.setAlignment(QtCore.Qt.AlignCenter)
        lb2.setStyleSheet('border: 2px solid black')
        lb2.setPixmap(self.defaultpix)
        self.lb2 = lb2
        
        lbequal = QLabel('=')
        lbequal.setStyleSheet('font-size:100px')
        lbequal.setAlignment(QtCore.Qt.AlignCenter)
        lbequal.setFixedSize(100,100)
        
        lb3 = QLabel()
        lb3.setFixedSize(100,100)
        lb3.setAlignment(QtCore.Qt.AlignCenter)
        lb3.setStyleSheet('border: 2px solid black')
        lb3.setPixmap(self.defaultpix)
        self.lb3 = lb3
        
        # localize the labels
        hboxUp.addStretch(1)
        hboxUp.addWidget(self.sli)
        hboxUp.addStretch(1)
        hboxUp.addWidget(self.lb1)
        hboxUp.addStretch(1)
        hboxUp.addWidget(lbplus)
        hboxUp.addStretch(1)
        hboxUp.addWidget(self.lb2)
        hboxUp.addStretch(1)
        hboxUp.addWidget(lbequal)
        hboxUp.addStretch(1)
        hboxUp.addWidget(self.lb3)
        hboxUp.addStretch(1)
        
        
        # down horizontal box for buttons
        hboxDown = QHBoxLayout()
        
        # buttons
        btnSel1 = QPushButton('Select',self)
        btnSel2 = QPushButton('Select',self)
        btnGet = QPushButton('Get', self)
        
        # set functions for buttons
        btnSel1.clicked.connect(self.openfile1)
        btnSel2.clicked.connect(self.openfile2)
        btnGet.clicked.connect(self.merge)
        
        # localize the btns
        hboxDown.addStretch(3)
        hboxDown.addWidget(btnSel1)
        hboxDown.addStretch(10)
        hboxDown.addWidget(btnSel2)
        hboxDown.addStretch(10)
        hboxDown.addWidget(btnGet)
        hboxDown.addStretch(0)
        
        # layout
        vbox.addStretch(1)
        vbox.addLayout(hboxUp)
        vbox.addStretch(1)
        vbox.addLayout(hboxDown)
        vbox.addStretch(1)
        self.setLayout(vbox)
        
        self.show()
        
    # scale the 24x24 raw iamge to 100x100
    def scalePixmap(self,pix):
        return pix.scaled(QtCore.QSize(100,100),QtCore.Qt.IgnoreAspectRatio)
    
    # open an image
    def openfile(self,which):
        fname = QFileDialog.getOpenFileName(self,'选择图片','./data/png')
        if fname[0]:
            #print('button{0} select {1}'.format(which,fname[0])) 
            pix = QPixmap(fname[0]) # read img
            pix = self.scalePixmap(pix) # scale img to 100x100
            if which ==1:
                self.lb1.setPixmap(pix)
                self.img1 = fname[0]
            elif which ==2:
                self.lb2.setPixmap(pix)
                self.img2 = fname[0]

    def openfile1(self):
        self.openfile(1)
            
    def openfile2(self):
        self.openfile(2)
        
    # merge the two images according to the slider
    def merge(self):
        percent = self.sli.value() # read the value of slider
        # crop imgs according to the value of slider
        img1 = Image.open(self.img1).resize((100,100)).crop((0,0,100,100-percent))
        img2 = Image.open(self.img2).resize((100,100)).crop((0,100-percent,100,100))
        # create new img
        target = Image.new('RGBA',(100,100),1)
        target.paste(img1,(0,0,100,100-percent))
        target.paste(img2,(0,100-percent,100,100))
        # save the output img and refresh the frame
        target.save('out.png')
        pix = QPixmap('out.png')
        pix = self.scalePixmap(pix)
        self.lb3.setPixmap(pix)
        
    # update images with slider
    def updateUpAndDown(self):
        percent = self.sli.value()
        img1 = Image.open(self.img1).resize((100,100)).crop((0,0,100,100-percent))
        img2 = Image.open(self.img2).resize((100,100)).crop((0,100-percent,100,100))
        if not os.path.exists('temp'):
            os.mkdir('temp')
        img1.save('temp/img1.png')
        img2.save('temp/img2.png')
        
        pix = QPixmap('temp/img1.png')
        pix = self.scalePixmap(pix)
        self.lb1.setPixmap(pix)
        
        pix = QPixmap('temp/img2.png')
        pix = self.scalePixmap(pix)
        self.lb2.setPixmap(pix)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    fm = FaceMerge()
    
    sys.exit(app.exec_())