import sys
import logging
import os
import fastf1
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QComboBox, QVBoxLayout, QPushButton, QLabel, QWidget, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal

# Set up logging
logging.basicConfig(level=logging.DEBUG)

class LoadTelemetryThread(QThread):
    result_signal = pyqtSignal(object, str)

    def __init__(self, circuit_name, driver_id):
        super().__init__()
        self.circuit_name = circuit_name
        self.driver_id = driver_id

    def run(self):
        try:
            cache_directory = 'f1_cache'
            if not os.path.exists(cache_directory):
                os.makedirs(cache_directory)
            fastf1.Cache.enable_cache(cache_directory)

            session = fastf1.get_session(2024, self.circuit_name, 'R')  # The season year
            session.load()

            driver_laps = session.laps.pick_drivers(self.driver_id.upper())
            if not driver_laps.empty:
                fastest_lap = driver_laps.pick_fastest()
                telemetry = fastest_lap.get_telemetry()
                self.result_signal.emit(telemetry, self.driver_id)
            else:
                self.result_signal.emit(None, self.driver_id)
        except Exception as e:
            logging.error(f"Error loading telemetry data for driver {self.driver_id}: {e}")
            self.result_signal.emit(None, self.driver_id)


class F1Simulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("F1 Race Strategy Simulator")
        self.setGeometry(0, 0, 1000, 800)
        self.init_ui()
        self.load_data()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.circuit_dropdown = QComboBox()
        layout.addWidget(QLabel("Select Circuit"))
        layout.addWidget(self.circuit_dropdown)

        self.driver1_dropdown = QComboBox()
        layout.addWidget(QLabel("Select Driver 1"))
        layout.addWidget(self.driver1_dropdown)

        self.driver2_dropdown = QComboBox()
        layout.addWidget(QLabel("Select Driver 2"))
        layout.addWidget(self.driver2_dropdown)

        self.compare_button = QPushButton("Compare Telemetry")
        self.compare_button.clicked.connect(self.compare_telemetry)
        layout.addWidget(self.compare_button)

        self.figure, self.axs = plt.subplots(5, 1, figsize=(10, 10))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_data(self):
        season_year = 2024  # The season year
        self.load_circuits(season_year)
        self.load_drivers(season_year)

    def load_circuits(self, season_year):
        circuits = fastf1.get_event_schedule(season_year)
        for _, event in circuits.iterrows():
            self.circuit_dropdown.addItem(event['EventName'], event['EventName'])

    def load_drivers(self, season_year):
        session = fastf1.get_session(season_year, 'Bahrain', 'R')  # Use any race to get driver list
        session.load()
        drivers = session.laps['Driver'].unique()
        self.driver1_dropdown.addItem("None", None)
        self.driver2_dropdown.addItem("None", None)
        for driver in drivers:
            self.driver1_dropdown.addItem(driver, driver)
            self.driver2_dropdown.addItem(driver, driver)

    def compare_telemetry(self):
        circuit_name = self.circuit_dropdown.currentText()
        driver1_id = self.driver1_dropdown.currentData()
        driver2_id = self.driver2_dropdown.currentData()

        for ax in self.axs:
            ax.clear()

        self.canvas.draw()

        if driver1_id:
            self.load_telemetry_thread1 = LoadTelemetryThread(circuit_name, driver1_id)
            self.load_telemetry_thread1.result_signal.connect(self.plot_telemetry)
            self.load_telemetry_thread1.start()

        if driver2_id:
            self.load_telemetry_thread2 = LoadTelemetryThread(circuit_name, driver2_id)
            self.load_telemetry_thread2.result_signal.connect(self.plot_telemetry)
            self.load_telemetry_thread2.start()

    def plot_telemetry(self, telemetry, driver_id):
        if telemetry is not None:
            color = 'blue' if driver_id == self.driver1_dropdown.currentData() else 'orange'
            label = f"Driver {driver_id}"

            lap_time_seconds = telemetry['Distance']

            self.axs[0].plot(lap_time_seconds, telemetry['Speed'], color=color, label=f"{label} Speed (km/h)")
            self.axs[0].set_ylabel("Speed (km/h)")
            self.axs[0].legend(loc="upper right")
            self.axs[0].grid(True)

            self.axs[1].plot(lap_time_seconds, telemetry['nGear'], color=color, label=f"{label} Gear")
            self.axs[1].set_ylabel("Gear")
            self.axs[1].legend(loc="upper right")
            self.axs[1].grid(True)

            self.axs[2].plot(lap_time_seconds, telemetry['Throttle'], color=color, label=f"{label} Throttle (%)")
            self.axs[2].set_ylabel("Throttle (%)")
            self.axs[2].legend(loc="upper right")
            self.axs[2].grid(True)

            self.axs[3].plot(lap_time_seconds, telemetry['Brake'], color=color, label=f"{label} Brake (%)")
            self.axs[3].set_ylabel("Brake (%)")
            self.axs[3].legend(loc="upper right")
            self.axs[3].grid(True)

            self.axs[4].plot(lap_time_seconds, telemetry['DRS'], color=color, label=f"{label} DRS")
            self.axs[4].set_ylabel("DRS")
            self.axs[4].legend(loc="upper right")
            self.axs[4].grid(True)

            self.axs[4].set_xlabel("Lap Time (MM:SS)")
            self.axs[4].xaxis.set_major_formatter(
                ticker.FuncFormatter(lambda x, pos: f"{int(x // 60)}:{int(x % 60):02d}"))
            self.canvas.draw()
        else:
            logging.error(f"No telemetry data available for driver {driver_id}.")

    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = F1Simulator()

    window.setGeometry(
        (window.screen().availableGeometry().width() - window.width()) // 2,
        (window.screen().availableGeometry().height() - window.height()) // 2,
        window.width(),
        window.height()
    )

    window.showMaximized()

    sys.exit(app.exec_())