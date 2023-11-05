import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset (replace 'your_dataset.csv' with your actual dataset file path)
df = pd.read_csv("D:\SEM-5\Advanced_Python\THEORY\Data Visualisation Assignment\\test2.csv")

# Set a style for your plots (optional)
sns.set(style="whitegrid")

# Unique Categorical Values
unique_values = df['State Abbreviation'].unique()
print("Unique Categorical Values:")
print(unique_values)

# Null Count
null_count = df.isnull().sum()
print("\nNull Count:")
print(null_count)

# Fill Null Values (replace 'Total Amount Spent' with the appropriate column name)
df['Total Amount Spent'].fillna(0, inplace=True)

# Pair Plot (for numerical columns)
numerical_columns = df.select_dtypes(include=['float64', 'int64'])
sns.pairplot(numerical_columns)
plt.show()

# Histogram
sns.histplot(df['Total Amount Spent'], bins=20, kde=True)
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency')
plt.title('Histogram of Total Amount Spent')
plt.show()

# Boxplot
sns.boxplot(x='Member Level', y='Total Amount Spent', data=df)
plt.xticks(rotation=45)
plt.show()

# Correlation Matrix and Heatmap
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# Bar Plot
sns.barplot(x='Member Level', y='Total Amount Spent', data=df)
plt.xticks(rotation=45)
plt.show()

# Line Plot (consider converting 'Birthdate' to datetime if it's not already)
sns.lineplot(x='Birthdate', y='Total Amount Spent', data=df)
plt.xticks(rotation=45)
plt.show()

# Scatter Plot (consider converting 'Birthdate' to datetime if it's not already)
sns.scatterplot(x='Birthdate', y='Total Amount Spent', data=df)
plt.xticks(rotation=45)
plt.show()

# Violin Plot
sns.violinplot(x='Member Level', y='Total Amount Spent', data=df)
plt.xticks(rotation=45)
plt.show()

# Count Plot
sns.countplot(x='Member Level', data=df)
plt.xticks(rotation=45)
plt.show()

# Missing Value Heatmap
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.show()
