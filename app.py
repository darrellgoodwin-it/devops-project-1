from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps / Cloud Engineer Portfolio</h1>
    <p>CI/CD with GitHub Actions & Azure App Service</p>
    <ul>
        <li>Dockerized Flask App</li>
        <li>Automated GitHub Actions Pipeline</li>
        <li>Azure App Service (Linux)</li>
        <li>Free Tier Infrastructure</li>
    </ul>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

@app.route("/about")
def about():
    return jsonify(
        name="Darrell Goodwin",
        role="DevOps / Cloud Engineer",
        stack=["Azure", "Docker", "GitHub Actions", "Python", "Linux"]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


