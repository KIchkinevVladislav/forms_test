from database.mongo import get_mongo_db


def insert_forms_to_mongo():
    db = get_mongo_db()

    db.forms.insert_many([
    {
        'name': 'Employee data',
        'name_employee': 'text',
        'surname_employee': 'text',
        'email': 'email',
        'phone_number': 'phone',
        'birthday': 'date',
    },
    {
        'name': 'Notification',
        'text': 'text',
        'date': 'date',
    },
    {
        'name': 'Сontractor',
        'name_contractor': 'text',
        'email': 'email',
        'phone_number': 'phone',
    },
])
    
if __name__ == "__main__":
    insert_forms_to_mongo()
