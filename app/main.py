from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apis.v1.records import records
from apis.v1.users import users
from repo.db import engine, Base
from create_admin import createadmin

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://your-frontend-domain.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(records)
app.include_router(users)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    createadmin()

def get_app():
    return app