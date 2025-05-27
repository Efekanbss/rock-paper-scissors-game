# Rock-Paper-Scissors AI Agent 🎮🧠

This project is an AI-powered Rock-Paper-Scissors game where the computer opponent uses a machine learning model to predict the player's next move.

## Features

- Machine Learning model (Decision Tree)
- Real-time prediction accuracy display
- Playable via GUI or command line
- Retrainable AI based on game history

## How It Works

- The model is trained using the last 3 player moves to predict the next move.
- During gameplay, the AI chooses a counter move based on its prediction.
- Gameplay data is saved to `game_history.csv` and used for future training.

## Usage

Install requirements:

pip install -r requirements.txt