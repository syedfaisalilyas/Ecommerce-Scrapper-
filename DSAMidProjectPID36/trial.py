import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import functionCall as sf
import pandas as pd


class Mainwindow(QMainWindow):
    def __init__(self):

        super(Mainwindow, self).__init__()
        self.resize(903, 582)  # Corrected line
        loadUi("trial.ui", self)
        # self.sortButton.clicked.connect(self.SortButtonClicked())

        self.load_DataFromFile()
        # Connect the combo box to a function when the selection changes
        # self.sortingMenu.currentIndexChanged.connect(self.combo_box_changed)
        # Connect the push button to a function
        self.sortButton.clicked.connect(self.sort_button_click)

    def sort_button_click(self):

        selected_item = self.sortingMenu.currentText()
        print(f"Selected item: {selected_item}")
        selected_column = self.columnBox.currentText()
        print(f"Selected item: {selected_column}")
        selected_order = self.sortingType.currentText()
        print(selected_order)
        n, p, d, r, re, dp, de, po = self.getDataFromTable()
        time = 0
        result = []

        if selected_column == "Name":
            result, time = sf.SortingAlgorithmFunction_Call(n, selected_order, selected_item)
            self.populate_table(result, p, d, r, re, dp, de, po)
        elif selected_column == "Price":
            result, time = sf.SortingAlgorithmFunction_Call(p, selected_order, selected_item)
            self.populate_table(n, result, d, r, re, dp, de, po)
        elif selected_column == "Description":
            result, time = sf.SortingAlgorithmFunction_Call(d, selected_order, selected_item)
            self.populate_table(n, p, result, r, re, dp, de, po)
        elif selected_column == "Ratings":
            result, time = sf.SortingAlgorithmFunction_Call(r, selected_order, selected_item)
            self.populate_table(n, p, d, result, re, dp, de, po)
        elif selected_column == "NoOfReviews":
            result, time = sf.SortingAlgorithmFunction_Call(re, selected_order, selected_item)
            self.populate_table(n, p, d, r, result, dp, de, po)
        elif selected_column == "DiscountedPrice":
            result, time = sf.SortingAlgorithmFunction_Call(dp, selected_order, selected_item)
            self.populate_table(n, p, d, r, re, result, de, po)
        elif selected_column == "Delivery":
            result, time = sf.SortingAlgorithmFunction_Call(de, selected_order, selected_item)
            self.populate_table(n, p, d, r, re, dp, result, po)
        elif selected_column == "PercentageOff":
            result, time = sf.SortingAlgorithmFunction_Call(po, selected_order, selected_item)
            self.populate_table(n, p, d, r, re, dp, de, result)

        roundedtime=round(time,4)
        self.timeLable.setText(str(roundedtime)+"seconds")
        for i in range(len(result)):
            print(result[i])
        print(time)

    def load_DataFromFile(self):
        with open("C:\\DSA\\Scraping Mid Project\\UI Implementation With Single level and Multiple Level Sorting\\sample.csv", 'r', encoding='iso-8859-1',
                  errors='replace') as fileInput:
            tableRows = 0
            self.data = list(csv.reader(fileInput))
            self.tableWidget.setRowCount(len(self.data))
            for row in self.data:
                self.tableWidget.setItem(
                    tableRows, 0, QtWidgets.QTableWidgetItem((row[0])))
                self.tableWidget.setItem(
                    tableRows, 1, QtWidgets.QTableWidgetItem((row[1])))
                self.tableWidget.setItem(
                    tableRows, 2, QtWidgets.QTableWidgetItem((row[2])))
                self.tableWidget.setItem(
                    tableRows, 3, QtWidgets.QTableWidgetItem((row[3])))
                self.tableWidget.setItem(
                    tableRows, 4, QtWidgets.QTableWidgetItem((row[4])))

                self.tableWidget.setItem(
                    tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
                self.tableWidget.setItem(
                    tableRows, 6, QtWidgets.QTableWidgetItem((row[6])))
                self.tableWidget.setItem(
                    tableRows, 7, QtWidgets.QTableWidgetItem((row[7])))

                tableRows += 1
   

    def populate_table(self, Name, Price, Description, Ratings, NoOfReviews, DiscountedPrice, Delivery, perOff):
        # Clear the existing items in the tableWidget (optional)
        self.tableWidget.clearContents()

        # Assuming len(Name) is the number of rows
        num_rows = len(Name)
        self.tableWidget.setRowCount(num_rows)

        for row in range(num_rows):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(Name[row])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(Price[row])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(Description[row])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(Ratings[row])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(NoOfReviews[row])))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(DiscountedPrice[row])))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(Delivery[row])))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(perOff[row])))

    def getDataFromTable(self):
        Names = []
        Price = []
        Description = []
        Rating = []
        NoOfReview = []
        DiscountedPrice = []
        Delivery = []
        perOff = []
        for row in self.data:
            Names.append(row[0])
            Price.append(row[1])
            Description.append(row[2])
            Rating.append(row[3])
            NoOfReview.append(row[4])
            DiscountedPrice.append(row[5])
            Delivery.append(row[6])
            perOff.append(row[7])
        return Names, Price, Description, Rating, NoOfReview, DiscountedPrice, Delivery, perOff

        # Now, you have separate lists for each column of data


app = QApplication(sys.argv)
window = Mainwindow()
window.show()
sys.exit(app.exec_())
