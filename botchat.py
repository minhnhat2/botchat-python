import tkinter as tk
from datetime import datetime
import webbrowser
import os

keywords = {}
with open('keywords.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        keyword, answer = line.strip().split('|')
        keywords[keyword] = answer

root = tk.Tk()
root.title("Chat Bot")
root.geometry("400x400")

input_box = tk.Entry(root, width=40)
input_box.pack(pady=10)

chat_box = tk.Text(root, width=40, height=15)
chat_box.pack()

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def handle_input():
    user_input = input_box.get()
    chat_box.insert(tk.END, f"\nYou: {user_input}")
    input_box.delete(0, tk.END)

    if user_input.lower() == "shutdown":
        os.system("shutdown /s /t 1")
        chat_box.insert(tk.END, f"\nBot: Shutting down the computer...")
    elif user_input.lower() == "open google":
        webbrowser.open("https://www.google.com")
        chat_box.insert(tk.END, f"\nBot: Opening Google...")
    elif "time" in user_input.lower():
        current_time = get_time()
        chat_box.insert(tk.END, f"\nBot: The current time is {current_time}")
    else:
        found_keyword = False
        for keyword in keywords:
            if keyword in user_input.lower():
                chat_box.insert(tk.END, f"\nBot: {keywords[keyword]}")
                found_keyword = True
                break
        if not found_keyword:
            webbrowser.open(f"https://www.google.com/search?q={user_input}")
            chat_box.insert(tk.END, f"\nBot: I'm sorry, I don't have an answer for that. "
                                     f"I've searched it on Google for you.")

    chat_box.see(tk.END)

submit_button = tk.Button(root, text="Submit", command=handle_input)
submit_button.pack()

root.mainloop()
