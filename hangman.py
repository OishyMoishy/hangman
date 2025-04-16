import tkinter as tk
import random

words = [
    "python", "tkinter", "hangman", "developer", "programming",
     "widget", "computer", "laptop", "keyboard", "monitor", "mouse",
     "internet", "software", "hardware", "database", "network", "security",
    "algorithm", "function", "variable", "loop", "condition", "array", "dictionary",
    "string", "integer", "boolean", "library", "machine", "learning", "artificial",
    "intelligence", "encryption", "debugging", "compiler", "interpreter", "cloud",
    "storage", "server", "client", "protocol", "router", "switch", "hacker", "cyber",
    "engineer"
]

guess = random.choice(words)
hidden = ["_"] * len(guess)
attempts = 6
guessed = set()

def checkLetter(letter, button):
    global attempts
    letter = letter.lower()
    guessed.add(letter)
    button.config(state="disabled", disabledforeground="red")

    if letter in guess:
        for index, char in enumerate(guess):
            if char == letter:
                hidden[index] = letter
        label_word.config(text=" ".join(hidden))
    else:
        attempts -= 1
        label_attempts.config(text=f"Attempts Left: {attempts}")

    if "_" not in hidden:
        label_status.config(text="You Won!", fg="green")
        disable_all_buttons()

    if attempts == 0:
        label_status.config(text=f"You Lost! The word was '{guess}'", fg="red")
        disable_all_buttons()

def disable_all_buttons():
    for btn in buttons.values():
        btn.config(state="disabled")

root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x400")

tk.Label(root, text="Guess the word:").pack(pady=5)
label_word = tk.Label(root, text=" ".join(hidden), font=("Arial", 20))
label_word.pack()

label_attempts = tk.Label(root, text=f"Attempts Left: {attempts}", font=("Arial", 12))
label_attempts.pack(pady=5)

label_status = tk.Label(root, text="", font=("Arial", 14))
label_status.pack(pady=10)

alphabet_frame = tk.Frame(root)
alphabet_frame.pack(pady=10)

buttons = {}

for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    btn = tk.Button(alphabet_frame, text=letter, width=3, command=lambda l=letter: checkLetter(l, buttons[l]))
    btn.grid(row=i//9, column=i%9, padx=2, pady=2)
    buttons[letter] = btn

root.mainloop()
