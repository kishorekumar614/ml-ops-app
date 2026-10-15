import numpy as np, pandas as pd, joblib
from sklearn.ensemble import RandomForestClassifier

rng = np.random.default_rng(42)
n = 500
df = pd.DataFrame({
    "study_hours": rng.uniform(0, 10, n),
    "attendance": rng.uniform(40, 100, n),
    "internal_marks": rng.uniform(0, 50, n),
})
score = (df.study_hours * 4 + df.attendance * 0.3 + df.internal_marks * 0.8
         + rng.normal(0, 4, n))
df["result"] = (score > 60).astype(int)  # 1 = Pass, 0 = Fail
df.to_csv("students.csv", index=False)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(df[["study_hours", "attendance", "internal_marks"]], df["result"])
joblib.dump(model, "model.pkl")
print("Model trained and saved")
