def abc(num):
    sum = 0
    for i in range(num):
        price = int(input("รับราคาสินค้า %d " % (i+1)))
        sum += price
    return sum


def Tax(sum):
    vat = sum*7/100
    return vat 

def disc(sum):
    vat = sum*5/100
    return vat 


def total(a,b,c):
    t = (a-c)+b
    return t




num = int(input("จำนวนสินค้า "))
sum = abc(num)
print("ราคารวม %.2f" % sum)
print("ภาษี %.2f" % Tax (sum))
print("ส่วนลด %2.f" % disc (sum))
print("รวมเป็นเงินทั้งสิน %.2f" % total(sum, Tax(sum), disc (sum)))
