import pandas as pd
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
        
    def summary_statistics(self, all: bool = True) -> 'Inspector':
        """
        Provides summary statistics of the dataset.
        """
        print('\nSummary Statistics:' + (' (including categorical data)' if all else ' (numerical data only)'))
        print('-' * 30)
        display(self.data.describe(include='all') if all else self.data.describe())
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
        else:
            print('\nNo missing values found.')
        return self