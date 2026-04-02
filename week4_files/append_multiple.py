file = open("study_log.txt", "a")
file.write("I now understand the difference between write and append.\n")
file.write("Append adds new text without deleting old text.\n")
file.close()

print("More log enteries added.")