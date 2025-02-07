import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import csv

data = {
    "speed": [],
    "timestamp": [],
    "supposedActivity": []
}

with open('user_activity.csv', newline='', encoding='utf-8') as csvfile:
    sr = csv.reader(csvfile, delimiter=',')
    next(sr)  # Skip header
    for row in sr:
        data['speed'].append(row[1])
        data['timestamp'].append(row[2])
        data['supposedActivity'].append(row[3])

df = pd.DataFrame(data)

# Ensure 'speed' is numeric (convert from string to float)
df["speed"] = pd.to_numeric(df["speed"], errors="coerce")

# Convert 'timestamp' to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# Extract features from 'timestamp'
df["hour_of_day"] = df["timestamp"].dt.hour
df["day_of_week"] = df["timestamp"].dt.weekday

# Encode 'supposedActivity' manually
activity_mapping = {"STILL": 0, "WALKING": 1, "RUNNING": 2, "IN_VEHICLE": 3}
df["activity_encoded"] = df["supposedActivity"].map(activity_mapping)

# Remove rows with missing values
df = df.dropna()

# Prepare features (X) and target (y)
X = df[["speed", "hour_of_day", "day_of_week"]]
# X = df[["speed"]]
y = df["activity_encoded"].astype(int)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict and print classification report
y_pred = clf.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

new_speed = float(input("Add speed: "))
hour_of_day = int(input("Add hour of the day: "))
day_of_week = int(input("Add day of the week: "))

# X_new = [[new_speed, hour_of_day, day_of_week]]
X_new = pd.DataFrame([[new_speed, hour_of_day, day_of_week]], columns=["speed",
                                                                       "hour_of_day",
                                                                       "day_of_week"])
# X_new = pd.DataFrame([[new_speed]], columns=["speed"])

# Predict activity
predicted_activity_encoded = clf.predict(X_new)[0]
activity_labels = {v: k for k, v in activity_mapping.items()}
predicted_activity = activity_labels.get(predicted_activity_encoded, "UNKNOWN")

print(f"Predicted activity for speed {new_speed} m/s: {predicted_activity}")
