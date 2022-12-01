from itertools import groupby

### PART 1 ###

src = open('D:\GIT\AoC_2022\Day1\input.txt','r').read().split("\n")
new_src = [list(sub) for ele, sub in groupby(src, key = bool) if ele]

sum_src = []
for i in new_src:
    for j in range(0, len(i)):
        i[j] = int(i[j])
    sum_src.append(sum(i))

print(max(sum_src))

### PART 2 ###

sum_src.sort()
print(sum(sum_src[-3::]))