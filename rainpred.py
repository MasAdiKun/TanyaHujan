from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the model using joblib
model_filename = "predictraindt.pkl"
loaded_model = joblib.load(model_filename)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/manual")
def manual():
    return render_template("rainmanual.html")


@app.route("/sensor")
def sensor():
    return render_template("rainsensor.html")


@app.route("/aboutus")
def about():
    return render_template("aboutus.html")


@app.route("/api/rainpredict", methods=["POST"])
def predict():
    data = request.get_json()
    suhu = float(data.get("suhu", 0.0))
    kelembapan = float(data.get("kelembapan", 0.0))
    features = np.array([[suhu, kelembapan]])
    # Make prediction
    prediction = loaded_model.predict(features)
    result = "YES" if prediction[0] == "YES" else "NO"
    return jsonify({"prediction": result})


if __name__ == "__main__":
    app.run()
