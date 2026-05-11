from config_db import db
import validators
import mysql.connector
from config_neo4j import get_session

# Database query functions
# Each function corresponds to a specific database operation, such as fetching speakers, attendees, adding new attendees, and managing connections between attendees.
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


# This function retrieves speakers and their associated sessions and rooms based on a search term. It uses a SQL query with a JOIN to combine data from the session and room tables, filtering results by speaker name using a LIKE clause for partial matching.
def attendees_by_company(company_id):
    cursor = db.cursor()
    check_sql = "SELECT companyName FROM company WHERE companyID = %s"
    cursor.execute(check_sql, (company_id,))
    company = cursor.fetchone()

    if company is None:
        print(f"*** ERROR *** Company ID {company_id} does not exist")
        cursor.close()
        return False
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
    return True


def add_new_attendee(a_id,a_name, a_dob, a_gen, company_id):
    if validators.is_attendee_existing(a_id):
        print(f"*** ERROR *** Attendee ID: {a_id} already exists")
        return

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


# This function adds a new attendee to the database. It first validates the attendee
def view_connected_attendees(attendee_id):
    cursor = db.cursor()
    cursor.execute("SELECT attendeeName FROM attendee WHERE attendeeID = %s", (int(attendee_id),))
    attendee = cursor.fetchone()

    if attendee is None:
        print("*** ERROR *** Attendee does not exist")
        cursor.close()
        return

    print(f"Attendee Name:  {attendee[0]}")
    print("-" * 20)    
    

    with get_session() as session:
        query = """
        MATCH (a:Attendee {AttendeeID: $id})-[:CONNECTED_TO]-(a2:Attendee)
        RETURN a2.AttendeeID AS id
        """

        results = session.run(query, id=int(attendee_id)) 
        records = list(results)
            
        if not records:
            print("No connections")
        else:
            print("These attendees are connected:")
            for record in records:
                cursor.execute("SELECT attendeeName FROM attendee WHERE attendeeID = %s", (record['id'],))
                name = cursor.fetchone()
                name = name[0] if name else "Unknown"
                print(f"{record['id']} |  {name}")

        cursor.close()

# This function retrieves and displays attendees that are connected to a given attendee ID. It first checks if the attendee exists in the MySQL database, then uses a Cypher query to find connected attendees in the Neo4j graph database. The results are printed in a formatted manner.
def add_attendee_connection(id1, id2):
    cursor = db.cursor()
    
    cursor.execute("SELECT attendeeID FROM attendee WHERE attendeeID IN (%s, %s)", (id1, id2))
    if len(cursor.fetchall()) < 2:
        print("*** ERROR *** One or both attendee IDs do not exist")
        return

    with get_session() as session:
        
        check = "MATCH (a1 {AttendeeID: $id1})-[r:CONNECTED_TO]-(a2 {AttendeeID: $id2}) RETURN r"
        if session.run(check, id1=int(id1), id2=int(id2)).single():
            print("*** ERROR *** These attendees are already connected")
            return


        query = """
        MERGE (a1:Attendee {AttendeeID: $id1})
        MERGE (a2:Attendee {AttendeeID: $id2})
        CREATE (a1)-[:CONNECTED_TO]->(a2)
        """
        session.run(query, id1=int(id1), id2=int(id2))
        print(f"Attendee {id1} is now connected to Attendee {id2}")


# This function creates a connection between two attendees in the Neo4j graph database. It first checks if both attendee IDs exist in the MySQL database, then verifies that they are not already connected in Neo4j. If all checks pass, it uses a Cypher query to create a bidirectional connection between the two attendees.
def view_rooms():
    cursor = db.cursor()
    query = "SELECT roomID, roomName, capacity FROM room ORDER BY roomID"
    cursor.execute(query)
    rooms = cursor.fetchall()

    print(f"{'RoomID':<8} | {'RoomName':<16} | {'Capacity':<8}")
    print("-" * 40)
    for r in rooms:
        print(f"{r[0]:<8} | {r[1]:<16} | {r[2]:<8}")
    cursor.close()

