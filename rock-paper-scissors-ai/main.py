import random
import csv
import os
from ai_model.predict import predict_next_move

MOVES = ['rock', 'paper', 'scissors']
DATA_PATH = 'data/game_history.csv'


def determine_winner(player, ai):
    if player == ai:
        return 'draw'
    elif (player == 'rock' and ai == 'scissors') or \
         (player == 'paper' and ai == 'rock') or \
         (player == 'scissors' and ai == 'paper'):
        return 'player'
    else:
        return 'ai'


def counter_move(predicted):
    if predicted == 'rock':
        return 'paper'
    elif predicted == 'paper':
        return 'scissors'
    elif predicted == 'scissors':
        return 'rock'
    return random.choice(MOVES)


def save_to_csv(player_move, ai_move, result):
    file_exists = os.path.isfile(DATA_PATH)
    with open(DATA_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['player_move', 'ai_move', 'result'])  
        writer.writerow([player_move, ai_move, result])


def play_game(rounds=10):
    print("🎮 Rock-Paper-Scissors with AI\n---")
    move_history = []

    for i in range(rounds):
        print(f"\nRound {i+1}")
        player_move = input("Your move (rock/paper/scissors): ").lower()

        while player_move not in MOVES:
            player_move = input("Invalid! Enter rock, paper, or scissors: ").lower()

       
        if len(move_history) >= 3:
            recent_moves = move_history[-3:]
            predicted = predict_next_move(recent_moves)
            ai_move = counter_move(predicted)
        else:
            ai_move = random.choice(MOVES)

        result = determine_winner(player_move, ai_move)
        print(f"AI chose: {ai_move}")
        print(f"Result: {result.upper()}")

        move_history.append(player_move)
        save_to_csv(player_move, ai_move, result)

    print(f"\n🎉 {rounds} round completed. Game data saved to {DATA_PATH}.")

if __name__ == "__main__":
    play_game(10)
