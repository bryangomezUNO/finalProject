from typing import Dict, List

class VoteManager:
    """It manages the voting logic with the data storage using a plain text file"""

    def __init__(self, data_file: str = 'votes.txt'):
        """It initializes the voting manager with a data file"""
        self.data_file = data_file
        self.votes, self.voter_ids = self.load_votes()

    def load_votes(self) -> (Dict[str, int], List[str]):
        """It will load votes from a plain text file"""
        try:
            with open(self.data_file, 'r') as file:
                data = file.readlines()
                votes = {line.split(":")[0].strip(): int(line.split(":")[1].strip()) for line in data if ":" in line}
                voter_ids = [line.strip() for line in data if ":" not in line]
        except FileNotFoundError:
            votes = {"Bryan": 0, "Fatima": 0, "Kyle": 0, "Robert": 0, "Azula": 0}
            voter_ids = []
        return votes, voter_ids

    def save_votes(self):
        """Saves the current votes and voter IDs to a plain text file"""
        with open(self.data_file, 'w') as file:
            for candidate, count in self.votes.items():
                file.write(f"{candidate}: {count}\n")
            for voter_id in self.voter_ids:
                file.write(f"{voter_id}\n")

    def add_vote(self, candidate: str, voter_id: str):
        """Adds a vote for a candidate if the voter_id has not been used"""
        if voter_id in self.voter_ids:
            raise ValueError("Duplicate voter ID")
        if candidate not in self.votes:
            raise ValueError("Candidate does not exist")
        self.votes[candidate] += 1
        self.voter_ids.append(voter_id)
        self.save_votes()

    def get_results(self) -> Dict[str, int]:
        """Resets the current vote counts for all candidates"""
        return self.votes
