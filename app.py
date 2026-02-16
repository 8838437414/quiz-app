from flask import Flask, render_template, request

app = Flask(__name__)

# -----------------------------
# Quiz Questions
# -----------------------------
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "HTML", "Java", "All"],
        "answer": "All"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["5", "8", "10", "6"],
        "answer": "8"
    }
]

# -----------------------------
# Home route (show quiz)
# -----------------------------
@app.route("/")
def quiz():
    return render_template("quiz.html", questions=questions)

# -----------------------------
# Submit route
# -----------------------------
@app.route("/submit", methods=["POST"])
def submit():
    score = 0

    for i, q in enumerate(questions):
        user_answer = request.form.get(f"q{i}")
        if user_answer == q["answer"]:
            score += 1

    total = len(questions)
    return render_template("result.html", score=score, total=total)

# -----------------------------
# Run app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
