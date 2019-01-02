import csv
from datetime import datetime
from matplotlib import pyplot as plt

#filename = "chapter_16/sitka_weather_07-2014.csv"
#filename = "chapter_16/sitka_weather_2014.csv"
filenames = ["chapter_16/death_valley_2014.csv", "chapter_16/sitka_weather_2014.csv"]

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))

for filename in filenames:
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)  # next() returns the next line

        for index, column_header in enumerate(header_row):  # enumerate() returns an index and value from header_row
            print(index, column_header)

        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")

                high = int(row[1])
                low = int(row[3])

            except ValueError:  # this try catch cathes any missing data from the set
                print(current_date, "missing data")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)



    plt.plot(dates, highs, c="red")
    plt.plot(dates, lows, c="blue")
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)  # alpha = 0 means completely transparent

    # Format plot
    #plt.title("Daily High Temperatures, July 2014", fontsize=24)
    plt.title("Daily High and Low Temperatures, 2014", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()