def text2time(timestamp):
    timestamp = timestamp[:-1]
    time_split = timestamp.split('m ')
    time_converted = float(time_split[0]) + (float(time_split[-1]) / 60)
    return round(time_converted, 2)


def categorize_kda(x):
    if 0 <= x < 1:
        x = 0
    elif 1 <= x < 2:
        x = 1
    elif 2 <= x < 3:
        x = 2
    elif x >= 3:
        x = 3
    return x





