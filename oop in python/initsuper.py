class prog():
    def __init__(self,r):
        self.r=r

class deri(prog):
    def __init__(self, r, n):
        super().__init__(r)
        self.n=n

class prog2(deri):
    def __init__(self, r, n, c):
        super().__init__(r, n)
        self.c=c

    def dis(self):
        print(self.r)
        print(self.n)
        print(self.c)

p=prog2(10, "sunny", "malegon")
p.dis()
