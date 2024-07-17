def traffic_signal(color):
    if color.lower() == 'red':
        return "RED - Stop"
    elif color.lower() == 'yellow':
        return "YELLOW - Stay"
    elif color.lower() == 'green':
        return "GREEN - Go"
    else:
        return "Invalid color"