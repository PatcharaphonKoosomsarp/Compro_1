heroes = ['Ironman', 'Thor', 'Hulk', 'Superman','Spiderman']
sort_heroes = []

def main():
    choice = 0
    while choice != 6:
        display_menu()
        choice = int(input('Enter your choice : '))
        if choice == 1:
            display_heroes()
        elif choice == 2:
            add_hero()
        elif choice == 3:
            insert_hero()
        elif choice == 4:
            remove_hero()
        elif choice == 5:
            display_sorted_heroes()
        elif choice == 6:
            exit_program()
            
def display_heroes():
    print(heroes)
def add_hero():
    add_hero = input('Add Enter Hero : ')
    heroes.append(add_hero)
    print(heroes)
def insert_hero():
    insert_hero = input('Insert Enter Hero : ')
    heroes.insert(0, insert_hero)
    print(heroes)
def remove_hero():
    remove_hero = input('Remove Enter Hero : ')
    heroes.remove(remove_hero)
    print(heroes)
def display_sorted_heroes():
    sort_heroes = heroes
    sort_heroes.sort()
    print(sort_heroes)
    sort_heroes.reverse()
    print(sort_heroes)
def exit_program():
    print('Exiting program...!')

def display_menu():
    print('\n','--------MENU--------')
    print('1.Display Heroes')
    print('2.Add Heroes')
    print('3.Insert Heroes')
    print('4.Remove Heroes')
    print('5.Display Sorted Heros[Ascending / Descending]')
    print('6.Exit')
main()
