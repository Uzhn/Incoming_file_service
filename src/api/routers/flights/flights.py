from fastapi import Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.models import Flight


def get_flights(date: str = Query(), db: Session = Depends(get_db)):
    flights = db.query(Flight).filter(Flight.dep_date == date).all()
    if not flights:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No flights found for the given date",
        )
    return flights
