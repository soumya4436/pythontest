import numpy as np
a=np.array([1,3,5,6])
print(a)
print(a.ndim)  # ndim is use to know the digree
# % timeit- it give time singAL LINE 
# %% timeit-it give time of full prigram
#%timeit np .arange(1,9)**4
#%timeit [j**4 for j in range(1,9)import numpy
# % timeit- it give time singAL LINE 
# %% timeit-it give time of full prigram
#%timeit np .arange(1,9)**4
#%timeit [j**4 for j in range(1,9)]

#l=[]
#for i in range(1,5):
    #int_1=int(input("rnter _"))
   # l.append(int_1)
#print(np.array(l))   
ary=np.array([1,3,4,5],ndmin=10)
print(ary)
print(ary.ndim)
# ZEROS
ar_zero=np.zeros(4)
ar_zero1=np.zeros((3,4))
print(ar_zero)
print(ar_zero1)
# ones
ae_aone=np.ones(3)
print(ae_aone)
ar_empty=np.empty(3) #empty use to get preveos value
print(ar_empty)
ar_arange=np.arange(4)
print(ar_arange)
#DIAGONAL
ar_dia=np.eye(3)
print(ar_dia)
#linespace[this is use same gape in list]
ar_lin=np.linspace(0,20,num=5)
print(ar_lin)
# CREAT NUMPY ARRAYS WITH RAMDOM NUMBERS
ver=np.random.rand(4) #rand give value between 0 and 1
ver1=np.random.rand(2,3) #(row,colume)
print(ver)
print(ver1)
ver2=np.random.randn(5)
print(ver2)
ver3=np.random.ranf(4)
print(ver3)
ver4=np.random.randint(5,20,5)
print(ver4)
# DATA TYPE IN NUMPY ARRAYS
ver5=np.array([1,2,34,5])
print("data type:",ver5.dtype) # to konw int type
ver6=np.array([1,2,33,5,8],dtype=np.int8)
print(ver6.dtype)
new=np.float32(ver6)
print(new)
print(new.dtype) 
x3=np.array([3,4,5,6,7])
new_1=x3.astype(float) #astype use to chon ver any type data
print(new_1.dtype)
#SHAPE AND RESHAPING
x4=np.array([4,7,9,8])
print(x4.shape)
# ARITMETIC OPERATION
s=np.array([1,2,3,4])
veradd=s+3
print(veradd)
# in the chase of 2d array
d1=np.array([[1,2,3],[6,9,7]])
d2=np.array([[4,2,1],[7,6,4]])
veradd1=d1+d2
print(veradd1)
print("mim :",np.min(s),np.argmin(s)) #argmin give the index num of the min
print(np.min(d1,axis=0)) #in 2d array axix=0 meaning it work in a colume amd axis=1 it woek in the rowe
#broadcasting[]
ver1=np.array([1,2,3,4])
print(ver1.ndim)
ver2=np.array([[5],[7],[9]])
print(ver2.ndim)
print(ver1+ver2)
x=np.array([[1],[2]])
y=np.array([[1,2,3],[1,2,3]])
print(x+y)
#indexing and slicing and lterating
ver4=np.array([[1,2,3],[6,8,9]])
print(ver4[0,2]) #[colume,index  number]
a=np.array([[[1,2,3],[7,9,8]]])
print(a[0,1,2])
#SLICING[STARTING:ENDING]
#ITERATIN {ndenumerator is use to get the value and index number}
print(a)
for i in a:
    print(i)
    for l in i:
        print(l)
        for k in l:
            print(k)#[oe 3d array]
#defarance between copy and view
ver=np.array([1,2,3,4])
co=ver.copy()
print(co)
vi=ver.view()
print(vi)
#JOIN AND SPLIT FUNCTION
ver=np.array([1,4,2])
ver1=np.array([5,9,6])
ar=np.concatenate((ver1,ver))
print(ar)
ar_1=np.stack((ver,ver1),axis=0)
ar_2=np.hstack((ver,ver1)) # row
ar_3=np.vstack((ver,ver1)) # colums
ar_4=np.dstack((ver,ver1)) # height
print(ar_1)
print(ar_2)
print(ar_3)
print(ar_4)
# split 
ver=np.array([1,2,3,4,5,6,6])
g=np.array_split(ver,3)
print(g)
# SEARCH, SORT,SEARCH SORTED,FILTER
#serch
ver=np.array([1,2,3,4,3,42,5,6,742,2,2,2])
x=np.where(ver==2) # where is use to kwon the index noumber to a sesefin value
print(x)
#search shorted array
ver1=np.array([1,2,3,4,6,7])
x1=np.searchsorted(ver1,5)
print(x1)
x2=np.searchsorted(ver,5,side="right")
print(x2)
# sort
ver1=np.array([1,2,3,4,3,42,5,6,742,2,2,2])
print(np.sort(ver1))
# filter array
ver_3=np.array(["a","b","h","k","l"])

#f=[True,False,True]
#new_a=ver_3[f]
print(ver_3)
# SHUFFLE,UNIQUE,RESIZE,FLATTEN,RAVEL FUNCTION
# shuffle[ use in chard game]
ver1=np.array([1,2,3,4,3,42,5,6,742,2,2,2])
np.random.shuffle(ver1)#shffl is reorganize the array
print(ver1)
# unique
ver1=np.array([1,2,3,4,3,42,5,6,742,2,2,2])
x=np.unique(ver1,return_index=True,return_counts=True) # return_counts=True tall the value is how many type use
print(x)
# resize [ it is use to mane (row and colume)]
ver1=np.array([1,2,3,4,3,42,5,6,742,2,2,2])
y=np.resize(ver1,(2,3))
print(x)
# falatten{ it use to made any dimention to 1D dimention }
# INSERT AND DELET FUNCTION{only inser int value}
ver=np.array([1,2,3,4,1])
b=np.insert(ver,2,40)#(_,index number,value)
print(b)
a=np.insert(ver,(1,2),(90,77))
print(a)
ver1=np.array([[1,2,3],[6,7,8]])
l=np.insert(ver1,2,66,axis=0)
print(l)
# append
x=np.append(ver1,6.5)
print(x)
#delet
j=np.delete(ver1,1)
print(j)
# MATRIX IN NUMPY
mat=np.matrix([[1,2,3],[7,8,9]])
print(mat)
mat1=np.matrix([[1,2,3],[7,8,9]])
print(mat+mat1)
print(mat-mat1)

#print(mat.dot(mat1))# dot is use to multiplichation of matrix
# matrix function
mat1=np.matrix([[1,2,3],[7,8,9]])
print(np.transpose(mat1))
ver2=np.matrix([[1,2],[3,4]])
print(ver2)
print(np.swapaxes(ver2,0,1))