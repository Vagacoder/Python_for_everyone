##
#  This module defines a class that models exam questions. 
#

## A question with a text and an answer.
#
class Question :
   ## Constructs a question with empty question and answer strings.
   #
   def __init__(self) :
      self._text = ""
      self._answer = ""
      
   ##  Sets the question text.
   #   @param questionText the text of this question
   #
   def setText(self, questionText) :   
      self._text = questionText
    

   def addText(self, addtionalText):
      self._text += (' ' + addtionalText)

   ## Sets the answer for this question.
   #  @param correctResponse the answer
   #
   def setAnswer(self, correctResponse) :
      self._answer = correctResponse

   ## Checks a given response for correctness.
   #  @param response the response to check
   #  @return True if the response was correct, False otherwise
   #
   def checkAnswer(self, response) :
      return response == self._answer

   ## Displays this question.
   #
   def display(self) :
      print(self._text)         

class AnyCorrectChoiceQuestion(Question):
    
    def __init__(self):
        super().__init__()
        self._text = 'There are multiple correct choices, please one of them.'
        self._choices = []
        self._correctAnswer = ''
        
        
    def addChoice(self, choice, correct) :
        self._choices.append(choice)
        
        if correct :
            self._correctAnswer += len(self._choices)
    
    def checkAnswer(self, response) :
        return response in self._correctAnswer
    
    def display(self) :
        super().display()
        
        for i in self._choices:
            print('%d, %s' %(i+1, self._choices[i]))