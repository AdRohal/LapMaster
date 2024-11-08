# F1  **LapMaster**

LapMaster is a Python application designed to compare telemetry data between two Formula 1 drivers. This simulator provides a graphical analysis of speed, throttle, and braking during a race session, helping teams and enthusiasts to analyze and compare driver performance on various circuits.

## Features

- **Telemetry Comparison**: Compare speed, throttle, and brake data between two drivers.
- **Circuit Selection**: Choose circuits from the 2024 Formula 1 season.
- **Driver Selection**: Select two drivers for telemetry analysis.
- **Graphical Interface**: Plot telemetry data using Matplotlib.

## Requirements

- **Python 3.6+**
- **Libraries**:
  - `fastf1` (For accessing F1 telemetry data)
  - `matplotlib` (For plotting telemetry data)
  - `PyQt5` (For GUI)
  - `seaborn` (For color palettes)
  - `logging` (For logging telemetry loading processes)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AdRohal/LapMaster.git
   cd LapMaster
   ```

2. **Install Required Libraries** 
   ```bash
   pip install fastf1 matplotlib PyQt5 seaborn logging
   ```
   
## Usage

Run the `main.py` file to start the LapMaster application. Select the circuit and drivers to compare telemetry data.
   ```bash
   python main.py
   ```

This project helps Formula 1 teams or curious people, analysts, and enthusiasts to visually compare and analyze the performance of different drivers on various circuits, providing insights into speed, gear usage, throttle, braking, and DRS activation.
