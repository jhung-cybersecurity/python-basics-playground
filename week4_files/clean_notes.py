file = open("messy_notes.txt", "r")
lines = file.readlines()
file.close()

cleaned_notes = []

for line in lines:
    clean_line = line.strip().title()
    cleaned_notes.append(clean_line)

for note in cleaned_notes:
    print(note)

print("Total notes:", len(cleaned_notes))

