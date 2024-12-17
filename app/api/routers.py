from fastapi import APIRouter, Request, HTTPException

from database.mongo import get_mongo_db
from app.utils.validate_form_value import validate_value
from app.crud.forms import get_form_name_from_mongo


form_routers = APIRouter()


@form_routers.post("/get_form")
async def get_form(request: Request):
    try:
        form_data = await request.form()

        validation_request_form = {key: validate_value(value) for key, value in form_data.items()}

        form_name = get_form_name_from_mongo(get_mongo_db(), validation_request_form)

        return form_name if form_name is not None else validation_request_form
    except Exception:
        raise HTTPException(status_code=500, detail='Что-то пошло не так, попробуйте снова')
