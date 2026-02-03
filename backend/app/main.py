from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import users_router, hardware_router, loans_router
from app.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hardware Inventory")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(hardware_router)
app.include_router(loans_router)