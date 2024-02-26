#numpy
import numpy
data1=numpy.array([1,345,56,45,32,])
print(data1.ndim)

print(type(data1))
print(data1)
print(data1.dtype)
print(data1[0:3]) #range function use [starting:ending:step]
print(data1.mean())# to know mean value
print(data1.min())#to find the min value
print(data1.max())#to find the max value
print(data1.var())
print(data1.std())
#print(data1.reshape())#to change shape [row and colum]
#creat 2d array
data2=numpy.array([[2,4,5],[6,89,5]]) #arry use same digit 
print(type(data2))
print(data2.ndim) #this is use to find the dimention
print(data2.shape)# this is fine the row and colum
print(data2+2) #add num 
print(data2[1][1]) 
print(data2[0:,1])
#print(data2.resize,(2,2))
#add array
a=[1,23,3,5,6,69]
data3=numpy.array(a)
data4=numpy.array([4,1,3,443,42,5])
print(data3)
print(data4)
print(data3+data4)# all arritmatik math oporation do
print(numpy.power(data3,2))
print(numpy.sqrt(data3))
#2D ARRAY
a=numpy.array([[1,23,4],[5,6,7]])#to add all value 
print(a.sum())
print(a.flatten())#make anay data in 1D
print(a.tolist())# array to list
print(numpy.random.randint(10,30,size=(2,2)))# to random array 
a=["a","f","g","h","k"]
print(numpy.random.choice(a,size=1)) #choice is use to pick a random item
