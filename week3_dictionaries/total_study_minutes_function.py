study_sessions = [
    {"topic": "Python", "minutes_studied": 20},
    {"topic": "Loops", "minutes_studied": 30},
    {"topic": "Dictionaries", "minutes_studied": 25}
]

def total_study_minutes(study_sessions):
    total = 0

    for session in study_sessions:
        total = total + session["minutes_studied"]

    return total



print("Total minutes studied:", total_study_minutes(study_sessions))