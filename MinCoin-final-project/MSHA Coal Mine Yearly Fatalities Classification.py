import pandas as pd
import matplotlib.pyplot as plt

# Load the DataFrame
dates_df = pd.read_csv("dates.csv")

# Convert the 'Date' column to datetime format
dates_df['Date'] = pd.to_datetime(dates_df['Date'], errors='coerce')

# Remove rows with invalid dates
dates_df.dropna(subset=['Date'], inplace=True)

# Extract the year from the 'Date' column
dates_df['Year'] = dates_df['Date'].dt.year

# Count the frequency of each year
year_counts = dates_df['Year'].value_counts().sort_index()

# Plot the yearly frequency
plt.figure(figsize=(12, 6))
plt.bar(year_counts.index, year_counts.values, color='teal')

# Add circles to highlight specific timelines
highlighted_years = {
    2010: "Start of decline in production",
    2020: "-24% from 2019 (Lowest since 1965)",
    2023: "-7.4% Productivity, -17.4% Consumption",
}

# Loop through the highlighted years and add circles
for year, description in highlighted_years.items():
    plt.scatter(year, year_counts.loc[year], s=150, edgecolor='red', facecolor='none', linewidth=2, label=f"{year}: {description}")

# Add labels, title, and legend
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Fatalities', fontsize=12)
plt.title('Number of Coal Mining Fatalities Per Year', fontsize=14)
plt.xticks(rotation=45, fontsize=10)
plt.legend(loc='upper right', fontsize=9)
plt.tight_layout()  # Adjust layout to prevent overlap

plt.show()
