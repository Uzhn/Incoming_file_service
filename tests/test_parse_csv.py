import datetime
from src.services.flight_processing import CSVParser
from .fixtures import csv_file


def test_csv_parser(csv_file):
    parser = CSVParser(csv_file)
    file_name, flight_date, flight_number, departure_airport, data = parser.parse()

    assert file_name == "20240101_123_XYZ.csv"
    assert flight_date == datetime.date(2024, 1, 1)
    assert flight_number == "123"
    assert departure_airport == "XYZ"
    assert len(data) == 2
    assert data[0]["bdate"] == "2021-01-01"
    assert data[1]["bdate"] == "2021-02-02"
