def breakdown_time(seconds):
    if type(seconds) != int:
        return -1
    if seconds < 0:
        return -1
    if seconds == 0:
        return {}
    
    if seconds >= 0:
        time_units = {3600: 0, 60: 0, 1: 0}
        for unit in time_units:
            while seconds >= unit:
                time_units[unit] += 1
                seconds -= unit
        return {k: v for k, v in time_units.items() if v > 0}