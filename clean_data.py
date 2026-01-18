import pandas as pd

# 1️⃣ Load your CSV file
final_data = pd.read_csv("final_dataset.csv")  # make sure the file is in the same folder

# 2️⃣ Strip any extra spaces from column names
final_data.columns = final_data.columns.str.strip()

# 3️⃣ Rename columns to match what we want
final_data = final_data.rename(columns={'Assignment Score': 'Assignment'})

# 4️⃣ Keep only the relevant columns
columns_to_keep = ['Attendance', 'Internal Test 1', 'Internal Test 2', 'Assignment', 'Study Hours', 'Performance']

# Make sure all columns exist
columns_to_keep_existing = [col for col in columns_to_keep if col in final_data.columns]

clean_data = final_data[columns_to_keep_existing]

# 5️⃣ Check the first few rows
print(clean_data.head())

# 6️⃣ Save the cleaned dataset
clean_data.to_csv("clean_final_data.csv", index=False)

print("Data cleaned and saved successfully!")
