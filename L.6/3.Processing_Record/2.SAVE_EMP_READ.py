def main():
    emp_file = open('employees.txt', 'r')

    line = emp_file.readline()

    while line != '':
        name = line.rstrip('\n')
        id_num = emp_file.readline().rstrip('\n')
        dept = emp_file.readline().rstrip('\n')

        print('Name:', name)
        print('ID:', id_num)
        print('Dept:', dept)

        line = emp_file.readline()

    emp_file.close()
main()