#1:list[]
#2.tuple()
#.3.set{}
#4.dic[]
frinds=["sanu","sayan","sumon","atunu","souransu"]
print(type(frinds))
frinds[2]="none" #change value list is muTable
print(frinds)
frinds.append(10) #append is use to add a valu in the last
print(frinds)
frinds.insert(1,"google") # add valie in a specifick possition 
print(frinds)
frinds.remove("atunu")
print(frinds)
frinds.pop(3) #delet with pop spisifik index
print(frinds)
del frinds[2] #delet a spisifik with del  
print(frinds)
for i in frinds:
    print(i)
for i in range(len(frinds)):#range and len use to aki
    print(i)
fruits=["apple","banana","charry"]
print(fruits[1])
fruits[0]="kiwi"#change the value for "apple" to "kiwi"
print(fruits)
hablilist=[
    [1,2,3,4],
    [6,7,8,9]
]
print(hablilist[0])
#==============================================================================
#python tuples
mytuple=(1,2,"sanu","sayan")
print(type(mytuple))
print(mytuple[0:4]) #range of index
makelist=list(mytuple)
print(type(makelist))
makelist.insert(2,"googe")
print(makelist)
thistuple=tuple(makelist)
print(thistuple)
#unpack tuple
fruit=("apple","banana","mango")
(a,b,c)=fruit
print(a)
(*a,)=fruit
print(fruit)
(a,b,*c)=fruit
print(fruit)
# loop in tuple
for i in fruit:
    print(i)
for i in range(len(fruit)):
     print(i)
frinds=("sanu","sayan","sumon","atunu","souransu")
i=0
while i<len(frinds):
    print(frinds[i])
    i=i+1
num1=(1,2,3,4,5)
num2=(8,9,10,11)
print(num2+num1)
print(num1*2)
indexing=frinds.index("atunu")# finde index number in tuple
print(indexing)
print(frinds.count("atunu"))#count a spasifik value in tuple
print(frinds[2])#pr=nun%4


#==========================================================================
#set is not allow no duplicate munber
#can not change but can be added
#no ordered
myset={1,False,"string","sanu"}
print(myset)
for i in myset:
    print(i)
print(1 in myset)
myset.add("SOUMYA")
print(myset)
set1={1,3,4,5,5}#not allow duplikate number
print(set1)
myset.update(set1)
print(myset)
print(set1)
set1.remove(5)
print(set1)
#set1.remove[2] {__we can not use index nunber because set are unordered__}
#print(set1)
set1.discard(4) #discard alo use to use remove iten in set
print(set1)
set1.pop()
print(set1)
ste1={"a","d","v"}
set2={1,2,3,4,5,6}
print(set2.union(set1))
#===============================================================
student_info={"soumyadeep":{"name":"soumya","roll":142,"depart ment":"ECE"},"pal":{"name":"soumyadeep pal","roll":
141,"depertment":"ECE"}}
print(type(student_info))
print(student_info)
print(student_info["soumyadeep"])#defint the name so use"""
x=student_info.get("soumyadeep")# get also the method to print keys
print(x)
a=student_info.keys()
print(a)
b=student_info.values()
print(b)
#update dic
student_info["soumya"]={"name":"deep","roll":4} # add keys and values
print(student_info)
student_info.update({"soumyadeep":"he is a ECE student"})#change values in keys
print(student_info )
for x in student_info: # to print onlu kyes 
    print(x)
for a in student_info.values():# print onlyvalues 
    print(a)
for item in student_info.items():
    print(item)
#copy directo
mydic=student_info.copy()# copy function use to copy the dict
print(mydic)
x=dict(student_info)
print(x)