class employee():
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary
    def earn(self):
        pass
class childemployee1(employee):
    def earn(self):
        print("no money")
class childenmployee2(employee):
    def earn(self):
        print("has money")

c = childemployee1
c.earn(employee)
d = childenmployee2
d.earn(employee)
