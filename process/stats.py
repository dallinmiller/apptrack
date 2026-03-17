from process.save_load import load_application

def statistics():
    apps = load_application()

    total_applications = 0
    responded_applications = 0
    rejected_applications = 0
    inactive_applications = 0
    total_interviews = 0
    active_interviews = 0
    offers = 0

    for app in apps:
        total_applications += 1
        if app["Status"] == "Rejected":
            rejected_applications += 1
        elif app["Status"] == "Interview":
            responded_applications += 1
            active_interviews += 1
        elif app["Status"] == "Awaiting Response":
            responded_applications += 1
        elif app["Status"] == "Accepted":
            responded_applications += 1
            offers += 1
        elif app["Status"] == "Inactive":
            inactive_applications += 1
        if app["Interview"] == "True":
            total_interviews += 1
            if app["Status"] == "Interview":
                active_interviews += 1

    response_rate = round((responded_applications / total_applications) * 100, 2)
    interview_rate = round((total_interviews / total_applications) * 100, 2)
    offer_rate = round((offers / total_applications) * 100, 2)
    rejected_rate = round((rejected_applications / total_applications) * 100, 2)
    inactive_rate = round((inactive_applications / total_applications) * 100, 2)


    return (total_applications, responded_applications, rejected_applications, inactive_applications, total_interviews,
            active_interviews, offers, response_rate, interview_rate, offer_rate, rejected_rate, inactive_rate)
