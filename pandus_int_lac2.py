import pandas as pd
# interpolate
var=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv")
a=var.interpolate() # interpolate atomatckly fill nole value according
print(a)
# marging and concat
a=pd.DataFrame({"A":[1,2,3,4],"b":[5,6,7,8]})
B=pd.DataFrame({"A":[1,2,3,4],"c":[11,33,4,45]})
C=pd.merge(a,B,on="A")
print(C)
a=pd.DataFrame({"A":[1,2,3,4],"b":[5,6,7,8]})
B=pd.DataFrame({"A":[1,2,3,4],"c":[11,33,4,45]})
C=pd.merge(a,B,how="left") #"right" is alo use
print(C)
a=pd.DataFrame({"A":[1,2,3,4],"b":[5,6,7,8]})
B=pd.DataFrame({"A":[1,2,3,4],"c":[11,33,4,45]})
C=pd.merge(a,B,how="outer",indicator=True) # to chake which para merter are marge
print(C)
a=pd.DataFrame({"A":[1,2,3,4],"b":[5,6,7,8]})
B=pd.DataFrame({"A":[1,2,3,4],"b":[11,33,4,45]})
C=pd.merge(a,B,right_index=True,left_index=True) # when keys are same
print(C)
# group by
student=pd.DataFrame({"name":["a","d","c","a","c","a","d","c","d","b","b"],
                     "num":[12,23,12,17,19,20,22,23,14,15,24]})
print(student)                     
student_new=student.groupby("name")
print(student_new)
for x,y in student_new:
    print(x)
    print(y)
a=student_new.get_group("a") # this is use to get a spasifik group 
print(a)
li=list(student_new) # to make list
print(li)
# join and append funtion
a=pd.DataFrame({"A":[1,2,3,4],"b":[5,6,7,8]})
B=pd.DataFrame({"p":[1,2,3,4],"c":[11,33,4,45]})
k=a.join(B)
print(k)
