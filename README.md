# python-basics-playground
My first Python practice repo as I start my AI Engineer journey.
## What I Practiced
- printing output
- user input
- variables
- integer and float conversion
- simple math
- lists 
- loops
- functions
- string splitting
- counting words and characters
- basic Git and GitHub workflow
- conditional with if / elif / else
- comparison operators
- checking string length
- using functions with logic
- simple chatbot-style input handling

## Files
### Week 1
- hello.py
- age_next_year.py
- favorite_food.py
- favorite_number.py
- hours_to_minutes.py
- simple_interest.py
- favorite_foods.py
- count_to_five.py
- greet_user.py
- food_picker.py
- word_counter.py
- character_counter.py
- daily_summary.py

### Week 2
- weather_advice.py
- age_check.py
- grade_checker.py
- password_length.py
- is_even.py
- greet_by_time.py
- simple_chatbot.py
- expense_checker.py
- study_tracker.py

### Week 3 
This week I learned how to use dictionaries, lists of dictionaries, string cleanup, and functions. The hardest part was understanding lists of dictionaries and knowing what exactly I was looping through. I'm starting to slowly grasp what each function does and the logic behind these functions.
- dictionaries.py
- lists of dictionaries.py
- string cleanup.py
- functions.py
- fake API-style data.py
- a mini support dashboard project.py

### Week 4
This week I learned how to read, write, and append text files in Python. I learned the difference between read() and readlines(), and how write mode and append mode behave differently. I also learned how to organize code using modules and import functions from another file. One of the biggest lessons this week was understanding file paths and why Python sometimes could not find my files even when the code looked correct.

### Week 5
This week I learned how to work with JSON files in Python. I practiced using `json.load()` to read structured data, looping through lists of dictionaries, working with nested dictionaries and lists, counting values with `+=`, and filtering data with `if` statements. I also completed a mini project that summarized support ticket data from a JSON file. Week 5 felt pretty easy overall, and JSON makes more sense to me now. Going forward, I want more challenge mode with less guided help so I can think through the logic more on my own.

# Week 6 Calling API's
## What I Learned
This week I learned to request API's and convert them into readable JSON data. Then transfer the JSON into useful formats. 
## Scripts
first_api_call.py - Makes a GET request to agify API and prints predicted age
multi_field_extraction.py - Extracts multiple fields from API response with try/except and None checking
name_analyzer.py - Calls two APIs and handles each independently with separate validation
name_lookup_loop.py - Loops API lookups using while True until user quits
name_profile.py - Fit everything in together, with all gates, inputs, add formatting, individual API  checks
nationality_lookup.py - Checks if country list is empty before accessing results
status_checker.py - Checks response status code before parsing JSON
## Key Concepts
- Request data from API's
- Input validation before API calls
- Pull specific values out from the API and return it to the user as requested.
- try/except for error handling
- Status code checking (response.status_code)
- while True loop with break
## Tools
- `requests` library
- agify.io API
- nationalize.io API

# Week 7 API Keys
## What I Learned
This week I learned how to build a structured AI-powered support tool that analyzes customer messages, extracts data, and formats it. 
## Scripts
env_practice.py - Practice reading environment variables with os.environ.get()
first_claude_call.py - First API call to Claude using the Anthropic SDK
chatbot_memory.py - Added memory function to the chatbot
chatbot_persona.py - Able to define a persona for the chatbot in the chat
chatbot_select_persona.py - Lets the user select the persona first before the prompt input
chatbot_v2.py - Add temperature option for users and change persona selection into a dictionary
ticket_analyzer.py - Takes an user input and clean up the output as JSON. 
support_dashboard.py - Combining everything I learned this week and lets users input what they have issues with and output it with a clean parsed format. 
## Key Concepts
- API keys
- Environment variables
- System prompts
- Conversation memory
- Structured JSON output
- Temperature control
## Tools
- `anthropic` SDK
- `json` module
- `os` module for environment variables
- Claude Sonnet 4.5 model
## Key Patterns
- while True + break for input validation loops
- Dictionary-based configuration instead of if/elif chains
- System prompt controls Claude's behavior and output format
- history list manages conversation memory

## Notes
This repo documents my first week learning Python while preparing for an AI Engineer career pivot.
