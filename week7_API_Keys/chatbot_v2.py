import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
history = []
personas = {
        "1": "You are a financial advisor",
        "2": "You are a medical professional",
        "3": "You are a well known customer service rep"
    }
temperatures = {
        "Precise": 0.0,
        "Neutral": 0.7,
        "Creative": 1.0
    }

## loop prompt selection
while True:
    choice = input("First, pick a persona (1/2/3): ")
    if choice in personas:
        persona = personas[choice]
        break
    else:
        print("You must pick a persona selection. Try again.")

## temperature selection
while True:
    temp_choice = input("Next, pick a temperature (Precise/Neutral/Creative): ")
    if temp_choice in temperatures:
        select_temperature = temperatures[temp_choice]
        break
    else:
        print("You must pick a temperature selection. Try again.")

## loop begins
while True:
    prompt = input("Next, enter your prompt: ")
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
                temperature=select_temperature,
                messages=history
            )
            history.append({"role": "assistant", "content": message.content[0].text})
            print(message.content[0].text)
        except Exception as e:
                print("Error:", e)

