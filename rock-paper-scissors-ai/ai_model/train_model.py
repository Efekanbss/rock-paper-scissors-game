import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pickle
import os


DATA_PATH = 'data/processed_data.csv'
MODEL_PATH = 'ai_model/model.pkl'


df = pd.read_csv(DATA_PATH)

X = df[['prev_1', 'prev_2', 'prev_3']].copy()
y = df['next']

encoder = LabelEncoder()
for col in X.columns:
    X[col] = encoder.fit_transform(X[col])

y = encoder.fit_transform(y) 


model = DecisionTreeClassifier()
model.fit(X, y)


with open(MODEL_PATH, 'wb') as f:
    pickle.dump((model, encoder), f)

print(f"✅ Model eğitildi ve kaydedildi: {MODEL_PATH}")
