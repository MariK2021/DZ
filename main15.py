lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
min_number = input("Enter min number: ")
max_number = input("Enter max number: ")
lst2 = [i for i in lst if int(min_number) <= i <= int(max_number)]
number = 0
for i in lst:
    if int(min_number) <= i <= int(max_number):
        if number == 0:
            number = ((number+1) * i)
        else:
            number = number * i
print(f"sum = {sum(lst2)}, product = {number}")
