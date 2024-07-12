person = ["Khunanon", 35 , 175, 75, "eleclabs@gmail.com"]
print(person)
person[1] = 40
print("อายุุ %d" % person[1])
print("ส่วนสูง %d นํ้าหนัก %d" % (person[2], person[3]))
print("อีเมล %s" % person[4])


print(person[0:3])
print(person[2:4])
print(person[2:])
print(person[:4])
print(person[-4:-1])