from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAction

class QTableWidgetOverload(QTableWidget):
    """
        overload of QTableWidget mouse events so we can handle deleting rows from the results
    """
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

        # create context menu
        self.popMenu = QMenu(self)
        self.reject_action = QAction('reject', self)
        self.move_to_top_action = QAction('move to top', self)
        self.copy_all_action = QAction('copy all', self)
        self.copy_selection_action = QAction('copy selection', self)
        self.popMenu.addAction(self.reject_action)
        self.popMenu.addAction(self.move_to_top_action )
        self.popMenu.addAction(self.copy_all_action )
        self.popMenu.addAction(self.copy_selection_action )
        # self.popMenu.addAction(QAction('test1', self))
        # self.popMenu.addSeparator()
        # self.popMenu.addAction(QAction('test2', self))

    def on_context_menu(self, point):
        # show context menu
        self.popMenu.exec_(self.mapToGlobal(point))


    # def mouseReleaseEvent(self, event):
    #     super().mouseReleaseEvent(event)
    #     if event.button() == Qt.LeftButton: #Release event only if done with left button, you can remove if necessary
    #         print("left  mouseReleaseEvent!")

    def mousePressEvent(self, event):
        super().mouseReleaseEvent(event)
        if event.button() == Qt.RightButton:  # Release event only if done with left button, you can remove if necessary
            print("right mousePressEvent!")

            # #Your code should go here
            # indexSelection = []
            #
            # for item in self.selectedIndexes():
            #     indexSelection.append( str(item.row())+ "-" + str(item.column()) )
            #
            # print indexSelection
