import tkinter as tk
from logic import VoteManager

def setup_gui(root: tk.Tk):
    """Set up GUI components within the window"""
    manager = VoteManager()

    def vote():
        """Function to handle voting logic"""
        candidate = candidate_var.get()
        voter_id = voter_id_entry.get().strip()

        if not voter_id or not voter_id.isdigit():
            message_label.config(text="Error: enter a valid voter ID.")
            return

        try:
            manager.add_vote(candidate, voter_id)
            message_label.config(text=f"You voted for: {candidate}")
            reset_interface()
        except ValueError:
            message_label.config(text="Error: Duplicate voter ID")

    def show_results():
        global results_label, back_button
        # Hide voting interface
        vote_button.grid_remove()
        results_button.grid_remove()
        candidate_label.grid_remove()
        candidate_option_menu.grid_remove()
        voter_id_label.grid_remove()
        voter_id_entry.grid_remove()
        message_label.grid_remove()

        results = manager.get_results()
        formatted_results = "\n\n".join([f"{candidate}: {votes}" for candidate, votes in results.items()])
        results_label = tk.Label(root, text=formatted_results, anchor="w", justify="left")
        results_label.grid(row=0, column=0, sticky="ew", columnspan=3, padx=20)

        back_button = tk.Button(root, text="Back", command=show_voting)
        back_button.grid(row=1, column=0, sticky="ew")

        root.update_idletasks()

    def show_voting():
        results_label.grid_remove()
        back_button.grid_remove()
        vote_button.grid()
        results_button.grid()
        candidate_label.grid()
        candidate_option_menu.grid()
        voter_id_label.grid()
        voter_id_entry.grid()
        message_label.grid()

        root.update_idletasks()

    def reset_interface():
        """Resets the GUI to its original look after the vote"""

        voter_id_entry.delete(0, tk.END)
        candidate_var.set("Bryan")

    candidate_label = tk.Label(root, text="Select Candidate:")
    candidate_label.grid(row=0, column=0, sticky="ew")
    candidate_var = tk.StringVar(root)
    candidate_var.set("Bryan")
    candidates = ["Bryan", "Fatima", "Kyle", "Robert", "Azula"]
    candidate_option_menu = tk.OptionMenu(root, candidate_var, *candidates)
    candidate_option_menu.grid(row=1, column=0, sticky="ew")

    voter_id_label = tk.Label(root, text="Enter Voter ID:")
    voter_id_label.grid(row=2, column=0, sticky="ew")
    voter_id_entry = tk.Entry(root)
    voter_id_entry.grid(row=3, column=0, sticky="ew")

    message_label = tk.Label(root, text="", fg="red")
    message_label.grid(row=4, column=0, sticky="ew")

    vote_button = tk.Button(root, text="Vote", command=vote)
    vote_button.grid(row=5, column=0, sticky="ew", pady=(20, 10))

    results_button = tk.Button(root, text="Results", command=show_results)
    results_button.grid(row=6, column=0, sticky="ew", pady=(10, 0))