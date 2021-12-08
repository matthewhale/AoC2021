import csv
counts = 0
with open('input.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        for i in range(10,14):
            if (len(line[i]) == 2) or (len(line[i]) == 3) or (len(line[i]) == 4) or (len(line[i]) == 7):
                counts += 1
print("Number of 1, 4, 7, 8's: ", counts)