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
            elif choice == '2':
            comp_id = input("Enter Company ID: ")
            results = db_queries.fetch_attendees_by_company(comp_id)
            
            if len(results) == 0:
                print("No records found.")
            else:
                print("Results:")
                for row in results:
                    # Просто печатаем элементы через запятую или пробел
                    print(row[0], "|", row[1], "|", row[2], "|", row[3])
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