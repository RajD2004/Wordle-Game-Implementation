# Wordle (Python Terminal Version)

A simple terminal-based Wordle clone implemented in Python.  
The game picks a random 5-letter target word and gives color-coded feedback for each guess.

## Features
- Random target word loaded from `words.txt`
- 5×5 board stored internally
- Color feedback:
  - 🟩 **Green** — correct letter, correct position  
  - 🟨 **Yellow** — correct letter, wrong position  
  - 🟥 **Red** — letter not in the word
- Frequency-based checking to handle duplicate letters correctly
- Up to 5 attempts per game
- Option to replay

## Files
- `wordle.py` — Game logic (board, validation, coloring, word checking) :contentReference[oaicite:0]{index=0}  
- `main.py` — CLI interface and gameplay loop :contentReference[oaicite:1]{index=1}  

## How to Run
```bash
python3 main.py
