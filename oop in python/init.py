class prog:
    def __init__(self):
        print(" base")
class p(prog):
    def __init__(self):
        super().__init__()
        print("parent")
class par(p):
    def __init__(self):
        super().__init__()
        print("child")
p=par()