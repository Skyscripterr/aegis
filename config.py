import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")

WAYPOINTS_FILE = os.path.join(DATA_DIR, "waypoints.csv")
GEOFENCE_FILE = os.path.join(DATA_DIR, "geofence.json")
MISSION_LOG_FILE = os.path.join(LOG_DIR, "mission.log")
MISSION_HISTORY_FILE = os.path.join(LOG_DIR, "mission_history.csv")

# Visualization settings
VISUALIZE = True