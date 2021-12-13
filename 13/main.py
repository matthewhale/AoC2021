import csv
import copy
import numpy
counts = 0
x = 0
y = 0
with open('input1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        if int(line[0]) > x:
            x = int(copy.copy(line[0]))
        if int(line[1]) > y:
            y = int(copy.copy(line[0]))
    print("x", x)
    print("y", y)
paper = numpy.zeros([x+1,y+1],int)
print(paper)
with open('input1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        paper[int(line[0]),int(line[1])] = 1
paper2 = numpy.zeros([655+1,y+1],int)
for idx,x1 in enumerate(paper):
    for idy,y1 in enumerate(x1):
        if y1 == 1:
            if idx > 655:
                print(idx)
                paper2[655+(655-idx),idy] = 1
            else:
                paper2[idx,idy] = 1
            print("Found1")
            print(idx, idy, y1)

count = 0
for x1 in paper2:
    for y1 in x1:
        count += y1
print("count", count)
exit()
