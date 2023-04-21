import pandas

DATA_FILE = "50_states.csv"


class DataManager():
    def __init__(self) -> None:
        self.states_data = pandas.read_csv(DATA_FILE)
        self.state_row = None
        self.state_cor = ()
        self.states_list = self.states_data.state.to_list()
        self.guessed_states = []
        self.to_learn_list = []

    def get_state_cor(self, state_guessed):
        self.state_row = (
            self.states_data[self.states_data.state == state_guessed])
        self.state_cor = (int(self.state_row.x), int(self.state_row.y))
        if state_guessed not in self.guessed_states:
            self.add_to_states_list(state_guessed)

    def add_to_states_list(self, state_guessed):
        self.guessed_states.append(state_guessed)

    def exit(self):
        for state in self.states_list:
            if state not in self.guessed_states:
                self.to_learn_list.append(state)
        to_learn = pandas.DataFrame(self.to_learn_list)
        to_learn.to_csv("states_to_learn.csv")
