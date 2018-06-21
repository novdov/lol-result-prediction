def text2time(timestamp):
    timestamp = timestamp[:-1]
    time_split = timestamp.split('m ')
    time_converted = float(time_split[0]) + (float(time_split[-1]) / 60)
    return round(time_converted, 2)

