class p1:
    def add(self):
        print("i am add function")
class p2(p1):
    def disp(self):
        print(" i dis function")
class p3(p2):
    def jy(self):
        print("i am jy function")

n=p3()
n.add()
n.disp()
n.jy()