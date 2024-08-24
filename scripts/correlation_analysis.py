import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('path_to_your_data.csv')

correlations = data[['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlations, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
