def study_message(hours):
    if hours >= 2:
        print("Great job studying today.")
    elif hours >= 1:
        print("Nice work. Keep building consistency.")
    elif hours == 0:
        print("You should try harder next time! ")
    elif hours < 0:
        print("You're funny but it's not possible to study less than 0 hours HAHA.")
    else:
        print("A little progress is still progress.")

hours = float(input("How many hours did you study today? "))
study_message(hours)
