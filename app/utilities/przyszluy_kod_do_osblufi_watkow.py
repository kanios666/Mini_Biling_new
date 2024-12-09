import sys
import schedule
import time
import psutil
import os
from datetime import datetime, timedelta
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QProgressBar, QLabel, QMessageBox, QDateEdit, QComboBox, QHBoxLayout, QCalendarWidget
from PySide6.QtCore import QThread, Signal, Slot, Qt

class Worker(QThread):
    progress = Signal(int)
    started_at = Signal(str)
    finished_at = Signal(str)
    total_time = Signal(str)
    interrupted = Signal()
    paused = Signal()

    def __init__(self, task, priority, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task = task
        self.priority = priority
        self._is_interrupted = False
        self._is_paused = False

    def run(self):
        # Ustawienie priorytetu wątku
        p = psutil.Process(os.getpid())
        p.nice(self.priority)

        start_time = time.time()
        self.started_at.emit(time.strftime("%H:%M:%S", time.localtime(start_time)))

        for i in range(100):
            if self._is_interrupted:
                self.interrupted.emit()
                return
            while self._is_paused:
                time.sleep(1)
            self.sleep(1)  # Symulacja długotrwałego procesu
            self.progress.emit(i + 1)

        end_time = time.time()
        self.finished_at.emit(time.strftime("%H:%M:%S", time.localtime(end_time)))
        self.total_time.emit(f"{end_time - start_time:.2f} seconds")
        self.task()

    def interrupt(self):
        self._is_interrupted = True

    def pause(self):
        self._is_paused = True
        self.paused.emit()

    def resume(self):
        self._is_paused = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automatyzacja zadań")

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)

        self.start_time_label = QLabel("Start Time: N/A")
        self.end_time_label = QLabel("End Time: N/A")
        self.total_time_label = QLabel("Total Time: N/A")

        self.date_edit = QDateEdit(calendarPopup=True)
        self.date_edit.setDate(datetime.now())

        self.priority_combo = QComboBox()
        self.priority_combo.addItems(["Low", "Below Normal", "Normal", "Above Normal", "High", "Realtime"])

        self.button = QPushButton("Start")
        self.button.clicked.connect(self.start_tasks)

        self.interrupt_button = QPushButton("Interrupt Current Task")
        self.interrupt_button.clicked.connect(self.interrupt_task)
        self.interrupt_button.setEnabled(False)

        self.pause_button = QPushButton("Pause Current Task")
        self.pause_button.clicked.connect(self.pause_task)
        self.pause_button.setEnabled(False)

        self.resume_button = QPushButton("Resume Current Task")
        self.resume_button.clicked.connect(self.resume_task)
        self.resume_button.setEnabled(False)

        self.interrupt_all_button = QPushButton("Interrupt All Tasks")
        self.interrupt_all_button.clicked.connect(self.interrupt_all_tasks)
        self.interrupt_all_button.setEnabled(False)

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)

        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.start_time_label)
        layout.addWidget(self.end_time_label)
        layout.addWidget(self.total_time_label)

        date_layout = QHBoxLayout()
        date_layout.addWidget(QLabel("Select Date:"))
        date_layout.addWidget(self.date_edit)
        date_layout.addWidget(QLabel("Select Priority:"))
        date_layout.addWidget(self.priority_combo)
        layout.addLayout(date_layout)

        layout.addWidget(self.button)
        layout.addWidget(self.interrupt_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.resume_button)
        layout.addWidget(self.interrupt_all_button)
        layout.addWidget(self.calendar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.scheduled_tasks = []
        self.schedule_tasks()

    def schedule_tasks(self):
        # Przykładowe harmonogramy z przerwami
        self.add_schedule("18:00", "22:00", self.task1, psutil.IDLE_PRIORITY_CLASS)
        self.add_schedule("02:00", "06:30", self.task2, psutil.NORMAL_PRIORITY_CLASS)

        self.scheduler_thread = QThread()
        self.scheduler_thread.run = self.run_scheduler
        self.scheduler_thread.start()

    def add_schedule(self, start_time, end_time, task, priority):
        schedule.every().day.at(start_time).do(self.add_task_to_queue, task, priority)
        schedule.every().day.at(end_time).do(self.pause_task)

    def run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

    def add_task_to_queue(self, task, priority):
        current_time = datetime.now().time()
        end_time = datetime.strptime("22:00", "%H:%M").time()
        if current_time < end_time and (datetime.combine(datetime.today(), end_time) - datetime.combine(datetime.today(), current_time)).total_seconds() >= 2 * 3600:
            self.scheduled_tasks.append((task, priority))
            self.interrupt_all_button.setEnabled(True)
            if not hasattr(self, 'worker') or not self.worker.isRunning():
                self.start_next_task()

    def start_scheduled_task(self, task, priority):
        self.worker = Worker(task, priority)
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.started_at.connect(self.start_time_label.setText)
        self.worker.finished_at.connect(self.end_time_label.setText)
        self.worker.total_time.connect(self.total_time_label.setText)
        self.worker.interrupted.connect(self.on_task_interrupted)
        self.worker.paused.connect(self.on_task_paused)
        self.worker.finished.connect(self.on_task_finished)
        self.worker.start()
        self.interrupt_button.setEnabled(True)
        self.pause_button.setEnabled(True)

    def start_tasks(self):
        selected_date = self.date_edit.date().toPyDate()
        selected_priority = self.priority_combo.currentText()
        priority_map = {
            "Low": psutil.IDLE_PRIORITY_CLASS,
            "Below Normal": psutil.BELOW_NORMAL_PRIORITY_CLASS,
            "Normal": psutil.NORMAL_PRIORITY_CLASS,
            "Above Normal": psutil.ABOVE_NORMAL_PRIORITY_CLASS,
            "High": psutil.HIGH_PRIORITY_CLASS,
            "Realtime": psutil.REALTIME_PRIORITY_CLASS
        }
        priority = priority_map[selected_priority]
        self.add_task_to_queue(self.task1, priority)

    def start_next_task(self):
        if self.scheduled_tasks:
            next_task, priority = self.scheduled_tasks.pop(0)
            self.start_scheduled_task(next_task, priority)
        else:
            self.interrupt_all_button.setEnabled(False)

    def interrupt_task(self):
        if hasattr(self, 'worker') and self.worker.isRunning():
            self.worker.interrupt()
            self.interrupt_button.setEnabled(False)
            self.pause_button.setEnabled(False)
            self.resume_button.setEnabled(False)

    def pause_task(self):
        if hasattr(self, 'worker') and self.worker.isRunning():
            self.worker.pause()
            self.pause_button.setEnabled(False)
            self.resume_button.setEnabled(True)

    def resume_task(self):
        if hasattr(self, 'worker') and self.worker.isRunning():
            self.worker.resume()
            self.pause_button.setEnabled(True)
            self.resume_button.setEnabled(False)

    def interrupt_all_tasks(self):
        self.scheduled_tasks.clear()
        self.interrupt_all_button.setEnabled(False)
        self.interrupt_task()

    @Slot()
    def on_task_interrupted(self):
        self.progress_bar.setValue(0)
        self.start_time_label.setText("Start Time: N/A")
        self.end_time_label.setText("End Time: N/A")
        self.total_time_label.setText("Total Time: N/A")
        self.interrupt_button.setEnabled(False)
        self.pause_button.setEnabled(False)
        self.resume_button.setEnabled(False)
        self.show_message("Task Interrupted", "The current task has been interrupted.")

    @Slot()
    def on_task_paused(self):
        self.show_message("Task Paused", "The current task has been paused.")

    @Slot()
    def on_task_finished(self):
        self.show_message("Task Finished", "The current task has been completed.")
        self.start_next_task()

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

    def task1(self):
        print("Zadanie 1 zakończone")

    def task2(self):
        print("Zadanie 2 zakończone")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
