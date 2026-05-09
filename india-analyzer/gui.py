import tkinter as tk
from tkinter import messagebox


def get_user_input(callback):
    """
    Launches a tkinter GUI window asking the user for two topics.
    Calls callback(fact1, fact2) when the user clicks Analyze.
    """

    window = tk.Tk()
    window.title("india-unfiltered")

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    window.geometry(f"{width}x{height}+0+0")
    
    window.resizable(True, True)
    window.configure(bg="#1e1e1e")

    # title label
    tk.Label(
        window,
        text="india-unfiltered",
        font=("Courier", 16, "bold"),
        bg="#1e1e1e",
        fg="#ffffff"
    ).pack(pady=(20, 4))

    tk.Label(
        window,
        text="Headline frequency analysis — 2001 to 2023",
        font=("Courier", 8),
        bg="#1e1e1e",
        fg="#888888"
    ).pack(pady=(0, 16))

    # fact1 input
    tk.Label(
        window,
        text="Base topic to analyze:",
        font=("Courier", 10),
        bg="#1e1e1e",
        fg="#cccccc"
    ).pack(anchor="w", padx=40)

    fact1_entry = tk.Entry(window, font=("Courier", 11), width=36, bg="#2d2d2d", fg="#ffffff",
                           insertbackground="white", relief="flat", bd=4)
    fact1_entry.pack(padx=40, pady=(2, 10))

    # fact2 input
    tk.Label(
        window,
        text="Topic to analyze against:",
        font=("Courier", 10),
        bg="#1e1e1e",
        fg="#cccccc"
    ).pack(anchor="w", padx=40)

    fact2_entry = tk.Entry(window, font=("Courier", 11), width=36, bg="#2d2d2d", fg="#ffffff",
                           insertbackground="white", relief="flat", bd=4)
    fact2_entry.pack(padx=40, pady=(2, 16))

    # analyze button
    def on_submit():
        fact1 = fact1_entry.get().strip().lower()
        fact2 = fact2_entry.get().strip().lower()

        if not fact1 or not fact2:
            messagebox.showwarning("Missing input", "Please enter both topics before analyzing.")
            return

        if fact1 == fact2:
            messagebox.showwarning("Same topics", "Please enter two different topics to compare.")
            return

        window.destroy()
        callback(fact1, fact2)

    tk.Button(
        window,
        text="Analyze →",
        font=("Courier", 11, "bold"),
        bg="#ffffff",
        fg="#1e1e1e",
        relief="flat",
        padx=16,
        pady=6,
        cursor="hand2",
        command=on_submit
    ).pack()

    window.mainloop()