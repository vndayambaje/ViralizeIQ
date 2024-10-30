import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

class EngagementPredictor:
    def __init__(self):
        self.model = None

    def extract_features(self, content):
        return len(content)

    def predict(self, features):
        if self.model is None:
            self.model = joblib.load("models/engagement_model.joblib")
        return self.model.predict([[features]])

def train_model(file_path):
    df = pd.read_csv(file_path)
    X = df[['caption_length']]
    y = df['likes']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, "models/engagement_model.joblib")
    print("Model trained and saved.")