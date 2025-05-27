# Project Report – Rock-Paper-Scissors AI Agent

## Objective

The goal of this project is to create an AI agent that can play Rock-Paper-Scissors using machine learning. The AI learns the player’s behavior over time and predicts their next move.

## Game Description

The player selects rock, paper, or scissors. After at least 3 rounds, the AI begins predicting the player’s next move based on the previous 3. It then selects the counter move to win.

## AI Method

- Machine Learning: Decision Tree Classifier
- Features: Player’s last 3 moves
- Label: Next move
- Training Data: Generated from gameplay history (`game_history.csv`)
- Model is retrainable and saved using `pickle`.

## Tools

- Python
- scikit-learn
- tkinter (GUI)
- pandas, numpy

## Results

- AI can improve as more games are played
- Real-time prediction accuracy is tracked
- GUI provides a user-friendly experience
- The model can be retrained anytime from the interface

## Conclusion

This project demonstrates how machine learning can be used to build adaptive agents in interactive environments. It’s a simple yet effective example of applying AI to gameplay.

