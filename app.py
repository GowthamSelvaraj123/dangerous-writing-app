import tkinter as tk
from tkinter import messagebox
import threading

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dangerous Writing App")
        self.root.geometry("600x400")

        self.text_area = tk.Text(root, font=("Arial", 14))
        self.text_area.pack(expand=True, fill='both')

        self.timeout = 5  # seconds
        self.timer = None

        # Bind keypress event
        self.text_area.bind("<Key>", self.reset_timer)

        # Start timer initially
        self.start_timer()

    def start_timer(self):
        self.cancel_timer()
        self.timer = threading.Timer(self.timeout, self.clear_text)
        self.timer.start()

    def reset_timer(self, event=None):
        self.start_timer()

    def cancel_timer(self):
        if self.timer:
            self.timer.cancel()

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)
        messagebox.showinfo("Oops!", "You stopped typing. All text has been deleted!")
        self.start_timer()  # restart timer after clearing

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    app.run()
