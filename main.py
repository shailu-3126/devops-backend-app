from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend app deployed from GitHub Actions to Cloud Run!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
# trigger
