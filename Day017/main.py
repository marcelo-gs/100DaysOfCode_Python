from data import PrepareQuestionList
from question_model import Question
from quiz_brain import QuizBrain
import random

question_bank = []
for item in PrepareQuestionList(random.randint(10, 30)):
    question_bank.append(Question(item['text'], item['answer']))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")