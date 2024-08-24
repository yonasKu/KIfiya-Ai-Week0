import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('path_to_your_data.csv')
wind_dir = np.deg2rad(data['WD'])
wind_speed = data['WS']

plt.figure(figsize=(8, 8))
plt.polar(wind_dir, wind_speed, 'o')
plt.title('Wind Speed and Direction')
plt.show()
