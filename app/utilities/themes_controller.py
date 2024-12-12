import os

import os

class ThemeController:
    def __init__(self, ui, folder_path="app/themes", default_stylesheet=None):
        self.ui = ui
        self.folder_path = folder_path
        self.stylesheets = self.load_stylesheets_from_folder()

        # Sortuj nazwy stylów alfabetycznie
        sorted_stylesheet_names = sorted(self.stylesheets.keys())

        # Dodaj domyślny styl na początku listy
        if default_stylesheet in sorted_stylesheet_names:
            sorted_stylesheet_names.remove(default_stylesheet)
        sorted_stylesheet_names.insert(0, default_stylesheet)

        # Dodaj style do QComboBox w posortowanej kolejności
        for name in sorted_stylesheet_names:
            self.ui.cbx_themes.addItem(name)

        # Ustaw domyślny styl, jeśli jest podany
        if default_stylesheet and default_stylesheet in self.stylesheets:
            self.ui.cbx_themes.setCurrentIndex(0)
            self.apply_stylesheet(0)

        # Podłącz sygnał zmiany wyboru do funkcji zmieniającej styl
        self.ui.cbx_themes.currentIndexChanged.connect(self.apply_stylesheet)

    def load_stylesheets_from_folder(self):
        stylesheets = {}
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".qss"):
                file_path = os.path.join(self.folder_path, filename)
                with open(file_path, "r", encoding='utf-8') as file:
                    stylesheets[filename[:-4]] = file.read()
        return stylesheets

    def apply_stylesheet(self, index):
        stylesheet_name = self.ui.cbx_themes.itemText(index)
        stylesheet = self.stylesheets.get(stylesheet_name, "")
        self.ui.setStyleSheet(stylesheet)


