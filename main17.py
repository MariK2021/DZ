lst = [['a', 'c', 'd'], ['f', 'b', 'a'], ['a', 'n', 'k'], ['e', 'l', 'i']]
lst2 = [i[0] for i in lst]
lst2.sort()
lst3 = [i[1] for i in lst]
lst3.sort()
lst4 = [i[2] for i in lst]
lst4.sort()
new_lst = [lst2, lst3, lst4]
new_lst2 = [i[0] for i in new_lst]
new_lst3 = [i[1] for i in new_lst]
new_lst4 = [i[2] for i in new_lst]
new_lst5 = [i[3] for i in new_lst]
final_lst = [new_lst2, new_lst3, new_lst4, new_lst5]
print(final_lst)
