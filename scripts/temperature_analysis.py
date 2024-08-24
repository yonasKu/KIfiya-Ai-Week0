import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('path_to_your_data.csv')

plt.figure(figsize=(10, 6))
sns.scatterplot(x='RH', y='Tamb', data=data)
plt.title('RH vs Tamb')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='RH', y='GHI', data=data)
plt.title('RH vs GHI')
plt.show()
