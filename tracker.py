from storage import load_data, save_data

def get_all_sessions():
    return load_data

def delete_sessions_by_subject(subject):
    data = load_data()

    new_data = [
        session for session in data if session["subject"].lower() != subject.lower()
    ]

    deleted_count = len(data) - len(new_data)
    save_data(new_data)

    return deleted_count

def add_session(subject, duration):
    data = load_data()
    data.append({
        "subject": subject,
        "duration": duration
    })
    save_data(data)

def get_total_time():
    data = load_data()
    total = 0
    for session in data:
        total += session["duration"]
    
    return total

