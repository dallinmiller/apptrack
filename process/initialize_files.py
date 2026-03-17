import csv
import os
from classes.application import Tracker

FIELDS = [
    "ID",
    "Company",
    "Position",
    "Location",
    "Date Applied",
    "Status",
    "Notes",
    "Next Alert",
    "Next Alert Date",
    "Alert Seen",
    "Interview"
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data_files")

def get_filepath(filename="applications.csv"):
    return os.path.join(DATA_DIR, filename)

def initialize_csv(filename="applications.csv"):

    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    filepath = get_filepath(filename)

    if not os.path.exists(filepath):
        with open(filepath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()

def initialize_tracker(filename="applications.csv"):

    filepath = get_filepath(filename)

    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)

            max_ID = 0

            for row in reader:
                current_ID = int(row["ID"])
                if current_ID > max_ID:
                    max_ID = current_ID

    except FileNotFoundError:
        return 0

    tracker = Tracker(max_ID)
    return tracker
