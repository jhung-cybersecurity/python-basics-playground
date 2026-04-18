import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
history = []


## loop prompt selection
while True:
    choice = input("Pick a persona (1/2/3): ")
    if choice == "1":
        persona = "You are a financial advisor"
        break
    elif choice == "2":
        persona = "You are a medical professional"
        break
    elif choice == "3":
        persona = "You are a well known customer service rep"
        break
    else:
        print("Please pick 1-3 only. Try again.")

## loop begins
while True:
    prompt = input("Enter your prompt: ")
    if prompt == "":
        print("You didn't enter a prompt. Try again.")
    elif prompt == "quit":
        print("Chat ended.")
        break
    else:
        try:
            history.append({"role": "user", "content": prompt})
            message = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=1024,
                system=persona,
                messages=history
            )
            history.append({"role": "assistant", "content": message.content[0].text})
            print(message.content[0].text)
        except:
            print("API failed to return result. Try again later.")


