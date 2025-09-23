c = input(" Nhập từ bàn phím 1 chữ cái viết hoa : ")
if c.islower() :
    print(" Bạn cần nhập kí tự hoa ")
elif c == "A":
    print("Trường hợp đặc biệt") 
else :
    print(chr(int(ord(c.lower()) - 1)))      