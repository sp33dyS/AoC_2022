import string

### PART 1 ###

src = open('D:\GIT\AoC_2022\Day3\input.txt','r').read().split("\n")

priorities = 0
letters_lower = list(string.ascii_lowercase)
letters_upper = list(string.ascii_uppercase)
letters = letters_lower + letters_upper
points = 0
points2 = 0
new_src = []

for i in src:
    rucksack1 = i[:len(i) // 2]
    rucksack2 = i[len(i) // 2:]
    same = [i for i in rucksack1 if i in rucksack2]
    points += letters.index(same[0]) + 1

print(points)

### PART 2 ###

for i in src:
    temp_src = []
    temp_src.append(src[0])
    temp_src.append(src[1])
    temp_src.append(src[2])
    new_src.append(temp_src)
    del src[0]
    del src[0]
    del src[0]

for i in new_src:
    same2 = [j for j in i[0] if j in i[1] and j in i[2]]
    for j in range(0, len(same2)):
        points2 += letters.index(same2[j]) + 1

print(points2) #2425