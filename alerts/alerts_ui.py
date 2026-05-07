from process.update_edit import update_value
from process.save_load import load_application
from menus.menu_creator import get_continue, clear_screen

### Divides applications alerts based on where the application is on the timeline.
def alerts(alert_list):
    milestones = []
    interviews = []
    deadlines = []
    misc = []

    for app, alert in alert_list:
        if app["Alert Seen"] != "True":
            if app["Status"] == "Applied":
                milestones.append(app)
            if app["Status"] == "Interview" or app["Status"] == "Awaiting Response":
                interviews.append(app)
            if app["Status:"] == "Deadline":
                deadlines.append(app)
            else:
                misc.append(app)

    return milestones, interviews, deadlines, misc

### Simple UI to load alerts.
def alerts_ui(alert_list):
    milestones, interviews, deadlines, misc = alerts(alert_list)
    if len(milestones) + len(interviews) + len(deadlines) + len(misc) == 0:
        print("No Alerts to Report.")
    if len(milestones) != 0:
        print("Milestones: \n")
        for app in milestones:
            print(f"{app['Position']} at {app['Company']} - {app['Current Alert']}")
            update_value(app["ID"], "Alert Seen", "True")
        print("")
        print("-" * 9)
        print("")
    if len(interviews) != 0:
        print("Interviews: \n")
        for app in interviews:
            print(f"{app['Position']} at {app['Company']} - {app['Current Alert']}")
            update_value(app["ID"], "Alert Seen", "True")
        print("")
        print("-" * 9)
        print("")
    if len(deadlines) != 0:
        print("Deadlines: \n")
        for app in deadlines:
            print(f"{app['Position']} at {app['Company']} - {app['Current Alert']}")
            update_value(app["ID"], "Alert Seen", "True")
        print("")
        print("-" * 9)
        print("")
    if len(misc) != 0:
        print("misc: \n")
        for app in misc:
            print(f"{app['Position']} at {app['Company']} - {app['Current Alert']}")
            update_value(app["ID"], "Alert Seen", "True")
        print("")
        print("-" * 9)
        print("")

    get_continue()
    clear_screen()

