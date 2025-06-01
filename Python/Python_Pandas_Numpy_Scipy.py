Outliers are data points that differ significantly from other observations and can skew statistical analyses.
import pandas as pd
from scipy import stats
# Define a sample DataFrame
df = pd.DataFrame({'column': [10, 20, 30, 1000]})
# Compute z-scores
z_scores = stats.zscore(df['column'])
# Filter out outliers where z-score < 3 (absolute value)
filtered_df = df[abs(z_scores) < 3]
print("Filtered DataFrame:")
print(filtered_df)
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df['column']<(Q1 - 1.5 * IQR)) | (df['column']>(Q3+1.5 * IQR)))]
import seaborn as sns
sns.boxplot(data=df,x='column')
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
Filtered DataFrame:
   column
0      10
1      20
2      30
3    1000
***********************************************************************************************
for index, value in enumerate(['a','b','c']):
    print(index, value)
0 a
1 b
2 c
***********************************************************************************************

***********************************************************************************************

***********************************************************************************************

***********************************************************************************************

***********************************************************************************************
