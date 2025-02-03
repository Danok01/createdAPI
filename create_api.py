from flask import Flask, jsonify, request
import json
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# 1. Load your JSON dataset
try:
    with open("dataset.json", "r") as f:  # Replace "your_dataset.json"
        dataset = json.load(f)
except FileNotFoundError:
    print("Error: your_dataset.json not found. Create the file.")
    exit()  # Or handle it differently

# 2. Define your RESTful API endpoints

@app.route("/data", methods=["GET"])
def get_all_data():
    return jsonify(dataset)

# @app.route("/data/<str:name>", methods=["GET"])  # <int:id> makes id an integer
# def get_data_by_name(name):
#     for item in dataset:
#         if item["name"] == name:
#             return jsonify(item)
#     return jsonify({"message": "Data not found"}), 404  # 404 Not Found

# Example of a POST endpoint to add new data (if needed)
@app.route("/data", methods=["POST"])
def add_data():
    new_data = request.get_json()  # Get data from the request body (JSON)
    if not new_data:
        return jsonify({"message": "No data provided"}), 400

    # Get the current time in ISO 8601 format
    now = datetime.utcnow()
    iso_time = now.isoformat() + "Z"

    new_data["current_datetime"] = iso_time # Add timestamp to data

    dataset.append(new_data) # Add to dataset
    try:
        with open("dataset.json", "w") as f:  # Write changes to JSON file
            json.dump(dataset, f, indent=4) # Save to JSON file. Indent for readability.
    except Exception as e:
        return jsonify({"message": f"Error saving to JSON file: {e}"}), 500
    return jsonify({"message": "Data added successfully"}), 201 # 201 Created

# Example of a PUT endpoint to update existing data (if needed)
@app.route("/data/<int:id>", methods=["PUT"])
def update_data(id):
    updated_data = request.get_json()
    if not updated_data:
        return jsonify({"message": "No data provided for update"}), 400

    for i, item in enumerate(dataset):
        if item["id"] == id:
            dataset[i] = updated_data # Update the data
            try:
                with open("dataset.json", "w") as f:
                    json.dump(dataset, f, indent=4)
            except Exception as e:
                return jsonify({"message": f"Error saving to JSON file: {e}"}), 500
            return jsonify({"message": "Data updated successfully"}), 200
    return jsonify({"message": "Data not found for update"}), 404


# Example of a DELETE endpoint to delete data (if needed)
@app.route("/data/<int:id>", methods=["DELETE"])
def delete_data(id):
    for i, item in enumerate(dataset):
        if item["id"] == id:
            del dataset[i]
            try:
                with open("dataset.json", "w") as f:
                    json.dump(dataset, f, indent=4)
            except Exception as e:
                return jsonify({"message": f"Error saving to JSON file: {e}"}), 500
            return jsonify({"message": "Data deleted successfully"}), 200
    return jsonify({"message": "Data not found for deletion"}), 404


if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False for production