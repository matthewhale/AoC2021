
gamma = ''
epsilon = ''
count = [0,0,0,0,0,0,0,0,0,0,0,0]

with open('input.txt', 'r') as input:
    report = input.readlines()
    for line in report:
        for i in range(0,12):
            inty = line.strip()
            count[i] = count[i] + int(inty[i])
    for i in range(0,12):
        if count[i] > 500:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
print(count)
print(int(gamma,2))
print(int(epsilon,2))
final = int(gamma,2) * int(epsilon,2)
print(final)

        #char_freq = Counter(line.strip())
        #char_freq2 = Counter(line.strip())
        #maximum = max(char_freq, key = char_freq.get)
        #minimum = min(char_freq, key = char_freq2.get)
        #print(line.strip())
        #print(len(line.strip()))
        #print("mostcommon:", maximum, " ", max(char_freq, key = char_freq.get))
        #print("leastcommon:", minimum, " ", min(char_freq, key = char_freq2.get))

input.close()