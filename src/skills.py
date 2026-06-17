import json

with open("data/skills_db.json") as f:
    skills_db = json.load(f)

ALL_SKILLS = []

for role in skills_db:
    ALL_SKILLS.extend(skills_db[role])

ALL_SKILLS = list(set(ALL_SKILLS))

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in ALL_SKILLS:

        if skill in text:
            found.append(skill)

    return found
