import csv

filename = "E:\\PycharmProjects\\data_visulization\\Downloading-Data-master\\sitka_weather_07-2014.csv"

with open(filename) as f:
    #create a CSV reader object
    reader = csv.reader(f)

    #store the head row
    head_row = next(reader)

    # reader object continues from where it left off in the CSV file and automatically
    # return each line following its current position
    for rows in reader:
        print(rows)
