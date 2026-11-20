import json


def write_flight_log(filename: str, events: list[dict]) -> None:
    f = open(filename, "w", encoding="utf-8")
    json.dump(events, f, ensure_ascii=False, indent=2)
    f.close()