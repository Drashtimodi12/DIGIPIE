details = {
    "person": {
        "name": "Drashti",
        "skills": ["Python", "Django", "MySQL"]
    }
}

# Print name
print(details["person"]["name"])
print("------------------------")

# Add new skill "HTML"
details["person"]["skills"].append("HTML")
print(details)
print("------------------------")

# Count skills
print(len(details['person']['skills']))