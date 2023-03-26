from chalice import Chalice
import os

app = Chalice(app_name="predictor")

@app.route("/", methods=["GET"])
def index():
    return os.environ.get("MY_VAR", "dev")

@app.route("/predict", methods=["POST"])
def predict():
    prediction = app.current_request.json_body
    return prediction