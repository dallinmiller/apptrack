from datetime import date, timedelta

# Company, Position, Location, Date Applied, Status, Notes
# Status: Applied, Rejected, Interview, Awaiting Response, Accepted, Inactive

class Tracker:
    def __init__(self, starting_ID=0):
        self.ID_tracker = starting_ID

    def return_ID(self):
        self.ID_tracker = self.ID_tracker + 1
        return self.ID_tracker

class Application:
    def __init__(
            self, tracker, company, position="Engineering Intern", city="Logan", state="Utah", date_applied=None,
            status="Applied", notes=None
    ):
        self.ID = tracker.return_ID()
        self.company = company
        self.position = position
        self.city = city
        self.state = state
        self.location = f"{city}, {state}"
        self.date_applied = (date.today().isoformat() if date_applied is None else date_applied)
        self.status = status
        self.notes = notes

        self.next_alert = "One Week Since Applied"
        self.next_alert_date = (date.fromisoformat(self.date_applied) + timedelta(weeks=1)).isoformat()
        self.alert_seen = False

        self.interview = False

        self.application_data = {
            "ID": self.ID,
            "Company": self.company,
            "Position": self.position,
            "Location": self.location,
            "Date Applied": self.date_applied,
            "Status": self.status,
            "Notes": self.notes,
            "Next Alert": self.next_alert,
            "Next Alert Date": self.next_alert_date,
            "Alert Seen": self.alert_seen,
            "Interview": self.interview
        }

    def __str__(self):
        return f"{self.ID}: {self.company} - {self.position} ({self.status})"


