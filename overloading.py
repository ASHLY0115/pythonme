class complex:
    def__init__(self,a=0,b=0):
        self.a=a
        self.b=b
    
    def display(self):
        if self.b>0:
            print("complex number is",self.a, "+",self.b,"j")
        else:    
            print("complex number is",self.a, self.b,"j")
            
    def__add__(self,other):
        r=self.a+other.a
        i+self.b+other.b
        return complex(r,i) 

c1=complex(2,-3)
c2+complex(3,4)
c3.display()
c1.display()
c2.display()
c3.dislpay()   
