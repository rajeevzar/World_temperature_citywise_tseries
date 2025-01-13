import numpy as np
from scipy.stats import linregress

def bootstrap_regression(x, y, n_iterations=1000, confidence_level=0.95):
    """
    Perform bootstrap resampling to estimate confidence intervals for linear regression parameters.
    
    Args:
        x (array-like): Independent variable (e.g., years).
        y (array-like): Dependent variable (e.g., temperatures).
        n_iterations (int): Number of bootstrap samples.
        confidence_level (float): Desired confidence level (e.g., 0.95 for 95% confidence).
    
    Returns:
        dict: A dictionary containing bootstrap results:
            - "slope_ci": (lower_bound, upper_bound) confidence interval for the slope.
            - "intercept_ci": (lower_bound, upper_bound) confidence interval for the intercept.
            - "slopes": List of bootstrap slope values.
            - "intercepts": List of bootstrap intercept values.
    """
    slopes = []
    intercepts = []

    n = len(x)
    for _ in range(n_iterations):
        # Resample the data with replacement
        indices = np.random.choice(n, n, replace=True)
        x_sample = x[indices]
        y_sample = y[indices]
        
        # Perform linear regression on the sample
        slope, intercept, _, _, _ = linregress(x_sample, y_sample)
        slopes.append(slope)
        intercepts.append(intercept)

    # Calculate the confidence interval for the slope and intercept
    alpha = 1 - confidence_level
    lower_percentile = 100 * (alpha / 2)
    upper_percentile = 100 * (1 - alpha / 2)

    slope_ci = (np.percentile(slopes, lower_percentile), np.percentile(slopes, upper_percentile))
    intercept_ci = (np.percentile(intercepts, lower_percentile), np.percentile(intercepts, upper_percentile))

    return {
        "slope_ci": slope_ci,
        "intercept_ci": intercept_ci,
        "slopes": slopes,
        "intercepts": intercepts
    }
