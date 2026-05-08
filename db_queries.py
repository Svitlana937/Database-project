from config_db import db
import validators
import mysql.connector
from config_neo4j import get_session


def fetch_speakers_and_sessions(search_term):   
    cursor = db.cursor() 
    sql = """
    SELECT s.speakerName, s.sessionTitle, r.roomName
    FROM session s
    JOIN room r ON s.roomID = r.roomID
    WHERE s.speakerName LIKE %s
    """
    cursor.execute(sql, (f"%{search_term}%",))
    results = cursor.fetchall()
    cursor.close()
    return results

def attendees_by_company(company_id):
    cursor = db.cursor()
    check_sql = "SELECT companyName FROM company WHERE companyID = %s"
    cursor.execute(check_sql, (company_id,))
    company = cursor.fetchone()

    if company is None:
        print(f"*** ERROR *** Company ID {company_id} does not exist")
        cursor.close()
        return
    print(f"\n{company[0]} Attendees")

    sql = """
    SELECT a.attendeeName, a.attendeeDOB, s.sessionTitle, s.speakerName, s.sessionDate, r.roomName
    FROM attendee a
    JOIN company c      ON a.attendeeCompanyID = c.companyID
    JOIN registration rg ON a.attendeeID = rg.attendeeID
    JOIN session s      ON rg.sessionID = s.sessionID
    JOIN room r         ON s.roomID = r.roomID
    WHERE c.companyID = %s
    ORDER BY a.attendeeName
    """
    cursor.execute(sql, (company_id,))
    results = cursor.fetchall()

    if not results:
        print(f"No registration records found for {company[0]}")  
    else:                                         
        for row in results:
            print(f"{row[0]} | DOB: {row[1]} | Session: {row[2]} | Speaker: {row[3]}") 
            
    cursor.close()


def add_new_attendee(a_id,a_name, a_dob, a_gen, company_id):
    if not validators.validate_attendee_id(a_id):
        return
    
    if not validators.gender_validation(a_gen):
        return

    if not validators.is_company_id_valid(company_id):
        return

    try:
        cursor = db.cursor()

        query = "INSERT INTO attendee (attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID) VALUES (%s, %s, %s, %s, %s)"
        values = (a_id, a_name, a_dob, a_gen, company_id)

        cursor.execute(query, values)
        db.commit()

        print("Attendee successfully added")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"\n*** DATABASE ERROR *** {err}")


def view_connected_attendees(attendee_id):
    cursor = db.cursor()
    cursor.execute("SELECT attendeeName FROM attendee WHERE attendeeID = %s", (attendee_id,))
    attendee = cursor.fetchone()
    
    if attendee:
        print(f"Attendee Name: {attendee[0]}")        
        query = "MATCH (a1:Attendee {attendeeID: $id})-[:CONNECTED_TO]-(a2:Attendee) RETURN a2.attendeeID AS id, a2.attendeeName AS name"
        RETURN a2.attendeeID AS id, a2.attendeeName AS name"

        with get_session() as session:
            results = session.run(query, id=attendee_id) 
            records = list(results)
            
            if records:
                print("These attendees are connected:")
                for record in records:
                    print(f"{record['id']} | {record['name']}")
            else:
                print("No connections found.")
    else:
        print("Attendee not found.")