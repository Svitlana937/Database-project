from config_db import db

def validate_attendee_id(attendee_id):
    if not attendee_id.isdigit():
        #print("Attendee ID must be a number.")
        return False
    return True

def is_company_id_valid(company_id):    
    cursor = db.cursor()
    cursor.execute("SELECT companyID FROM company WHERE companyID = %s", (int(company_id),))
    result = cursor.fetchone()
    cursor.close()
    
    if result is None:
        print("*** ERROR *** Company ID does not exist.")
        return False
    return True
    

def gender_validation(gender):
    valid_genders = ['Male', 'Female']
    if gender not in valid_genders:
        print(f"*** ERROR *** Gender must be Male/Female")
        return False
    return True 


def is_attendee_existing(attendee_id):
    cursor = db.cursor()
    cursor.execute("SELECT attendeeID FROM attendee WHERE attendeeID = %s", (int(attendee_id),))
    result = cursor.fetchone()
    cursor.close()
    if result is None:
        return False
    return True