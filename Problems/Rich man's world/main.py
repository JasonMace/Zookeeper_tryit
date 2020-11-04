num = int(input())
year = 0
while num < 700000:
    num *= 1.071
    year = year + 1
print(year)
