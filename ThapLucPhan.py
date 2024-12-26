n=317547
def H10toH16 (n):
    if n>0:
        sd= n % 16
        n = n//16
        if sd == 10:
            return H10toH16(n) + "A"
        elif sd == 11:
            return H10toH16(n) + "B"
        elif sd == 12:
            return H10toH16(n) + "C"
        elif sd == 13:
            return H10toH16(n) + "D"
        elif sd == 14:
            return H10toH16(n) + "E"
        elif sd == 15:
            return H10toH16(n) + "F"
        else:
            return H10toH16(n) + str(sd)
    else:
        return ""

Hex = H10toH16(n)
print (Hex, end=" ")

