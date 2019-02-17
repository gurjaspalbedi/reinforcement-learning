from typing import List, Tuple

class StatesAndBlocks:

    def __init__(self, positive_terminal_states, negative_terminal_states, starting_states, blocking_states):
        self.positive_terminal_states = positive_terminal_states
        self.negative_terminal_states = negative_terminal_states
        self.starting_states = starting_states
        self.blocking_states = blocking_states

    def get_terminal_states(self) -> List[int]:
        """Returns the list containing the state number of terminal states
        
        Returns
        -------
        List[int]
            The list containing the state number of the terminal states
        """
        return self.positive_terminal_states + self.negative_terminal_states    
    