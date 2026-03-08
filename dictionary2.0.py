#Mbaga Tuzinde mahaga 
#Admission no:BSCIT-01-0064/2025
#dictionary2.0
f=open("C:\\Users\\Admin\\Desktop\\pyhton class\\dictionary2.0.txt","a")
# Simple Inventory System

inventory = {}

while True:
    print("\nInventory Menu")
    print("1. Add item")
    print("2. View item")
    print("3. View total quantity")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))

        if item in inventory:
            inventory[item] += quantity
            print("Quantity updated.")
        else:
            inventory[item] = quantity
            print("Item added to inventory.")

    elif choice == "2":
        item = input("Enter item name to search: ")

        if item in inventory:
            print("Item:", item)
            print("Quantity:", inventory[item])
        else:
            print("Item not found.")

    elif choice == "3":
        total = sum(inventory.values())
        print("Total quantity of all items:", total)

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
# Save inventory to file
for item, quantity in inventory.items():    
    print(f"{item}: {quantity}", file=f)    
