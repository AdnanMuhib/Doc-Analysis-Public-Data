# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Table_Recognition.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import setup as setup
import ntpath
import os
import re
import weka.core.jvm as jvm



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    ## Global Variables
    file_name = None
    file_path = None
    write_path = None
    model_path = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(800, 529)
        MainWindow.showFullScreen()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("table.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabTraining = QtGui.QWidget()
        self.tabTraining.setObjectName(_fromUtf8("tabTraining"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tabTraining)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.tabTraining)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.txtBoxArff = QtGui.QLineEdit(self.tabTraining)
        self.txtBoxArff.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtBoxArff.setObjectName(_fromUtf8("txtBoxArff"))
        self.horizontalLayout_3.addWidget(self.txtBoxArff)
        self.btnBrowseArff = QtGui.QPushButton(self.tabTraining)
        self.btnBrowseArff.setObjectName(_fromUtf8("btnBrowseArff"))
        # signal for Arff browse Button
        self.btnBrowseArff.clicked.connect(self.browse_arff)

        self.horizontalLayout_3.addWidget(self.btnBrowseArff)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.tabTraining)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.txtBoxCSV = QtGui.QLineEdit(self.tabTraining)
        self.txtBoxCSV.setEnabled(True)
        self.txtBoxCSV.setAcceptDrops(True)
        self.txtBoxCSV.setObjectName(_fromUtf8("txtBoxCSV"))
        self.horizontalLayout_2.addWidget(self.txtBoxCSV)
        self.btnBrowseCSV = QtGui.QPushButton(self.tabTraining)
        self.btnBrowseCSV.setObjectName(_fromUtf8("btnBrowseCSV"))
        # signal for csv browse Button
        self.btnBrowseCSV.clicked.connect(self.browse_csv)

        self.horizontalLayout_2.addWidget(self.btnBrowseCSV)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.btnTrain = QtGui.QPushButton(self.tabTraining)
        self.btnTrain.setObjectName(_fromUtf8("btnTrain"))
        self.horizontalLayout_5.addWidget(self.btnTrain)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_6 = QtGui.QLabel(self.tabTraining)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.txtBoxModel = QtGui.QLineEdit(self.tabTraining)
        self.txtBoxModel.setObjectName(_fromUtf8("txtBoxModel"))
        self.horizontalLayout_4.addWidget(self.txtBoxModel)
        self.btnBrowseModel = QtGui.QPushButton(self.tabTraining)
        self.btnBrowseModel.setObjectName(_fromUtf8("btnBrowseModel"))
        # signal for model browse Button
        self.btnBrowseModel.clicked.connect(self.browse_model)

        self.horizontalLayout_4.addWidget(self.btnBrowseModel)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabTraining, _fromUtf8(""))
        self.tabTesting = QtGui.QWidget()
        self.tabTesting.setObjectName(_fromUtf8("tabTesting"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tabTesting)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnShowRows = QtGui.QPushButton(self.tabTesting)
        self.btnShowRows.setObjectName(_fromUtf8("btnShowRows"))
        # signal for show Rows Button
        self.btnShowRows.clicked.connect(self.show_rows)
        self.gridLayout_2.addWidget(self.btnShowRows, 4, 5, 1, 1)
        self.labelInputImage = QtGui.QLabel(self.tabTesting)
        self.labelInputImage.setText(_fromUtf8(""))
        self.labelInputImage.setPixmap(QtGui.QPixmap(_fromUtf8(":/img/preview.jpeg")))
        self.labelInputImage.setScaledContents(False)
        self.labelInputImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInputImage.setObjectName(_fromUtf8("labelInputImage"))
        self.gridLayout_2.addWidget(self.labelInputImage, 1, 0, 1, 3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 1, 3, 1, 1)
        self.labelOutputImage = QtGui.QLabel(self.tabTesting)
        self.labelOutputImage.setText(_fromUtf8(""))
        self.labelOutputImage.setPixmap(QtGui.QPixmap(_fromUtf8(":/img/preview.jpeg")))
        self.labelOutputImage.setScaledContents(False)
        self.labelOutputImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOutputImage.setObjectName(_fromUtf8("labelOutputImage"))
        self.gridLayout_2.addWidget(self.labelOutputImage, 1, 5, 1, 3)
        self.btnShowCells = QtGui.QPushButton(self.tabTesting)
        self.btnShowCells.setObjectName(_fromUtf8("btnShowCells"))
         # signal for show cells Button
        self.btnShowCells.clicked.connect(self.show_cells)

        self.gridLayout_2.addWidget(self.btnShowCells, 4, 2, 1, 1)
        self.btnImageBrowse = QtGui.QPushButton(self.tabTesting)
        self.btnImageBrowse.clicked.connect(self.browse_picture)
        self.btnImageBrowse.setObjectName(_fromUtf8("btnImageBrowse"))
        self.gridLayout_2.addWidget(self.btnImageBrowse, 4, 0, 1, 1)
        self.btnProcessImage = QtGui.QPushButton(self.tabTesting)
        self.btnProcessImage.setObjectName(_fromUtf8("btnProcessImage"))
        # signal for Process Image Button
        self.btnProcessImage.clicked.connect(self.process_image)

        self.gridLayout_2.addWidget(self.btnProcessImage, 4, 1, 1, 1)
        self.btnShowStructure = QtGui.QPushButton(self.tabTesting)
        self.btnShowStructure.setObjectName(_fromUtf8("btnShowStructure"))
        # signal for show structure Button
        self.btnShowStructure.clicked.connect(self.show_struct)
        self.gridLayout_2.addWidget(self.btnShowStructure, 4, 7, 1, 1)
        self.btnShowTable = QtGui.QPushButton(self.tabTesting)
        self.btnShowTable.setObjectName(_fromUtf8("btnShowTable"))
       # signal for show table Button
        self.btnShowTable.clicked.connect(self.show_table)
       
        self.gridLayout_2.addWidget(self.btnShowTable, 4, 6, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tabTesting, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Table Recognition", None))
        self.label_5.setText(_translate("MainWindow", "Arff File", None))
        self.btnBrowseArff.setText(_translate("MainWindow", "Browse", None))
        self.label_4.setText(_translate("MainWindow", "CSV File", None))
        self.btnBrowseCSV.setText(_translate("MainWindow", "Browse", None))
        self.btnTrain.setText(_translate("MainWindow", "Train", None))
        self.label_6.setText(_translate("MainWindow", "Model File", None))
        self.btnBrowseModel.setText(_translate("MainWindow", "Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTraining), _translate("MainWindow", "Training", None))
        self.btnShowRows.setText(_translate("MainWindow", "show Rows", None))
        self.btnShowCells.setText(_translate("MainWindow", "Show Cells", None))
        self.btnImageBrowse.setText(_translate("MainWindow", "Browse Picture", None))
        self.btnProcessImage.setText(_translate("MainWindow", "Process", None))
        self.btnShowStructure.setText(_translate("MainWindow", "Show Structure", None))
        self.btnShowTable.setText(_translate("MainWindow", "Show table", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTesting), _translate("MainWindow", "Testing", None))
    def browse_picture(self):
        image = QtGui.QFileDialog.getOpenFileName(None,'OpenFile','c:\\',"Image file(*.png *.jpg)")
        image = str(image)
        print(image)
        self.file_name = ntpath.basename(image)
        self.file_name, ext=os.path.splitext(self.file_name)
        self.file_path = ntpath.dirname(image)
        self.write_path = ntpath.expanduser('~\\Documents\\Document Analysis')
        # creating write path if not exists 
        if not os.path.exists(self.write_path):
            os.makedirs(self.write_path)
        if image:
        	self.labelInputImage.setPixmap(QtGui.QPixmap(image).scaled(self.labelInputImage.width(), self.labelInputImage.height()))
    def process_image(self):
        if (not (self.file_path == None) and not(self.file_name == None) and not (self.write_path == None)):
            jvm.start()
            setup.setup_main(self.file_path, self.file_name, self.write_path)
            jvm.stop()
        else:
            print("Load Image First")
    def browse_csv(self):
        fileName = QtGui.QFileDialog.getOpenFileName(None,'OpenFile','.csv')
        self.txtBoxCSV.setText(fileName)
        print(fileName)
    def browse_arff(self):
        fileName = QtGui.QFileDialog.getOpenFileName(None,'OpenFile','.arff')
        self.txtBoxArff.setText(fileName)
        print(fileName)
    def browse_model(self):
        fileName = QtGui.QFileDialog.getOpenFileName(None,'OpenFile','.model')
        self.txtBoxModel.setText(fileName)
        print(fileName)
    def show_cells(self):
        path = self.write_path+"\\" + self.file_name + "_cells.png"
        self.labelOutputImage.setPixmap(QtGui.QPixmap(path).scaled(self.labelOutputImage.width(), self.labelOutputImage.height(),QtCore.Qt.KeepAspectRatio))
    def show_rows(self):
        path = self.write_path+"\\" + self.file_name + "_rows.png"
        self.labelOutputImage.setPixmap(QtGui.QPixmap(path).scaled(self.labelOutputImage.width(), self.labelOutputImage.height(),QtCore.Qt.KeepAspectRatio))
    def show_table(self):
        path = self.write_path+"\\" + self.file_name + "_table.png"
        self.labelOutputImage.setPixmap(QtGui.QPixmap(path).scaled(self.labelOutputImage.width(), self.labelOutputImage.height(),QtCore.Qt.KeepAspectRatio))
    def show_struct(self):
        path = self.write_path+"\\" + self.file_name + "_struct_identification.png"
        self.labelOutputImage.setPixmap(QtGui.QPixmap(path).scaled(self.labelOutputImage.width(), self.labelOutputImage.height(),QtCore.Qt.KeepAspectRatio))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

