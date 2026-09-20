"""Inventory management.



Sample:

    Add product -> Name: Pen, Price: 10, Quantity: 50

    Total inventory value: 500.00

"""





def read_number(prompt, cast, minimum=0):

    """Keep asking until a valid number >= minimum is entered."""

    while True:

        try:

            value = cast(input(prompt))

        except ValueError:

            print("Invalid input. Try again.")

            continue

        if value < minimum:

            print(f"Value must be at least {minimum}.")

            continue

        return value





def add_product(inventory):

    """Add a new product to the inventory."""

    name = input("Product name: ").strip()

    if not name:

        print("Name cannot be empty.")

        return

    key = name.lower()

    if key in inventory:

        print("Product already exists. Use 'Update quantity' instead.")

        return

    price = read_number("Price: ", float, 0)

    quantity = read_number("Quantity: ", int, 0)

    inventory[key] = {"name": name, "price": price, "quantity": quantity}

    print(f"Added {name}.")





def display_products(inventory):

    """Show all products in a table."""

    if not inventory:

        print("Inventory is empty.")

        return

    print(f"{'Name':<15}{'Price':>10}{'Qty':>8}")

    print("-" * 33)

    for product in inventory.values():

        print(f"{product['name']:<15}{product['price']:>10.2f}{product['quantity']:>8}")





def search_product(inventory):

    """Find a product by name."""

    key = input("Search product name: ").strip().lower()

    product = inventory.get(key)

    if product:

        print(f"Found: {product['name']} | Price: {product['price']:.2f} | Qty: {product['quantity']}")

    else:

        print("Product not found.")





def update_quantity(inventory):

    """Set a new quantity for an existing product."""

    key = input("Product name to update: ").strip().lower()

    if key not in inventory:

        print("Product not found.")

        return

    inventory[key]["quantity"] = read_number("New quantity: ", int, 0)

    print("Quantity updated.")





def calculate_total_value(inventory):

    """Return total value of all stock (price x quantity)."""

    total = 0

    for product in inventory.values():

        total += product["price"] * product["quantity"]

    return total





def main():

    inventory = {}

    while True:

        print("\n--- Inventory Menu ---")

        print("1. Add product\n2. Display products\n3. Search product")

        print("4. Update quantity\n5. Total inventory value\n6. Exit")

        choice = input("Enter choice (1-6): ").strip()



        if choice == "1":

            add_product(inventory)

        elif choice == "2":

            display_products(inventory)

        elif choice == "3":

            search_product(inventory)

        elif choice == "4":

            update_quantity(inventory)

        elif choice == "5":

            print(f"Total inventory value: {calculate_total_value(inventory):.2f}")

        elif choice == "6":

            print("Goodbye!")

            break

        else:

            print("Invalid choice.")





if __name__ == "__main__":

    main()
