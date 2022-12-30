from PyQt5 import QtCore, QtWidgets

class Ui_CreateHousing(object):
    def setupUi(self, CreatHousing):
        CreatHousing.setObjectName("CreatHousing")
        CreatHousing.resize(390, 460)
        CreatHousing.setMinimumSize(QtCore.QSize(390, 460))
        CreatHousing.setMaximumSize(QtCore.QSize(390, 460))
        self.verticalLayoutWidget = QtWidgets.QWidget(CreatHousing)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 60, 281, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nameLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        self.housingNameTextEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.housingNameTextEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.housingNameTextEdit.setObjectName("housingNameTextEdit")
        self.verticalLayout.addWidget(self.housingNameTextEdit)
        self.adminUsernameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.adminUsernameLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.adminUsernameLabel.setObjectName("adminUsernameLabel")
        self.verticalLayout.addWidget(self.adminUsernameLabel)
        self.adminUsernameTextEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.adminUsernameTextEdit.setMaximumSize(QtCore.QSize(16777212, 30))
        self.adminUsernameTextEdit.setObjectName("adminUsernameTextEdit")
        self.verticalLayout.addWidget(self.adminUsernameTextEdit)
        self.adminPasswordLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.adminPasswordLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.adminPasswordLabel.setObjectName("adminPasswordLabel")
        self.verticalLayout.addWidget(self.adminPasswordLabel)
        self.adminPasswordTextEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.adminPasswordTextEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.adminPasswordTextEdit.setObjectName("adminPasswordTextEdit")
        self.verticalLayout.addWidget(self.adminPasswordTextEdit)
        self.adminNameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.adminNameLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.adminNameLabel.setObjectName("adminNameLabel")
        self.verticalLayout.addWidget(self.adminNameLabel)
        self.adminNameTextEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.adminNameTextEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.adminNameTextEdit.setObjectName("adminNameTextEdit")
        self.verticalLayout.addWidget(self.adminNameTextEdit)
        self.createHousingButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.createHousingButton.setObjectName("createHousingButton")
        self.verticalLayout.addWidget(self.createHousingButton)
        self.crLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.crLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.crLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.crLabel.setObjectName("crLabel")
        self.verticalLayout.addWidget(self.crLabel)

        self.retranslateUi(CreatHousing)
        QtCore.QMetaObject.connectSlotsByName(CreatHousing)

    def retranslateUi(self, CreatHousing):
        _translate = QtCore.QCoreApplication.translate
        CreatHousing.setWindowTitle(_translate("CreatHousing", "Saha Housings - Create Housing"))
        self.nameLabel.setText(_translate("CreatHousing", "Name"))
        self.adminUsernameLabel.setText(_translate("CreatHousing", "Admin Username"))
        self.adminPasswordLabel.setText(_translate("CreatHousing", "Admin Password"))
        self.adminNameLabel.setText(_translate("CreatHousing", "name"))
        self.createHousingButton.setText(_translate("CreatHousing", "Create "))
        self.crLabel.setText(_translate("CreatHousing", "Saha Housings"))