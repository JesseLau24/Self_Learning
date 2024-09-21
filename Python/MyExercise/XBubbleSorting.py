tar = [1, 13, 2, 91, 4, 0, 6, 24, 8, 7, 9, 10, 14, 17, 63, 25 ]

max = len(tar)
while max > 0:
    for i in range(0, max-1):
        if tar[i] > tar[i+1]:
            tar[i], tar[i+1] = tar[i+1], tar[i]
    max -= 1

print(tar)

