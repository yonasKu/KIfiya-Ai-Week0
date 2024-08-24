import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('path_to_your_data.csv')

data[['GHI', 'DNI', 'DHI', 'WS', 'Tamb']].hist(bins=20, figsize=(10, 8))
plt.show()