class Arith:
    sum = 0
    def read(self,a,b):
        self.a = a
        self.b = b
        Arith.sum = a+b
        print("The two numbers are {self.a} and {self.b}")
    
    def add(self,a,b):
        self.sum = self.a + self.b
        return self.sum
    a1 = add(1,2)
    print(a1.add())
    print(a1)

