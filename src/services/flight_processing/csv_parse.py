import csv
import os
import json
from datetime import datetime


class CSVParser:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def parse(self):
        file_name = os.path.basename(self.csv_file)
        file_name_parts = file_name.split("_")
        flight_date = datetime.strptime(file_name_parts[0], "%Y%m%d").date()
        flight_number = file_name_parts[1]
        departure_airport = file_name_parts[2].split(".")[0]

        data = []
        with open(self.csv_file, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                bdate_str = row["bdate"]
                bdate_obj = datetime.strptime(bdate_str, "%d%b%y")
                row["bdate"] = bdate_obj.strftime("%Y-%m-%d")
                data.append(row)
        return file_name, flight_date, flight_number, departure_airport, data
