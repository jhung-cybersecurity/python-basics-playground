file = open("notes.txt", "r")
lines = file.readlines()
file.close()

print(lines)
print("Total lines:", len(lines))