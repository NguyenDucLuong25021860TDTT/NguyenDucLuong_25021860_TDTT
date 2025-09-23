year = int(input("Nhập vào số năm : ")) 
if year % 4 == 0 and year % 100 != 0 :
    print("Đây là năm nhuận")
else :
    print("Đây không phải là năm nhuận")   