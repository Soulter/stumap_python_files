def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)
calc(3,4,5)