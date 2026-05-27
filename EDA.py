# Exploratory Data Analysis (EDA) Project
# Name: Naman Sanadhya

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("------ Exploratory Data Analysis Project ------")

# Loading dataset
df = pd.read_csv("sales_data.csv")

# Display first records
print("\nFirst 5 Records:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Dataset shape
print("\nRows and Columns:")
print(df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Correlation analysis
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

# Histogram
plt.figure(figsize=(8,5))
plt.hist(df['Sales'])

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Boxplot
plt.figure(figsize=(8,5))
sns.boxplot(x=df['Profit'])

plt.title("Profit Boxplot")
plt.show()

# Bar chart
plt.figure(figsize=(8,5))
sns.barplot(
    x='Category',
    y='Sales',
    data=df
)

plt.title("Sales by Category")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8,6))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)

plt.title("Correlation Heatmap")
plt.show()

print("\nObservations:")

print("1. Dataset statistics were analyzed.")
print("2. Sales patterns were visualized.")
print("3. Outliers can be observed using boxplots.")
print("4. Correlations between variables were identified.")
print("5. Data trends were explored.")

print("\nProject Completed Successfully")