Tworzenie środowiska:

Polecenia:
python -m venv nazwa  alternatywnie python -m venv nazwa /scieżka do wirtualne środowiska(projektu)/
nazwa\Scripts\activate
pip install pyside6

Pozostałe rzadkie 
pip install sqlite # nie trzeba instalować bo jest w standardzie




Dodatkowe: 
pyside6-uic mainwindow.ui > ui_mainwindow.py




Struktura katalogów projektu:
nazwa_projektu/
|
|--main.py       # Plik uruchmieniowy
|--database/     # Baza danych 
|  '-- base.db
|--queries/      # zapytania SQL 
|--ui/ 	         # Qt Designer 
|--resources/    # Zasoby ikony, obrazy loga
|--widget/       # Własne widgety - opcjonalne 
|--models/       # Model danych 
|--controllers/  # Kontrolery do zarządzania logiką 
|--views/        # widoki wygenerowane z ui. polecenie 
|--styles        # style zapisane w json 
|--logs/         # logi 
|--documentation # Dokumentacja

być może wszystko poza main wrzucić w folder src



1. Własna belka górna:
 - z przyciskami (z czcionki)
 - drag drop ( mimalize maxymalize)
 - drag drop z opcją snap windows 
 - doble click maxymalize
 - na górnym pasku opcja setting => prawy panel 
2. Okno powinno przy maksymalizacji nie zakrywać paska start
3. cieniowanie okna 
4. zaokrąglone krawędzie 
5. Przeźroczystość okna w opcjach setting => suwak 
6. W setting wybór koloru okna


