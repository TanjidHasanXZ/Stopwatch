import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.running = False
        self.start_time = None
        self.elapsed_time = 0

        # Display Label
        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack()

        # Start Button
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(fill=tk.BOTH, expand=True)

        # Stop Button
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(fill=tk.BOTH, expand=True)

        # Reset Button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(fill=tk.BOTH, expand=True)

    def update_timer(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.display_time(self.elapsed_time)
            self.root.after(50, self.update_timer)

    def display_time(self, elapsed):
        hours, rem = divmod(elapsed, 3600)
        minutes, seconds = divmod(rem, 60)
        self.time_label.config(text="{:02}:{:02}:{:05.2f}".format(int(hours), int(minutes), seconds))

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_timer()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.start_time = time.time()
        self.elapsed_time = 0
        self.display_time(self.elapsed_time)

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()
