"""Calculate mean absolute error (MAE) and mean squared error (MSE)."""


def calculate_mae_mse(y_true, y_pred):
    """Return (MAE, MSE) for equally sized sequences of actual and predicted values."""
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    if not y_true:
        raise ValueError("y_true and y_pred must not be empty")

    errors = [actual - predicted for actual, predicted in zip(y_true, y_pred)]
    mae = sum(abs(error) for error in errors) / len(errors)
    mse = sum(error ** 2 for error in errors) / len(errors)
    return mae, mse


if __name__ == "__main__":
    actual = [3.0, -0.5, 2.0, 7.0]
    predicted = [2.5, 0.0, 2.0, 8.0]
    mae, mse = calculate_mae_mse(actual, predicted)
    print(f"MAE: {mae:.4f}")
    print(f"MSE: {mse:.4f}")