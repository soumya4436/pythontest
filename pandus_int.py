import pandas as pd
x=[1,2,3,4,5]
ver=pd.Series(x) # {S in chapital}[series is use to read data ]
print(ver)
ver1=pd.Series(x,index=['a','b','c','d','j'],dtype="float",name="python")
print(ver1)
dic={"name":['python','c','c++','java'],"por":[12,23,34,45],"rank":[1,2,3,4,5]}
ver1=pd.Series(dic)
print(ver1)
s=pd.Series('c',index=[1,2,3,4,5])
print(s)
print(type(s))
s1=pd.Series('c',index=[1,2,3,4,5,6,7])
s2=pd.Series('c',index=[1,2,3,4])
print(s1+s2)
# DATA Feame
l=[1,2,3,4,5,6,7]
ver=pd.DataFrame(l)
print(ver)
print(type(ver))
dA={"a":[1,2,3,4],"s":[1,2,3,4],1:[1,2,3,4]} # mandatari to give same number of item in the set
ver1=pd.DataFrame(dA)
print(ver1)
#ver2=pd.DataFrame(d,columns=["s",1],index=['a','b','c','j']) # spling of columns
#print(ver2)
list_1=[[1,2,3,4],[1,2,3,4]]
ver=pd.DataFrame(list_1)
print(ver)
sr={"s":pd.Series([1,2,3,4]),"r":pd.Series([1,2,3,4])}
ver2=pd.DataFrame(sr)
print(ver2) 
# ARITHMETIC OPERATION
ver=pd.DataFrame({"a":[1,2,3,4],"b":[5,6,7,8]})
print(ver)
ver["c"]=ver["a"]+ver["b"]
print(ver)
ver["python"]=ver["a"]<=3
print(ver)
#  how to creat csv file
# csv format is a plain format in which values are separated coummas(comma separated values)
# XLC file format is an excel sheet binary format
ver=pd.DataFrame({"a":[1,2,3,4],"b":[5,6,7,8]})
print(ver)
ver.to_csv("test_new.csv")
ver.to_csv("csb1_new.csv",index=False)
# READ CSV
csv_1=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv")
print(csv_1)
csv_2=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv",nrows=11)
print(csv_2)
csv_3=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv",usecols=["Rank"]) # both colam anad index unber is use
print(csv_3)
csv_4=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv",skiprows=[1]) # skiprow is use for avoid a sesifik rows
print(csv_4)
csv_5=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv",index_col=["Year"]) # index_col is use for it woer as a indintypi by its basis
print(csv_5)
csv_5=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv",header=[2]) # header make heading
print(csv_5)
csv_6=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv",names=["cal1","cal2"]) # names make new colume name
print(csv_6)
csv_7=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv",header=None) # none remuve all header file and prefix is use for rename header
print(csv_7)
csv_8=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv",dtype={"Year":"float"}) # must use {} /  {"row name":"type"}
print(csv_8)
csv_9=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv")
a=csv_9.columns # columns use to find colums
print(a)
b=csv_9.describe() # summer of the csv file
print(b)
c=csv_9.head() # head( ) give frist 5 rows
print(c)
d=csv_9.tail() # tail give last 5 data
print(d)
f=csv_9[:6]
print(f)
h=csv_9.index.array # get all index
print(h)
j=csv_9.to_numpy() # ti nunpay chon ver to all in array
print(j)
g=csv_9.sort_index(axis=0,ascending=False) # this use for assindin oder
print(g)
csv_9=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv")
print(csv_9)
i=csv_9.loc[0,"Country"]="python" # thi is the way to change the valus in cvs file
print(i)
print(csv_9)
o=csv_9.loc[[2,3],["Year","Total"]] # to find sesifik data
print(o)
p=csv_9.iloc[1,2] # iloc give secifik file value
print(p)
d=csv_9.drop("Total",axis=1) #[axis=1 work as a columns and axis=0 work as arow]
print(d)
# DROPNA AND FILLNA
 # dropna is use when any rows has none value .dropna remove the rows
ver=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv")
a1=ver.dropna(how="any") #(how="all" this is also use) # this is remove the row which has no values
print(a1)
b=ver.dropna(subset="Year") # this work no a partiqular colume which has nole valu 
print(b)
ver.dropna(inplace=True) # it alo drop nole valu
print(ver)
h=ver.dropna(thresh=1) # (thresh= no of nole value) this alo repalce nole value
print(h)
#FILLNA
ver2=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv")
a=ver.fillna("soumya") # fillna fill nome value("value")
print(a)
k=ver.fillna("hii",limit=3) # LIMIT fill 3 colume
print(k)
print("fillna ")
g=ver.fillna({"Year":"samanta","Year":"soumya"}) # {"rows name":"nole valu fil uo with"}
print(g)
#g=ver.fillna(method="ffill") # this method fill the none value with pre vious colum valiue
#print(g)
#j=ver.fillna(method="dfill") # dfill fill the nole value with  bakword fill
#print(j)
ver2.fillna(12,inplace=True) # it (the value) the fill the value
print(ver2)
# replace and interpolate

ver1=pd.read_csv("C:\\Users\\Soumyadeep\\Downloads\\FSI-2023-DOWNLOAD.csv")
print(ver1)
h=ver1.replace(to_replace=2023,value=2025) # it is use to replace values
print(h)
j=ver1.replace([9.0,9.3],66) # it aloso repace data
print(j)
k=ver1.replace("[A-Z]","soumya",regex=True) # this is call regular expration .
print(k)
#g=ver1.repalce({" Country",'[A-Z]'},22,regex=True)
#print(g)
#mathod parmeter

