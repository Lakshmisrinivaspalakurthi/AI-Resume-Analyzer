import re

def resume_quality(text):

    score = 0

    if "linkedin" in text.lower():
        score += 20

    if "github" in text.lower():
        score += 20

    if "project" in text.lower():
        score += 20

    if "skill" in text.lower():
        score += 20

    numbers = re.findall(
        r'\d+%',
        text
    )

    if len(numbers) > 0:
        score += 20

    return score
