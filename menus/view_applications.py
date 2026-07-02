from process.save_load import load_application
from menus.menu_creator import get_continue

def view_applications():
    apps = load_application()
    for app in apps:
        print(f"ID: {app['ID']}; Company: {app['Company']}; Position: {app['Position']}; Location: {app['Location']}; "
              f"Date Applied: {app['Date Applied']}; Status: {app['Status']}; Notes: {app['Notes']}")

    get_continue()

def view_application(ID):
    apps = load_application()
    app = apps[ID - 1]
    print(f"ID: {app['ID']}; Company: {app['Company']}; Position: {app['Position']}; Location: {app['Location']}; "
          f"Date Applied: {app['Date Applied']}; Status: {app['Status']}; Notes: {app['Notes']}\n\n")
