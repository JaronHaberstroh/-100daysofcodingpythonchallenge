from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dictionary in question_data:
    new_q = Question(dictionary["question"], dictionary["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(
    f"You've completed the quiz.\nYour final score was: {quiz.score}/{len(quiz.question_list)}")
