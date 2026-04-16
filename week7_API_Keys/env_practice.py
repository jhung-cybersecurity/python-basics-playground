import os 

api_key = os.environ.get("MY_SECRET")

if api_key is None:
    print("API key not found. Set your environment variable.")
else:
    print("Key loaded successfully.")

    