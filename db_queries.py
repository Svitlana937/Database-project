from config_db import cursor

def fetch_speakers_and_sessions(search_term):    
    sql = """
    SELECT s.speakerName, s.sessionTitle, r.roomName
    FROM session s
    JOIN room r ON s.roomID = r.roomID
    WHERE s.speakerName LIKE %s
    """
    cursor.execute(sql, (f"%{search_term}%",))
    return cursor.fetchall()

def attendees_by_company(company_id):
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
    return cursor.fetchall()