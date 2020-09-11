from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt

class QTextEditOverload(QTextEdit):

    focusOutEventSignal = pyqtSignal()
    enter_pressed = pyqtSignal()


    def __init__(self, *__args):
        super().__init__(*__args)


    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.focusOutEventSignal.emit()

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if self.hasFocus():
            if event.key() == Qt.Key_Return:
                self.enter_pressed.emit()
