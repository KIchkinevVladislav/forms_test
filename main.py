import uvicorn
from fastapi import FastAPI

from conf.mongodb import mongodb_config
from app.api.routers import form_routers


app = FastAPI()

app.include_router(form_routers, tags=["forms"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
