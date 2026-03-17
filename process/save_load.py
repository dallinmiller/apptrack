from process.initialize_files import FIELDS, get_filepath
import csv

def save_application(app, filename="applications.csv"):

    filepath = get_filepath(filename)

    with open(filepath, "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow(app.application_data)

def load_application(filename="applications.csv"):

    filepath = get_filepath(filename)

    apps = []

    with open(filepath, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            apps.append(row)

    return apps

