import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
data = pd.read_csv("Breast_cancer_data.csv")

# Split the data into features (X) and target variable (y)
X = data.drop('diagnosis', axis=1)
y = data['diagnosis']

# Split the data into training and testing sets (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the SVM classifier with a linear kernel
svm_classifier = SVC(kernel='linear', random_state=42)

# Train the classifier using the training data
svm_classifier.fit(X_train, y_train)

# Evaluate the Model
y_pred = svm_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy*100:.2f}%")
print("\nClassification Report:")
print(class_report)

# Initialize the standard scaler
scaler = StandardScaler()
X_train_normalized = scaler.fit_transform(X_train)
X_test_normalized = scaler.transform(X_test)

# Define the hyperparameters and their distributions
param_dist = {
    'C': [0.1, 1, 10, 100],
    'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],
    'gamma': ['scale', 'auto', 0.1, 1, 10]
}

# Initialize the RandomizedSearchCV
random_search = RandomizedSearchCV(
    SVC(), 
    param_distributions=param_dist, 
    n_iter=10, 
    cv=10, 
    n_jobs=-1, 
    verbose=1, 
    random_state=42
)

# Fit the randomized search to the normalized training data
random_search.fit(X_train_normalized, y_train)

# Extract the best hyperparameters from the randomized search
best_params = random_search.best_params_

# Train and Evaluate SVM with Optimal Hyperparameters
optimized_svm_classifier = SVC(**best_params)
optimized_svm_classifier.fit(X_train_normalized, y_train)
y_pred_optimized = optimized_svm_classifier.predict(X_test_normalized)
accuracy_optimized = accuracy_score(y_test, y_pred_optimized)
class_report_optimized = classification_report(y_test, y_pred_optimized)

print(f"Optimized Model Accuracy: {accuracy_optimized*100:.2f}%")
print("\nOptimized Model Classification Report:")
print(class_report_optimized)

# Save the trained model and scaler
joblib.dump(optimized_svm_classifier, "SVM_model.joblib")
joblib.dump(scaler, "scaler.joblib")
