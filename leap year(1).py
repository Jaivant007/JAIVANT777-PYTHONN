date=input("enter the date(DD/MM/YYYY):")
day,month,year=map(int,date.split("/"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year")
    print("next anniversary:",f"{day}/{month}/{year+4}")
else:
    print(f"{year} is NOT a leap year")
    print("previous anniversary:",f"{day}/{month}/{year-1}")
 
