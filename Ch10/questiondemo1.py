##
#  This program shows a simple quiz with one question.
#

from questions import Question
from choicequestion import ChoiceQuestion

# Create the question and expected answer.
q = Question()
q.setText("Who is the inventor of Python?")
q.setAnswer("Guido van Rossum")      

# Display the question and obtain user's response.
q.display()
response = input("Your answer: ")
print(q.checkAnswer(response))

cq = ChoiceQuestion()
cq.setText('Test question1')
cq.addText(' new text')
cq.setAnswer('2')
print(cq.checkAnswer('2'))