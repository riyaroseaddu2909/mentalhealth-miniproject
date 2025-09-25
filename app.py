from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy function – replace with ML model later
def get_emotion(user_input):
    if "sad" in user_input.lower():
        return "Sad"
    elif "happy" in user_input.lower():
        return "Happy"
    else:
        return "Neutral"

# Recommendations map
recommendations = {
    "Happy": {
        "affirmation": "Keep shining! Your energy is contagious ✨",
        "activity": "Go for a walk and share your joy with someone.",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"
    },
    "Sad": {
        "affirmation": "It’s okay to feel down. Brighter days are ahead 🌈",
        "activity": "Try journaling your thoughts or calling a close friend.",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1"
    },
    "Neutral": {
        "affirmation": "Stay balanced and centered. You’re doing great 🌿",
        "activity": "Read a short article or listen to a calming podcast.",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ"
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form["user_input"]
        emotion = get_emotion(user_text)
        recs = recommendations.get(emotion, recommendations["Neutral"])
        return render_template("result.html", emotion=emotion, recs=recs, user_text=user_text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
