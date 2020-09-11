# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_results_window(object):
    def setupUi(self, results_window):
        results_window.setObjectName("results_window")
        results_window.resize(474, 523)
        self.tableView = QtWidgets.QTableView(results_window)
        self.tableView.setGeometry(QtCore.QRect(10, 70, 451, 441))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(results_window)
        QtCore.QMetaObject.connectSlotsByName(results_window)

    def retranslateUi(self, results_window):
        _translate = QtCore.QCoreApplication.translate
        results_window.setWindowTitle(_translate("results_window", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    results_window = QtWidgets.QDialog()
    ui = Ui_results_window()
    ui.setupUi(results_window)
    results_window.show()
    sys.exit(app.exec_())
