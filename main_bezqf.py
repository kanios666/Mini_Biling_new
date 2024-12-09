import sys
from PySide6.QtWidgets import QApplication
from app.controllers.main_controller import MainController

def main():
    app = QApplication(sys.argv)  # Inicjalizacja aplikacji
    window = MainController()  # Tworzenie okna głównego
    window.show()  # Wyświetlenie okna
    sys.exit(app.exec())  # Uruchomienie pętli zdarzeń

if __name__ == "__main__":
    main()
