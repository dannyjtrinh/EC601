#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
import os
import time
from PyQt4.QtGui import *


class ui():

    def __init__(self):
        # Create an PyQT4 application object.
        self.a = QApplication(sys.argv)
        
        # The QWidget widget is the base class of all user interface objects in PyQt4.
        self.w = QWidget()
        
        # Set window size.
        self.w.resize(320, 240)
    
        # Set window title
        self.w.setWindowTitle("Flop or Not")

        # Setup ui elements
        self.setup_ui_elements()

        # Setup buttons and textboxes
        self.setup_textbox_and_buttons()
        
        # Show window
        self.w.show()

        # Setup gradient and palette for window color
        self.gradient = QLinearGradient(0, 0, 0, 400)
        self.p = QPalette()
        self.set_color(255, 255, 255)

        sys.exit(self.a.exec_())

    def setup_ui_elements(self):
        # Place Twitter logo in gui
        label = QLabel(self.w)
        pixmap = QPixmap(os.getcwd() + '/ui_elements/twitter_scaled.png')
        label.setPixmap(pixmap)
        label.move(50,50)

        # Place Product logo in gui
        label = QLabel(self.w)
        pixmap = QPixmap(os.getcwd() + '/ui_elements/product_scaled.png')
        label.setPixmap(pixmap)
        label.move(50,105)

    def setup_textbox_and_buttons(self):
        # Create Twitter username textbox
        self.username_textbox = QLineEdit(self.w)
        self.username_textbox.move(110, 60)
        self.username_textbox.resize(175,30)

        # Create Product textbox
        self.product_textbox = QLineEdit(self.w)
        self.product_textbox.move(110, 115)
        self.product_textbox.resize(175,30)

        # Place Analyzer Button
        self.analyze_button = QPushButton('Analyze', self.w)
        self.analyze_button.move(125,175)
        self.analyze_button.clicked.connect(self.on_analyze_click)

    def on_analyze_click(self):
        username = str(self.username_textbox.text())
        product = str(self.product_textbox.text())
        self.analyze_button.setEnabled(True)
        
        self.set_color(220,20,60)
        #self.set_color(255,165,0) #orange
        #self.set_color(124,252,0) #green
        #self.set_color(255, 255, 0) #yellow
  
    def set_color(self, x, y, z):
        self.gradient.setColorAt(0.0, QColor(int(x), int(x), int(x)))
        self.gradient.setColorAt(1.0, QColor(int(x), int(y), int(z)))
        self.p.setBrush(QPalette.Window, QBrush(self.gradient))
        self.w.setPalette(self.p)

