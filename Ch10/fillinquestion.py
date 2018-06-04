## class FillInQuestion for Ch10 P10.2

from questions import Question

class FillInQuestion(Question):
    
    def __init__(self, fullQuestionText):
        super().__init__()
        start = fullQuestionText.index('_')
        end = fullQuestionText.index('_', start+1)
        questionText = fullQuestionText[0:start +1] + '___' + fullQuestionText[end:]
        super().setText(questionText)
        answer = fullQuestionText[start+1:end]
        super().setAnswer(answer)

    def setText(self):
        print('Please use constructor.')
        
    def setAnswer(self):
        print('Please use constructor.')