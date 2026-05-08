from datetime import date
from process.update_edit import update_value
from process.save_load import load_application, load_application_by_id
from alerts.alerts_ui import alerts_ui

### Alerts are defined by the status of an application. The object all_alerts holds every alert, divided by application
### status.
### Each alert division is a dictionary with the key defining time to or since status date. Keys of form "X" are weekly,
### while keys of form 0.X are daily.


start_alerts = {
    1: "One Week Since Applied",
    2: "Two Weeks Since Applied, Consider Contacting Company",
    3: "Three Weeks Since Applied",
    4: "Four Weeks Since Applied",
    5: "Five Weeks Since Applied, Last Alert",
    "Inactive": "Setting to Inactive"
}

interview_alerts = {
    -2: "Two Weeks Until Interview",
    -1: "Less than One Week Until Interview",
    -0.3: "Three Days Until Interview",
    -0.2: "Two Days Until Interview",
    -0.1: "One Day Until Interview",
    0: "Interview Today",
    1: "One Week Since Interview",
    2: "Two Weeks Since Interview",
    3: "Three Weeks Since Interview",
    4: "Four Weeks Since Interview",
    5: "Five Weeks Since Interview, Last Alert",
    "Inactive": "Setting to Inactive"
}

deadline_alerts = {
    -2: "Two Weeks to Apply",
    -1: "Less than One Week to Apply",
    -0.3: "Three Days to Apply",
    -0.2: "Two Days to Apply",
    -0.1: "Last Day to Apply",
    "Inactive": "Application Day Missed, Setting to Inactive."
}

misc_alerts = {
    1: "One Week Since Last Alert",
    2: "Two Weeks Since Last Alert",
    3: "Three Weeks Since Last Alert",
    4: "Four Weeks Since Last Alert, Last Alert",
    "Inactive": "Setting to Inactive"
}

### Alerts stored here
all_alerts = [start_alerts, interview_alerts, deadline_alerts, misc_alerts]

### Find time from or to status date. -X means date is in the future, +X means date is in the past.
def get_alert_time(app):
    alert_days = (date.today() - date.fromisoformat(app["Status Date"])).days
    if -3 < alert_days < 3:
        return alert_days * 0.1
    else:
        return alert_days // 7 + 1 if alert_days > 1 else alert_days // 7

def status_update(app, alert_index, alert_time, potential_alert):
    if potential_alert == all_alerts[alert_index]["Inactive"]:
        update_value(app["ID"], "Status", "Inactive")
    elif app["Status"] == "Interview" and alert_time >= 0:
        update_value(app["ID"], "Status", "Awaiting Response")

### Creates a list of alerts, and makes necessary updates.
def general_updates():
    apps = load_application()
    alert_list = [[], [], [], []]

    alert_status = {
        "Applied": 0,
        "Interview": 1,
        "Awaiting Response": 1,
        "Deadline": 2
    }

    for app in apps:
        if app["Status"] in alert_status:
            alert_index = alert_status[app["Status"]]
        else:
            alert_index = 3
        alert_time = get_alert_time(app)
        if (alert_index == 0 or alert_index == 3) and alert_time < 1:
            alert_time = None
        elif 0 < alert_time < 1:
            alert_time = 0
        try:
            potential_alert = all_alerts[alert_index][alert_time]
        except (KeyError, IndexError):
            if alert_time is None or alert_time < 0:
                potential_alert = app["Current Alert"]
            else:
                potential_alert = all_alerts[alert_index]["Inactive"]

        if potential_alert != app["Current Alert"]:
            status_update(app, alert_index, alert_time, potential_alert)
            update_value(app["ID"], "Alert Seen", "False")
            update_value(app["ID"], "Current Alert", potential_alert)
            alert_list[alert_index].append(load_application_by_id(app["ID"]))

    alerts_ui(alert_list)
