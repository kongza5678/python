def bmi(kg, cm):
    BMI = kg/(cm/100)**2
    return BMI

def check(bmi):
    if bmi<18.50:
        print("น้ำหนักต่ำกว่าเกณฑ์")
    elif bmi>=18.50 and bmi <= 22.90:
        print("สมส่วน")
    elif bmi>=23 and bmi <= 24.90:
        print("น้ำหนักเกิน")
    elif bmi>=25 and bmi <= 29.90:
        print("โรคอ้วน")
    elif bmi>=30:
        print("โรคอ้วนอันตราย")
   
   
kg = int(input("น้ำหนัง "))
cm = int(input("ส่วนสูง "))
print("BMI= %.2f" % bmi(kg, cm))
check(bmi(kg, cm))
