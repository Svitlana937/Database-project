from mysql_connection import mydb

def validate_attendee_id(attendee_id):
    if not attendee_id.isdigit():
        print("Attendee ID must be a number.")
        return False
    return True 

def is_company_id_valid(company_id):    
    cursor = mydb.cursor()
    cursor.execute("SELECT companyID FROM company WHERE companyID = %s", (int(company_id),))
    result = cursor.fetchone()
    if result is None:
        print("Company ID does not exist.")
        return False
    return True
    cursor.close()