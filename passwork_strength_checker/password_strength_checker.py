import tkinter as tk
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    
    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    
    # Character variety checks
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    
    # Common password check
    common_passwords = ["password", "123456", "qwerty", "letmein", "welcome"]
    if password.lower() in common_passwords:
        score -= 2
    
    # Repetitive patterns
    if re.search(r'(.)\1\1\1', password) or re.search(r'(123|abc)', password):
        score -= 1

    # Password strength categories
    if score >= 5:
        return "Strong"
    elif 3 <= score < 5:
        return "Moderate"
    else:
        return "Weak"

# Function to handle the button click event
def check_strength():
    password = password_entry.get()
    strength = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}")

# Set up the Tkinter window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

# Add widgets
title_label = tk.Label(root, text="Enter a Password", font=("Helvetica", 12))
title_label.pack(pady=10)

password_entry = tk.Entry(root, width=25, show="*")
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
