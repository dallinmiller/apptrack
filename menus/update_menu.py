from menus.menu_creator import get_int, create_menu
from process.update_edit import update_value
from menus.add_application import parse_date
from datetime import date, timedelta

def update_menu(tracker):

    ID = get_int("ID #: ", 1, max_value=tracker.ID_tracker)

    prompt = "Choose New Status: "
    options = ["Not Applied", "Applied", "Interview", "Offer", "Accepted", "Rejected"]
    choice = create_menu(prompt, options)

    new_status = options[int(choice) - 1]

    update_value(ID, "Status", new_status)

    if choice == 3:
        while True:
            interview_date = input(f"Input Interview Date (YYYY-MM-DD or YYYYMMDD): ")
            if parse_date(interview_date):
                break
        update_value(ID, "Next Alert", "Three Days Until Interview")
        update_value(ID, "Next Alert Date", (date.fromisoformat(interview_date) - timedelta(days=3)))
        update_value(ID, "Alert Seen", "False")
        update_value(ID, "Interview", "True")
