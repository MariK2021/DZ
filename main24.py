def second_largest_number(lst):
    if not lst:
        return None
    else:
        lst.sort()
        return lst[-2]


print(second_largest_number([3, 1, -5, -3, 0, -3, 2.10, 2.20, -5]))
print(second_largest_number([]))
