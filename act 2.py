class parent:
    def __init__(self, name, idno):
        self.name=name
        self.idno = idno
    def display(self):
        print(self.name)
        print(self.idno)

class emp(parent):
    def __init__(self,name,idno,salary,post):
        self.salary = salary
        self.post=post
        self.name = name
        self.idno = idno
e=emp('ishaan','1234', '1 cr', 'md')
e.display()
print(e.salary)
    