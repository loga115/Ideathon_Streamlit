import csv

data = [
    ["Number", "Component Type", "Component Model", "Quantity", "Price", "Notes"],
    [1, "Suspension", "Model A", 10, 100, "Some notes"],
    [2, "Steering", "Model B", 5, 200, "More notes"],
    [3, "Chassis", "Model C", 2, 500, "Additional notes"],
    # Add more rows here
]

filename = "inventory.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{filename}' has been created.")
subsystems = [
    "Suspension",
    "Steering",
    "Chassis",
    "Powertrain",
    "Brakes",
    "Tractive System",
    "DAQ",
    "Miscellaneous",
    "Operations"
]

data = [
    ["Number", "Component Type", "Component Model", "Quantity", "Price", "Notes"],
    [1, "Suspension", "Model A", 10, 100, "Some notes"],
    [2, "Steering", "Model B", 5, 200, "More notes"],
    [3, "Chassis", "Model C", 2, 500, "Additional notes"],
    # Add more rows here
]

# Create separate CSV files for each subsystem
for subsystem in subsystems:
    filename = f"{subsystem.lower()}_inventory.csv"
    subsystem_data = [row for row in data if row[1] == subsystem]
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(subsystem_data)
    print(f"CSV file '{filename}' has been created.")

# Merge all CSV files into one single CSV file
merged_filename = "merged_inventory.csv"
with open(merged_filename, "w", newline="") as merged_file:
    writer = csv.writer(merged_file)
    for subsystem in subsystems:
        filename = f"{subsystem.lower()}_inventory.csv"
        with open(filename, "r") as file:
            reader = csv.reader(file)
            writer.writerows(reader)
    print(f"All CSV files have been merged into '{merged_filename}'.")