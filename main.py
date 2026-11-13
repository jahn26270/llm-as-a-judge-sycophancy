
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix
)

# Datensatz laden
data = pd.read_csv("data/dataset.csv")

# Vorläufige Testvorhersagen
predictions = [1, 0, 0, 1, 0, 0]

# Ground Truth
actual = data["expected_label"]

print("=== Sycophancy Evaluation ===")

print("Accuracy:", accuracy_score(actual, predictions))
print("Precision:", precision_score(actual, predictions))
print("Recall:", recall_score(actual, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(actual, predictions))

# False Positive Rate
tn, fp, fn, tp = confusion_matrix(
    actual, predictions
).ravel()

fpr = fp / (fp + tn)

print("\nFalse Positive Rate:", fpr)
