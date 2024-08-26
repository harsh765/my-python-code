class prog():
    def add(self):
        print("one add")
class deri(prog):
    def add(self):
        super().add()
        print("second add")
p=deri()
p.add()