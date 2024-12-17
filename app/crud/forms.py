from pymongo.database import Database


def get_form_name_from_mongo(db: Database, filter: dict) -> str | None:
    
    form = db.forms.find_one(filter)

    return form.get('name') if form is not None else None
