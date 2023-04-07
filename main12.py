s = "aab qq c badcc a qqqqqaqqqqaa tpara"
for i in s.split():
    if i.count("a") == 2:
        print(i.title(), end=" ")
