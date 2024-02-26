import random
top_range_of_number=input("top_range of the number: ")
if top_range_of_number.isdigit():
    top_range_of_number=int(top_range_of_number)
    if top_range_of_number<=0:
        print("please print gater than 0")
        quit()
else:
    print("enter a number next time")
    quit()

random_number=random.randint(0,top_range_of_number)
guess=0
while True:
    guess +=1
    user_input=input("your guess number: ")
    if user_input.isdigit():
        user_input=int(user_input)
    else:
        print("please type a number next time")
        continue
    if user_input==random_number:
        print("you gote it!")
    if user_input > random_number:
        print("your number is big the number")
    elif user_input < random_number:
        print("your number is lower")
    print("your total guess"+str(guess))