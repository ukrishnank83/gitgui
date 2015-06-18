#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This example shows three labels on a window
using absolute positioning. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        
        lbl1 = QtGui.QLabel('Welcome to GIT GUI', self)
        lbl1.move(15, 10)

        lbl2 = QtGui.QLabel('Welcome to GIT', self)
        lbl2.move(100,300 )

        okButton = QtGui.QPushButton("Next")
        cancelButton = QtGui.QPushButton("Quit")

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)   
               
        self.setGeometry(100, 100, 1000, 1000)
        self.setWindowTitle('GIT GUI')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

