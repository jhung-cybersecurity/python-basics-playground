import os
import json
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
history = []
personas = {
        "1": "You are a ticket analyzer",
        "2": "You are a customer responder",
    }
temperatures = {
        "Precise": 0.0,
        "Neutral": 0.5,
        "Creative": 1.0
    }

def divider():
    print("══════════════════════════════════════")

## format
divider()
print("SUPPORT TICKET ANALYSIS")
divider()

## loop prompt selection
while True:
    choice = input("First, pick a persona (1/2): ")
    if choice in personas:
        persona = personas[choice]
        divider()
        break
    else:
        print("You must pick a persona selection. Try again.")
        divider()

## persona
system_prompt = f"{persona}. Response ONLY with valid JSON containing these fields: summary, urgency, category, department, sentiment, response. No other text."

## temperature selection
while True:
    temp_choice = input("Next, pick a temperature (Precise/Neutral/Creative): ")
    if temp_choice in temperatures:
        select_temperature = temperatures[temp_choice]
        divider()
        break
    else:
        print("You must pick a temperature selection. Try again.")
        divider()
## loop begins
while True:
    prompt = input("Describe your issue: ")
    if prompt == "":
        print("You didn't enter an issue. Try again.")
        divider()
    elif prompt == "quit":
        print("Chat ended.")
        divider()
        break
    
    else:
        try:
            ## call API
            history.append({"role": "user", "content": prompt})
            message = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=1024,
                system=system_prompt, 
                temperature=select_temperature,
                messages=history
            )
            ## clean & parse
            history.append({"role": "assistant", "content": message.content[0].text})
            raw = message.content[0].text
            clean = raw.replace("```json", "").replace("```", "").strip()
            parsed = json.loads(clean)

            print("Summary:", parsed["summary"])
            print("Urgency:", parsed["urgency"])
            print("Category:", parsed["category"])
            print("Department:", parsed["department"])
            print("Sentiment:", parsed["sentiment"])
            print("Response:", parsed["response"])
            divider()

        ## error msg
        except Exception as e:
                print("Error:", e)
                divider()
