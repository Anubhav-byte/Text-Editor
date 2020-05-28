import sys
from PyQt5.QtWidgets import QMainWindow,QTextEdit,QAction,QApplication,QMessageBox,QFileDialog
from PyQt5.QtGui import QIcon 


class Text(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):

        self.textedit=QTextEdit()
        self.setCentralWidget(self.textedit)
        self.textedit.setText(" ")

        saveAction=QAction(QIcon('save.png'),'Save',self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setToolTip("Save the file")
        saveAction.triggered.connect(self.save)
        

        openAction=QAction(QIcon('open.png'),'Open',self)
        openAction.setShortcut('Ctrl+o')
        openAction.triggered.connect(self.open)
        
        newAction=QAction(QIcon('new.png'),'New',self)
        newAction.setShortcut('Ctrl+n')
        newAction.triggered.connect(self.__init__)




        menubar=self.menuBar()
        filemenu=menubar.addMenu('&File')
        filemenu.addAction(saveAction)
        filemenu.addAction(openAction)
        filemenu.addAction(newAction)

        tb=self.addToolBar('File')
        tb.addAction(saveAction)
        tb.addAction(openAction)
        tb.addAction(newAction)

    def save(self):
        fname=QFileDialog.getSaveFileName(self,'Save File')
        data=self.textedit.toPlainText()
        file=open(fname[0],'w')
        file.write(data)
        file.close()
    

    def open(self):
        fname=QFileDialog.getOpenFileName(self,'Open File', '/home')
        if fname[0]:
            file=open(fname[0],'r')

            with file:
                data=file.read()
                self.textedit.setText(data)

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Text()
    ex.show()
    sys.exit(app.exec_())

