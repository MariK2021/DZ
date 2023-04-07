s = "aab qq c badcc a qqqqqaqqqqaa tpara"
words = s.split()
s2 = [i for i in words if i.count("a") == 2]
print(" ".join(s2).title())