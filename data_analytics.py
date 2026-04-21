import csv
from pathlib import Path

file_name = Path(__file__).with_name("airtravel.csv")

months = []
data = []

with open(file_name, "r", newline="") as file:
    reader = csv.reader(file)
    headers = next(reader)  # Skip header row

    for row in reader:
        months.append(row[0])
        values = list(map(int, row[1:]))
        data.append(values)

# Flatten all values
all_values = [num for row in data for num in row]

# Basic analysis
total = sum(all_values)
average = total / len(all_values)
max_value = max(all_values)
min_value = min(all_values)

print("Total Passengers:", total)
print("Average Passengers:", round(average, 2))
print("Highest Value:", max_value)
print("Lowest Value:", min_value)

# Find best month
month_totals = [sum(row) for row in data]
best_month_index = month_totals.index(max(month_totals))

print("Best Month:", months[best_month_index])
