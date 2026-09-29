"""Interpretation notes

- Coefficients: each coefficient shows the expected change in the target variable for a one-unit increase in that feature, holding other features constant. A positive coefficient increases the prediction; a negative coefficient decreases it.
- Predictions: the model predicts y = intercept + sum(coefficient_i * feature_i). Compare predicted values to actual outcomes to assess accuracy and direction of error.
- Model behavior: the sign reveals positive or negative relationships, while the magnitude indicates strength. Check whether effects are realistic, whether interactions or nonlinearities matter, and whether residuals suggest bias or poor fit.
"""
