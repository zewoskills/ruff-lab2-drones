def add_waypoint(
    drone_id: str, point: str | None, route: list[str] | None = None
) -> list[str]:
    if route is None:
        route = []
    if point is not None:
        route.append(f"{drone_id}:{point}")
    return route


def _select_normal_flight_mode(payload_kg: float, is_raining: bool) -> str:
    if is_raining:
        if payload_kg > 3.0:
            return "HOLD_POSITION"
        return "ECO_FLIGHT"
    if payload_kg > 5.0:
        return "HEAVY_LIFT"
    return "STANDARD"


def select_drone_mode(
    battery: int, payload_kg: float, is_raining: bool, emergency: bool
) -> str:
    if emergency:
        return "LAND_IMMEDIATELY"
    if battery < 15:
        if payload_kg > 2.0:
            return "DROP_CARGO_AND_RETURN"
        return "RETURN_TO_BASE"
    return _select_normal_flight_mode(payload_kg, is_raining)
