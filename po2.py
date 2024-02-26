number=int(input("enter the num :"))
original= number
num=0


while number !=0:
    
    last_num=((number%10)**3)
    num=num+last_num
    number=(number//10)
    
print("the nun is :",num)
if num==original:
    print("true")
else:
    print("false")