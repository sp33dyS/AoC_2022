### PART 1 ###

src = open('D:\GIT\AoC_2022\Day2\input.txt','r').read().split("\n")
sorted_src = [i.split(" ") for i in src]

score = 0
score2 = 0
win = 6
lose = 0
draw = 3
rock = 1
paper = 2
scissors = 3
new_src =[]

for i in sorted_src:
    elf = i[0]
    my = i[1]
    if elf == "A" and my == "X":
        score += rock + draw
    elif elf == "A" and my == "Y":
        score += paper + win
    elif elf == "A" and my == "Z":
        score += scissors + lose
    elif elf == "B" and my == "X":
        score += rock + lose
    elif elf == "B" and my == "Y":
        score += paper + draw
    elif elf == "B" and my == "Z":
        score += scissors + win
    elif elf == "C" and my == "X":
        score += rock + win
    elif elf == "C" and my == "Y":
        score += paper + lose
    elif elf == "C" and my == "Z":
        score += scissors + draw

print(score)

### PART 2 ###

for i in sorted_src:
    elf = i[0]
    my = i[1]
    if elf == "A" and my == "X":
        score2 += scissors + lose
    elif elf == "A" and my == "Y":
        score2 += rock + draw
    elif elf == "A" and my == "Z":
        score2 += paper + win
    elif elf == "B" and my == "X":
        score2 += rock + lose
    elif elf == "B" and my == "Y":
        score2 += paper + draw
    elif elf == "B" and my == "Z":
        score2 += scissors + win
    elif elf == "C" and my == "X":
        score2 += paper + lose
    elif elf == "C" and my == "Y":
        score2 += scissors + draw
    elif elf == "C" and my == "Z":
        score2 += rock + win

print(score2)