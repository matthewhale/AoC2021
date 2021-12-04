# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

import csv
aim = 0
depth = 0
distance = 0
with open('C:\\temp\\sub.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] == 'forward':
            distance = distance + int(row[1])
            depth = depth + (int(row[1]) * aim)
        elif row[0] == 'down':
            aim = aim + int(row[1])
        else:
            aim = aim - int(row[1])
final = distance * depth
print(final)
