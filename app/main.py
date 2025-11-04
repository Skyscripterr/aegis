
from utils import load_waypoints, load_geofence
from services.geofence_checker import check_path
from services.alert_manager import trigger_alert
from services.persistence_manager import save_mission_history
from services.visualize import visualize_live
from config import WAYPOINTS_FILE, GEOFENCE_FILE, VISUALIZE
from logger import logger

def main():
    logger.info("🚀 Aegis Mission Started")

    polygon = load_geofence(GEOFENCE_FILE)
    waypoints = load_waypoints(WAYPOINTS_FILE)

    results = []
    for point in waypoints:
        status = check_path([point], polygon)[0]["status"]
        trigger_alert([{"point": point, "status": status}])
        results.append((point, status))

    visualize_live(polygon, results, delay=0.5)

if __name__ == "__main__":
    main()