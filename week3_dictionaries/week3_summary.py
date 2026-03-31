week3_progress = {
    "week": 3,
    "topics_learned": ["dictionaries", "lists of dictionaries", "string cleanup", "functions", "fake API data"],
    "mini_project": "support dashboard",
    "hardest_topic": "lists of dictionaries",
    "confidence_level": "improving"
}

print("Week:", week3_progress["week"])
print("Mini Project:", week3_progress["mini_project"])
print("Hardest Topic:", week3_progress["hardest_topic"])
print("Confidence Level:", week3_progress["confidence_level"])
print()

print("Topics Learned:")
for topic in week3_progress["topics_learned"]:
    print("-", topic.title())