import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the sleep data
sleep_data = pd.read_csv('Sleep_Efficiency.csv')

# Preprocess the data
# TODO: segment the data into individual sleep cycles and label them as REM or non-REM sleep

# Extract relevant features
X = sleep_data[['Sleep duration (hrs)', 'Sleep efficiency (%)', 'Age']].values
y = sleep_data['REM sleep percentage'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

# Deploy the model in a real-time environment
# TODO: use the trained model to predict REM cycle sleep in a mobile app or a web application
