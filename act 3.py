class Bird:
    def __init__(self):
        print("Bird is Ishaan and ready")
    
    def whoisthis(self):
        print(Bird)
    
    def swim(self):
        print("Swim Faster")
class Penguin(Bird):
        def __init__(self):
             super().__init__()
             print("Bird is Ishaan and ready")
        def whoisthis(self):
             print("penguin")
        def swim(self):
             print("Penguin is swimming")
peggy=Penguin()
peggy.swim()