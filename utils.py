import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict(text):
    vec = vectorizer.transform([text])
    prob = model.predict_proba(vec)[0]
    prediction = model.predict(vec)[0]
    return prediction, max(prob)