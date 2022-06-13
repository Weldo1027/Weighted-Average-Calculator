n = 0
koniec = 0
s = 0
o = 0
exit = 0
c = o
##########################
l = float(input("input value "))
w = int(input("input weight "))

o = w * l
n = w
c = o


while exit == 0:
    l = float(input("input value "))
    w = int(input("input weight "))

    o = w * l
    n = w + n
    c = c + o
    s = c / n
    final = round(s,2)

    print("weighted value = " + str(final))
