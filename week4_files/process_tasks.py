file = open("tasks.txt", "r")
lines = file.readlines()
file.close()

for task in lines:
    clean_task = task.strip().title()
    print(clean_task)

    