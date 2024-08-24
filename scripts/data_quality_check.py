import pandas as pd

data = pd.read_csv('path_to_your_data.csv')

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values:\n", missing_values)

# Check for negative values where they shouldn't exist
invalid_data = data[(data['GHI'] < 0) | (data['DNI'] < 0) | (data['DHI'] < 0)]
print("Invalid data:\n", invalid_data)

# Outliers using boxplots (requires visualization)
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data['GHI'])
plt.show()
