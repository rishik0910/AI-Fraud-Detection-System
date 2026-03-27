def explain_text(text):
    suspicious_words = ["bank", "verify", "urgent", "password", "click"]

    found = [word for word in suspicious_words if word in text.lower()]
    
    return found