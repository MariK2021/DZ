a = int(input("Enter size of triangle: "))
b = (a - (a-1))
while b != 0:
    print(" "*(a-b), "*" *b)
    b += 1
    if b == a+1:
        break




