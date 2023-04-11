import os

def all_file_read():
    folder_path = "weatherfiles"
    files = os.listdir(folder_path)
    rows = []

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r") as f:
            contents = f.readlines()[1:-1]
            rows.extend(contents)

    return rows

file_values =all_file_read()

temps = []
dates = []
for row in file_values:
    row = row.strip()
    date, temp = row.split(",")[0:2]

    if temp:
        dates.append(date)
        temps.append(float(temp))

if temps:
    min_temp = min(temps)
    min_date = dates[temps.index(min_temp)]

    max_temp = max(temps)
    max_date = dates[temps.index(max_temp)]
    print("Minimum temperature:",min_temp,"/ date:",min_date)
    print("Maximum temperature:",max_temp,"/ date:",max_date)
else:
    print("No values found.")
