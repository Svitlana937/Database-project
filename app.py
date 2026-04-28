import interface

def run():
    status = True
    while status:
        interface.show_menu()
        choice = input("Your choice: ")

        if choice == '1':
            name = input("Search for speaker: ")
            results = db_queries.fetch_speakers_and_sessions(name)
            print(f"\n--- Results for '{name}' ---")
            for speaker, title, room in results:
                print(f"[*] {speaker} | Session: {title} | Room: {room}")
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