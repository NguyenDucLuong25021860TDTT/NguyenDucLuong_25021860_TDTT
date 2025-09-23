day, month, year = map ( int(), input().split("/"))
if month < 1 or month > 12 or year > 2025 or year < 1900 :
    print("invalid")
else : 
    if month in [1 , 3 , 5 , 7 , 8 ,10 ,12] :
       max_day = 31
    elif month in [4 , 6 , 9 , 11] :
        max_day =30 
    elif month == 2 :
        if (year % 4 == 0 and year % 100 != 0) or  (year % 400)== 0 :
            max_day = 29
        else :
            max_day = 28          
    if day > max_day or day < 1 :
        print(" invalid ")
    else :
        print( " valid ")    