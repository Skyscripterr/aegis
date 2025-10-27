import matplotlib.pyplot as plt

def plot_mission(waypoints, polygon, results):
    # Draw geofence
    px, py = zip(*polygon)
    plt.plot(px + (px[0],), py + (py[0],), "r-")

    # Draw waypoints
    wx, wy = zip(*waypoints)
    plt.plot(wx, wy, "bo-")

    # Mark violations
    for (x, y), status in results:
        if status == "Violation":
            plt.plot(x, y, "ro")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Mission with Geofence")
    plt.show()
