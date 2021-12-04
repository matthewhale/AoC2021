import numpy
import csv
import copy
import sys

boards = 0
with open('boards.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    linenum = 0
    inc = 0
    for csvline in csvreader:
        linenum += 1
        if linenum == 6:
            linenum = 0
            boards += 1
csvfile.close()
print(boards)
board = numpy.zeros((boards + 1, 5, 5), dtype=int)
playboard = copy.deepcopy(board)
with open('boards.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    linenum = 0
    inc = 0
    for csvline in csvreader:
        if linenum < 5:
            for i in range(0, 5):
                #print("csvline ", csvline[i], " inc ", inc, " linenum ", linenum)
                board[inc][linenum][i] = copy.deepcopy(csvline[i])
        linenum += 1
        if linenum == 6:
            linenum = 0
            inc += 1
            # boards += 1
    print(board)
    print(playboard)
totfound = 0
boardnumbers = []
boardnumbers.extend(range(100))
print("boardnumbers ", boardnumbers)
with open('numbers.csv', 'r') as inputnumbers:
    inputreader = csv.reader(inputnumbers)
    for inputline in inputreader:
        print("hi ", len(inputline))
        print("hi2 ", inputline[0])
        print("hi3 ", inputline[len(inputline) - 1])
        maxinput = len(inputline) - 1
        print(maxinput)
        for i in range(0, maxinput):
            print("i input", i, " ", inputline[i])
            for z in range(0, boards + 1):
                for x in range(0, 5):
                    for y in range(0, 5):
                        # print("x y z i", x, " ", y, " ", z, " ", i, boards)
                        # print("Board ", board[z][x][y])
                        if board[z][x][y] == int(inputline[i]):
                            # print("FOUND ONE")
                            # print("x y z i board inputline", x, " ", y, " ", z, " ", i, " ", board[z][x][y], " ",inputline[i])
                            totfound += 1
                            playboard[z][x][y] = 1;
                            countnumx = 0
                            incy = 0
                            for x2 in range(0, 5):
                                countnumy = 0
                                for y2 in range(0, 5):
                                    countnumx = 0
                                    for x3 in range(0, 5):
                                        if playboard[z][x3][y2] == 1:
                                            countnumx += 1
                                            if countnumx == 5:
                                                print("FOUND WINNING BOARD ", z)
                                                print(board[z])
                                                print(playboard[z])
                                                notfoundsum = 0
                                                for xfinal in range(0, 5):
                                                    for yfinal in range(0, 5):
                                                        if (playboard[z][xfinal][yfinal]) == 0:
                                                            notfoundsum = notfoundsum + int(board[z][xfinal][yfinal])
                                                print("Final Answer ", (notfoundsum * int(inputline[i])))
                                                if z in boardnumbers:
                                                    boardnumbers.remove(z)
                                                print("boardnumbers ", boardnumbers)
                                                print(int(z), " ", len(boardnumbers), " ", inputline[i])
                                                if (len(boardnumbers)) == 0:
                                                    notfoundsum = 0
                                                    print("FINAL BOARD ", boardnumbers[0])
                                                    print(board[z])
                                                    print(playboard[z])
                                                    for xfinal in range(0, 5):
                                                        for yfinal in range(0, 5):
                                                            if (playboard[boardnumbers[0]][xfinal][yfinal]) == 0:
                                                                notfoundsum = notfoundsum + int(board[z][xfinal][yfinal])
                                                                print(notfoundsum, " ", int(board[z][xfinal][yfinal]))
                                                    print("Final Answer ", (notfoundsum * int(inputline[i])))
                                                    exit()
                                    if playboard[z][x2][y2] == 1:
                                        countnumy += 1
                                        if countnumy == 5:
                                            print("FOUND WINNING BOARD ", z)
                                            print(board[z])
                                            print(playboard[z])
                                            notfoundsum = 0
                                            for xfinal in range(0, 5):
                                                for yfinal in range(0, 5):
                                                    if (playboard[z][xfinal][yfinal]) == 0:
                                                        print(notfoundsum, " ", inputline[i])
                                                        notfoundsum = notfoundsum + int(board[z][xfinal][yfinal])
                                            print("Final Answer ", (notfoundsum * int(inputline[i])))
                                            if z in boardnumbers:
                                                boardnumbers.remove(z)
                                            print("boardnumbers ", boardnumbers)
                                            print(int(z), " ", len(boardnumbers), " ", inputline[i])
                                            if (len(boardnumbers)) == 0:
                                                notfoundsum = 0
                                                print("FINAL BOARD ", z)
                                                print(board[z])
                                                print(playboard[z])
                                                for xfinal in range(0, 5):
                                                    for yfinal in range(0, 5):
                                                        if (playboard[z][xfinal][yfinal]) == 0:
                                                            notfoundsum = notfoundsum + int(board[z][xfinal][yfinal])
                                                            print(notfoundsum, " ", int(board[z][xfinal][yfinal]))
                                                print("Final Answer ", (notfoundsum * int(inputline[i])))
                                                exit()