#AoC 2021 - Day 3, Part 2
import copy

with open('input.txt', 'r') as input:
    newreport = input.readlines()
    for position in range(0,12):
        print(newreport)
        totcount = 0
        counts = 0
        report = copy.copy(newreport)
        for line in report:
            totcount = totcount + 1
            liner = line.strip()
            if liner[position] == '1':
                counts = counts + 1
        print("totcount ", totcount)
        print("counts", counts)
        if counts >= (totcount / 2):
            print('1')
            indy = 0
            for line in report:
                liner = line.strip()
                print("liner " , liner, " linerpos ", liner[position], " pos ", position, " index ", indy)
                if liner[position] == '0':
                    print(newreport[indy])
                    print("indy ", indy)
                    del newreport[indy]
                    print(newreport)
                else:
                    indy = indy + 1
        else:
            print('0')
            indy = 0
            for line in report:
                liner = line.strip()
                if liner[position] == '1':
                    print(newreport[indy])
                    del newreport[indy]
                else:
                    indy = indy + 1
        print("indy: ", indy)
    oxygen = copy.copy(newreport)
    input.close()
    print("NEXT SECTION")
with open('input.txt', 'r') as input:
    newreport = input.readlines()
    for position in range(0,12):
        print(newreport)
        print("newreport len ", len(newreport))
        if (len(newreport) == 1):
            break
        totcount = 0
        counts = 0
        report = copy.copy(newreport)
        for line in report:
            totcount = totcount + 1
            liner = line.strip()
            if liner[position] == '1':
                counts = counts + 1
        print("totcount ", totcount)
        print("counts", counts)
        if counts >= (totcount / 2):
            print('0')
            indy = 0
            for line in report:
                liner = line.strip()
                print("liner " , liner, " linerpos ", liner[position], " pos ", position, " index ", indy)
                if liner[position] == '1':
                    print(newreport[indy])
                    print("indy ", indy)
                    del newreport[indy]
                    print(newreport)
                else:
                    indy = indy + 1
        else:
            print('1')
            indy = 0
            for line in report:
                liner = line.strip()
                if liner[position] == '0':
                    print(newreport[indy])
                    del newreport[indy]
                else:
                    indy = indy + 1
    print("oxygen ", int(oxygen[0].rstrip(),2))
    print("co2 ", int(newreport[0].rstrip(),2))
    print("combined in decimal: ", (int(oxygen[0].rstrip(),2) * int(newreport[0].rstrip(),2)))
    input.close()
