import os
import json
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
history = []

## loop begins
while True:
    prompt = input("What is your emergency? ")
    if prompt == "":
        print("You didn't enter anything. Try again.")
    elif prompt == "quit":
        print("Chat ended.")
        break
    else:
        try:
            ## call API
            history.append({"role": "user", "content": prompt})
            message = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=1024,
                system="You are a support ticket analyzer. Response ONLY with valid JSON containing these fields: summary, urgency, category, suggested_response. No other text.",
                temperature=0.0,
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
            print("Suggested Response:", parsed["suggested_response"])
        except Exception as e:
                print("Error:", e)

