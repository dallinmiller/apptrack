from datetime import date, timedelta
from process.update_edit import update_value
from process.save_load import load_application
from alerts.alerts import timed_alert_list

def alert_updates(app, alert, new_status, time_change=timedelta(days=1)):
    if app["Next Alert"] == alert:
        update_value(app["ID"], "Status", new_status)
        update_value(app["ID"], "Next Alert", "")
        update_value(app["ID"], "Next Alert Date", "")
        update_value(app["ID"], "Alert Seen", "")
    else:
        update_value(
            app["ID"],
      "Next Alert",
            timed_alert_list[timed_alert_list.index(app["Next Alert"]) + 1]
        )

        update_value(
            app["ID"],
      "Next Alert Date",
            (date.fromisoformat(app["Next Alert Date"]) + time_change).isoformat()
        )

def post_alert_update(milestones, interviews, deadlines):
    for app in milestones:
        alert_updates(app, alert="Setting to Inactive", new_status="inactive", time_change=timedelta(weeks=1))
    for app in interviews:
        alert_updates(app, alert="Interview Today", new_status="Awaiting Response")
    for app in deadlines:
        alert_updates(app, alert="Last Day to Apply", new_status="Inactive")

def general_updates():
    apps = load_application()

    milestone_alerts = timed_alert_list[:6]
    interview_alerts = timed_alert_list[6:10]
    deadline_alerts = timed_alert_list[10:13]

    milestones = []
    interviews = []
    deadlines = []

    for app in apps:
        if app["Next Alert"] in milestone_alerts and date.fromisoformat(app["Next Alert Date"]) > date.today():
            milestones.append(app)
        if app["Next Alert"] in interview_alerts and date.fromisoformat(app["Next Alert Date"]) > date.today():
            interviews.append(app)
        if app["Next Alert"] in deadline_alerts and date.fromisoformat(app["Next Alert Date"]) > date.today():
            deadlines.append(app)

    for app in milestones:
        alert_updates(app, alert="Setting to Inactive", new_status="inactive", time_change=timedelta(weeks=1))
    for app in interviews:
        alert_updates(app, alert="Interview Today", new_status="Awaiting Response")
    for app in deadlines:
        alert_updates(app, alert="Last Day to Apply", new_status="Inactive")
