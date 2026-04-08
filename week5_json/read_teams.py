import json

file = open("teams.json", "r")
teams = json.load(file)
file.close()

active_teams = 0

for team in teams:
    print("Team:", team["team_name"])
    print("Members:", len(team["members"]))

    if team["active"]:
        active_teams += 1

    for member in team["members"]:
        print("-", member)

    print()

print("Active teams:", active_teams)

print()

for members in teams:
    if len(members["members"]) > 2:
        print("Large team:", members["team_name"])