def circle(r):
    A = 22/7* (r**2)
    print("พื้นที่วงกลม %.2f" % A)
    return A


A = int(input("รับค่ารัศมี "))
circle(A)