num = int(input())

for i in range(0, num * 2 + 1):
    if i < num:
        for j in range(0, num - i):
            print(" ", end = "")
        print("*")
    elif i == num:
        for j in range(0, num + 1):
            print("*", end = "")
        print()
    else:
        k = i - num
        for j in range(0, num - k):
            print(" ", end = "")
        print("*")
