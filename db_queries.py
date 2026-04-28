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