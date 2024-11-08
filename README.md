# F1 Race Strategy Simulator **LapMaster**

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

## Screenshots

### Main Window
<img src="image/Documentation/Screenshot 2024-11-08 041051.png" alt="Main Window"></img>
### Circuit Dropdown
<img src="image/Documentation/Screenshot 2024-11-08 041111.png" alt="Circuit Dropdown"></img>  
### Driver Dropdown
<img src="image/Documentation/Screenshot 2024-11-08 041120.png" alt="Driver Dropdown"></img>
### Telemetry Comparison
<img src="image/Documentation/Screenshot 2024-11-08 042242.png" alt="Telemetry Comparison"></img>
<img src="image/Documentation/Screenshot 2024-11-08 041553.png" alt="Telemetry Comparison"></img>
This project helps Formula 1 teams, analysts, and enthusiasts to visually compare and analyze the performance of different drivers on various circuits, providing insights into speed, gear usage, throttle, braking, and DRS activation.
