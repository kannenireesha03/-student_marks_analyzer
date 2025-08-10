import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Embedded CSV data
csv_data = StringIO("""Name,Math,Science,English
Alice,85,78,92
Bob,67,72,70
Charlie,90,88,94
David,45,56,50
Eva,75,85,80
""")

# Load dataset from the string
df = pd.read_csv(csv_data)

# Calculate total and average marks
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3

# Display summary
print("Summary of Student Marks:")
print(df)

# Plot average marks per student
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Average"], color='skyblue')
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Average Marks per Student")
plt.show()

# Plot subject-wise average
subject_avg = df[["Math", "Science", "English"]].mean()
plt.figure(figsize=(8, 5))
subject_avg.plot(kind="bar", color='orange')
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Subject-wise Average Marks")
plt.show()
