from process.save_load import load_application
from datetime import date

timed_alert_list = [
    "One Week Since Applied",
    "Two Weeks Since Applied, Consider Contacting Company",
    "Three Weeks Since Applied",
    "Four Weeks Since Applied",
    "Five Weeks Since Applied, Last Alert",
    "Setting to Inactive",
    "Three Days Until Interview",
    "Two Days Until Interview",
    "One Day Until Interview",
    "Interview Today",
    "Three Days to Apply",
    "Two Days to Apply",
    "Last Day to Apply"
    ]

def alerts():
    apps = load_application()

    milestone_alerts = timed_alert_list[:6]
    interview_alerts = timed_alert_list[6:10]
    deadline_alerts = timed_alert_list[10:13]

    milestones = []
    interviews = []
    deadlines = []

    for app in apps:
        seen = app["Alert Seen"] == "True"

        if (app["Next Alert"] in milestone_alerts and date.fromisoformat(app["Next Alert Date"]) <= date.today()
                and not seen):
            milestones.append(app)
        if (app["Next Alert"] in interview_alerts and date.fromisoformat(app["Next Alert Date"]) <= date.today()
                and not seen):
            interviews.append(app)
        if (app["Next Alert"] in deadline_alerts and date.fromisoformat(app["Next Alert Date"]) <= date.today()
                and not seen):
            deadlines.append(app)

    return milestones, interviews, deadlines


