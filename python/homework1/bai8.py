ten_chu_ho = input("Nhập vào tên chủ hộ :")
chi_so_thang_truoc = int(input())
chi_so_thang_sau = int(input())
a = chi_so_thang_sau - chi_so_thang_truoc
if a <= 50 :
   b = 1.08*1984*a 
   print("Họ và tên :" , ten_chu_ho)
   print("Tiền phải trả là :",round(b) )
elif a >= 51 and a <= 100 :
   b = 1.08*(50*1984 + (a-50)*2050)
   print("Họ và tên :" , ten_chu_ho)
   print("Tiền phải trả là :",round(b) )
elif a >= 101 and a <= 200 :
   b = 1.08*(50*1984 + 50*2050 + (a - 100)*2380)
   print("Họ và tên :" , ten_chu_ho)
   print("Tiền phải trả là :",round(b) )
elif a >= 201 and a <= 300 :
   b = 1.08*(50*1984 + 50*2050 + 100*2380 + (a - 200)*2998)
   print("Họ và tên :" , ten_chu_ho)
   print("Tiền phải trả là :",round(b) )
elif a >= 301 and a <= 400 :
   b = 1.08*(50*1984 + 50*2050 + 100*2380 +  200*2998 + (a - 300)*3350)
   print("Họ và tên :" , ten_chu_ho)
   print("Tiền phải trả là :",round(b) )
else :
   b= 1.08*(50*1984 + 50*2050 + 100*2380 +  200*2998 + 300*3350 (a -400)*3460) 
   print("Họ và tên :" , ten_chu_ho)
   print("Tiền phải trả là :",round(b))
