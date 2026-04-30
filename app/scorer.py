from app.skills import ALIASES, WEIGHTS

def normalize_text(text):
    return text.lower().strip()

def contains(text, term):
    return term.lower() in text.lower()

def is_skill_matched(resume, skill):
    if skill in ALIASES:
        for alias in ALIASES[skill]:
            if contains(resume, alias):
                return True
        return False

    return contains(resume, skill)

def scan_resume(resume, jd):
    resume = normalize_text(resume)
    jd = normalize_text(jd)

    matched = []
    missing = []

    total_weight = 0
    earned_weight = 0

    for skill, weight in WEIGHTS.items():
        if contains(jd, skill):
            total_weight += weight

            if is_skill_matched(resume, skill):
                earned_weight += weight
                matched.append(skill)
            else:
                missing.append(skill)

    score = int((earned_weight / total_weight) * 100) if total_weight else 0

    return {
        "score": score,
        "matched_keywords": matched,
        "missing_keywords": missing,
        "suggestions": [f"Add {x}" for x in missing[:5]]
    }