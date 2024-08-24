import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('path_to_your_data.csv')
data['timestamp'] = pd.to_datetime(data['timestamp'])

plt.figure(figsize=(10, 6))
plt.plot(data['timestamp'], data['GHI'], label='GHI')
plt.plot(data['timestamp'], data['DNI'], label='DNI')
plt.plot(data['timestamp'], data['DHI'], label='DHI')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Time Series Analysis')
plt.legend()
plt.show()
