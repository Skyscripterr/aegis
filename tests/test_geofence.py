from services.geofence_checker import check_path

def test_basic_geofence():
    polygon = [(0,0), (0,10), (10,10), (10,0)]
    waypoints = [(5,5), (12,8)]
    results = check_path(waypoints, polygon)
    assert results[0][1] == "Violation"
    assert results[1][1] == "Safe"
