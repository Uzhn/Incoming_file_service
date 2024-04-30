import csv
import os
import pytest


@pytest.fixture
def csv_file(tmp_path):
    csv_file_path = os.path.join(tmp_path, "20240101_123_XYZ.csv")
    with open(csv_file_path, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["bdate"])
        writer.writeheader()
        writer.writerow({"bdate": "01Jan21"})
        writer.writerow({"bdate": "02Feb21"})
    return csv_file_path
