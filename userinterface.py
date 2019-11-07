# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userinterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(363, 374)
        MainWindow.setMinimumSize(QtCore.QSize(150, 200))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_go_back = QtWidgets.QPushButton(self.centralwidget)
        self.pb_go_back.setGeometry(QtCore.QRect(80, 60, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.pb_go_back.setFont(font)
        self.pb_go_back.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pb_go_back.setMouseTracking(False)
        self.pb_go_back.setStyleSheet("#pb_go_back {\n"
"background: gray;\n"
"border: 5px rgb(0, 170, 255);\n"
"border-radius: 12px;\n"
"background:lightgray;\n"
"}")
        self.pb_go_back.setObjectName("pb_go_back")
        self.pb_sync_time = QtWidgets.QPushButton(self.centralwidget)
        self.pb_sync_time.setGeometry(QtCore.QRect(80, 170, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pb_sync_time.setFont(font)
        self.pb_sync_time.setStyleSheet("#pb_sync_time {\n"
"background: gray;\n"
"border: 5px rgb(0, 170, 255);\n"
"border-radius: 12px;\n"
"background:mediumseagreen;\n"
"}")
        self.pb_sync_time.setObjectName("pb_sync_time")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 331))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(17, 328, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 363, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_go_back.setToolTip(_translate("MainWindow", "<div>\n"
"    <style scoped>\n"
"\n"
"        .button-success,\n"
" {\n"
"            color: white;\n"
"            border-radius: 4px;\n"
"            text-shadow: 0 1px 1px rgba(0, 0, 0, 0.2);\n"
"        }\n"
"\n"
"        .button-success {\n"
"            background: rgb(28, 184, 65); /* this is a green */\n"
"        }\n"
"\n"
"\n"
"    </style>\n"
"\n"
"    <button class=\"button-success pure-button\">Success Button</button>\n"
"</div>"))
        self.pb_go_back.setText(_translate("MainWindow", "Go back to 2005"))
        self.pb_sync_time.setText(_translate("MainWindow", "Sync Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

