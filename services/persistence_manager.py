import csv
import os
from config import MISSION_HISTORY_FILE, LOG_DIR

os.makedirs(LOG_DIR, exist_ok=True)

def save_mission_history(results):
    fieldnames = ["point_x", "point_y", "status"]

    file_exists = os.path.isfile(MISSION_HISTORY_FILE)

    with open(MISSION_HISTORY_FILE, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        for entry in results:
            x, y = entry["point"]
            writer.writerow({"point_x": x, "point_y": y, "status": entry["status"]})