from tracker import (add_session, get_total_time, delete_sessions_by_subject, get_all_sessions)
import os

MAX_DURATION = 1440

def clear_screen():
    os.system("cls" if os.name== "nt" else "clear")

def show_menu():
    print("\nStudy Tracker")
    print("1. Add study session")
    print("2. Show total study time")
    print("3. Delete sessions by subject")
    print("4. Show all sessions")
    print("5. Exit")

def show_sessions():
    sessions = get_all_sessions()

    if not sessions:
        print("\nNo study sessions found.")
        return False
    
    print("\nCurrent study sessions:\n")

    for i, session in enumerate(sessions, start=1):
        print(f"{i}. {session["subject"]} - {session["duration"]} minutes")
    return True

def get_int_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Please enter a number greater than or equal to {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Please enter a number less than or equal to {max_value}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")
    
def get_subject_input():
    while True:
        subject = input("Subject: ").strip()

        if not subject:
            print("Subject cannot be empty.")
            continue

        return subject


def main():
    continue_msg = "\nPress enter to continue..."
    while True:
        clear_screen()
        show_menu()
        choice = get_int_input("Choose an option: ", 1 , 5)

        if choice == 1:
            subject = get_subject_input()
            duration = get_int_input("Duration(minutes): ", min_value=1, max_value=MAX_DURATION)
            add_session(subject, duration)
            print("Study session added.")
            input(continue_msg)
        
        elif choice == 2:
            total = get_total_time()
            hours, minutes = divmod(total, 60)
            print(f"Total study time: {hours}h {minutes}m")
            input(continue_msg)

        elif choice == 3:
            if not show_sessions():
                input(continue_msg)
                continue

            print()
            subject = get_subject_input()
            deleted = delete_sessions_by_subject(subject)

            if deleted == 0:
                print("No study sessions found.")
            else:
                print(f"Deleted {deleted} session(s) for '{subject}'.")
            
            input(continue_msg)
        
        elif choice == 4:
            show_sessions()
            input(continue_msg)
        
        elif choice == 5:
            confirm = input("Are you sure you want to exit? (y/n): ").lower()
            if confirm == "y":
                print("Leaving...")
                break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
