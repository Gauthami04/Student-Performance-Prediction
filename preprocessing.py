import pandas as pd

df = pd.read_csv("dataset.csv")

def performance_label(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    elif score >= 70:
        return "Average"
    else:
        return "Poor"

df["Performance"] = df["Total_score"].apply(performance_label)

df.drop(columns=["Total_score"], inplace=True)

df.to_csv("final_dataset.csv", index=False)

print("Final dataset created successfully!")
