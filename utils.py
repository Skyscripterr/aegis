# utils.py
import json
import csv
from typing import List, Tuple
from config import WAYPOINT_FILE, GEOFENCE_FILE

def load_geofence() -> List[Tuple[float, float]]:
    """Load polygon coordinates from JSON file."""
    with open(GEOFENCE_FILE, "r") as f:
        data = json.load(f)
    return data["geofence"]

def load_waypoints() -> List[Tuple[float, float]]:
    """Load waypoints from CSV file."""
    waypoints = []
    with open(WAYPOINT_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lat = float(row["latitude"])
            lon = float(row["longitude"])
            waypoints.append((lat, lon))
    return waypoints
