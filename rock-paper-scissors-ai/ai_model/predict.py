import pickle
import numpy as np
import pandas as pd


MODEL_PATH = 'ai_model/model.pkl'


def predict_next_move(prev_moves):
    """
    prev_moves: List of 3 strings, e.g., ['rock', 'paper', 'scissors']
    returns: predicted move (string)
    """
    
    with open(MODEL_PATH, 'rb') as f:
        model, encoder = pickle.load(f)

    
    encoded_input = [encoder.transform([move])[0] for move in prev_moves]

    encoded_input = pd.DataFrame([encoded_input], columns=['prev_1', 'prev_2', 'prev_3'])


    
    predicted_label = model.predict(encoded_input)[0]

    
    predicted_move = encoder.inverse_transform([predicted_label])[0]
    return predicted_move
