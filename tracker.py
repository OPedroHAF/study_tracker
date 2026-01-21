from storage import load_data, save_data

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

