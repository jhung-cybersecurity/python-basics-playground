read_file = open("messy_notes.txt", "r")
lines = read_file.readlines()
read_file.close()

write_file = open("clean_notes.txt", "w")

for line in lines:
    clean_line = line.strip().title()
    write_file.write(clean_line + "\n")

write_file.close()

print("clean_notes.txt was created.")
