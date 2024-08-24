import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('path_to_your_data.csv')

cleaned = data[data['Cleaning'] == 'Yes']
not_cleaned = data[data['Cleaning'] == 'No']

plt.figure(figsize=(10, 6))
plt.plot(cleaned['timestamp'], cleaned['ModA'], label='ModA (Cleaned)')
plt.plot(not_cleaned['timestamp'], not_cleaned['ModA'], label='ModA (Not Cleaned)')
plt.xlabel('Time')
plt.ylabel('ModA')
plt.title('Impact of Cleaning on ModA')
plt.legend()
plt.show()
