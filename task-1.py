import pandas as pd

df = pd.read_csv("KaggleV2-May-2016.csv")

# Display Dataset Info
print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())


# Handle Missing Values
for col in df.columns:

    if df[col].dtype == "int64" or df[col].dtype == "float64":
        df[col].fillna(df[col].mean(), inplace=True)

    else:
        df[col] = df[col].fillna(df[col].mode()[0])

# Remove Duplicate Rows
print("\nDuplicate Rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

# Rename Column Names
df.columns = [
    "patient_id",
    "appointment_id",
    "gender",
    "scheduled_day",
    "appointment_day",
    "age",
    "neighbourhood",
    "scholarship",
    "hypertension",
    "diabetes",
    "alcoholism",
    "handicap",
    "sms_received",
    "no_show"
]

print("\nUpdated Column Names:")
print(df.columns)

# Convert Date Columns
df["scheduled_day"] = pd.to_datetime(df["scheduled_day"])
df["appointment_day"] = pd.to_datetime(df["appointment_day"])

# Standardize Text Values
df["gender"] = df["gender"].str.upper()
df["no_show"] = df["no_show"].str.upper()

# Fix Age Values
df = df[df["age"] >= 0]

# Check Data Types
print("\nData Types:")
print(df.dtypes)

# Final Information
print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Save Cleaned Dataset
df.to_csv("Cleaned_Medical_Appointment.csv", index=False)

print("\nData Cleaning Completed Successfully!")
print("Cleaned file saved as Cleaned_Medical_Appointment.csv")
