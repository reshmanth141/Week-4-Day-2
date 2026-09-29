"""Train a simple linear regression model and generate predictions."""

import numpy as np
from sklearn.linear_model import LinearRegression


def main():
    # Example training data: one input feature and its target values.
    X_train = np.array([[1], [2], [3], [4], [5]])
    y_train = np.array([2, 4, 6, 8, 10])

    model = LinearRegression()
    model.fit(X_train, y_train)

    X_new = np.array([[6], [7], [8]])
    predictions = model.predict(X_new)

    print(f"Slope: {model.coef_[0]:.2f}")
    print(f"Intercept: {model.intercept_:.2f}")
    for value, prediction in zip(X_new[:, 0], predictions):
        print(f"Prediction for x={value}: {prediction:.2f}")


if __name__ == "__main__":
    main()