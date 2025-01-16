import tkinter as tk
from tkinter import ttk
import subprocess
import threading
import cv2
import os
import signal


class HandRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hand Recognition App")
        self.root.geometry("600x400")
        self.root.configure(bg="#1e272e")  # Darker background for a sleek look

        self.process = None  # To store the process handle of test.py

        self.setup_ui()

    def setup_ui(self):
        # App Title
        tk.Label(
            self.root,
            text="🖐 Hand Recognition App 🖐",
            font=("Helvetica", 24, "bold"),
            bg="#1e272e",
            fg="#ffffff",
        ).pack(pady=30)

        # Add a frame for central alignment
        button_frame = tk.Frame(self.root, bg="#1e272e")
        button_frame.pack(expand=True)

        # Start Prediction Button
        start_button = ttk.Button(
            button_frame,
            text="▶ Start Prediction",
            command=self.start_prediction,
            style="Custom.TButton"
        )
        start_button.grid(row=0, column=0, padx=10, pady=10)

        # Exit Button
        exit_button = ttk.Button(
            button_frame,
            text="✖ Exit",
            command=self.exit_app,
            style="Custom.TButton"
        )
        exit_button.grid(row=1, column=0, padx=10, pady=10)

        # Apply custom button style
        style = ttk.Style()
        style.theme_use("clam")  # Use a clean theme
        style.configure(
            "Custom.TButton",
            font=("Helvetica", 14, "bold"),
            background="#2ecc71",
            foreground="#ffffff",
            padding=10,
            relief="flat",
        )
        style.map(
            "Custom.TButton",
            background=[("active", "#27ae60")],
        )

    def start_prediction(self):
        # Close all OpenCV windows before starting
        cv2.destroyAllWindows()

        # Run test.py in a new thread
        threading.Thread(target=self.run_script, args=("test.py",)).start()

    def run_script(self, script_name):
        # Get the path to the Python executable in the venv
        venv_python = os.path.join("venv", "Scripts", "python.exe")

        # Start test.py as a background process
        self.process = subprocess.Popen([venv_python, script_name])

    def exit_app(self):
        # Close all OpenCV windows
        cv2.destroyAllWindows()

        # Terminate the running process (if any)
        if self.process:
            self.process.terminate()  # Use terminate() to terminate the process


        # Destroy the main Tkinter window
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = HandRecognitionApp(root)
    root.mainloop()
