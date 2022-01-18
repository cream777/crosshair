from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow, QPushButton, QWidget
import sys




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(190, 110)
        self.selectFile()
        self.buttons()


    def selectFile(self):
        self.selectFile = QPushButton('Select File', self)
        self.selectFile.setGeometry(10, 20, 70, 70)
        self.selectFile.clicked.connect(self.select_file)


    def buttons(self):
        self.up = QPushButton('🡹', self)
        self.up.setGeometry(120, 10, 30, 30)
        self.up.clicked.connect(self.moveup)

        self.down = QPushButton('🡻', self)
        self.down.setGeometry(120, 70, 30, 30)
        self.down.clicked.connect(self.movedown)


        self.left = QPushButton('🡸', self)
        self.left.setGeometry(90, 40, 30, 30)
        self.left.clicked.connect(self.moveleft)


        self.right = QPushButton('🡺', self)
        self.right.setGeometry(150, 40, 30, 30)
        self.right.clicked.connect(self.moveright)


    def select_file(self):
        file = QFileDialog.getOpenFileName(self, 'Open A File', '.', '(*.jpg, *.jpeg, *.png)')
        self.crosshair = QWidget()
        label = QLabel(self.crosshair)
        pixmap = QPixmap(file[0])
        label.setPixmap(pixmap)
        label.resize(pixmap.width(),pixmap.height())

        self.crosshair.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.crosshair.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.crosshair.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint | QtCore.Qt.WindowType.FramelessWindowHint)

        res = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        x = int((res.width() / 2) - (pixmap.width() / 2))
        y = int((res.height() / 2) + (pixmap.height() / 2))
        self.crosshair.move(x, y)
        
        self.crosshair.show()


    def moveup(self):
        pos = self.crosshair.pos()
        self.crosshair.move(pos.x(), pos.y() - 1)

    def movedown(self):
        pos = self.crosshair.pos()
        self.crosshair.move(pos.x(), pos.y() + 1)
        
    def moveleft(self):
        pos = self.crosshair.pos()
        self.crosshair.move(pos.x() - 1, pos.y())        
    
    def moveright(self):
        pos = self.crosshair.pos()
        self.crosshair.move(pos.x() + 1, pos.y())


    def closeEvent(self, event):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MW = MainWindow()
    MW.show()
    app.exec()
