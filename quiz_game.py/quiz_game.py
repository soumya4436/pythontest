print("walcome to game!")
option=input("to start yes! =")
if option.lower() !="yes":
    quit()
print("let`s start!")
score=0



answer=input(str("1+1="))
if answer=="2":
    
    score +=1
    print("good")
else:
    print("right answer=2")

answer1=input("5-3=")
if answer1=="2":
    
    score +=1
    print("good")
else:
    print("right answer is=2")

answer2=input("3+2=")
if answer2=="5":
    
    score +=1
    print("good")
else:
    print("right answer id =5")
print("your score"+str(score))
print("your parcentage is" +str((score/3)*100)+"%")