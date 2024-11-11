print("Welcome User!")

users = {}
inventories = {}

def register():
    username = input("Enter a username to register: ")
    password = input("Enter a password: ")

    if username in users:
        print("Username already exists.")
    else:
        users[username] = password
        inventories[username] = {}  # Initialize an empty inventory for the new user
        print("User registered successfully!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful!")
        return username  # Return the logged-in username
    else:
        print("Log in failed")
        return None

def add_item(username):
    item = input("Enter the item name: ")
    quantity = int(input("Enter the quantity: "))

    inventory = inventories[username]  # Access the user's inventory
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"{quantity} of {item} added to inventory.")

def remove_item(username):
    item = input("Enter the item name to remove: ")
    quantity = int(input("Enter the quantity to remove: "))
    inventory = inventories[username]  # Access the user's inventory
    if item in inventory:
        if inventory[item] >= quantity:
            inventory[item] -= quantity
            if inventory[item] == 0:
                del inventory[item]
            print(f"{quantity} of {item} removed from inventory.")
        else:
            print("Not enough stock to remove.")
    else:
        print("Item not found in inventory.")

def view_inventory(username):
    inventory = inventories[username]  # Access the user's inventory
    if inventory:
        print("Current Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    else:
        print("The inventory is empty.")


# Main program loop
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        register()
    elif choice == '2':
        logged_in_user = login()
        if logged_in_user:
            while True:
                print("\n1. View Inventory")
                print("2. Add Item")
                print("3. Remove Item")
                print("4. Logout")

                action = input("Choose an action: ")
                if action == '1':
                    view_inventory(logged_in_user)
                elif action == '2':
                    add_item(logged_in_user)
                elif action == '3':
                    remove_item(logged_in_user)
                elif action == '4':
                    print("Logged out.")
                    break
                else:
                    print("Invalid option.")
    elif choice == '3':
        print("Leaving...")
        break
    