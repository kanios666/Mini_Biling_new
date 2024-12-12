from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from qframelesswindow import TitleBar

class CustomTitleBar(TitleBar):
    """ Custom title bar """

    def __init__(self, parent):
        super().__init__(parent)

        # create a new button dynamically
        self.newBtn = QPushButton("New", self)

        # add the new button to the title bar layout
        self.layout().insertWidget(1, self.newBtn)

    def on_newBtn_clicked(self):
        print("New button clicked")

    def set_button_visible(self, button, visible):
        if visible:
            button.show()
        else:
            button.hide()

    def set_minimize_button_visible(self, visible):
        self.set_button_visible(self.minBtn, visible)

    def set_maximize_button_visible(self, visible):
        self.set_button_visible(self.maxBtn, visible)

    def set_close_button_visible(self, visible):
        self.set_button_visible(self.closeBtn, visible)

    def set_new_button_visible(self, visible):
        self.set_button_visible(self.newBtn, visible)
