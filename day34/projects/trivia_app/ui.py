import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.canvas = tk.Canvas(width=600, height=500)
        self.canvas.configure(highlightthickness=0)
        self.question_text = (
            self.canvas.create_text(
                300, 250, width=550,
                text="Sample",
                font=("Arial", 20, "italic")))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50, pady=50)
        self.score_label = tk.Label(text="Score: 0")
        self.score_label.config(background=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, padx=20, pady=20)
        self.iamge_false = tk.PhotoImage(file="images/false.png")
        self.image_true = tk.PhotoImage(file="images/true.png")
        self.button_true = tk.Button(
            image=self.image_true,
            command=self.ans_true)
        self.button_true.config(background=THEME_COLOR, highlightthickness=0)
        self.button_true.grid(row=2, column=0, padx=20, pady=20)
        self.button_false = tk.Button(
            image=self.iamge_false,
            command=self.ans_false)
        self.button_false.config(background=THEME_COLOR, highlightthickness=0)
        self.button_false.grid(row=2, column=1, padx=20, pady=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")
        self.canvas.config(bg="white")

    def ans_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def ans_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
