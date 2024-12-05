import pandas as pd
import matplotlib.pyplot as plt

# Load the Accident Classification DataFrame
accident_keywords_df = pd.read_csv("accident_keywords.csv")

# Ensure the 'Year' column exists and preprocess data
if 'Year' in accident_keywords_df.columns:
    # Count occurrences of each classification per year
    classification_counts = accident_keywords_df.groupby(['Year', 'Accident Classification']).size().unstack(
        fill_value=0)

    # Plot each year's data as a separate horizontal bar chart
    for year in classification_counts.index:
        plt.figure(figsize=(12, 6))
        classification_counts.loc[year].sort_values(ascending=True).plot(kind='barh', color='skyblue')
        plt.title(f"Number of Fatalities Based on Classification (Coal) - {year}", fontsize=16)
        plt.xlabel("Number of Fatalities", fontsize=14)
        plt.ylabel("Accident Classification", fontsize=14)
        plt.yticks(fontsize=12)  # Optional: adjust font size of y-tick labels
        plt.tight_layout()
        plt.show()
else:
    print("The dataset does not have a 'Year' column.")


