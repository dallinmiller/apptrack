import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_continue(clear=True):
    input("Press enter to continue. ")
    clear_screen() if clear else None

def get_yes_no(prompt, clear=True):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["y", "n"]:
            clear_screen() if clear else None
            return answer == "y"
        print("Invalid input. Please enter 'y' or 'n'.")

def get_int(prompt, min_value=None, max_value=None, clear=True):
    while True:
        value = input(prompt).strip()

        if not value:
            print("Input cannot be empty. Please enter a valid number.")
            continue

        try:
            number = int(value)
        except ValueError:
            print("Invalid input. Please enter an integer value.")
            continue

        if min_value is not None and number < min_value:
            print(f"Value must be at least {min_value}.")
            continue

        if max_value is not None and number > max_value:
            print(f"Value must be at most {max_value}.")
            continue

        if clear:
            clear_screen()

        return number

def create_menu(prompt, options_array):
    while True:
        print("\nOption:".ljust(20) + "Select:".rjust(20))
        print()
        for i, option in enumerate(options_array, start=1):
            print(option.ljust(20) + str(i).rjust(20))

        choice = get_int(f"\n{prompt} ")

        clear_screen()

        if 1 <= choice <= len(options_array):
            return choice

        print("Invalid Selection: Try again.")
