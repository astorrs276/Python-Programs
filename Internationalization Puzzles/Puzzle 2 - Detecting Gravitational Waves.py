timestamps = dict()

with open("Internationalization Puzzles/data/test.txt") as file:
    for line in file:
        stripped_line = line.strip()
        broken1 = stripped_line.split("T")
        date = broken1[0]
        if "-" in broken1[1]:
            broken2 = broken1[1].split("-")
            time = broken2[0]
            change = broken2[1]

            new_hour = (int(time[0:2]) - int(change[0:2]) + 24) % 24
            if new_hour < 10:
                new_time = "0" + str(new_hour) + ":"
            else:
                new_time = str(new_hour) + ":"

            new_minutes = (int(time[3:5]) - int(change[3:5]) + 59) % 60 + 1
            if new_minutes < 10:
                new_time += "0" + str(new_minutes) + ":" + time[6:8]
            else:
                new_time += str(new_minutes) + ":" + time[6:8]

            new_timestamp = date + "T" + new_time + "+00:00"
            if new_timestamp not in timestamps:
                timestamps[new_timestamp] = 0
            timestamps[new_timestamp] += 1
        else:
            broken2 = broken1[1].split("+")
            time = broken2[0]
            change = broken2[1]

            new_hour = (int(time[0:2]) + int(change[0:2])) % 24
            if new_hour < 10:
                new_time = "0" + str(new_hour) + ":"
            else:
                new_time = str(new_hour) + ":"

            new_minutes = (int(time[3:5]) + int(change[3:5]) - 1) % 60 + 1
            if new_minutes < 10:
                new_time += "0" + str(new_minutes) + ":" + time[6:8]
            else:
                new_time += str(new_minutes) + ":" + time[6:8]

            new_timestamp = date + "T" + new_time + "+00:00"
            if new_timestamp not in timestamps:
                timestamps[new_timestamp] = 0
            timestamps[new_timestamp] += 1

max = 0
maxKey = ""
for key in timestamps:
    if timestamps[key] > max:
        max = timestamps[key]
        maxKey = key

print(timestamps)
print(maxKey, max)