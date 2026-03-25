study_session = {
    "topic": "AI",
    "minutes_studied": 60,
    "day": 1
}

print("Original topic:", study_session["topic"])
print("Original minutes:", study_session["minutes_studied"])
print("Day:", study_session["day"])

study_session["minutes_studied"] = 45
study_session["topic"] = "Social studies"

print("Updated topic:", study_session["topic"])
print("Updated minutes:", study_session["minutes_studied"])
print("Day:", study_session["day"])