import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("./iris.csv")

# Clean up column names in case of whitespaces
df.columns = df.columns.str.strip()

# Drop 'Id' column if it exists
if 'Id' in df.columns:
    df.drop('Id', axis=1, inplace=True)

# Check if 'Species' column exists before proceeding
if 'Species' not in df.columns:
    print("Error: 'Species' column not found in the dataset.")
    exit()

# Separate features and label
X = df.drop('Species', axis=1)
y = df['Species']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model accuracy: ",accuracy)

# Save model to .pkl file
with open("iris_model.pkl", "wb") as file:
    pickle.dump(model, file)
