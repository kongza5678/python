
def Fa(C):
    F =(9/5)*C + 32
    return F

def Kel(C):
    K =(C+273.15)
    return K
    
    
C = int(input("รับองศาเซลเซียส: "))
print("องศาฟาเรนไฮน์ %.2f" % Fa(C))
print("องศาฟาเรนไฮน์ %.2f" % Kel(C))


