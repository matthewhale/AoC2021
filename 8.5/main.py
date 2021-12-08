import csv
import copy
from itertools import permutations

newnum = 0
preparray = ["","","","","","","","","",""]
counts = 0
with open('input.csv', 'r') as csvfile:
#with open('testdata.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        decoder = ["", "", "", "", "", "", ""]
        decoder2 = ["a", "b", "c", "d", "e", "f", "g"]
        print("line ", line)
        for i in range(0,10):
        #   print("line[i] ", line[i], " ", i, " len ", len(line[i]))
        #    print("preparray ", preparray)
            if len(line[i]) == 2:
                preparray[1] = copy.deepcopy(line[i])
        #        print("here1")
            elif len(line[i]) == 3:
                preparray[7] = copy.deepcopy(line[i])
        #        print("here2")
            elif len(line[i]) == 4:
                preparray[4] = copy.deepcopy(line[i])
        #        print("here3")
            elif len(line[i]) == 7:
                preparray[8] = copy.deepcopy(line[i])
        #        print("here4")

        finda = copy.deepcopy(preparray[7])
        #print("finda ", finda)
        for c in preparray[1]:
            finda = finda.replace(c,"")
        #print("finda ", finda)
        decoder[0] = copy.deepcopy(finda)
        #print("decoders ", decoder)
        #print("preparrays ", preparray)
        for i in range(0,10):
            if len(line[i]) == 6:
        #        print("line[i] 6: ", line[i], " ", preparray[1])
                for i3 in preparray[1]:
        #            print("i3 ", i3)
                    if line[i].find(i3) == -1:
        #                print("I GOT HERE")
        #                print("decoder ", decoder)
                        preparray[6] = copy.deepcopy(line[i])
                        temper = copy.deepcopy(preparray[1])
                        decoder[5] = copy.deepcopy(temper.replace(i3,""))
                        decoder[2] = copy.deepcopy(i3)
        #                print("decoder ", decoder)
        for i in range (0,10):
            if len(line[i]) == 6:
                for i2 in preparray[4]:
                    temper = copy.deepcopy(preparray[4])
                    #print("temper ",temper, " ", decoder[2], " ", decoder[5])
                    temper = temper.replace(decoder[2],"")
                    temper = temper.replace(decoder[5],"")
                    #print("temper ",temper, " ", decoder[2], " ", decoder[5])
                    for i3 in temper:
        #                print("line ", line[i], " i3 ", i3, " temper ", temper)
                        if line[i].find(i3) == -1:
        #                    print("decoder ", decoder)
                            decoder[3] = copy.deepcopy(i3)
                            decoder[1] = copy.deepcopy(temper.replace(i3,""))
                            preparray[0] = copy.deepcopy(line[i])
        #                    print("decoder ", decoder)
        for i in range(0, 10):
            if len(line[i]) == 6:
                if line[i] == preparray[0]:
                    i5 = 0
                elif line[i] == preparray[6]:
                    i5 = 0
                else:
                    preparray[9] = copy.deepcopy(line[i])
        #print("preparray ", preparray)
        #print("decoder ", decoder)
        #print("decoder2 ", decoder2)
        #print(decoder[0])
        #print("decoder2 ", decoder2)
        #print("line ", line)
        decoder2.remove(decoder[0])
        decoder2.remove(decoder[1])
        decoder2.remove(decoder[2])
        decoder2.remove(decoder[3])
        decoder2.remove(decoder[5])
        tempy = 0
        threefive = ["",""]
        #print("THREEFIVE1 ", threefive, " decoder2 ", decoder2)
        for i in range(0, 10):
            if len(line[i]) == 5:
                for i2 in decoder2:
                    if line[i].find(i2) == -1:
        #                print("THREEFIVE ", threefive)
                        threefive[tempy] = copy.deepcopy(line[i])
                        decoder[4] = copy.deepcopy(i2)
                        tempy += 1
        #                print("THREEFIVE2 ", threefive)
        for i in range (0, 10):
            if len(line[i]) == 5:
        #            print("finding i2 ", i2, " line[i] ", line[i])
                    if line[i] not in threefive:
                        preparray[2] = copy.deepcopy(line[i])
                    #if line[i] == i2:
                    #    print("I FOUND MATCH ")
                    #    print("finding i2 ", i2, " line[i] ", line[i])
                    #else:
                    #    preparray[2] = copy.deepcopy(line[i])
        decoder2.remove(decoder[4])
        decoder[6] = copy.deepcopy(decoder2[0])
        tempy = 0
        print(threefive, " ", decoder)
        for i in threefive:
#            for i2 in i:
            if decoder[2] in i:
                print("FOUND 3 ", i)
                preparray[3] = copy.deepcopy(i)
                threefive2 = copy.deepcopy(threefive)
                threefive2.remove(i)
                #if i2 == decoder[2]:
                #    preparray[5] = copy.deepcopy(i)
                #else:
                #    preparray[3] = copy.deepcopy(i)
        print("threefive2 ", threefive2)
        preparray[5] = copy.deepcopy(threefive2[0])

        #print("decoder ", decoder)
        #print("preparray ", preparray)
        #number = str(preparray.index(line[10])) + str(preparray.index(line[11])) + str(preparray.index(line[12])) + str(preparray.index(line[13]))
        #print("IM HERE")
        #print(line[10])
        number = ""
        for i5 in range(10,14):
            perms = set(["".join(p) for p in permutations(line[i5])])
            print(perms)
            print(preparray)
            for permitem in perms:
                if permitem in preparray:
                    number = number + str(preparray.index(permitem))

        #print(preparray.index(perms))
        print(number)
        newnum += int(number)

print("Final Value: ", newnum)