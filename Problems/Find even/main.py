inp = int(input())
i = 1
tmp = 0
while i < inp:
    tmp = i % 2
    if tmp == 0:
        print(i)
    i = i + 1