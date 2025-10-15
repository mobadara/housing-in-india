import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Tuple
from matplotlib.container import BarContainer
from matplotlib.axes import Axes
plt.style.use('ggplot')

class Univariate:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
        
    def categorial_analysis(self, column: str) -> Tuple[BarContainer, 'Univariate']:
        """
        Perform univariate analysis on a categorical column.
        
        Args:
            column (str): The name of the categorical column to analyze.
        
        Returns:
            self
        """
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame.")
        
        if column not in self.df.select_dtypes(include=['object', 'category']).columns:
            raise ValueError(f"Column '{column}' is not categorical.")
        
        total = sum(self.df[column].value_counts().values)
        plt.figure(figsize=(6, 4))
        x = self.df[column].value_counts().index
        y = self.df[column].value_counts().values   
        bars = plt.bar(x, y,
                        color=sns.color_palette('pastel')[0:5],
                        alpha=0.7,
                        edgecolor='black',
                        width=0.3
                        )
        
        for bar in bars:
            height = bar.get_height() + 0.1
            pct = 100 * height / total
            plt.text(bar.get_x() + bar.get_width() / 2, height,
                     f'{pct:.2f}%',
                     ha='center', va='bottom', fontdict={'fontsize': 14})
            
        plt.title(f'Count Plot of {column}')
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        return bars, self
    
    
    def numerical_analysis(self, column: str) -> Tuple[Axes, 'Univariate']:
        """
        Performs bivariate analysis on a numerical column.
        
        Arg:
            column (str): The name of the numerical column to analyze.
        """
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame.")
        
        if column not in self.df.select_dtypes(include=['number']).columns:
            raise ValueError(f"Column '{column}' is not numerical.")
        
        plt.figure(figsize=(6,4))
        plt.axis('tight')
        ax = sns.histplot(data=self.df, x=column, kde=True, bins=10, color='skyblue')
        ax.set_xlabel(f'{column}')
        ax.set_title(f'Distribution of {column}')
        plt.show()
        return ax, self