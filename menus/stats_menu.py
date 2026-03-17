from process.stats import *
from menus.menu_creator import get_continue

def stats_ui():
    (t_app, resp_app, rej_app, in_app, t_int, a_int, offers, resp_rate, int_rate,
     offer_rate, rej_rate, in_rate) = statistics()

    print(f"Total Applications: {t_app} \n")
    print(f"Total Responses: {resp_app}")
    print(f"Response Rate: {resp_rate} % \n")
    print(f"Rejected Applications: {rej_app}")
    print(f"Rejected Rate: {rej_rate} % \n")
    print(f"Inactive Applications: {in_app}")
    print(f"Inactive Rate: {in_rate} % \n")
    print(f"Total Interviews: {t_int}")
    print(f"Active Interviews: {a_int}")
    print(f"Interview Rate: {int_rate} % \n")
    print(f"Offers: {offers}")
    print(f"Offer Rate: {offer_rate} % \n")

    get_continue()
