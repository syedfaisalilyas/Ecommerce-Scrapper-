import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import singleLevelSearchingAlgo as sa
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import functionCall as sf
import pandas as pd
from PyQt5.QtGui import QColor


class Mainwindow(QMainWindow):
    def __init__(self):

        super(Mainwindow, self).__init__()
        self.resize(903, 582)  # Corrected line
        loadUi("singleLevelSearching.ui", self)
        # self.sortButton.clicked.connect(self.SortButtonClicked())

        self.load_DataFromFile()
        # Connect the combo box to a function when the selection changes
        # self.sortingMenu.currentIndexChanged.connect(self.combo_box_changed)
        # Connect the push button to a function
        self.searchButton.clicked.connect(self.searchButtonClick)

    def searchButtonClick(self):
        self.clearHighlightedRows()
        selected_choice = self.choice.currentText()
        print(f"Selected item: {selected_choice}")
        selected_column = self.columnBox.currentText()
        print(f"Selected item: {selected_column}")
        searchQuery = self.query.text()
        print(f"Selected item: {searchQuery}")
        n, p, d, r, re, dp, de, po = self.getDataFromTable()
        listToSearch = []
        if selected_column == "Name":
            listToSearch = n
        elif selected_column == "Price":
            listToSearch = p
        elif selected_column == "Description":
            listToSearch = d
        elif selected_column == "Ratings":
            listToSearch = r
        elif selected_column == "NoOfReviews":
            listToSearch = re
        elif selected_column == "DiscountedPrice":
            listToSearch = dp
        elif selected_column == "Delivery":
            listToSearch = de
        elif selected_column == "PercentageOff":
            listToSearch = po

        searched = []

        if selected_choice == "Contains":
            searched = sa.contains(listToSearch, searchQuery)
        elif selected_choice == "StartsWith":
            searched = sa.startsWith(listToSearch, searchQuery)
        elif selected_choice == "EndWith":
            searched = sa.endWith(listToSearch,searchQuery )

        print(searched)
        selected=self.getMatchingRows(listToSearch,searched)

        self.highlightRows(selected)

    def getMatchingRows(self,listToSearch,searched):
        selected=[]
        for i in range(len(listToSearch)):
            # print(searched[i])
            for j in range(len(searched)):
                if searched[j] == listToSearch[i]:
                    selected.append(i)
        return selected

    def clearHighlightedRows(self):
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item.setBackground(QColor(255, 255, 255))  # Reset background color to default


    def highlightRows(self,selected):

        for row in selected:
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                item.setBackground(QColor(97,12,159))  # Set the background color (here, it's red)


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

    def load_Data(self):
        tableRows = 0
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
            # if int(row[5].split(":")[0]) >= int(24):
            #     row[5] = row[5][0:len(row[5])-1]
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
