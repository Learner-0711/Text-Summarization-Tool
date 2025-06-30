import tkinter as tk
from tkinter import messagebox, scrolledtext
from summarizer import generate_summary

def perform_summary():
    user_input = input_box.get("1.0", tk.END).strip()
    if len(user_input) < 10:
        messagebox.showwarning("Input Too Short", "Please enter at least 10 characters.")
        return

    try:
        result = generate_summary(user_input, lines=3)
        
        input_box.delete("1.0", tk.END)

        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)
        output_box.config(state=tk.DISABLED)

    except Exception as err:
        messagebox.showerror("Processing Error", f"An error occurred:\n{err}")

# Initialize window
root = tk.Tk()
root.title("Text Summary Assistant 🧠")
root.geometry("880x680")
root.configure(bg="#eef2f7")

# Styling
TITLE_FONT = ("Calibri", 18, "bold")
LABEL_FONT = ("Calibri", 12)
TEXT_FONT = ("Courier New", 12)
PRIMARY_COLOR = "#1976d2"
HOVER_COLOR = "#125ea0"

# Header
title = tk.Label(root, text="AI-Based Text Summarization", font=TITLE_FONT, bg="#eef2f7", fg="#222")
title.pack(pady=(20, 15))

# Input Section
input_text_label = tk.Label(root, text="Insert your text below:", font=LABEL_FONT, bg="#eef2f7")
input_text_label.pack(anchor="w", padx=25)

input_box = scrolledtext.ScrolledText(root, height=12, width=100, wrap=tk.WORD, font=TEXT_FONT, bg="white", bd=1, relief=tk.SUNKEN)
input_box.pack(padx=25, pady=(5, 20))

# Hover Effects
def highlight(e): summarize_button.config(bg=HOVER_COLOR)
def unhighlight(e): summarize_button.config(bg=PRIMARY_COLOR)

# Summarize Button
summarize_button = tk.Button(root, text="Generate Summary", font=("Calibri", 12, "bold"),
                             bg=PRIMARY_COLOR, fg="white", padx=20, pady=10,
                             relief=tk.FLAT, command=perform_summary, cursor="hand2")
summarize_button.bind("<Enter>", highlight)
summarize_button.bind("<Leave>", unhighlight)
summarize_button.pack(pady=10)

# Output Section
output_label = tk.Label(root, text="Generated Summary:", font=LABEL_FONT, bg="#eef2f7")
output_label.pack(anchor="w", padx=25, pady=(15, 0))

output_box = scrolledtext.ScrolledText(root, height=9, width=100, wrap=tk.WORD, font=TEXT_FONT, bg="#e3e3e3", bd=1, relief=tk.SUNKEN)
output_box.config(state=tk.DISABLED)
output_box.pack(padx=25, pady=(5, 15))

# Footer
credit = tk.Label(root, text="Developed by Yash Sharma", font=("Calibri", 10, "italic"), bg="#eef2f7", fg="#666")
credit.pack(side=tk.BOTTOM, pady=10)

# Launch the GUI
root.mainloop()
