from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import sys
import time  
import traceback
import SortingAlgorithms

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AlgoComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.AlgoComboBox.setGeometry(QtCore.QRect(370, 90, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AlgoComboBox.setFont(font)
        self.AlgoComboBox.setObjectName("AlgoComboBox")
        self.AlgoComboBox.addItems(["Merge Sort", "Bubble Sort", "Selection Sort", "Insertion Sort", 
                                    "Hybrid Merge Sort", "Quick Sort", "Counting Sort", 
                                    "Radix Sort", "Bucket Sort", "PigeonHole Sort", 
                                    "Cycle Sort", "Tim Sort"])
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 90, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 150, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.AttributeComboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.AttributeComboBox_2.setGeometry(QtCore.QRect(370, 150, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AttributeComboBox_2.setFont(font)
        self.AttributeComboBox_2.setObjectName("AttributeComboBox_2")
        self.AttributeComboBox_2.addItems(["Price", "Title", "Location", "City", "Beds", "Baths", "Area"])
        self.SortButton = QtWidgets.QPushButton(self.centralwidget)
        self.SortButton.setGeometry(QtCore.QRect(580, 200, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SortButton.setFont(font)
        self.SortButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SortButton.setStyleSheet("color:white;\n"
                                      "background-color:rgb(0, 85, 0)")
        self.SortButton.setObjectName("SortButton")
        self.datatableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.datatableWidget.setGeometry(QtCore.QRect(40, 250, 681, 311))
        self.datatableWidget.setColumnCount(7)
        self.datatableWidget.setObjectName("datatableWidget")
        self.datatableWidget.setRowCount(0)
        self.datatableWidget.setHorizontalHeaderLabels(["Title", "Price", "Location", "City", "Beds", "Baths", "Area"])
        self.runtime = QtWidgets.QLabel(self.centralwidget)
        self.runtime.setGeometry(QtCore.QRect(70, 200, 80, 26))
        self.runtime.setStyleSheet("color:white;\n"
                                   "background-color:rgb(0, 85, 0);\n"
                                   "padding-left:6px;\n"
                                   "padding-right:6px;\n")
        self.runtime.setObjectName("runtime")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.data = [] 
        self.loadDataFromCSV('Data/zameen_homes.csv')  

        self.SortButton.clicked.connect(self.sortData)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select Sorting Algorithm: "))
        self.label_2.setText(_translate("MainWindow", "Data Sorting "))
        self.label_3.setText(_translate("MainWindow", "Select Attribute to sort: "))
        self.SortButton.setText(_translate("MainWindow", "Sort"))
        self.runtime.setText(_translate("MainWindow", "Runtime:"))

    def loadDataFromCSV(self, fileName):
        with open(fileName, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  
            self.data = []  
            for row in reader:
                self.data.append(row)
                rowPosition = self.datatableWidget.rowCount()
                self.datatableWidget.insertRow(rowPosition)
                for column, value in enumerate(row):
                    self.datatableWidget.setItem(rowPosition, column, QtWidgets.QTableWidgetItem(value))

    def sortData(self):
        self.runtime.setGeometry(QtCore.QRect(70, 200, 80, 21))
        self.runtime.setText("Runtime: ")
        try:
            selected_algo = self.AlgoComboBox.currentText()
            selected_attribute = self.AttributeComboBox_2.currentText()
            attribute_index = self.getAttributeIndex(selected_attribute)

            if attribute_index == -1:
                raise ValueError("Invalid attribute selected.")

            array_to_sort = [(row[attribute_index], row) for row in self.data]

            start_time = time.time()

            if selected_algo == 'Merge Sort':
                SortingAlgorithms.MergeSort(array_to_sort, 0, len(array_to_sort))

            elif selected_algo == 'Hybrid Merge Sort':
                SortingAlgorithms.HybridMergeSort(array_to_sort, 0, len(array_to_sort) - 1)

            elif selected_algo == 'Bubble Sort':
                SortingAlgorithms.BubbleSort(array_to_sort, 0, len(array_to_sort))

            elif selected_algo == 'Selection Sort':
                SortingAlgorithms.SelectionSort(array_to_sort, 0, len(array_to_sort))

            elif selected_algo == 'Insertion Sort':
                SortingAlgorithms.InsertionSort(array_to_sort, 0, len(array_to_sort))

            elif selected_algo == 'Quick Sort':
                SortingAlgorithms.QuickSort(array_to_sort, 0, len(array_to_sort))

            elif selected_algo == 'Cycle Sort':
                SortingAlgorithms.CycleSort(array_to_sort)

            elif selected_algo == 'Counting Sort':
                array_to_sort = SortingAlgorithms.CountingSort(array_to_sort)

            elif selected_algo == 'Radix Sort':
                array_to_sort = SortingAlgorithms.RadixSort(array_to_sort)

            elif selected_algo == 'Bucket Sort':
                array_to_sort = SortingAlgorithms.BucketSort(array_to_sort)

            elif selected_algo == 'PigeonHole Sort':
                SortingAlgorithms.pigeonhole_sort(array_to_sort)

            elif selected_algo == 'Tim Sort':
                SortingAlgorithms.TimSort(array_to_sort)

            end_time = time.time()
            runtime = (end_time - start_time) * 1000  
            self.runtime.setGeometry(QtCore.QRect(70, 200, 180, 21))
            self.runtime.setText(f"Runtime: {runtime:.2f} ms")

            self.displaySortedArray([row for _, row in array_to_sort])

        except Exception as e:
            error_message = str(e)
            self.runtime.setText(f"Error: {error_message}")
            print("An error occurred:", error_message)
            print(traceback.format_exc())

    def getAttributeIndex(self, attribute):
        attribute_map = {
            "Title": 0,
            "Price": 1,
            "Location": 2,
            "City": 3,
            "Beds": 4,
            "Baths": 5,
            "Area": 6
        }
        return attribute_map.get(attribute, -1)

    def displaySortedArray(self, sorted_data):
        self.datatableWidget.setRowCount(0)
        existing_rows = set()  
    
        for row in sorted_data:
            row_tuple = tuple(row)  
            
            if row_tuple not in existing_rows:  
                existing_rows.add(row_tuple)  
                rowPosition = self.datatableWidget.rowCount()
                self.datatableWidget.insertRow(rowPosition)
                for column, value in enumerate(row):
                    self.datatableWidget.setItem(rowPosition, column, QtWidgets.QTableWidgetItem(value))
    





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())