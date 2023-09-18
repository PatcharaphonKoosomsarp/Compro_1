import pickle

heroes = []
#เปิดไฟล์ตั้งเเต่เริ่ม เเละ ปิดไฟลฺ์เมื่อกด 6 ในโปรแกรม#
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
#สามารถดูได้ว่ามี HERO อะไรบ้าง ใน ไฟล์ heroes.dat#



def add_hero():
#เพิ่ม heroes ในไฟล์ heroes.dat#



def insert_hero():
#สามารถเพิ่ม heroes ได้ตำแหน่งที่ต้องการ#



def remove_hero():
#ลบ heroes ในไฟล์ heroes.dat#



def display_sorted_heroes():
#แสดง heroes ที่เรียงลำดับจากน้อยไปมาก หรือมากไปน้อย#



def exit_program():
#ออกจากโปรแกรม เเละปิดไฟล์#



def display_menu():
    print('\n','--------MENU--------')
    print('1.Display Heroes')
    print('2.Add Heroes')
    print('3.Insert Heroes')
    print('4.Remove Heroes')
    print('5.Display Sorted Heros[Ascending / Descending]')
    print('6.Exit')
main()
