from PyQt5 import QtCore, QtWidgets

class Ui_SearchHouse(object):
    def setupUi(self, SearchHouse):
        SearchHouse.setObjectName("SearchHouse")
        SearchHouse.resize(664, 408)
        SearchHouse.setMaximumSize(QtCore.QSize(664, 408))
        self.verticalLayoutWidget = QtWidgets.QWidget(SearchHouse)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 621, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.infoLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.infoLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout.addWidget(self.infoLabel)
        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(SearchHouse)
        QtCore.QMetaObject.connectSlotsByName(SearchHouse)

    def retranslateUi(self, SearchHouse):
        _translate = QtCore.QCoreApplication.translate
        SearchHouse.setWindowTitle(_translate("SearchHouse", "Saha Housings - Search for Houses"))
        self.infoLabel.setText(_translate("SearchHouse", "Houses"))