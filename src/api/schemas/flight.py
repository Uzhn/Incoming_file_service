import datetime
from pydantic import BaseModel


class FlightSchema(BaseModel):
    file_name: str
    fit: int
    dep_date: datetime.date
    dep: str
