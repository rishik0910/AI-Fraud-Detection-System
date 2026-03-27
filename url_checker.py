def check_url(url):
    score = 0

    if len(url) > 50:
        score += 1
    if "@" in url:
        score += 1
    if "-" in url:
        score += 1
    if "https" not in url:
        score += 1

    if score >= 3:
        return "Dangerous"
    elif score == 2:
        return "Suspicious"
    else:
        return "Safe"