color: str = "unknown color signal"

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Start/Slow down")
    case "green":
        print("Go")
    case _:
        print("Unknown color signal")