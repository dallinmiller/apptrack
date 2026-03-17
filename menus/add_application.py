from classes.application import Application
from menus.menu_creator import get_yes_no, clear_screen
from datetime import date

def optional_input(prompt):
    value = input(prompt).strip()
    return value if value else None

def parse_date(date_string):
    if date_string is None:
        return True
    try:
        date.fromisoformat(date_string)
        return True
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD or YYYYMMDD.")
        return False

def create_application(tracker):

    while True:
        while True:
            company = input("Company: ").strip()
            if company:
                break
            print("Company name is required.")

        position = optional_input("Position (default Engineering Intern): ")
        city = optional_input("City (default Logan): ")
        state = optional_input("State (default Utah): ")
        while True:
            date_applied = optional_input(f"Date (default {date.today().isoformat()}): ")
            if parse_date(date_applied):
                break
        
        notes = optional_input("Notes: ")
        clear_screen()

        kwargs = {}

        if position:
            kwargs["position"] = position
        if city:
            kwargs["city"] = city
        if state:
            kwargs["state"] = state
        if date_applied:
            kwargs["date_applied"] = date_applied
        if notes:
            kwargs["notes"] = notes

        app = {
            "Company": company,
            "Position": position,
            "Location": f"{city}, {state}",
            "Date Applied": date_applied,
            "Notes": notes
        }

        print(f"Company: {app['Company']}; Position: {app['Position']}; Location: {app['Location']}; "
              f"Date Applied: {app['Date Applied']}; Notes: {app['Notes']}")
        if get_yes_no("Is this information correct? (y/n) "):
            break
        else:
            clear_screen()

    ap = Application(tracker, company, **kwargs)

    return ap
