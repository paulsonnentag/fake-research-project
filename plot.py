import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('coral_growth.csv')

# Plot the data
plt.figure(figsize=(10, 6))

for location in df['Location'].unique():
    location_data = df[df['Location'] == location]
    plt.plot(location_data['Month'], location_data['Average Coral Growth (cm)'], label=location)

# Customize the plot
plt.title('Monthly Average Coral Growth')
plt.xlabel('Month')
plt.ylabel('Average Coral Growth (cm)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot to disk
plt.savefig('coral_growth_chart.png')
plt.show()