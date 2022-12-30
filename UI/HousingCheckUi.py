from PyQt5 import QtCore, QtWidgets


class Ui_HousingCheck(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(380, 220)
        Form.setMinimumSize(QtCore.QSize(380, 220))
        Form.setMaximumSize(QtCore.QSize(380, 220))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 50, 280, 110))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.createHousingButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.createHousingButton.setObjectName("createHousingButton")
        self.verticalLayout.addWidget(self.createHousingButton)
        self.signinHousingButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.signinHousingButton.setObjectName("signinHousingButton")
        self.verticalLayout.addWidget(self.signinHousingButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Saha Housings - Start"))
        self.createHousingButton.setText(_translate("Form", "Create Housing"))
        self.signinHousingButton.setText(_translate("Form", "Sign in to a housing"))
