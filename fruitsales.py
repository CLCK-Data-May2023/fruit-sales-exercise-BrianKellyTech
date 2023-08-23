import pandas as pd

# Create a dictionary
data = {
    'Apples': [35, 41],
    'Bananas': [21, 34]
}

# Create a DataFrame
df = pd.DataFrame(data, index=['2017 Sales', '2018 Sales'])

# Save the DataFrame to a CSV file named 'fruit'
df.to_csv('fruit.csv')

# Print a message to let me know the file was saved
print("DataFrame saved to 'fruit.csv'")
