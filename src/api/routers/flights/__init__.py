from fastapi import APIRouter

from src.api.routers.flights.upload_csv import upload_csv
from src.api.routers.flights.flights import get_flights

flights_router = APIRouter(
    tags=["Flights"],
)


flights_router.post("/upload_csv")(upload_csv)
flights_router.get("/flights")(get_flights)
