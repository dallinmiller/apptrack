from menus.menu_creator import create_menu
from menus.add_application import create_application
from menus.view_applications import view_applications
from menus.stats_menu import stats_ui
from menus.update_menu import update_menu
from process.save_load import *

def main_menu(tracker):
    while True:
        prompt = "Internship Tracker"
        options = ["Add Application", "View Applications", "Update Status", "Stats", "Exit"]
        choice = create_menu(prompt, options)

        if choice == 1:
            new_app = create_application(tracker)
            save_application(new_app)
        if choice == 2:
            view_applications()
        if choice == 3:
            update_menu(tracker)
        if choice == 4:
            stats_ui()
        if choice == 5:
            break
        else:
            print("Please select an option")
