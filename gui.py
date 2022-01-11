import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir

import subprocess

class LexicalAnalyzerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setupWidgets()
        self.setupLayouts()

    def setupLayouts(self):
        layout = QVBoxLayout()
        layout.addWidget(self.fileInputBtn)
        layout.addWidget(self.textEditor)
        self.setLayout(layout)

    def setupWidgets(self):
        self.resize(300, 500)
        self.setWindowTitle("Lexical Analyzer GUI")
        self.fileInputBtn = QPushButton("Select File")
        self.fileInputBtn.clicked.connect(self.getFile)
        self.textEditor = QTextEdit()

    def getFile(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            filepaths = dialog.selectedFiles()
            filepath = filepaths[0]
            if filepath.endswith('.spyc'):# check if the filename extension is supported
                output = subprocess.run('python shell.py -o -f ' + '"' + filepath + '"', shell=True, capture_output=True)# execute the lexical analyzer script
                # print('OUTPUT:' + output.stdout.decode('UTF-8'))
                self.textEditor.setPlainText(output.stdout.decode('UTF-8')) # output the result of the lexical analyzer to the texteditor
                
                # with open(filename, 'r') as f:
                #     data = f.read()
                #     self.textEditor.setPlainText(data)
                #     f.close()
            else:
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    demo = LexicalAnalyzerGUI()
    demo.show()

    sys.exit(app.exec_())