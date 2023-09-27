class employee():
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

    def show_empyoee(self):
        print('Employee Name ', self.name, ' Age ', self.age, ' ID ', self.id, ' Salary ', self.salary)

emp1 = employee("Peter", 22, 1000, 1234)
print(emp1.__dict__)
emp2 = employee("John", 25, 1001, 2345)
emp2.show_empyoee()