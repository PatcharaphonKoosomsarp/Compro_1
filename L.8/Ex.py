records = {'6506022620095' : ['Anirach Mingkhawan','Anirach@gmail.com','0817320766']}
#1.Display Records
#2.Search [id]
#3.Add
#4.Multiply Records[id]
#5.Delete[id]
#6.Exit
def main():
    choice = 0
    while choice != 6:
        display_menu()
        choice = int(input('Enter your choice : '))

        if choice == 1:
            for key,value in records.items():
                print(key,value)

        elif choice == 2:
            id = input('Search [id] : ')
            print(records.keys(),records.get(id))

        elif choice == 3:
            add_id = input('Add Enter ID : ')
            add_name = input('Add Enter Name : ')
            add_gmail = input('Add Enter Gmail : ')
            add_phone_number = input('Add Enter Phone Number : ')
            records[add_id] = add_name , add_gmail , add_phone_number
            print(records)
            
        elif choice == 4:
            add_id = input('Add Enter ID : ')
            add_name = input('Add Enter Name : ')
            add_gmail = input('Add Enter Gmail : ')
            add_phone_number = input('Add Enter Phone Number : ')
            records[add_id] = add_name , add_gmail , add_phone_number
            print(records)

        elif choice == 5:
            id = input('Delete Enter ID: ')
            records.pop(id)
            print(records)
            
        elif choice == 6:
            print('Exiting program.')
        else:
            print('Error: Invalid number')
    
def display_menu():
    print('\n','--------MENU--------')
    print('1.Display Records')
    print('2.Search [id]')
    print('3.Add')
    print('4.Multiply Records[id]')
    print('5.Delete[id]')
    print('6.Exit')

main()