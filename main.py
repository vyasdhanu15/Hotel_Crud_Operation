from fastapi import FastAPI
from routes import hotel_routes

app = FastAPI(title="Hotel CRUD API", version="1.0.0")

app.include_router(hotel_routes.router)

@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to the Hotel CRUD API! Head over to /docs to test endpoints."}