import pandas as pd
import seaborn as sns
from IPython.display import display


class Inspector:
    """
    Performs data inspection for the house price prediction project.
    """
    def __init__(self, data: pd.DataFrame):
        self.data = data
    
    def inspect(self) -> 'Inspector':
        """
        Inspects the dataset for missing values, data types, and basic statistics.
        """
        print(f'Dataset Shape: {self.data.shape}')
        print('\nData Types:')
        print('-' * 30)
        display(self.data.dtypes)
        print('\nBasic Information:')
        print('-' * 30)
        display(self.data.info())
        return self
        
    def statistics(self, all: bool = True) -> 'Inspector':
        """
        Provides summary statistics of the dataset.
        """
        print('\nSummary Statistics:' + (' (including categorical data)' if all else ' (numerical data only)'))
        print('-' * 30)
        display(self.data.describe(include='all') if all else self.data.describe())
        
        print('\nUnique Values per Categorical Column:')
        print('-' * 30)
        discrete_cols = self.data.select_dtypes(include=['object', 'category', 'int']).columns
        for col in discrete_cols:
            unique_counts = self.data[col].nunique()
            # Display only if unique values are less than 10
            if unique_counts < 10: 
                print(f'\nColumn: {col} (Unique Values: {unique_counts})')
                print('-' * 30)
                display(self.data[col].unique())
            else:
                print("There are more than 10 unique values.")
        return self
    
    def duplicates(self) -> 'Inspector':
        """
        Checks for duplicate rows in the dataset.
        """
        duplicates = self.data.duplicated().sum()
        if duplicates > 0:
            print(f'\nNumber of duplicate rows: {duplicates}')
        else:
            print('\nNo duplicate rows found.')
        return self
    
    def missing_values(self) -> 'Inspector':
        """
        Identifies and summarizes missing values in the dataset.
        """
        missing = self.data.isnull().sum()
        missing = missing[missing > 0]
        if not missing.empty:
            print('\nMissing Values:')
            print('-' * 30)
            display(missing)
            print('\nMissing Values Heatmap:')
            print('-' * 30)
            sns.heatmap(self.data.isnull(), cbar=False, yticklabels=False, cmap='viridis')
        else:
            print('\nNo missing values found.')
        return self