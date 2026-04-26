import interface

def run():
    status = True
    while status:
        interface.show_menu()
        choice = input("Your choice: ")

        if choice == '1':
            print("Loading Speakers...")
        elif choice == '2':
            print("Loading Attendees by Company...")
        elif choice == '3':
            print("Loading New Attendees...")
        elif choice == '4':
            print("Loading Connected Attendees...")
        elif choice == '5':
            print("Loading Attendee Connection...")
        elif choice == '6':
            print("Loading Rooms...")
        elif choice == 'x':
            print("Closing application.")
            status = False
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    run()