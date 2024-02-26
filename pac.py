def sum(a,b):
    c=a+b
    return(c)
print(sum(2,6))
#coumt list itemrasult
rasult=[74,78,83,90,97,40,40]
print(rasult.count(40)) #count use to count the itemes 
print(max(rasult))
print(min(rasult))
rasult.sort()#sort is use to small to big
print(rasult)
rasult.reverse()# arrange the list big to small
print(rasult)
ki=rasult.index(90)#
print(ki)
#zip function
zip1=[1,2,3,]
zip2=[4,5,6,]
print(list(zip(zip1,zip2)))
for a,b in zip(zip1,zip2):
       print(a,b)
for h in range(len(zip1)):
    print(zip1[h],zip2[h])
#splite string 
ki=("soumya")
hi=ki.split(ki);
print(hi)
name=input("soumya")
print(name)
a=name.split();
print(a)
colour=[]
for a in range(1,3):
    b=input("your favarit collor:-"+str(a))
    colour.append(b)
print(colour)
#boolent type data
g=True
print(g)
h=2*"python"*2#str maltiplika tion
print(h)
#in list[min max ,sort , reverse,index] function are use
list=[10,20,30,60,50,70]
k=max(list)
print(k)
l=min(list)
print(l)
list.sort()
print(list)
list.reverse()
print(list)
l=list.index(30)
print(l)
#pthon loop
#(1)-while loop
h=0
while  h<10:
         print("yes it is trou")
         h=h+1
#(2) for loop         
frout=[10,20,30,6050,40]
for j in frout:
    print(j)
for g in range(11):
    if g==6:
      break
    print(g)
frout=["red","green","yellow","orange"]
for h in frout:
    if h=="yellow":
      break
    print(h)
for h in range(10):
    if h==7:
        continue
    print(h)
#def function
def soumya():
    print("i need laptop")
soumya()
def sum(a,b):
    c=a+b
    print(c)
sum(10,20)
zip1=["soumya","souransu"]
zip2=["aot","kolagat"]
print(list(zip(zip1,zip2)))
#python lambda
x=lambda a,b:a+b
print(x(10,20))

d=lambda h,k,l,m:(h+k)/(l-m)
print(d(10,20,11,1))
arry=["soumya","sanu","souransu","sayan"]
arry[0]="argho"
print(arry)
class hablu:
    name=""
    number=""
a=hablu()
a.name="eashan"
print(a.name)
a.name="soumyadep"
print(a.name)
class baba:
    car="bmw"
    tk="100cr"
    home="6 floor"
    
class kaka(baba):
    brokenphon="kkoo"
    brokenhome=""
    
k=kaka
print(k.car)
print(k.brokenphon)
list=["soumya","sanu","souransu","sayan"]
for i in range(len(list)):
   print(i)
x=iter(list)
print(list[i])
hablu=420
print(type(hablu))
goblu=40.2
print(type(goblu))
#complex type data
kobo=30j+10
print(type(kobo))
#string
yourname="sanu"
myname="soumya"
print(yourname+myname)
print(yourname+"  "+myname)
bool=True
print(type(bool))
x=10
y=30
print(x>y)
k=10
print(x==k)
#python string for mationg
num1=20
num2=30
print(f"the sum of the num is",num1+num2)
print(f"the sum of the num is{num1+num2}")
#binary type data
hablulist=[1,11,3,6,8,6]
b=bytes(hablulist)
print(type(b))
print(b)
#bite arrary
#b1=bytearry(hablulist)
#print(b1)
x=None
print(type(x))
list=[1,2,3,6]
print(type(list))
tuple=(1,2,3,8)
print(type(tuple))
print(tuple)
set={1,5,6,3,9}
#print(type(set)}
print(set)
ram=rang(11);
print(ram)
 #addition
a=10
b=30
print(a+b)
#multiplication
print(a-b)
#divition
print(a/b)
#exponetiotion
print(a**b)
#multiplication
print(a*b)
#floor divition
d=6
c=5
print(d//c)
#python operatore [assigment operator]
d=5
sum=d+5
print(sum)
s=10
s+=20
print(s)
s-=5
print(s)
#python comparition operator
#swapping
c=50
d=60
c,d=d,c
print(c,d)
print(c)#change value
#user input 
username=input("")
print(username)
username=input("enter your name:-")
pasward=input("enter your password:-")
print(username)
print(pasward)
#type chastion
name="12365"
print(type(int(name)))
print(int(name))
#python list
list=[10,22,33,66,88,77]
print(list)
list[2]=44
print(list)
frind=["soumya","sanu","sayan"]
frind[2]="souransu"
print(frind)
list.append(100)
print(list)
list.insert(1,"soumen")
print(list)
#RENOVE LIST ITEN
newline=["eshan","hablu","tutul"]
newline.remove("hablu")
print(newline)
newline.pop(1)
print(newline)
newline.clear()
print(newline)
#looplist
looplist=["gopa","krisno","kana","nondodulal","nakonchor"]
for i in looplist:
    print(i)
for j in range(len(looplist)):
    print(j)
y=0
while y<len(looplist):
         print(looplist[y])
         y=y+1
#list comparistion
num=[1,2,3,6,8,9]
for i in num:
    print(i*2) 
double=[2*i for i in num]
print(double)
#short list09l
num=[3,6,9,5,4,6,3]
num.sort()
print(num)
#reverse list
num=[1,2,3,54,9]
num.reverse()
print(num)
#copy list
num=[1,2,3,6,9,8]
num.copy()
#join two list
num1=[1,2,3,5,6]
num2=[5,6,9,7,5]
num3=num1+num2
print(num3)
#tuple
tuple=(1,2,3,"sanu","soumya")
print(tuple[1:3])
#loop tuple
frout=("applr","banaa","charry")
h=len(frout)
for i in range(h):
    print(i)