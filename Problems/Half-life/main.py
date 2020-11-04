begin = int(input())
end = int(input())

move = begin
count = 0

while move >= end:
    move = move / 2
    count = count + 1

print(count * 12)