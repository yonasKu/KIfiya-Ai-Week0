import pandas as pd

# Load the dataset
data = pd.read_csv('path_to_your_data.csv')

# Drop rows where specific columns are entirely null
data = data.dropna(subset=['Comments'])

# Handle missing values
# Fill missing values with mean (for numerical columns)
data['GHI'].fillna(data['GHI'].mean(), inplace=True)
data['DNI'].fillna(data['DNI'].mean(), inplace=True)
data['DHI'].fillna(data['DHI'].mean(), inplace=True)

# Alternatively, drop rows with missing values
# data = data.dropna()

# Handle negative values where they shouldn't exist
# For example, if GHI should not have negative values
data = data[data['GHI'] >= 0]
data = data[data['DNI'] >= 0]
data = data[data['DHI'] >= 0]

# Save the cleaned data to a new CSV file
data.to_csv('path_to_cleaned_data.csv', index=False)

print("Data cleaning completed. Cleaned data saved to 'path_to_cleaned_data.csv'.")
