"""Shopping cart.



Sample:

    Add -> Apple x3 | View -> Apple x3 @ 30.00 = 90.00 | Bill -> Total: 90.00

"""



CATALOG = {"apple": 30.0, "milk": 55.0, "bread": 40.0, "eggs": 8.0, "rice": 70.0}





def show_catalog():

    """Print products available to buy."""

    print("\nAvailable products:")

    for name, price in CATALOG.items():

        print(f"  {name.capitalize():<8} {price:.2f}")





def read_quantity():

    """Read a positive integer quantity, or return None if invalid."""

    try:

        quantity = int(input("Quantity: "))

    except ValueError:

        print("Quantity must be a whole number.")

        return None

    if quantity <= 0:

        print("Quantity must be greater than 0.")

        return None

    return quantity





def add_product(cart):

    """Add a catalog product to the cart."""

    show_catalog()

    name = input("Product name: ").strip().lower()

    if name not in CATALOG:

        print("Product not available.")

        return

    quantity = read_quantity()

    if quantity is None:

        return

    cart[name] = cart.get(name, 0) + quantity

    print(f"Added {quantity} x {name.capitalize()}.")





def remove_product(cart):

    """Remove a product (or some quantity of it) from the cart."""

    if not cart:

        print("Cart is empty.")

        return

    name = input("Product to remove: ").strip().lower()

    if name not in cart:

        print("That product is not in your cart.")

        return

    quantity = read_quantity()

    if quantity is None:

        return

    if quantity >= cart[name]:

        del cart[name]

        print(f"Removed {name.capitalize()} completely.")

    else:

        cart[name] -= quantity

        print(f"Removed {quantity} x {name.capitalize()}.")





def view_cart(cart):

    """Print cart contents with line totals."""

    if not cart:

        print("Your cart is empty.")

        return

    print("\n--- Your Cart ---")

    for name, quantity in cart.items():

        line_total = CATALOG[name] * quantity

        print(f"{name.capitalize():<8} x{quantity:<3} @ {CATALOG[name]:.2f} = {line_total:.2f}")





def calculate_bill(cart):

    """Return the total bill."""

    total = 0

    for name, quantity in cart.items():

        total += CATALOG[name] * quantity

    return total





def main():

    cart = {}

    running = True



    while running:

        print("\n--- Shopping Cart ---")

        print("1. Add product\n2. Remove product\n3. View cart")

        print("4. Calculate bill\n5. Exit")

        choice = input("Enter choice (1-5): ").strip()



        if choice == "1":

            add_product(cart)

        elif choice == "2":

            remove_product(cart)

        elif choice == "3":

            view_cart(cart)

        elif choice == "4":

            view_cart(cart)

            print(f"Total bill: {calculate_bill(cart):.2f}")

        elif choice == "5":

            print("Thanks for shopping!")

            running = False

        else:

            print("Invalid choice.")





if __name__ == "__main__":

    main()
