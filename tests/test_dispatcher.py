from dispatcher import add_waypoint, select_drone_mode


def test_drone_routes_do_not_mix():
    route_alpha = add_waypoint("DRONE-A", "Sector-1")
    route_beta = add_waypoint("DRONE-B", None)
    assert route_alpha == ["DRONE-A:Sector-1"]
    assert route_beta == []


def test_drone_modes():
    assert select_drone_mode(10, 3.5, False, False) == "DROP_CARGO_AND_RETURN"
    assert select_drone_mode(80, 1.0, True, False) == "ECO_FLIGHT"
