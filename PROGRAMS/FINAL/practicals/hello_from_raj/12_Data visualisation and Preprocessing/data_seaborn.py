# Raj Randive - 21BCP378

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv(
    "E:\\Just Code\\PDEU_Labs\\5th_Sem\\Advance_Python\\12_Data visualisation and Preprocessing\\test2.csv"
)

sns.set(style="whitegrid")

# 1 Unique Categorical Values
unique_values = df["State Abbreviation"].unique()
print("Unique Categorical Values:")
print(unique_values)

# 2 Null Count
null_count = df.isnull().sum()
print("\nNull Count:")
print(null_count)

# 3 Fill Null Values (replace 'Total Amount Spent' with the appropriate column name)
df["Total Amount Spent"].fillna(0, inplace=True)

# 4 Pair Plot (for numerical columns)
numerical_columns = df.select_dtypes(include=["float64", "int64"])
sns.pairplot(numerical_columns)
plt.show()

# 5 Histogram
sns.histplot(df["Total Amount Spent"], bins=20, kde=True)
plt.xlabel("Total Amount Spent")
plt.ylabel("Frequency")
plt.title("Histogram of Total Amount Spent")
plt.show()

# 6 Boxplot
sns.boxplot(x="Member Level", y="Total Amount Spent", data=df)
plt.xticks(rotation=45)
plt.show()

# 7 Correlation Matrix and Heatmap
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.show()

# 8 Bar Plot
sns.barplot(x="Member Level", y="Total Amount Spent", data=df)
plt.xticks(rotation=45)
plt.show()

# 9 Line Plot (consider converting 'Birthdate' to datetime if it's not already)
sns.lineplot(x="Birthdate", y="Total Amount Spent", data=df)
plt.xticks(rotation=45)
plt.show()

# 10 Scatter Plot (consider converting 'Birthdate' to datetime if it's not already)
sns.scatterplot(x="Birthdate", y="Total Amount Spent", data=df)
plt.xticks(rotation=45)
plt.show()

# 12 Violin Plot
sns.violinplot(x="Member Level", y="Total Amount Spent", data=df)
plt.xticks(rotation=45)
plt.show()

# 13 Count Plot
sns.countplot(x="Member Level", data=df)
plt.xticks(rotation=45)
plt.show()

# 14 To date time conversion (value conversion)
df["Birthdate"] = pd.to_datetime(df["Birthdate"])

# 15 Plotting the range based conversed value
df["Age"] = pd.to_datetime("now") - df["Birthdate"]
sns.boxplot(y="Age", data=df)
plt.ylabel("Age")
plt.show()


# 16 Pivot plot
pivot_df = df.pivot_table(
    index="Member Level", values="Total Amount Spent", aggfunc="mean"
)
sns.barplot(x=pivot_df.index, y="Total Amount Spent", data=pivot_df)
plt.xticks(rotation=45)
plt.show()

# 17 Pair grid
g = sns.PairGrid(numerical_columns)
g.map(plt.scatter)
plt.show()

# 18 Missing Value Heatmap
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.show()
