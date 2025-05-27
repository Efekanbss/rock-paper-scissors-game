import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pickle
import os

RAW_DATA_PATH = 'data/game_history.csv'
PROCESSED_PATH = 'data/processed_data.csv'
MODEL_PATH = 'ai_model/model.pkl'

def prepare_processed_data():
    df_raw = pd.read_csv(RAW_DATA_PATH)

    sequences = []
    moves = list(df_raw['player_move'])

    for i in range(3, len(moves)):
        seq = {
            'prev_1': moves[i-3],
            'prev_2': moves[i-2],
            'prev_3': moves[i-1],
            'next': moves[i]
        }
        sequences.append(seq)

    df_processed = pd.DataFrame(sequences)
    df_processed.to_csv(PROCESSED_PATH, index=False)
    return df_processed

def retrain_model():
    df = prepare_processed_data()

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

    return len(df)
