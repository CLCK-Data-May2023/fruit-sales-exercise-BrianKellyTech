import pandas as pd

# Create the DataFrame
df = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                           index=['2017 Sales', '2018 Sales'])

# Save the DataFrame to a CSV file
df.to_csv('fruit.csv')

# print("DataFrame saved to 'fruit.csv'")
