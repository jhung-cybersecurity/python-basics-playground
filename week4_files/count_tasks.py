file = open("tasks.txt", "r")
lines = file.readlines()
file.close()

print("Total tasks:", len(lines))

