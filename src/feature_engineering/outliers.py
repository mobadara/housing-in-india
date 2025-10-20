import pandas as pd

def cap_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Cap outliers in a specified column of a DataFrame using the IQR method.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column (str): The column name to cap outliers for.

    Returns:
    pd.DataFrame: The DataFrame with outliers capped.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df[column] = df[column].apply(lambda x: lower_bound if x < lower_bound else upper_bound if x > upper_bound else x)

    return df