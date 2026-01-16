import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1️⃣ Load cleaned dataset
data = pd.read_csv("clean_final_data.csv")

# 2️⃣ Features and target
X = data[['Attendance', 'Internal Test 1', 'Internal Test 2', 'Assignment', 'Study Hours']]
y = data['Performance']

# 3️⃣ Encode target if categorical
if y.dtype == 'object':
    le = LabelEncoder()
    y = le.fit_transform(y)

# 4️⃣ Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5️⃣ Train Logistic Regression model
best_model = LogisticRegression(max_iter=1000)
best_model.fit(X_train, y_train)

# 6️⃣ Evaluate model
y_pred = best_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 7️⃣ Save the model for future use
joblib.dump(best_model, "best_model.pkl")
print("Best model saved as 'best_model.pkl'")

# 8️⃣ Optional: Predict new data
# new_student = pd.DataFrame([[85, 30, 36, 7, 3]], columns=['Attendance', 'Internal Test 1', 'Internal Test 2', 'Assignment', 'Study Hours'])
# prediction = best_model.predict(new_student)
# print("Predicted Performance:", prediction)
