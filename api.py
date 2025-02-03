from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone

# Initialize Flask app
app = Flask(__name__)

# Configure CORS
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=["GET"])
def get_root():
    """
    Root endpoint that returns JSON response with email,
    current datetime (UTC ISO 8601),
    and GitHub URL.
    """
    response = {
        "email": "dhaniroyal01@gmail.com",
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/Danok01/created_Api",
    }
    return jsonify(response), 200
# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)