import interface
import db_queries
import validators

def run():
    status = True
    while status:
        interface.show_menu()
        choice = input("Your choice: ")

        if choice == '1':
            name = input("Enter speaker name : ")
            results = db_queries.fetch_speakers_and_sessions(name)
            print(f"Session Details for : {name}")
            print("-"*30)
            print("No speakers found of that name")
            for speaker, title, room in results:
                print(f" {speaker} | {title} | {room}")

        elif choice == '2':
            while True:
                comp_id = input("Enter Company ID : ")
                if not comp_id.isdigit() or int(comp_id) <= 0:
                    continue
                result = db_queries.attendees_by_company(comp_id)
                if result is False:
                    continue
                break

        elif choice == '3':
                print("Add New Attendee")
                print("-"*30)
                id = input("Attendee ID: ")
                name = input("Name: ")
                dob = input("DOB: ")
                gender = input("Gender: ")
                company_id = input("Company ID: ")
                db_queries.add_new_attendee(id, name, dob, gender, company_id)

        elif choice == '4':
            attendee_id = input("Enter Attendee ID : ")
            
            if attendee_id.isdigit():
                db_queries.view_connected_attendees(attendee_id)
            else:
                print("*** ERROR *** Attendee ID must be a number")


        elif choice == '5':
            while True:
                id1 = input("Enter Attendee 1 ID : ")
                id2 = input("Enter Attendee 2 ID : ")

                if not id1.isdigit() or not id2.isdigit():
                    print("*** ERROR *** Attendee IDs must be numbers")
                    print()
                    continue

                if id1 == id2:
                    print("*** ERROR *** An attendee cannot connect to him/herself")
                    print()
                    continue

                if db_queries.add_attendee_connection(id1, id2):
                    break


        elif choice == '6':
            db_queries.view_rooms()
            
        elif choice == 'x':
            print("Closing application.")
            status = False
        else:
            print("Invalid option, try again.")

            

if __name__ == "__main__":
    run()