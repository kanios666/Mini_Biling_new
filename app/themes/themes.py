import os

class Themes(object):
    def __init__(self, theme_name="default"):
        super(Themes, self).__init__()
        self.theme_name = theme_name

    @property
    def qss_path(self):
        app_path = os.path.abspath(os.getcwd())
        qss_file = f"gui/themes/{self.theme_name}.qss"
        return os.path.normpath(os.path.join(app_path, qss_file))

    def load_qss(self):
        with open(self.qss_path, "r", encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def get_available_themes():
        app_path = os.path.abspath(os.getcwd())
        themes_dir = os.path.join(app_path, "gui/themes")
        return [f.split(".")[0] for f in os.listdir(themes_dir) if f.endswith(".qss")]
