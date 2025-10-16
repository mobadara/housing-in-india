"""
This class handles multivariate analysis of the housing dataset.
It contains methods to analyze the relationship between multiple variables in the dataset.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
plt.style.use('ggplot')

class Multivariate:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
        
    def pairplot_analysis(self):
        """
        Performs multivariate analysis using pairplot for the given columns.
        
        Arg:
            columns (list): List of column names to include in the pairplot.
        """
        columns = self.df.select_dtypes(include=['number']).columns
        if len(columns) < 2:
            raise ValueError("DataFrame must contain at least two numerical columns for pairplot analysis.")
        
        plt.figure(figsize=(10, 8))
        sns.pairplot(self.df[columns], diag_kind='kde', markers='+', plot_kws={'alpha':0.5, 's':30})
        plt.suptitle('Pairplot Analysis', y=1.02)
        plt.show()
        
        
    def heatmap_analysis(self):
        """
        Performs multivariate analysis using a heatmap to show correlations between numerical features.
        """
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        corr = self.df[numeric_cols].corr()
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
        plt.title('Heatmap of Correlation Matrix')
        plt.show()
        