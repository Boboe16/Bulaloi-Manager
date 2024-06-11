import json
import os

listOfFileNames = os.listdir(r'./Bulaloi-App-Development-Experiment\next-app\public\apps-games-data\apps')
dir = r'./Bulaloi-App-Development-Experiment\next-app\public\apps-games-data\apps/'
listOfDics = []

for fileName in listOfFileNames:
    with open(dir + fileName, 'r') as file:
        data = json.load(file)
        listOfDics.append(data)

print(listOfDics)

for dic in listOfDics:
    print(dic['appName'])
    
    # self.iterateAppsAndSetWindowTitle()

    # def iterateAppsAndSetWindowTitle(self):
    #         listOfFileNames = os.listdir(r'./Bulaloi-App-Development-Experiment\next-app\public\apps-games-data\apps')
    #         dir = r'./Bulaloi-App-Development-Experiment\next-app\public\apps-games-data\apps/'
    #         listOfDics = []

    #         for fileName in listOfFileNames:
    #             with open(dir + fileName, 'r') as file:
    #                 data = json.load(file)
    #                 listOfDics.append(data)
            
    #         for index, dic in enumerate(listOfDics):
    #             self.groupBox = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents_2)
    #             self.groupBox.setObjectName(f"groupBox_{index}")
    #             self.checkBox = QtWidgets.QCheckBox(parent=self.groupBox)
    #             self.checkBox.setGeometry(QtCore.QRect(10, 10, 16, 20))
    #             self.checkBox.setText("")
    #             self.checkBox.setObjectName(f"checkBox_{index}")
    #             self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
    #             self.pushButton.setGeometry(QtCore.QRect(30, 10, 81, 24))
    #             self.pushButton.setObjectName(f"pushButton_{index}")
    #             self.verticalLayout.addWidget(self.groupBox)
                
    #             _translate = QtCore.QCoreApplication.translate
    #             self.pushButton.setText(_translate("MainWindow", dic['appName']))
    #             MainWindow.setWindowTitle(_translate("MainWindow", "Bulaloi Manager"))
