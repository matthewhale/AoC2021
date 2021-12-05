import copy
import csv
import numpy

board = numpy.zeros((1000, 1000), dtype=int)
with open('input.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        x1 = int(line[0])
        y1 = int(line[1])
        x2 = int(line[2])
        y2 = int(line[3])
        print("line ", line)
        if x1 == x2 and y1 == y2:
            board[x1][y1] += 1
        else:
            if x1 == x2:
                if y1 >= y2:
                    for y in range(y2, y1+1):
                        board[x1][y] += 1
                else:
                    for y in range (y1, y2+1):
                        board[x1][y] += 1
            elif y1 == y2:
                if x1 >= x2:
                    for x in range (x2, x1+1):
                        board[x][y1] += 1
                else:
                    for x in range (x1, x2+1):
                        board[x][y1] += 1
            else:
                if x1 > x2:
                    xinc = copy.deepcopy(x1)
                    if y1 > y2:
                        print("GOTHERE")
                        if (y1 - y2) == (x1 - x2):
                            print("Equal ", line)
                        else:
                            print("ERROR NOT EQUAL ", line)
                        print("5x1 x2 y1 y2 xinc", x1, " ", x2, " ", y1, " ", y2, " ", xinc)
                        for y in range(y1, y2-1):
                            board[xinc][y] += 1
                            xinc -= 1
                            print("1x1 x2 y1 y2 xinc y ", x1, " ", x2, " ", y1, " ", y2, " ", xinc, " ", y)
                    else:
                        if (y2 - y1) == (x1 - x2):
                            print("Equal ", line)
                        else:
                            print("ERROR NOT EQUAL ", line)
                        for y in range(y1, y2+1):
                            board[xinc][y] += 1
                            xinc -= 1
                            #print("2x1 x2 y1 y2 xinc y ", x1, " ", x2, " ", y1, " ", y2, " ", xinc, " ", y)
                elif x2 > x1:
                    xinc = copy.deepcopy(x1)
                    if y1 > y2:
                        if (y1 - y2) == (x2 - x1):
                            print("Equal ", line)
                        else:
                            print("ERROR NOT EQUAL ", line)
                        for y in range(y1, y2-1):
                            board[xinc][y] += 1
                            xinc += 1
                            #print("3x1 x2 y1 y2 xinc y ", x1, " ", x2, " ", y1, " ", y2, " ", xinc, " ", y)
                    else:
                        if (y2 - y1) == (x2 - x1):
                            print("Equal ", line)
                        else:
                            print("ERROR NOT EQUAL ", line)
                        for y in range(y1, y2+1):
                            board[xinc][y] += 1
                            xinc += 1
                            #print("4x1 x2 y1 y2 xinc y ", x1, " ", x2, " ", y1, " ", y2, " ", xinc, " ", y)
                else:
                    print("ERROR ", line)


    cnt = 0
    for x in range (0, 1000):
        for y in range (0, 1000):
           if board[x][y] >= 2:
               cnt += 1
    print("Dangerous Areas: ", cnt)