go = 'y'
while go == 'y':
    wholesale = float(input("Enter the item's wholesale cost: "))
    retail = wholesale * 2.5
    print("Retail price: $", retail)
    go = input("Do you have another item? (Enter y for yes): ")