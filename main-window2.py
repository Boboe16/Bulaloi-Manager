# Form implementation generated from reading ui file 'main-window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 495)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("B-icon.png"), QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background: gray;")
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea_2.setEnabled(True)
        self.scrollArea_2.setGeometry(QtCore.QRect(50, 10, 641, 411))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setBold(False)
        self.scrollArea_2.setFont(font)
        self.scrollArea_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.scrollArea_2.setMouseTracking(False)
        self.scrollArea_2.setAutoFillBackground(False)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 622, 409))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_29 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_29.sizePolicy().hasHeightForWidth())
        self.checkBox_29.setSizePolicy(sizePolicy)
        self.checkBox_29.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_29.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_29.setText("")
        self.checkBox_29.setObjectName("checkBox_29")
        self.horizontalLayout_10.addWidget(self.checkBox_29)
        self.pushButton_31 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy)
        self.pushButton_31.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_31.setObjectName("pushButton_31")
        self.horizontalLayout_10.addWidget(self.pushButton_31)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.checkBox_30 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_30.sizePolicy().hasHeightForWidth())
        self.checkBox_30.setSizePolicy(sizePolicy)
        self.checkBox_30.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_30.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_30.setText("")
        self.checkBox_30.setObjectName("checkBox_30")
        self.horizontalLayout_11.addWidget(self.checkBox_30)
        self.pushButton_32 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy)
        self.pushButton_32.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_32.setObjectName("pushButton_32")
        self.horizontalLayout_11.addWidget(self.pushButton_32)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.checkBox_31 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_31.sizePolicy().hasHeightForWidth())
        self.checkBox_31.setSizePolicy(sizePolicy)
        self.checkBox_31.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_31.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_31.setText("")
        self.checkBox_31.setObjectName("checkBox_31")
        self.horizontalLayout_12.addWidget(self.checkBox_31)
        self.pushButton_33 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy)
        self.pushButton_33.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_33.setObjectName("pushButton_33")
        self.horizontalLayout_12.addWidget(self.pushButton_33)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.checkBox_28 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_28.sizePolicy().hasHeightForWidth())
        self.checkBox_28.setSizePolicy(sizePolicy)
        self.checkBox_28.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_28.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_28.setText("")
        self.checkBox_28.setObjectName("checkBox_28")
        self.horizontalLayout_9.addWidget(self.checkBox_28)
        self.pushButton_30 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy)
        self.pushButton_30.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_30.setObjectName("pushButton_30")
        self.horizontalLayout_9.addWidget(self.pushButton_30)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_27 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_27.sizePolicy().hasHeightForWidth())
        self.checkBox_27.setSizePolicy(sizePolicy)
        self.checkBox_27.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_27.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_27.setText("")
        self.checkBox_27.setObjectName("checkBox_27")
        self.horizontalLayout_8.addWidget(self.checkBox_27)
        self.pushButton_29 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy)
        self.pushButton_29.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout_8.addWidget(self.pushButton_29)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.checkBox_32 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_32.sizePolicy().hasHeightForWidth())
        self.checkBox_32.setSizePolicy(sizePolicy)
        self.checkBox_32.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_32.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_32.setText("")
        self.checkBox_32.setObjectName("checkBox_32")
        self.horizontalLayout_13.addWidget(self.checkBox_32)
        self.pushButton_34 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy)
        self.pushButton_34.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_34.setObjectName("pushButton_34")
        self.horizontalLayout_13.addWidget(self.pushButton_34)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_26 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_26.sizePolicy().hasHeightForWidth())
        self.checkBox_26.setSizePolicy(sizePolicy)
        self.checkBox_26.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_26.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_26.setText("")
        self.checkBox_26.setObjectName("checkBox_26")
        self.horizontalLayout_7.addWidget(self.checkBox_26)
        self.pushButton_28 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy)
        self.pushButton_28.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout_7.addWidget(self.pushButton_28)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_14.setSpacing(2)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.checkBox_33 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_33.sizePolicy().hasHeightForWidth())
        self.checkBox_33.setSizePolicy(sizePolicy)
        self.checkBox_33.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_33.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_33.setText("")
        self.checkBox_33.setObjectName("checkBox_33")
        self.horizontalLayout_14.addWidget(self.checkBox_33)
        self.pushButton_35 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy)
        self.pushButton_35.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_35.setObjectName("pushButton_35")
        self.horizontalLayout_14.addWidget(self.pushButton_35)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_16.setSpacing(2)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.checkBox_35 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_35.sizePolicy().hasHeightForWidth())
        self.checkBox_35.setSizePolicy(sizePolicy)
        self.checkBox_35.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_35.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_35.setText("")
        self.checkBox_35.setObjectName("checkBox_35")
        self.horizontalLayout_16.addWidget(self.checkBox_35)
        self.pushButton_37 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy)
        self.pushButton_37.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_37.setObjectName("pushButton_37")
        self.horizontalLayout_16.addWidget(self.pushButton_37)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_20.setSpacing(2)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.checkBox_39 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_39.sizePolicy().hasHeightForWidth())
        self.checkBox_39.setSizePolicy(sizePolicy)
        self.checkBox_39.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_39.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_39.setText("")
        self.checkBox_39.setObjectName("checkBox_39")
        self.horizontalLayout_20.addWidget(self.checkBox_39)
        self.pushButton_41 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy)
        self.pushButton_41.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_41.setObjectName("pushButton_41")
        self.horizontalLayout_20.addWidget(self.pushButton_41)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_15.setSpacing(2)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.checkBox_34 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_34.sizePolicy().hasHeightForWidth())
        self.checkBox_34.setSizePolicy(sizePolicy)
        self.checkBox_34.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_34.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_34.setText("")
        self.checkBox_34.setObjectName("checkBox_34")
        self.horizontalLayout_15.addWidget(self.checkBox_34)
        self.pushButton_36 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy)
        self.pushButton_36.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_36.setObjectName("pushButton_36")
        self.horizontalLayout_15.addWidget(self.pushButton_36)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_19.setSpacing(2)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.checkBox_38 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_38.sizePolicy().hasHeightForWidth())
        self.checkBox_38.setSizePolicy(sizePolicy)
        self.checkBox_38.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_38.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_38.setText("")
        self.checkBox_38.setObjectName("checkBox_38")
        self.horizontalLayout_19.addWidget(self.checkBox_38)
        self.pushButton_40 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_40.sizePolicy().hasHeightForWidth())
        self.pushButton_40.setSizePolicy(sizePolicy)
        self.pushButton_40.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_40.setObjectName("pushButton_40")
        self.horizontalLayout_19.addWidget(self.pushButton_40)
        self.verticalLayout_2.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_18.setSpacing(2)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.checkBox_37 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_37.sizePolicy().hasHeightForWidth())
        self.checkBox_37.setSizePolicy(sizePolicy)
        self.checkBox_37.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_37.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_37.setText("")
        self.checkBox_37.setObjectName("checkBox_37")
        self.horizontalLayout_18.addWidget(self.checkBox_37)
        self.pushButton_39 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_39.sizePolicy().hasHeightForWidth())
        self.pushButton_39.setSizePolicy(sizePolicy)
        self.pushButton_39.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_39.setObjectName("pushButton_39")
        self.horizontalLayout_18.addWidget(self.pushButton_39)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_17.setSpacing(2)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.checkBox_36 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_36.sizePolicy().hasHeightForWidth())
        self.checkBox_36.setSizePolicy(sizePolicy)
        self.checkBox_36.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_36.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_36.setText("")
        self.checkBox_36.setObjectName("checkBox_36")
        self.horizontalLayout_17.addWidget(self.checkBox_36)
        self.pushButton_38 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy)
        self.pushButton_38.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_38.setObjectName("pushButton_38")
        self.horizontalLayout_17.addWidget(self.pushButton_38)
        self.verticalLayout_2.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_25 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_25.sizePolicy().hasHeightForWidth())
        self.checkBox_25.setSizePolicy(sizePolicy)
        self.checkBox_25.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_25.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_25.setText("")
        self.checkBox_25.setObjectName("checkBox_25")
        self.horizontalLayout_6.addWidget(self.checkBox_25)
        self.pushButton_27 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy)
        self.pushButton_27.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_27.setObjectName("pushButton_27")
        self.horizontalLayout_6.addWidget(self.pushButton_27)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_21 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_21.sizePolicy().hasHeightForWidth())
        self.checkBox_21.setSizePolicy(sizePolicy)
        self.checkBox_21.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_21.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_21.setText("")
        self.checkBox_21.setObjectName("checkBox_21")
        self.horizontalLayout_2.addWidget(self.checkBox_21)
        self.pushButton_23 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout_2.addWidget(self.pushButton_23)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_22 = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_22.sizePolicy().hasHeightForWidth())
        self.checkBox_22.setSizePolicy(sizePolicy)
        self.checkBox_22.setMinimumSize(QtCore.QSize(13, 0))
        self.checkBox_22.setStyleSheet("width: 11px;\n"
"padding-right: -100px;\n"
"background-color: red;\n"
"")
        self.checkBox_22.setText("")
        self.checkBox_22.setObjectName("checkBox_22")
        self.horizontalLayout_3.addWidget(self.checkBox_22)
        self.pushButton_24 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)
        self.pushButton_24.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_3.addWidget(self.pushButton_24)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 430, 641, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.deleteButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bulaloi Manager"))
        self.pushButton_31.setText(_translate("MainWindow", "First App Name "))
        self.pushButton_32.setText(_translate("MainWindow", "App Name"))
        self.pushButton_33.setText(_translate("MainWindow", "App Name"))
        self.pushButton_30.setText(_translate("MainWindow", "App Name"))
        self.pushButton_29.setText(_translate("MainWindow", "App Name"))
        self.pushButton_34.setText(_translate("MainWindow", "App Name"))
        self.pushButton_28.setText(_translate("MainWindow", "App Name"))
        self.pushButton_35.setText(_translate("MainWindow", "App Name"))
        self.pushButton_37.setText(_translate("MainWindow", "App Name"))
        self.pushButton_41.setText(_translate("MainWindow", "App Name"))
        self.pushButton_36.setText(_translate("MainWindow", "App Name"))
        self.pushButton_40.setText(_translate("MainWindow", "App Name"))
        self.pushButton_39.setText(_translate("MainWindow", "App Name"))
        self.pushButton_38.setText(_translate("MainWindow", "App Name"))
        self.pushButton_27.setText(_translate("MainWindow", "App Name"))
        self.pushButton_23.setText(_translate("MainWindow", "App Name"))
        self.pushButton_24.setText(_translate("MainWindow", "Last App Name"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>sdfsdfsd</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_2.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())