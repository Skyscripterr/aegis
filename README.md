# 🛰️ Aegis – UAV Geofencing & No-Fly Zone Enforcer

**Aegis** is a real-time UAV geofencing simulator that monitors drone flight paths and detects intrusions into restricted or no-fly zones.  
It visualizes live trajectories, flags violations, and logs alerts — forming the foundation for UAV mission safety systems.

---

## 🚀 Features
- 🗺️ Define and visualize geofences (No-Fly Zones)
- ✈️ Simulate UAV flight paths in real time
- ⚠️ Detect and alert on geofence violations
- 📊 Live plotting with Matplotlib
- 🧩 Modular, testable Python architecture
- 🔧 Extensible design — ready for ROS2 or MAVLink integration

---

## 📂 Project Structure
app/
└── main.py → Entry point for simulation
services/
├── geofence_checker.py → Core logic for zone detection
├── alert_manager.py → Handles alerts/logs
├── persistence_manager.py
└── visualizer.py → Real-time plotting
algorithms/
└── point_in_polygon.py → UAV trajectory generator
tests/
└── test_geofence.py → Unit tests
demo/
├── aegis_run.gif → Sample demo animation
└── sample_output.txt


## 🧠 Tech Stack
- **Language:** Python  
- **Libraries:** `matplotlib`, `shapely`, `pytest`  
- **Environment:** Cross-platform (Windows/Linux/macOS)  

---

## ▶️ How to Run
```bash ```
# 1. Clone this repository
git clone https://github.com/<your-username>/Aegis-UAV-Geofencing.git
cd Aegis-UAV-Geofencing

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run simulation
python -m app.main
🎥 Demo

## 🧩 Future Enhancements
- 🛰️ ROS2 / MAVLink integration for live UAV data
- 🌍 Import geofences from KML/GeoJSON
- 🖥️ Web dashboard (Plotly/Streamlit)
- 🧮 3D flight visualization

## 📈 Keywords
UAV • Drone Safety • Geofencing • Simulation • Matplotlib • Python • Autonomous Systems

👨‍💻 Author
Minaha Nafeesa
Aerospace Engineer | UAV Systems Developer
🔗 LinkedIn • Portfolio

