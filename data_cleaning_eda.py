import pandas as pd
import numpy as np

# 1. Create a realistic synthetic dataset
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107],
    'Age': [25, 30, np.nan, 22, 35, 28, 40],
    'Salary': [50000, 60000, 52000, np.nan, 75000, 62000, 80000],
    'Department': ['IT', 'Data', 'IT', 'HR', 'Data', 'Data', 'HR'],
    'Experience_Years': [2, 5, 3, 1, 8, np.nan, 12]
}

df = pd.DataFrame(data)

# 2. Data Cleaning: Fill missing values with median/mode
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Experience_Years'] = df['Experience_Years'].fillna(0)

# 3. Exploratory Data Analysis (EDA)
print("--- Cleaned Dataset Overview ---")
print(df)

print("\n--- Summary Statistics ---")
print(df.describe())

print("\n--- Average Salary per Department ---")
dept_salary = df.groupby('Department')['Salary'].mean()
print(dept_salary)
