import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
history = []

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
                system="You are a well sought after financial advisor focusing on personal finance planning.",
                messages=history
            )
            history.append({"role": "assistant", "content": message.content[0].text})
            print(message.content[0].text)
        except:
            print("API failed to return result. Try again later.")


