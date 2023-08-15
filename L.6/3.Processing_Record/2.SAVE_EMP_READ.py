def main():
    emp_file = open('employee.txt', 'r')
    for line in emp_file:
        amount = line
        name = line
        id_num = line
        dept = line

        emp_file.read(name + '\n')
        emp_file.read(id_num + '\n')
        emp_file.read(dept + '\n')

        print(name, id_num, dept, (amount))
    emp_file.close()
main()