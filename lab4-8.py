def bmi(cm,kg):
    b = kg/(cm/100)**2
    return b

def compare(bmi):
    if bmi<18.50:
        print("น้ำหนักน้อย")
    elif bmi>=18.50 and bmi <= 22.90:
        print("ปกติ")
    elif bmi>=23 and bmi <= 24.90:
        print("ท้วม")
    elif bmi>=25 and bmi <= 29.90:
        print("อ้วน")
    elif bmi>=30:
        print("อ้วนมาก")
   
   
c = int(input("รับค่าส่วนสูง "))
k = int(input("รับค่าน้ำหนัก "))
print("BMI= %.2f" % bmi(c,k))
compare(bmi(c,k))