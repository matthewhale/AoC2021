import numpy
risk = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    reader = [""] * (len(lines))
    for idx2, line in enumerate(lines):
        if idx2 < 1:
            reader[idx2] = line.strip()
            print("idx2", idx2)
            print(reader[idx2])
        else:
            if idx2 == 1:
                reader[idx2] = line.strip()
                print("reader",reader[0])
                for idx, char in enumerate(reader[0]):
                    print(idx, char, " | ", )
                    if idx == 0:
                        if (char < reader[0][1]) and (char < reader[1][0]):
                            print("FOUND LESS THAN 1", char)
                            risk += int(char) + 1
                    elif idx == len(reader[0])-1:
                        if (char < reader[0][idx-1]) and (char < reader[1][idx]):
                            print("FOUND LESS THAN 2", char)
                            risk += int(char) + 1
                    else:
                        if (char < reader[0][idx-1]) and (char < reader[1][idx]) and (char < reader[0][idx+1]):
                            print("FOUND LESS THAN 3", char)
                            risk += int(char) + 1
            elif idx2 == len(lines)-1:
                reader[idx2] = line.strip()
                print("BEFORE EOF: reader",reader[idx2-1])
                for idx, char in enumerate(reader[idx2-1]):
                    print(idx, char, " | ", )
                    if idx == 0:
                        if (char < reader[idx2-1][1]) and (char < reader[idx2][0]) and (char < reader[idx2-2][0]):
                            print("FOUND LESS THAN 1", char)
                            risk += int(char) + 1
                    elif idx == len(reader[idx2-1])-1:
                        if (char < reader[idx2-2][idx]) and (char < reader[idx2-1][idx-1]) and (char < reader[idx2][idx]):
                            print("FOUND LESS THAN 2", char)
                            risk += int(char) + 1
                    else:
                        print(idx, idx2)
                        print(reader)
                        if (char < reader[idx2-2][idx]) and (char < reader[idx2-1][idx-1]) and (char < reader[idx2][idx]) and (char < reader[idx2-1][idx+1]):
                            print("FOUND LESS THAN 3", char)
                            risk += int(char) + 1

                print("EOF")
                print("reader",reader[idx2])
                #print("reader2",reader[idx2+1])
                for idx, char in enumerate(reader[idx2]):
                    print(idx, char, " | ", )
                    if idx == 0:
                        if (char < reader[idx2-1][0]) and (char < reader[idx2][1]):
                            print("FOUND LESS THAN 1", char)
                            risk += int(char) + 1
                    elif idx == len(reader[idx2])-1:
                        if (char < reader[idx2][idx-1]) and (char < reader[idx2-1][idx]):
                            print("FOUND LESS THAN 2", char)
                            risk += int(char) + 1
                    else:
                        print(idx, idx2)
                        print(reader)
                        if (char < reader[idx2][idx-1]) and (char < reader[idx2-1][idx]) and (char < reader[idx2][idx+1]):
                            print("FOUND LESS THAN 3", char)
                            risk += int(char) + 1
            else:
                reader[idx2] = line.strip()
                print("IN ELSE: reader",reader[idx2-1])
                for idx, char in enumerate(reader[idx2-1]):
                    print(idx, char, " | ", )
                    if idx == 0:
                        if (char < reader[idx2-1][1]) and (char < reader[idx2][0]) and (char < reader[idx2-2][0]):
                            print("FOUND LESS THAN 1", char)
                            risk += int(char) + 1
                    elif idx == len(reader[idx2-1])-1:
                        if (char < reader[idx2-2][idx]) and (char < reader[idx2-1][idx-1]) and (char < reader[idx2][idx]):
                            print("FOUND LESS THAN 2", char)
                            risk += int(char) + 1
                    else:
                        print(idx, idx2)
                        print(reader)
                        if (char < reader[idx2-2][idx]) and (char < reader[idx2-1][idx-1]) and (char < reader[idx2][idx]) and (char < reader[idx2-1][idx+1]):
                            print("FOUND LESS THAN 3", char)
                            risk += int(char) + 1

print("Risk: ",risk)