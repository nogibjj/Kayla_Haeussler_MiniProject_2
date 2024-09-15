"""Main Python file"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loadind csv data set
df = pd.read_csv('ClassicHit.csv')

# Generating sumamry statistics
print(df)

# Creating visualization
plt.figure(figsize=(10, 6))
sns.histplot(df['Duration'].dropna(), bins=30, kde=True)
plt.title('Histogram of Your Song Duration')
plt.xlabel('Duration')
plt.ylabel('Frequency')
plt.show()
