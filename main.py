# Import the Pandas library
import pandas as pd

# Create a sample DataFrame (you can replace this with your own data)
data = {
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}

df = pd.DataFrame(data)

# Display basic statistics
print("Basic Statistics:")
print(df.describe())

# Calculate specific statistics
print("\nMean Age:", df['Age'].mean())
print("Median Salary:", df['Salary'].median())
print("Standard Deviation of Age:", df['Age'].std())
print("Sum of Salaries:", df['Salary'].sum())
print("Minimum Age:", df['Age'].min())
print("Maximum Salary:", df['Salary'].max())

# Calculate percentiles
percentiles = [25, 50, 75]
print("\nPercentiles of Age:")
print(df['Age'].quantile(percentiles))

# Count unique values
print("\nCount of unique Age values:")
print(df['Age'].nunique())

# Value counts for a categorical variable
# Example: Count how many times each age occurs in the 'Age' column
print("\nValue counts of Age:")
print(df['Age'].value_counts())
