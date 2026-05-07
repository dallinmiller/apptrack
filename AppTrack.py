from process.initialize_files import *
from menus.main_menu import main_menu
from alerts.alerts_ui import alerts_ui
from alerts.update_data import general_updates


initialize_csv()
tracker = initialize_tracker()

if __name__ == "__main__":
    general_updates()
    main_menu(tracker)
