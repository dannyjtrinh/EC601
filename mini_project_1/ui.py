import sys
import os
import time
from twitter_api import *
from google_api import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

            

class result_ui(QMainWindow):
    
    def __init__(self, parent=None):
        super(result_ui, self).__init__(parent)
        

class ui():

    def __init__(self, keys):
        self.thread = AThread(self.analysis_cmds)
        
        # Create Twitter scrapper class instance
        self.twitter_scrapper = twitter_scrapper(keys)
        
        # Create an PyQT4 application object.
        self.a = QApplication(sys.argv)

        # Create Results UI
        self.result_ui = result_ui()
        self.result_ui.setWindowTitle("Results")
        self.result_ui.setGeometry(1200, 300, 100, 50)
        self.result_ui.resize(300, 300)
        
        # The QWidget widget is the base class of all user interface objects in PyQt4.
        self.w = QWidget()
        self.w.connect(self.thread, self.thread.signal, self.post_results)
        
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
        self.result_ui.show()

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

        # Place progress spinner icon
        label = QLabel(self.w)
        label.resize(70,50)
        self.progress_spinner = \
            QMovie(os.getcwd() + '/ui_elements/ajax-loader-static.gif')
        label.setMovie(self.progress_spinner)
        label.move(250, 200)
        self.progress_spinner.start()

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

        # Place Results Textbox
        self.results_text = QTextEdit(self.result_ui)
        self.results_text.resize(300,300)
        self.results_text.setReadOnly(True)
        
    def on_analyze_click(self):
        self.results_text.clear()
        self.analyze_button.setEnabled(False)
        self.set_color(255, 255, 255)
        self.progress_spinner.stop()
        self.progress_spinner.setFileName(\
                            os.getcwd() + '/ui_elements/ajax-loader.gif')
        self.progress_spinner.start()
        
        self.thread.start()

    def analysis_cmds(self):       
        username = str(self.username_textbox.text())
        product = str(self.product_textbox.text())

        try:
            tweet_sentence_block = \
                self.twitter_scrapper.search_twitter(username, product)
            
            score, top_tweets = analyze(tweet_sentence_block)

            results_string = "Top Tweets\n\n"+top_tweets[0][1]+"\n\n"+\
                top_tweets[1][1]+"\n\n"+\
                top_tweets[2][1]+"\n\n"+\
                "Worst Tweets"+"\n\n"+\
                top_tweets[3][1]+"\n\n"+\
                top_tweets[4][1]+"\n\n"+\
                top_tweets[5][1]
        except Exception as e:
            print e
            score = 0
            results_string = ""

        return score, results_string

    def post_results(self, score, results_string):
        if (score == 0.0):
            self.set_color(255, 255, 255) #white
        elif(score <= -0.3):
            self.set_color(220,20,60) #red
        elif(score < 0):
            self.set_color(255,165,0) #orange
        elif(score <= 0.3):
            self.set_color(255, 255, 0) #yellow
        else:
            self.set_color(124,252,0) #green
            
        self.results_text.insertPlainText(results_string+"\n\nScore: "+
                                          str(score)+"\n")
        self.analyze_button.setEnabled(True)
        self.progress_spinner.stop()
        
    def set_color(self, x, y, z):
        self.gradient.setColorAt(0.0, QColor(int(x), int(x), int(x)))
        self.gradient.setColorAt(1.0, QColor(int(x), int(y), int(z)))
        self.p.setBrush(QPalette.Window, QBrush(self.gradient))
        self.w.setPalette(self.p)


class AThread(QThread):

    def __init__(self, function, parent=None):
        super(AThread, self).__init__(parent)
        self.function = function
        self.signal = SIGNAL("signal")
    
    def run(self):
        value, result_string = self.function()
        self.emit(self.signal, value, result_string)
