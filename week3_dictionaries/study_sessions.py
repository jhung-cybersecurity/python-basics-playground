study_sessions = [
    {"topic": "Python", "minutes_studied": 60, "day": 1},
    {"topic": "Dictionaries", "minutes_studied": 45, "day": 2},
    {"topic": "Loops", "minutes_studied": 30, "day": 3}
]

total_minutes = 0

for session in study_sessions:
    print("Topic:", session["topic"])
    print("Minutes Studied:", session["minutes_studied"])
    print("Day:", session["day"])
    print()

    total_minutes = total_minutes + session["minutes_studied"]

print("Total minutes studied:", total_minutes)