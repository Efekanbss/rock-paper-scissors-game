import tkinter as tk
from ai_model.predict import predict_next_move
from main import determine_winner, counter_move
import random
from tkinter import messagebox
from ai_model.retrain import retrain_model
import csv
import os



def save_to_csv_gui(player_move, ai_move, result):
    data_path = 'data/game_history.csv'
    file_exists = os.path.isfile(data_path)
    
    with open(data_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['player_move', 'ai_move', 'result'])  
        writer.writerow([player_move, ai_move, result])

MOVES = ['rock', 'paper', 'scissors']
player_history = []
player_score = 0
ai_score = 0
draws = 0
correct_predictions = 0
prediction_count = 0

def on_player_move(player_move):
    global player_score, ai_score, draws, correct_predictions, prediction_count

    
    if len(player_history) >= 3:
        recent = player_history[-3:]
        predicted = predict_next_move(recent)
        ai_move = counter_move(predicted)
        prediction_count += 1
        if predicted == player_move:
            correct_predictions += 1
    else:
        ai_move = random.choice(MOVES)

    result = determine_winner(player_move, ai_move)
    player_history.append(player_move)
    save_to_csv_gui(player_move, ai_move, result)

    if result == 'player':
        player_score += 1
    elif result == 'ai':
        ai_score += 1
    else:
        draws += 1

    
    result_label.config(text=f"AI chose: {ai_move} — Result: {result.upper()}")
    score_label.config(text=f"Player: {player_score} | AI: {ai_score} | Draws: {draws}")
    
    if prediction_count > 0:
        accuracy = correct_predictions / prediction_count * 100
        accuracy_label.config(text=f"Prediction Accuracy: {accuracy:.1f}%")
    else:
        accuracy_label.config(text="Prediction Accuracy: —")


def retrain_and_notify():
    try:
        sample_count = retrain_model()
        messagebox.showinfo("Model Retrained", f"✅ AI model retrained with {sample_count} samples.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")


root = tk.Tk()
root.title("Rock Paper Scissors AI")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()


tk.Label(frame, text="Choose your move:", font=("Arial", 16)).pack()


for move in MOVES:
    btn = tk.Button(frame, text=move.capitalize(), width=15, height=2, command=lambda m=move: on_player_move(m))
    btn.pack(pady=5)
   
    retrain_btn = tk.Button(frame, text="🔁 Retrain AI Model", bg="lightblue", command=retrain_and_notify)
    retrain_btn.pack(pady=10)



result_label = tk.Label(frame, text="", font=("Arial", 14))
result_label.pack(pady=10)

score_label = tk.Label(frame, text="Player: 0 | AI: 0 | Draws: 0", font=("Arial", 12))
score_label.pack()

accuracy_label = tk.Label(frame, text="Prediction Accuracy: —", font=("Arial", 12))
accuracy_label.pack()


root.mainloop()
