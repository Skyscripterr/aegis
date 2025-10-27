from mission import load_mission
from geofence import check_path
from visualize import plot_mission
from logger import get_logger


log = get_logger("main")
log.info("🚀 Mission started.")
# ... your existing code ...
log.info("✅ Mission completed successfully.")

def main():
    # Load mission waypoints
    waypoints = load_mission()

    # Simple square geofence (example)
    geofence_polygon = [(0,0), (0,10), (10,10), (10,0)]

    # Check each waypoint
    results = check_path(waypoints, geofence_polygon)

    # Print results
    for point, status in results:
        print("Point", point, "is", status)

    # Show visualization
    plot_mission(waypoints, geofence_polygon, results)

if __name__ == "__main__":
    main()