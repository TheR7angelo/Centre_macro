import os
import datetime
import re
import shutil
import sys

from PySide6.QtCore import QObject, Signal, QRunnable

class WorkerSignals(QObject):
    start = Signal(bool)
    progress = Signal(int)
    erreur = Signal(bool)


class Worker(QRunnable):
    """
    Worker thread
    Inherits from QRunnable to handle worker thread setup, signals
    and wrap-up.
    """

    signals = WorkerSignals()

    def __init__(self, fonction, files, path):
        super(Worker, self).__init__()

        self.fonction = fonction
        self.files = files
        self.path = path

    def run(self):
        try:

            pass

        except Exception as error:
            error = f"Ligne {sys.exc_info()[-1].tb_lineno} {error}"
            print(error)

            date = datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')
            file = os.path.basename(__file__).replace('.py', '')
            directory = fr"log/crash/{self.fonction}/"

            os.makedirs(directory, exist_ok=True)
            with open(f'{directory}{file}_{date}.txt', 'w') as crash_report:
                crash_report.write(str(error))
            os.startfile(os.path.abspath(f'{directory}{file}_{date}.txt'))

        self.signals.start.emit(False)
