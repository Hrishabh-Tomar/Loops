"""Mini authentication system.



Sample:

    Username: admin  Password: wrong -> Failed. Attempts left: 2

    Username: admin  Password: Super30@123 -> Login successful!

"""



USERNAME = "admin"

PASSWORD = "Super30@123"

MAX_ATTEMPTS = 3





def login():

    """Give the user up to MAX_ATTEMPTS tries. Return True on success."""

    attempts = 0                          # initialization

    while attempts < MAX_ATTEMPTS:        # condition: attempts remain

        username = input("Username: ").strip()

        password = input("Password: ")

        attempts += 1                     # update: guarantees the loop ends



        if username == USERNAME and password == PASSWORD:

            print("Login successful!")

            return True



        remaining = MAX_ATTEMPTS - attempts

        if remaining > 0:

            print(f"Login failed. Attempts left: {remaining}")

        else:

            print("Login failed. Maximum attempts reached. Account locked.")

    return False





def user_session():

    """Logged-in menu. Returns when the user logs out."""

    print(f"\nWelcome, {USERNAME}!")

    while True:

        print("\n--- Dashboard ---")

        print("1. View profile\n2. Logout")

        choice = input("Enter choice (1-2): ").strip()

        if choice == "1":

            print(f"Logged in as: {USERNAME}")

        elif choice == "2":

            print("Logged out successfully.")

            return

        else:

            print("Invalid choice.")





def main():

    while True:

        print("\n--- Authentication System ---")

        print("1. Login\n2. Exit")

        choice = input("Enter choice (1-2): ").strip()



        if choice == "1":

            if login():

                user_session()

            else:

                retry = input("Do you want to retry? (y/n): ").strip().lower()

                if retry != "y":          # retry logic

                    print("Goodbye!")

                    break

        elif choice == "2":

            print("Goodbye!")

            break

        else:

            print("Invalid choice.")





if __name__ == "__main__":

    main()
