from process.update_edit import update_value
from alerts.alerts import alerts
from menus.menu_creator import get_continue, clear_screen

def alerts_ui():
  
    milestones, interviews, deadlines = alerts()
    if len(milestones) + len(interviews) + len(deadlines) == 0:
        print("No Alerts to Report.")
    if len(milestones) != 0:
        print("Milestones: \n")
        for app in milestones:
            print(f"{app['Position']} at {app['Company']} - {app['Next Alert']}")
            update_value(app["ID"], "Alert Seen", "True")
        print("")
        print("-" * 9)
        print("")
    if len(interviews) != 0:
        print("Interviews: \n")
        for app in interviews:
            print(f"{app['Position']} at {app['Company']} - {app['Next Alert']}")
            update_value(app["ID"], "Alert Seen", "True")
        print("")
        print("-" * 9)
        print("")
    if len(deadlines) != 0:
        print("Deadlines: \n")
        for app in deadlines:
            print(f"{app['Position']} at {app['Company']} - {app['Next Alert']}")
            update_value(app["ID"], "Alert Seen", "True")
        print("")
        print("-" * 9)
        print("")

    get_continue()
    clear_screen()

