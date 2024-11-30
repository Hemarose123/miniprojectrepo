import tkinter as tk
from tkinter import scrolledtext

# Function to send messages
def send_message():
    message = message_entry.get()
    if message != "":
        chat_area.config(state=tk.NORMAL)  # Enable the chat area for editing
        chat_area.insert(tk.END, "You: " + message + "\n")
        chat_area.config(state=tk.DISABLED)  # Disable it after updating
        message_entry.delete(0, tk.END)  # Clear the entry box

# Create the main window
root = tk.Tk()
root.title("Simple Chat Application")

# Create the chat area (scrollable text box)
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the message entry field
message_entry = tk.Entry(root, width=40, font=("Arial", 14))
message_entry.grid(row=1, column=0, padx=10, pady=10)

# Create the send button
send_button = tk.Button(root, text="Send", font=("Arial", 14), command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the main event loop
root.mainloop()
