your_set=set()
while True:
    user_input=input("enter the natural number(1<n<11) or 'done' to finish : ")
    if user_input=='done':
        break
    try:
        num=int(user_input)
        if 1<num<11 and num not in your_set:
            your_set.add(num)
        else:
            ("please enter the natural number in the given range")
    except ValueError:
        print("please enter the natural number in the given range")
print("your set is ",your_set)
a=min(your_set)
print("the least nun",a)

for i in your_set:
    


       print(i*a)