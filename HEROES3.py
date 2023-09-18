import pickle

# Global variable to hold the list of heroes
heroes = []

def main():
    load_heroes()
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

def load_heroes():
    global heroes
    try:
        with open('heroes.dat', 'rb') as file:
            heroes = pickle.load(file)
    except FileNotFoundError:
        heroes = []

def save_heroes():
    with open('heroes.dat', 'wb') as file:
        pickle.dump(heroes, file)

def display_heroes():
    print('\nList of Heroes:')
    for idx, hero in enumerate(heroes, start=1):
        print(f'{idx}. {hero}')

def add_hero():
    hero_name = input('Enter the name of the hero: ')
    heroes.append(hero_name)
    save_heroes()
    print(f'{hero_name} has been added.')

def insert_hero():
    position = int(input('Enter the position to insert: '))
    if position < 1 or position > len(heroes) + 1:
        print('Invalid position. Please try again.')
        return
    hero_name = input('Enter the name of the hero: ')
    heroes.insert(position - 1, hero_name)
    save_heroes()
    print(f'{hero_name} has been inserted at position {position}.')

def remove_hero():
    display_heroes()
    try:
        choice = int(input('Enter the number of the hero to remove: '))
        if choice < 1 or choice > len(heroes):
            print('Invalid choice. Please try again.')
            return
        removed_hero = heroes.pop(choice - 1)
        save_heroes()
        print(f'{removed_hero} has been removed.')
    except ValueError:
        print('Invalid input. Please enter a number.')

def display_sorted_heroes():
    ascending = input('Do you want to display in ascending order? (y/n): ')
    sorted_heroes = sorted(heroes)
    if ascending.lower() == 'n':
        sorted_heroes = sorted(heroes, reverse=True)
    print('\nSorted List of Heroes:')
    for idx, hero in enumerate(sorted_heroes, start=1):
        print(f'{idx}. {hero}')

def exit_program():
    save_heroes()
    print('Exiting program. Goodbye!')
    exit()

def display_menu():
    print('\n--------MENU--------')
    print('1. Display Heroes')
    print('2. Add Hero')
    print('3. Insert Hero')
    print('4. Remove Hero')
    print('5. Display Sorted Heroes (Ascending / Descending)')
    print('6. Exit')

if __name__ == '__main__':
    main()
