import csv
import copy
import numpy
import sys
numpy.set_printoptions(threshold=sys.maxsize)
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
#paper2 = numpy.zeros([655+1,y+1],int)
#for idx,x1 in enumerate(paper):
#    for idy,y1 in enumerate(x1):
#        if y1 == 1:
#            if idx > 655:
#                print(idx)
#                paper2[655+(655-idx),idy] = 1
#            else:
#                paper2[idx,idy] = 1
#            print("Found1")
#            print(idx, idy, y1)
paper2 = copy.copy(paper)
with open('foldinstructions.txt', "r") as folds:
    foldread = folds.readlines()
    for fold in foldread:
        folding = fold.split()
        if folding[2][0] == "x":
            print("FOUND X")
            newx = copy.copy(folding[2])
            newx = newx.replace("x=","")
            newx = int(newx)
            newpaper = copy.copy(paper2)
            y = len(newpaper[0])
            x = len(newpaper)
            paper2 = numpy.zeros([newx + 1, y + 1], int)
            for idx, x1 in enumerate(newpaper):
                for idy, y1 in enumerate(x1):
                    if y1 == 1:
                        if idx > newx:
                            print(idx)
                            paper2[newx + (newx - idx), idy] = 1
                        else:
                            paper2[idx, idy] = 1
        else:
            print("FOUND Y")
            newy = copy.copy(folding[2])
            newy = newy.replace("y=","")
            newy = int(newy)
            newpaper = copy.copy(paper2)
            y = len(newpaper[0])
            x = len(newpaper)
            paper2 = numpy.zeros([x+1,newy+1], int)
            for idx, x1 in enumerate(newpaper):
                for idy, y1 in enumerate(x1):
                    if y1 == 1:
                        if idy > newy:
                            #print(idy)
                            paper2[idx,newy + (newy - idy)] = 1
                        else:
                            paper2[idx,idy] = 1


print(folding[2][0])
count = 0
for x1 in paper2:
    for y1 in x1:
        count += y1
print("count", count)
#exit()

count = 0
for x1 in paper2:
    for y1 in x1:
        count += y1
print("count",count)

print("Answer?")
print(paper2)
print(paper2[1,0])