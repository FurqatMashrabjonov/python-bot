

hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
def fromDectoHex(son):
    """ 10 likni 16 lik sanoq sistemasiga o'tkazish."""
    dec = int(son)
    h = ''
    while dec!=0:
        q = dec%16
        dec = dec//16
        h = hex[q] +h
    return h.upper()

def fromDectoBin (son):
    """10 likni 2 lik sanoq sistemesiga o'tkazish"""
    dec = int(son)
    b = ''
    while dec!=0:
        if dec%2==1:
            b = '1'+ b
            dec = dec//2
        elif dec%2==0:
            b = '0' + b
            dec = dec//2
    return str(b)

def fromBintoDec(son):
    """2 likni 10 lik sanoq sistemaga o'tkazish."""
    un = 0
    for i in range(len(son)):
        if son[-i-1]=='0' or son[-i-1]==0:
            un +=0
        elif son[-i-1]=='1'or son[-1-i]==1:
            un += pow(2,i)
        else:
            return f"{son}  ikkilik sanoq sistemasida emas."
    return un

def fromBintoHex(son):
    """2 likni 16 lik sanoq sistemasiga o'tkazish."""
    dec = int(fromBintoDec(son))
    h = ''
    while dec !=0:
        q = dec%16
        dec = dec//16
        h = hex[q] + h
    return h.upper()

def fromHextoDec(son):
    """
    16 likni 10 likga o'tkazadi.
    """
    hex = son.upper()
    index = len(hex)
    d = 0
    for i in range(index):
        if hex[-1-i]=='A':
            d += pow(16,i) * 10
        elif hex[-1-i]=='B':
            d += pow(16,i) *11
        elif hex[-1-i]=='C':
            d += pow(16,i) *12
        elif hex[-1-i]=='D':
            d += pow(16,i) *13
        elif hex[-1-i]=='E':
            d += pow(16,i) *14
        elif hex[-1-i]=='F':
            d += pow(16,i) *15
        else:
            d += pow(16,i) * int(hex[-1-i])
    return d

def fromHextoBin(son):
    """
    16 likni 2 likga o'tkazib beradi.
    """
    dec = int(fromHextoDec(son))
    b = ''
    while dec != 0:
        if dec % 2 == 1:
            b = '1' + b
            dec = dec // 2
        elif dec % 2 == 0:
            b = '0' + b
            dec = dec // 2
    return b

def fromDectoRim(son):
    d = int(son)
    R = ''
    while d!=0:
        if d>=3999:
            return f"None"

        elif(d//1000>=1):
            R += "M"
            d -=1000
        elif (d // 900 >= 1):
            R += 'CM'
            d -= 900
        elif (d // 500 >= 1):
            R += "D"
            d -= 500
        elif (d // 400 >= 1):
            R += 'CD'
            d -= 400
        elif (d // 100 >= 1):
            R += 'C'
            d -= 100
        elif (d // 90 >= 1):
            R += "XC"
            d -= 90
        elif (d // 50 >= 1):
            R += "L"
            d -= 50
        elif (d // 40 >= 1):
            R += "XL"
            d -= 40
        elif (d // 10 >= 1):
            R += "X"
            d -= 10
        elif (d // 9 >= 1):
            R += "IX"
            d -= 9
        elif (d // 5 >= 1):
            R += "V"
            d -= 5
        elif (d // 4 >= 1):
            R += "IV"
            d -= 4
        elif (d // 1 >= 1):
            R += "I"
            d -= 1
    return R

def fromRimtoDec(son):
    R = son.upper() +" "
    d = 0
    i =0
    l = len(R)
    while i < l:
        if R[i]=="M":
            d += 1000
            i+=1
        elif R[i]=="C" and R[i+1]=="M":
            d +=900
            i +=2
        elif R[i]=="D":
            d +=500
            i +=1
        elif R[i]=="C" and R[i+1]=="D":
            d +=400
            i+=2
        elif R[i]=="C":
            d +=100
            i+=1
        elif R[i]=="X" and R[i+1]=="C":
            d +=90
            i+=2
        elif R[i]=="L":
            d +=50
            i+=1
        elif R[i]=="X" and R[i+1]=="L":
            d +=40
            i+=2
        elif R[i]=="X":
            d +=10
            i +=1
        elif R[i]=="I" and R[i+1]=="X":
            d +=9
            i+=2
        elif R[i]=="V":
            d +=5
            i+=1
        elif R[i]=="I" and R[i+1]=="V":
            d +=4
            i+=1
        elif R[i]=="I":
            d +=1
            i+=1
        else:
            i+=1
    return d

def BAZA(baza, text):
    b = baza
    t = text
    if t not in  b:
        return True
    return False
