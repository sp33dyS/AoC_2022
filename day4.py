### PART 1 ###

src = open('D:\GIT\AoC_2022\Day4\input.txt','r').read().split("\n")
sorted_src = [i.replace("-", ",").split(",") for i in src]

contains = 0
contains2 = 0
new_src = []

for i in range(0, len(sorted_src)):
    if (int(sorted_src[i][0]) >= int(sorted_src[i][2]) and int(sorted_src[i][1]) <= int(sorted_src[i][3])) or (int(sorted_src[i][0]) <= int(sorted_src[i][2]) and int(sorted_src[i][1]) >= int(sorted_src[i][3])):
        contains += 1

print(contains)

### PART 2 ###

for i in range(0, len(sorted_src)):
    new_src.append([[sorted_src[i][0], sorted_src[i][1]], [sorted_src[i][2], sorted_src[i][3]]])

for i in new_src:
    ls1 = [*range(int(i[0][0]), int(i[0][1]) + 1)]
    ls2 = [*range(int(i[1][0]), int(i[1][1]) + 1)]
    ls3 = [i for i in ls1 if i in ls2]
    if len(ls3) > 0:
        contains2 += 1

print(contains2)