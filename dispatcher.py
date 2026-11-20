from typing import Dict, List, Optional


def add_waypoint(drone_id: str, point: Optional[str], route: List[str] = []) -> List[str]:
    if point is not None:
        route.append(f"{drone_id}:{point}")
    return route


def select_drone_mode(battery: int, payload_kg: float, is_raining: bool, emergency: bool) -> str:
    if emergency:
        return "LAND_IMMEDIATELY"
    if battery < 15:
        if payload_kg > 2.0:
            return "DROP_CARGO_AND_RETURN"
        else:
            return "RETURN_TO_BASE"
    if is_raining:
        if payload_kg > 3.0:
            return "HOLD_POSITION"
        return "ECO_FLIGHT"
    if payload_kg > 5.0:
        return "HEAVY_LIFT"
    return "STANDARD"