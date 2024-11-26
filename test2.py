    
import sys
from PySide6.QtWidgets import QApplication
from app.controllers.test  import TestController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestController()  # Logowanie z efektami
    window.show()
    sys.exit(app.exec())
