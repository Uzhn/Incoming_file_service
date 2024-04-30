import datetime
import os
from src.models import Flight
from src.services.flight_processing import FlightProcessor
from tests.fixtures import folders


def test_move_file(tmp_path, folders):
    file_path = os.path.join(folders["in_folder"], "temp_file.csv")
    with open(file_path, "w") as f:
        f.write("")
    processor = FlightProcessor(session=None)
    processor.move_file(file_path, folders["ok_folder"])

    assert os.path.exists(os.path.join(folders["ok_folder"], "temp_file.csv"))
    assert not os.path.exists(file_path)


def test_save_to_database(session):
    processor = FlightProcessor(session)
    expected_date = datetime.date(2024, 4, 30)
    processor.save_to_database(session, "test_file.csv", "2024-04-30", 123, "XYZ")
    flights = session.query(Flight).all()
    assert len(flights) == 1
    assert flights[0].file_name == "test_file.csv"
    assert flights[0].fit == 123
    assert flights[0].dep_date == expected_date
    assert flights[0].dep == "XYZ"
