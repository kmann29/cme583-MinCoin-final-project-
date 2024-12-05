import pandas as pd
import matplotlib.pyplot as plt

# Load the state classifications DataFrame
state_classifications_df = pd.read_csv("state_classifications.csv")

state_counts = state_classifications_df['State Abbreviation'].value_counts()

# Sort the state counts in descending order
state_counts = state_counts.sort_values(ascending=False)

# Display the sorted state counts
print("State Counts:")
print(state_counts.sum())

# Create a horizontal bar chart for the state counts
plt.figure(figsize=(12, 6))
state_counts.plot(kind='bar', color='orange')
plt.title("Number of Fatalites by State (Coal)", fontsize=16)
plt.xlabel("Number of Fatalities", fontsize=14)
plt.ylabel("State", fontsize=14)
plt.yticks(fontsize=12)  # Optional: adjust the font size of y-tick labels
plt.tight_layout()

# Show the plot
plt.show()

