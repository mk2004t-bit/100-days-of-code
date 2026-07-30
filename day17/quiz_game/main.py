from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for bit in question_data:
  question = Question(bit["text"],bit["answer"])
  question_bank.append(question)



quiz = QuizBrain(question_list=question_bank)
while quiz.still_has_questions:
  quiz.next_question()
print("You have completed the quiz.")
print(f"Your final score was : {quiz.score}/{len(question_bank)}")



"""You still got index out of bound and you didnt use trivial db to switch the questions."""