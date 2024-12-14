a=int(input("enter a number1:"))
sum=0
temp=a
while temp>0:
    digit=temp%10
    sum+=digit
    temp=temp//10
    print("sum of digits:",sum)
