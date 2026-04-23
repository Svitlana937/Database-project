import interface

def run():
    status = True
    while status:
        interface.show_menu()
        choice = input("Your choice: ")

        if choice == '1':
            print("Loading Speakers...")
        elif choice == '6':
            print("Loading Rooms...")
        elif choice == 'x':
            print("Closing application.")
            status = False
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    run()