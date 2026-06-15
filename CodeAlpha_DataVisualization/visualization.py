import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from Task 1
df = pd.read_csv("quotes_dataset.csv")

# Display first 5 rows
print("Dataset Preview:")
print(df.head())

# Count quotes by author
author_counts = df["Author"].value_counts()

print("\nQuote Count by Author:")
print(author_counts)

# Create Bar Chart
plt.figure(figsize=(10, 6))

author_counts.plot(
    kind="bar",
    color="skyblue"
)

plt.title("Number of Quotes by Author")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")

plt.xticks(rotation=45)

plt.tight_layout()

# Save chart
plt.savefig("author_bar_chart.png")

# Show chart
plt.show()

# Create Pie Chart
plt.figure(figsize=(8, 8))

author_counts.head(5).plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Top 5 Authors Share")
plt.ylabel("")

plt.savefig("author_pie_chart.png")

plt.show()

print("\nCharts created successfully!")
print("Files saved:")
print("1. author_bar_chart.png")
print("2. author_pie_chart.png")