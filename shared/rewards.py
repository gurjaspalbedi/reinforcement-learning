class Rewards:

    def __init__(self, positive_reward, negative_reward, step_reward, state_and_blockers):
        self.positive_reward = positive_reward
        self.negative_reward = negative_reward
        self.step_reward = step_reward
        self.state_and_blockers = state_and_blockers

    def get_reward(self, state_number: int):
        """Returns the reward associated witht the particular state
        
        Parameters
        ----------
        state_number : int
            State number for the particular state
        
        """
        if state_number in self.state_and_blockers.positive_terminal_states:
            return self.positive_reward
        
        if state_number in self.state_and_blockers.negative_terminal_states:
            return self.negative_reward
        else:
            return self.step_reward