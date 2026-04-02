file = open("daily_progress.txt", "a")
file.write("I learned how to use append to add lines into txt file.\n")
file.write("It does so without replacing lines in the file.\n")
file.close()

print("Append complete")