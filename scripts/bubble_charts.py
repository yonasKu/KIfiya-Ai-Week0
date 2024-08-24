import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/bubble_charts.py')

plt.figure(figsize=(10, 6))
plt.scatter(data['GHI'], data['Tamb'], s=data['RH'], alpha=0.5)
plt.xlabel('GHI')
plt.ylabel('Tamb')
plt.ylabel('Tamb')
plt.title('GHI vs Tamb vs RH')
plt.show()
