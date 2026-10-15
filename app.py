from flask import Flask, request, render_template_string
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")
MODEL_VERSION = "1.0"

PAGE = """
<!doctype html>
<title>Student Result Predictor</title>
<body style="font-family:sans-serif;max-width:420px;margin:40px auto;padding:0 16px">
<h2>Student Result Predictor</h2>
<p><b>Model Version: {{ version }}</b></p>
<form method="post">
  <label>Study hours (0-10)</label><br>
  <input name="hours" type="number" step="0.1" required><br><br>
  <label>Attendance %</label><br>
  <input name="attendance" type="number" step="0.1" required><br><br>
  <label>Internal marks (0-50)</label><br>
  <input name="marks" type="number" step="0.1" required><br><br>
  <button type="submit">Predict</button>
</form>
{% if result %}<h3>Prediction: {{ result }}</h3>{% endif %}
</body>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        x = [[float(request.form["hours"]),
              float(request.form["attendance"]),
              float(request.form["marks"])]]
        result = "Pass" if model.predict(x)[0] == 1 else "Fail"
    return render_template_string(PAGE, version=MODEL_VERSION, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
