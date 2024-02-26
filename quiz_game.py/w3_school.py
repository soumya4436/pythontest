class person():
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr

    def myfunc(self):
        print("hellow my name is " +  self.name) 
p2=person("sanu",76)
p2.myfunc()

class father():
    def __init__(self,fname,lname):
        self.fname=fname
        self.addr=lname
    def son(self):
       print(self.fname,self.addr)
x=father("soumya","samanta")
x.son()