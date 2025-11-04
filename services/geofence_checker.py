from algorithms.point_in_polygon import point_in_polygon


def check_path(waypoints, polygon):
    results = []
    for point in waypoints:
        status = point_in_polygon(point, polygon)
        results.append({"point": point, "status": status})
    return results
