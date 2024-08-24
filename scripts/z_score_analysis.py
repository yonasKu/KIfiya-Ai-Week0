import pandas as pd
from scipy.stats import zscore

data = pd.read_csv('path_to_your_data.csv')

data['zscore_GHI'] = zscore(data['GHI'])
data['zscore_DNI'] = zscore(data['DNI'])
outliers = data[(data['zscore_GHI'].abs() > 3) | (data['zscore_DNI'].abs() > 3)]

print("Outliers:\n", outliers)
