# M11 — Geofencing & NFZ Enforcer (Core)

**One-line:** Simple geofence checker for UAV waypoints (ray-casting).

## What this is
A beginner-friendly minimal project that:
- Loads waypoints and a polygon geofence,
- Checks each waypoint with a point-in-polygon algorithm,
- Visualizes the polygon and results,
- Logs mission events to `logs/mission.log`.

## Files
- `main.py` — entry point
- `geofence.py` — point-in-polygon algorithm
- `mission.py` — waypoints loader / runner
- `visualize.py` — matplotlib visualization
- `utils.py`, `config.py`, `logger.py` — helpers
- `data/` — example input files (geofence.json, waypoints.csv)
- `logs/` — runtime logs

## Quick start
```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
# .\venv\Scripts\activate       # Windows PowerShell

pip install -r requirements.txt  # if you have this
python main.py
