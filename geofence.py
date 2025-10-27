def point_in_polygon(point, polygon):
    x, y = point
    inside = False

    # Ray casting algorithm (beginner version)
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        if (y1 > y) != (y2 > y):
            x_cross = (x2 - x1) * (y - y1) / (y2 - y1) + x1
            if x < x_cross:
                inside = not inside

    return "Violation" if inside else "Safe"


def check_path(waypoints, polygon):
    results = []
    for point in waypoints:
        results.append((point, point_in_polygon(point, polygon)))
    return results
