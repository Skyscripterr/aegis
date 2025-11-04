import csv
import json
from typing import List, Tuple

def load_waypoints(file_path): 
    waypoints = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            waypoints.append((float(row[0]), float(row[1])))
    return waypoints

def load_geofence(file_path: str) -> List[Tuple[float, float]]:
    with open(file_path, "r") as f:
        data = json.load(f)
    return [tuple(coord) for coord in data["polygon"]]
