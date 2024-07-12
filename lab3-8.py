a = 0
s = int(input("รับค่า n:"))

for i in range(s):
    y = int(input("รับค่า %d:" % (i+1)))
    a = a + y
print("รวมคือ %d" % a)
