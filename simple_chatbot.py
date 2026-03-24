message = input("Say something: ")

if "hello" in message.lower():
    print("Hi there!")
elif "bye" in message.lower():
    print("Goodbye!")
elif "help" in message.lower():
    print("I am here to help.")
elif "thanks" in message.lower():
    print("You're welcome!")
else:
    print("I do not understand yet.")
