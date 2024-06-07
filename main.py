from question_model import Question
from fake_data import question_data
from quiz_brain import QuizBrain

questions = [Question(text=question['text'], answer=question['answer']) for question in question_data]

quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz!", f"Your final grade is {quiz.score}/{quiz.question_number}")