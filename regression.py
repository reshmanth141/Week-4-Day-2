"""Plot actual versus predicted values for a regression model."""

import matplotlib.pyplot as plt
import numpy as np


def plot_actual_vs_predicted(actual, predicted):
	"""Display a scatter plot comparing actual and predicted values."""
	actual = np.asarray(actual).ravel()
	predicted = np.asarray(predicted).ravel()

	if actual.size == 0 or actual.size != predicted.size:
		raise ValueError("actual and predicted must be non-empty and have equal lengths")

	lower = min(actual.min(), predicted.min())
	upper = max(actual.max(), predicted.max())

	plt.figure(figsize=(8, 6))
	plt.scatter(actual, predicted, alpha=0.7, edgecolors="black")
	plt.plot([lower, upper], [lower, upper], "r--", label="Perfect prediction")
	plt.xlabel("Actual values")
	plt.ylabel("Predicted values")
	plt.title("Actual vs. Predicted Values")
	plt.xlim(lower, upper)
	plt.ylim(lower, upper)
	plt.grid(True, alpha=0.3)
	plt.legend()
	plt.tight_layout()
	plt.show()
