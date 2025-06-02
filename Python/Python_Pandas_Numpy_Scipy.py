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
method chaining in pandas - is a practice where multiple pandas methods are called sequentially, using dots 
(.), often enclosed in parentheses. 
df_cleaned = (
 df.dropna()
 .assign(sales_tax=lambda x: x['Sales'] * 0.18)
 .query('sales_tax > 50')
 .sort_values(by='sales_tax', ascending=False)
)
namedtuple
from collections import namedtuple
Point = namedtuple('Point', ['x','y'])
p = Point(10, 20)
print(p.x)
print(p.y)
10
20
***********************************************************************************************
import pandas as pd

# Creating two DataFrames with a common column 'id' to demonstrate merge
df1 = pd.DataFrame({'id': [1, 2, 3, 4], 'value1': ['A', 'B', 'C', 'D']})
df2 = pd.DataFrame({'id': [3, 4, 5, 6], 'value2': ['X', 'Y', 'Z', 'W']})

# Example of merge (on key column 'id')
merged = pd.merge(df1, df2, on='id', how='inner')
print("Merge Result:\n", merged)

# Example of join (on index)
df1_indexed = df1.set_index('id')
df2_indexed = df2.set_index('id')
joined = df1_indexed.join(df2_indexed, how='left')
print("\nJoin Result:\n", joined)

# Vertical stacking  concat
concat_vertical = pd.concat([df1, df2], axis=0, ignore_index=True)
print("\nConcat Vertical:\n", concat_vertical)

# Horizontal stacking (index should be same or align properly)
df1_short = pd.DataFrame({'A': [1, 2]})
df2_short = pd.DataFrame({'B': [3, 4]})
concat_horizontal = pd.concat([df1_short, df2_short], axis=1)
print("\nConcat Horizontal:\n", concat_horizontal)
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
Merge Result:
    id value1 value2
0   3      C      X
1   4      D      Y

Join Result:
    value1 value2
id              
1       A    NaN
2       B    NaN
3       C      X
4       D      Y

Concat Vertical:
    id value1 value2
0   1      A    NaN
1   2      B    NaN
2   3      C    NaN
3   4      D    NaN
4   3    NaN      X
5   4    NaN      Y
6   5    NaN      Z
7   6    NaN      W

Concat Horizontal:
    A  B
0  1  3
1  2  4
***********************************************************************************************
pivot tables in pandas
import pandas as pd
df = pd.DataFrame({
 'Region': ['North', 'South', 'North', 'South'],
 'Product': ['A', 'A', 'B', 'B'],
 'Sales': [100, 150, 200, 250]
})
pivot = df.pivot_table(index='Region', columns='Product', values='Sales', aggfunc='sum')
print(pivot)
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
Product    A    B
Region           
North    100  200
South    150  250
***********************************************************************************************
import numpy as np
a = np.array([1, 2, 3])
b = np.asarray(a)
print(a is b)         ----->      True

from collections import Counter      # most frequent element

lst = [1,2,3,2,2,3,3,3,4]
count = Counter(lst)
most_common = count.most_common(1)[0][0]
print(most_common)   ====>      3
***********************************************************************************************

***********************************************************************************************

***********************************************************************************************

***********************************************************************************************

***********************************************************************************************
