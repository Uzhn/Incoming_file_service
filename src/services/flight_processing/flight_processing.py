import os
import json
import shutil
import logging

from .csv_parse import CSVParser
from src.core.constants import IN_FOLDER, OK_FOLDER, ERR_FOLDER, OUT_FOLDER
from src.api.schemas import FlightSchema
from src.models import Flight

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)


class FlightProcessor:
    def __init__(self, session):
        self.in_folder = IN_FOLDER
        self.out_folder = OUT_FOLDER
        self.ok_folder = OK_FOLDER
        self.err_folder = ERR_FOLDER
        self.session = session

    def process_file(self, file_path):
        try:
            parser = CSVParser(file_path)
            file_name, flight_date, flight_number, departure_airport, json_data = (
                parser.parse()
            )

            self.save_to_database(
                self.session, file_name, flight_date, flight_number, departure_airport
            )
            self.move_file(file_path, self.ok_folder)
            self.create_json_file(
                file_path, flight_date, flight_number, departure_airport, json_data
            )
            logging.info(f"File {os.path.basename(file_path)} processed successfully.")

        except Exception as e:
            logging.error(f"Error processing file {file_path}: {str(e)}")
            self.move_file(file_path, self.err_folder)

    def save_to_database(
        self, db, file_path, flight_date, flight_number, departure_airport
    ):
        flight = FlightSchema(
            file_name=file_path,
            fit=flight_number,
            dep_date=flight_date,
            dep=departure_airport,
        )
        db_flight = Flight(**flight.dict())
        db.add(db_flight)
        db.commit()

    def move_file(self, file_path, destination_folder):
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(file_path, destination_path)

    def create_json_file(
        self, file_path, flight_date, flight_number, departure_airport, data
    ):
        json_data = {
            "fit": int(flight_number),
            "flight_date": flight_date.strftime("%Y-%m-%d"),
            "dep": departure_airport,
            "prl": data,
        }
        json_file_name = os.path.basename(file_path).replace(".csv", ".json")
        json_file_path = os.path.join(self.out_folder, json_file_name)
        with open(json_file_path, "w") as json_file:
            json.dump(json_data, json_file, indent=4)
