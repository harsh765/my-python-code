class prog:
    def __init__(self,a,b):
        c=a+b
        print("prog init class",c)
class deri(prog):
    def __init__(self):
        super().__init__(10, 20)
        print("deri class fun")
    def dis(self):
        print("dis class function")
d=deri()
d.dis()