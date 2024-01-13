import sys

from PyQt5.QtGui import QColor
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import multiSearchingAlgo as se
import singleLevelSearchingAlgo as sa


class Mainwindow(QMainWindow):
    def __init__(self):

        super(Mainwindow, self).__init__()
        self.resize(903, 582)  # Corrected line
        loadUi("multiLevelSearching.ui", self)
        # self.sortButton.clicked.connect(self.SortButtonClicked())

        self.load_DataFromFile()
        self.searchButton.clicked.connect(self.search_button_click)

    def search_button_click(self):
        self.clearHighlightedRows()
        selected_algo = self.algo.currentText()
        print(f"Selected item: {selected_algo}")
        selectedType = self.type.currentText()
        print(selectedType)
        selectedOrder = self.order.currentText()
        print(selectedOrder)

        searchQuery = self.query.text()
        print(searchQuery)
        n, p, d, r, re, dp, de, po = self.getDataFromTable()
        checkedBoxes = self.getCheckBoxes()
        lists = []

        for i in range(len(checkedBoxes)):
            if checkedBoxes[i] == "Name":
                lists.append(n)
            elif checkedBoxes[i] == "Price":
                lists.append(p)
            elif checkedBoxes[i] == "Description":
                lists.append(d)
            elif checkedBoxes[i] == "Ratings":
                lists.append(r)
            elif checkedBoxes[i] == "NoOfReviews":
                lists.append(re)
            elif checkedBoxes[i] == "DiscountedPrice":
                lists.append(dp)
            elif checkedBoxes[i] == "Delivery":
                lists.append(de)
            elif checkedBoxes[i] == "PercentageOff":
                lists.append(po)

        searched = []
        mainList = []
        for i in range(len(lists)):
            if selectedType == "Contains":
                searched.append(sa.contains(lists[i], searchQuery))
            elif selectedType == "StartsWith":
                searched.append(sa.startsWith(lists[i], searchQuery))
            elif selectedType == "EndWith":
                searched.append(sa.endWith(lists[i], searchQuery))

        for i in range(len(searched)):
            mainList.append(self.getMatchingRows(lists[i], searched[i]))
        min_length = float('inf')
        min_length_list = None
        max_length_list = None
        max_length = 0
        min_length_index = None
        max_length_index = None
        other_lengths = []
        other_lists = []
        other_indices = []
        # Iterate through the sublists
        for index, sublist in enumerate(mainList):
            # Check the length of each sublist
            sublist_length = len(sublist)

            # If the length is smaller than the current minimum, update the minimum and the corresponding list
            if sublist_length < min_length:
                min_length = sublist_length
                min_length_list = sublist
                min_length_index = index
            if sublist_length > max_length:
                max_length = sublist_length
                max_length_list = sublist
                max_length_index = index
            if sublist_length != max_length or sublist_length != min_length:
                other_lengths.append(sublist_length)
                other_lists.append(sublist)
                other_indices.append(index)

        rowsToHighlight = []

        print("LENGTH OF MAIN LIST", len(mainList))
        if len(mainList) == 2:
            col0 = mainList[min_length_index]
            col1 = mainList[max_length_index]
            set1 = set(col0)
            set2 = set(col1)
            if selectedOrder == "AND":
                intersection = set1.intersection(set2)
                # Convert the result back to a list
                intersection_list = list(intersection)
                self.highlightRows(intersection_list)
            elif selectedOrder=="OR":
                union = set1.union(set2)
                unionList = list(union)
                self.highlightRows(unionList)
            else:
                negation_result=set1-set2
                negationList = list(negation_result)
                self.highlightRows(negationList)
        elif len(mainList) == 3:
            print(other_indices[0])
            print(max_length_index)
            print(min_length_index)
            col0 = mainList[min_length_index]
            col1 = mainList[max_length_index]
            col2 = mainList[other_indices[0]]
            set0 = set(col0)
            set1 = set(col1)
            set2 = set(col2)
            if selectedOrder == "AND":
                intersection = set0.intersection(set2, set1)
                # Convert the result back to a list
                intersection_list = list(intersection)
                self.highlightRows(intersection_list)
            elif selectedOrder=="OR":
                union = set0.union(set2, set1)
                unionList = list(union)
                self.highlightRows(unionList)
            else:
                negation_result = set0 - set1-set2
                negationList = list(negation_result)
                self.highlightRows(negationList)
        elif len(mainList) == 4:
            print(other_indices[0])
            print(other_indices[1])
            print(max_length_index)
            print(min_length_index)
            col0 = mainList[min_length_index]
            col1 = mainList[max_length_index]
            col2 = mainList[other_indices[0]]
            col3 = mainList[other_indices[1]]
            set0 = set(col0)
            set1 = set(col1)
            set2 = set(col2)
            set3 = set(col3)
            if selectedOrder == "AND":
                intersection = set0.intersection(set2, set1, set3)
                # Convert the result back to a list
                intersection_list = list(intersection)
                self.highlightRows(intersection_list)
            elif selectedOrder=="OR":
                union = set0.union(set2, set1, set3)
                unionList = list(union)
                self.highlightRows(unionList)
            else:
                negation_result = set0-set1 - set2-set3
                negationList = list(negation_result)
                self.highlightRows(negationList)
        elif len(mainList) == 5:
            print(other_indices[0])
            print(other_indices[1])
            print(max_length_index)
            print(min_length_index)
            col0 = mainList[min_length_index]
            col1 = mainList[max_length_index]
            col2 = mainList[other_indices[0]]
            col3 = mainList[other_indices[1]]
            col4 = mainList[other_indices[2]]
            set0 = set(col0)
            set1 = set(col1)
            set2 = set(col2)
            set3 = set(col3)
            set4 = set(col4)
            if selectedOrder == "AND":
                intersection = set0.intersection(set2, set1, set3, set4)
                # Convert the result back to a list
                intersection_list = list(intersection)
                self.highlightRows(intersection_list)
            elif selectedOrder == "OR":
                union = set0.union(set2, set1, set3, set4)
                unionList = list(union)
                self.highlightRows(unionList)
            else:
                negation_result = set0 - set1 - set2 - set3 - set4
                negationList = list(negation_result)
                self.highlightRows(negationList)
        elif len(mainList) == 6:
            print(max_length_index)
            print(min_length_index)
            col0 = mainList[min_length_index]
            col1 = mainList[max_length_index]
            col2 = mainList[other_indices[0]]
            col3 = mainList[other_indices[1]]
            col4 = mainList[other_indices[2]]
            col5 = mainList[other_indices[3]]
            set0 = set(col0)
            set1 = set(col1)
            set2 = set(col2)
            set3 = set(col3)
            set4 = set(col4)
            set5 = set(col5)
            if selectedOrder == "AND":
                intersection = set0.intersection(set2, set1, set3, set4)
                # Convert the result back to a list
                intersection_list = list(intersection)
                self.highlightRows(intersection_list)
            elif selectedOrder == "OR":
                union = set0.union(set2, set1, set3, set4, set5)
                unionList = list(union)
                self.highlightRows(unionList)
            else:
                negation_result = set0 - set1 - set2 - set3 - set4-set5
                negationList = list(negation_result)
                self.highlightRows(negationList)
        elif len(mainList) == 7:
            print(other_indices[0])
            print(other_indices[1])
            print(max_length_index)
            print(min_length_index)
            col0 = mainList[min_length_index]
            col1 = mainList[max_length_index]
            col2 = mainList[other_indices[0]]
            col3 = mainList[other_indices[1]]
            col4 = mainList[other_indices[2]]
            col5 = mainList[other_indices[3]]
            col6 = mainList[other_indices[4]]
            set0 = set(col0)
            set1 = set(col1)
            set2 = set(col2)
            set3 = set(col3)
            set4 = set(col4)
            set5 = set(col5)
            set6 = set(col6)

            if selectedOrder == "AND":
                intersection = set0.intersection(set2, set1, set3, set4,set5, set6)
                # Convert the result back to a list
                intersection_list = list(intersection)
                self.highlightRows(intersection_list)
            elif selectedOrder == "OR":
                union = set0.union(set2, set1, set3, set4, set5, set6)
                unionList = list(union)
                self.highlightRows(unionList)
            else:
                negation_result = set0 - set1 - set2 - set3 - set4-set5-set6
                negationList=list(negation_result)
                self.highlightRows(negationList)
        elif len(mainList) == 8:
            print(other_indices[0])
            print(other_indices[1])
            print(max_length_index)
            print(min_length_index)
            col0 = mainList[min_length_index]
            col1 = mainList[max_length_index]
            col2 = mainList[other_indices[0]]
            col3 = mainList[other_indices[1]]
            col4 = mainList[other_indices[2]]
            col5 = mainList[other_indices[3]]
            col6 = mainList[other_indices[4]]
            col7 = mainList[other_indices[5]]
            set0 = set(col0)
            set1 = set(col1)
            set2 = set(col2)
            set3 = set(col3)
            set4 = set(col4)
            set5 = set(col5)
            set6 = set(col6)
            set7 = set(col7)

            if selectedOrder == "AND":
                intersection = set0.intersection(set2, set1, set3, set4, set5, set6,set7)
                # Convert the result back to a list
                intersection_list = list(intersection)
                self.highlightRows(intersection_list)
            elif selectedOrder == "OR":
                union = set0.union(set2, set1, set3, set4, set5, set6,set7)
                unionList = list(union)
                self.highlightRows(unionList)
            else:
                negation_result = set0 - set1 - set2 - set3 - set4-set5-set6-set7
                negationList = list(negation_result)
                self.highlightRows(negationList)




    def getMatchingRows(self, listToSearch, searched):
        selected = []
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
                    item.setBackground(QColor(23, 107, 135))  # Reset background color to default

    def highlightRows(self, selected):

        for row in selected:
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                item.setBackground(QColor(255, 0, 0))  # Set the background color (here, it's red)

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


app = QApplication(sys.argv)
window = Mainwindow()
window.show()
sys.exit(app.exec_())
