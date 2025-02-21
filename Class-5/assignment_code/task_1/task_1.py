import os
import glob
import shutil
import pandas as pd

os.makedirs("backup_folder", exist_ok=True)

csv_files = glob.glob("Class-5/assignment_code/task_1/csv_files/*.csv")  
for file in csv_files:
    shutil.move(file, "Class-5/assignment_code/task_1/backup_folder/")
    print(f"Moved file: {file}")

def export_data(df, filename, format_type):
    if format_type == "csv":
        df.to_csv(filename, index=False)
        print(f"Data exported to {filename} in CSV format.")
    elif format_type == "json":
        df.to_json(filename, orient="records")
        print(f"Data exported to {filename} in JSON format.")
    else:
        print("Unsupported format.")

data = {'Name': ['Daud', 'Rayyan', 'Afnan'],
        'Age': [20, 21, 19],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# Exporting to CSV
export_data(df, "Class-5/assignment_code/task_1/output.csv", "csv")

# Exporting to JSON
export_data(df, "Class-5/assignment_code/task_1/output.json", "json")
