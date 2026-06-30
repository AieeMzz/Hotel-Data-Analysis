import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/hotel_occupancy.csv")

# Show first rows
print(df.head())

# Basic analysis
print("Average Occupancy:", df["Occupancy"].mean())
print("Total Revenue:", df["Revenue"].sum())

# Create chart
plt.plot(df["Month"], df["Occupancy"], marker="o")
plt.title("Hotel Occupancy by Month")
plt.xlabel("Month")
plt.ylabel("Occupancy (%)")
plt.xticks(rotation=45)
plt.show()
