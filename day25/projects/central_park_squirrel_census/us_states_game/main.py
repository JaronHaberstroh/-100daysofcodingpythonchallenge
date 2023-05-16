from turtle import Screen
from write_states import Writter
from scoreboard import ScoreBoard
from manage_data import DataManager

IMAGE = "blank_states_img.gif"
SCREEN_W = 800
SCREEN_H = 600

screen = Screen()
screen.setup(width=SCREEN_W, height=SCREEN_H)
screen.title("U.S States Game")
screen.bgpic(IMAGE)

scoreboard = ScoreBoard()
data_manager = DataManager()
writter = Writter()


while True:

    if len(data_manager.guessed_states) == 50:
        break

    user_guess = screen.textinput(
        title=f"SCORE: {scoreboard.score}/50 Guess the state!",
        prompt="Which state would you like to guess?").title()

    if user_guess.lower() == "exit":
        data_manager.exit()
        break

    if (user_guess in data_manager.states_list and
            user_guess not in data_manager.guessed_states):
        scoreboard.increase_score()
        data_manager.get_state_cor(state_guessed=user_guess)
        writter.write_state(user_guess, coordinates=data_manager.state_cor)
