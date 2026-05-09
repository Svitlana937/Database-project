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
                    print(row[0], "|", row[1], "|", row[2], "|", row[3])

        elif choice == '3':
            elif choice == '3':
                id = input("Enter attendee ID: ")
                name = input("Enter attendee name: ")
                dob = input("Enter date of birth (YYYY-MM-DD): ")
                gender = input("Enter gender: ")
                company_id = input("Enter company ID: ")
                db_queries.add_new_attendee(id, name, dob, gender, company_id)

        elif choice == '4':
            attendee_id = input("Enter Attendee ID : ")
            
            if attendee_id.isdigit():
                db_operations.view_connected_attendees(attendee_id)
            else:
                print("*** ERROR *** Attendee ID must be a number")
        elif choice == '5':
            while True:
                id1 = input("Enter Attendee 1 ID : ")
                id2 = input("Enter Attendee 2 ID : ")

                if not id1.isdigit() or not id2.isdigit():
                    print("*** ERROR *** Attendee IDs must be numbers")
                elif id1 == id2:
                    print("*** ERROR *** An attendee cannot connect to him/herself")
                else:
                    db_operations.add_attendee_connection(id1, id2)
                    break
        elif choice == '6':
            print("Loading Rooms...")
        elif choice == 'x':
            print("Closing application.")
            status = False
        else:
            print("Invalid option, try again.")

            

if __name__ == "__main__":
    run()