kg = int(input("นํ้าหนัก"))
cm = int(input("ส่วนสูง"))
bmi = kg/(cm/100)**2
print (bmi)

if bmi < 18.50:
    print("นํ้าหนักน้อย")
elif bmi >= 18.5 and bmi <= 22.90:
    print("ปกติสุขภาพดี")
elif bmi >= 23 and bmi <= 24.90:
    print("ท้วม/โรคอ้วนระดับ 1")
elif bmi >= 25 and bmi <= 29.90:
    print("อ้วน/โรคอ้วนระดับ 2")
elif bmi >= (30):
    print("อ้วนมาก/โรคอ้วนระดับ 3")
    
