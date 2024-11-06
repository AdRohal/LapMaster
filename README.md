# F1 Race Strategy Simulator **LapMaster**

A Python application that compares telemetry data between two Formula 1 drivers. This simulator provides a graphical analysis of speed, throttle, and braking during a race session.

## Features

- **Telemetry Comparison**: Compare speed, throttle, and brake data between two drivers.
- **Circuit Selection**: Choose circuits from the 2024 Formula 1 season.
- **Driver Selection**: Select two drivers for telemetry analysis.
- **Graphical Interface**: Plot telemetry data using Matplotlib.

### Requirements

- **Python 3.6+**
- **Libraries**:
  - `fastf1` (For accessing F1 telemetry data)
  - `matplotlib` (For plotting telemetry data)
  - `PyQt5` (For GUI)
  - `logging` (For logging telemetry loading processes)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AdRohal/LapMaster.git
   cd LapMaster
   ```

2. **Install Required Libraries** 
   ```bash
   pip install fastf1 matplotlib PyQt5
   ```
