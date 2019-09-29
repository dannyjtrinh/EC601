import sys
from ui import *


def main():
    app = QApplication(sys.argv)
    gui = ui()
    gui.show()
    sys.exit(app.exec_())

    
main()
