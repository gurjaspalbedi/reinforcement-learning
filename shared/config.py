class Config:

    def __init__(self):
        self.positive_terminal_states = [3]
        self.negative_terminal_states = [7]
        self.starting_states = [8]
        self.blocking_states = [5]

        self.number_of_columns  = 4
        self.numer_of_rows  = 3 
        
        self.positive_reward = 1
        self.negative_reward = -1
        self.step_reward = 0
