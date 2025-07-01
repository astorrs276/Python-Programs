timestamps = dict()

with open("Internationalization Puzzles/data/puzzle2.txt") as file:
    for line in file:
        month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        stripped_line = line.strip()
        broken = stripped_line.split("T")
        date = broken[0]
        time = broken[1]
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
        hour = int(time[0:2])
        min = int(time[3:5])
        sec = int(time[6:8])
        change_hour = int(time[9:11])
        change_min = int(time[12:14])
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            month_days[2] = 29
        if "-" in time:
            min += change_min
            hour += change_hour
            if min >= 60:
                min -= 60
                hour += 1
            if hour >= 24:
                hour -= 24
                day += 1
            if day > month_days[month]:
                day -= month_days[month]
                month += 1
            if month > 12:
                month -= 12
                year += 1
        elif "+" in time:
            min -= change_min
            hour -= change_hour
            if min < 0:
                min += 60
                hour -= 1
            if hour < 0:
                hour += 24
                day -= 1
            if day < 0:
                day += month_days[month]
                month -= 1
            if month <= 0:
                month += 12
                year -= 1
        info = [year, month, day, hour, min, sec]
        str_info = []
        for item in info:
            str_info.append(str(item) if item >= 10 else "0" + str(item))
        final = str_info[0] + "-" + str_info[1] + "-" + str_info[2] + "T" + str_info[3] + ":" + str_info[4] + ":" + str_info[5] + "+00:00"
        if final not in timestamps:
            timestamps[final] = 0
        timestamps[final] += 1

max_count = 0
most_frequent = ""
for key in timestamps:
    if timestamps[key] > max_count:
        max_count = timestamps[key]
        most_frequent = key
print(most_frequent)