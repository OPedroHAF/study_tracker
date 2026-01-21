from tracker import (add_session, get_total_time, delete_sessions_by_subject, get_all_sessions)
import os

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
        return
    
    print("\nCurrent study sessions:\n")

    for i, session in enumerate(sessions, start=1):
        subject = session["subject"]
        duration = session["duration"]
        print(f"{i}. {subject} - {duration} minutes")

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
    while True:
        clear_screen()
        show_menu()
        choice = get_int_input("Choose an option: ", 1 , 5)

        if choice == 1:
            subject = get_subject_input()
            duration = get_int_input("Duration(minutes): ", min_value=1, max_value=1440)
            add_session(subject, duration)
            print("Study session added.")
            input("\nPress enter to continue...")
        
        elif choice == 2:
            total_minutes = get_total_time()
            hours = total_minutes // 60
            minutes = total_minutes % 60
            print(f"Total study time: {hours}h {minutes}m")
            input("\nPress enter to continue...")

        elif choice == 3:
            show_sessions()
            print()
            subject = get_subject_input()
            deleted = delete_sessions_by_subject(subject)

            if deleted == 0:
                print("No sessions found for that subject.")
            else:
                print(f"Deleted {deleted} session(s) for '{subject}'.")
            
            input("\nPress enter to continue...")
        
        elif choice == 4:
            sessions = get_all_sessions()
            if not sessions:
                print("There are no sessions yet.")
                input("\nPress enter to continue...")
                continue
            show_sessions()
            input()
        
        elif choice == 5:
            print("Leaving...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
