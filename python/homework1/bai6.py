
a = float(input())
b = float(input())
c = float(input())
p = (a + b + c)/2
if a + b >= c and a + c >= b and b + c >= a :
    import math
    print ("Diện tích của tam giác là :", round(math.sqrt((p - a)*(p - b)*(p - c)*p) , 1 ))
else :
    print("không phải 3 cạnh của tam giác ")