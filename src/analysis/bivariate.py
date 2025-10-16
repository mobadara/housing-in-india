"""
This is a module for bivariate analysis of a the housing dataset.
It contains methods to analyze the relationship between two variables -- the target
and each feature in the dataset.
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.style.use('ggplot')


class Bivariate:
    def __init__(self, df: pd.DataFrame, target: str = 'TARGET(PRICE_IN_LACS)'):
        self.df = df
        self.target = target
        
        
    def numerical_analysis(self, column: str):
        """
        Performs bivariate analysis between the target
        and a numerical feature.
        
        Arg:
            column (str): The name of the numerical column to analyze.
        """
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame.")
        
        if column not in numeric_cols:
            raise ValueError(f"Column '{column}' is not numerical.")
        
        plt.figure(figsize=(6,4))
        ax = sns.scatterplot(data=self.df, x=column, y=self.target, color='skyblue')
        ax.set_xlabel(f'{column}')
        ax.set_ylabel('f{self.target}')
        ax.set_title(f'Scatter Plot of {self.target} vs {column}')
        plt.show()
        
        
    def categorial_analysis(self, column: str):
        """
        Performs bivariate analysis between the target
        and a categorical feature.
        
        Arg:
            column (str): The name of the categorical column to analyze.
        """
        categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame.")
        
        if column not in categorical_cols:
            raise ValueError(f"Column '{column}' is not categorical.")
        
        plt.figure(figsize=(6,4))
        ax = sns.boxplot(data=self.df, hue=column, y=self.target, palette='pastel')
        ax.set_xlabel(f'{column}')
        ax.set_ylabel(f'{self.target}')
        ax.set_title(f'Box Plot of {self.target} vs {column}')
        plt.xticks(rotation=45)
        plt.show()