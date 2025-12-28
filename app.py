from flask import Flask, request, jsonify

# Flask app create
app = Flask(__name__)

# Home route (testing)
@app.route("/", methods=["GET"])
def home():
    return "Skin Disease Detection Backend is Running"

# Dummy predict route (for testing)
@app.route("/predict", methods=["POST"])
def predict():
    return jsonify({
        "message": "Prediction API is working",
        "status": "success"
    })

# Run server
if __name__ == "__main__":
    app.run(debug=True)
