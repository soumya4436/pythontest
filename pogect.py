number=int(input("enterthr value :"))
num=((number//100)**3)+(((number%100)//10)**3)+((number%10)**3)
if number==num:
    print("the number is true")
else:
    print("the number is false")