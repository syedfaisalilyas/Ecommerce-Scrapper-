import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import functionCall as sf
class Mainwindow(QMainWindow):
    def __init__(self):

        super(Mainwindow,self).__init__()
        self.resize(903, 582)  # Corrected line
        loadUi("multiLevel.ui",self)
        # self.sortButton.clicked.connect(self.SortButtonClicked())

        self.load_DataFromFile()
        self.sortButton.clicked.connect(self.sort_button_click)


    def sort_button_click(self):
        selected_item = self.sortingMenu.currentText()
        print(f"Selected item: {selected_item}")
        selectedOrder = self.sortingType.currentText()
        print(selectedOrder)
        n, p, d, r, re, dp, de, po = self.getDataFromTable()
        checkedBoxes = self.getCheckBoxes()
        print("Checked checkboxes:", checkedBoxes)
        time = 0
        for i in range(len(checkedBoxes)):
            if checkedBoxes[i] == "Name":
                n , time = sf.SortingAlgorithmFunction_Call(n, selectedOrder, selected_item)
                print(n)
            elif checkedBoxes[i] == "Price":
                p,time = sf.SortingAlgorithmFunction_Call(p, selectedOrder, selected_item)
                print(p)
            elif checkedBoxes[i] == "Description":
                d,time = sf.SortingAlgorithmFunction_Call(d, selectedOrder, selected_item)
                print(d)
            elif checkedBoxes[i] == "Ratings":
                r,time = sf.SortingAlgorithmFunction_Call(r, selectedOrder, selected_item)
                print(r)
            elif  checkedBoxes[i] == "NoOfReviews":
                re ,time= sf.SortingAlgorithmFunction_Call(re, selectedOrder, selected_item)
                print(re)
            elif  checkedBoxes[i] == "DiscountedPrice":
                dp,time = sf.SortingAlgorithmFunction_Call(dp, selectedOrder, selected_item)
                print(dp)
            elif  checkedBoxes[i] == "Delivery":
                de,time = sf.SortingAlgorithmFunction_Call(de, selectedOrder, selected_item)
                print(de)
            elif  checkedBoxes[i] == "PercentageOff":
                po,time = sf.SortingAlgorithmFunction_Call(po, selectedOrder, selected_item)
                print(po)
            print(time)

        self.populate_table(n, p, d, r, re, dp, de, po)
        # self.label.setText(str(time))
        roundedtime = round(time, 4)
        self.label.setText(str(roundedtime) + "seconds")


    def getCheckBoxes(self):
        checked_checkboxes = []

        if self.Name.isChecked():
            checked_checkboxes.append("Name")
        if self.Price.isChecked():
            checked_checkboxes.append("Price")
        if self.Description.isChecked():
            checked_checkboxes.append("Description")
        if self.Ratings.isChecked():
            checked_checkboxes.append("Ratings")
        if self.NoOfReviews.isChecked():
            checked_checkboxes.append("NoOfReviews")
        if self.DiscountedPrice.isChecked():
            checked_checkboxes.append("DiscountedPrice")
        if self.Delivery.isChecked():
            checked_checkboxes.append("Delivery")
        if self.PercentageOff.isChecked():
            checked_checkboxes.append("PercentageOff")
        # print("Checked checkboxes:", checked_checkboxes)
        return checked_checkboxes


    def populate_table(self, Name, Price, Description, Ratings, NoOfReviews, DiscountedPrice, Delivery,perOff):
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

    def load_DataFromFile(self):
        with open("C:\\DSA\\Scraping Mid Project\\UI Implementation With Single level and Multiple Level Sorting\\sample.csv", 'r', encoding='iso-8859-1', errors='replace') as fileInput:
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


app = QApplication(sys.argv)
window = Mainwindow()
window.show()
sys.exit(app.exec_())