from process.initialize_files import FIELDS, get_filepath
import csv

def update_value(app_id, field, new_value, filename="applications.csv"):

    if field not in FIELDS:
        raise ValueError(f"Field {field} not found.")

    filepath = get_filepath(filename)

    rows = []

    with open(filepath, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["ID"] == str(app_id):
                row[field] = new_value
            rows.append(row)

    with open(filepath, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
