ELECTORS = {'CA': 55, 'TX': 38, 'FL': 29, 'MA': 11}


class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=[], votes=0):
        """Initialize candidate.

        name: string
        winning_states: a list of strings representing initial winning state(s).
        votes: integer, representing number of votes
        """
        self.name = name
        self.winning_states = winning_states
        self.votes = votes

    def __str__(self):
        """Return a string representaion of this candidate,
        including name and winning state(s).
        """
        return '{} wins in these states: {}, and has a vote total of {}.'.format(self.name, self.winning_states, self.votes)

    def __gt__(self, other_candidate):
        if self.votes > other_candidate.votes:
            return True
        else:
            return False

    def win_state(self, state):
        """Adds a state to winning_states and updates votes.

        state: a string of state abbreviation
        """
        self.winning_states.append(state)

        for key in ELECTORS:
            if key == state:
                self.votes += ELECTORS[key]
        self.votes += 1



def main():
    trump = Candidate('Donald Trump')
    clinton = Candidate('Hillary Clinton', winning_states=['CA'], votes=55)
    print(trump)
    print(clinton)
    print()
    print('After election:')
    trump.win_state('FL')
    trump.win_state('TX')
    clinton.win_state('MA')
    print(trump)
    print(clinton)
    print('Does Trump win?')
    print(trump > clinton)

if __name__ == '__main__':
    main()