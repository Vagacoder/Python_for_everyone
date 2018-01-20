## For Ch09 P9.7

class Student:
    
    def __init__(self, name):
        
        self._name = name
        self._totalScore = 0.0
        self._quizCount = 0
    
    def getName(self):
        return self._name
    
    def addQuiz(self, score):
        
        self._totalScore += score
        self._quizCount += 1
    
    def getTotalScore(self):
        return self._totalScore
    
    def getAverageScore(self):
        return self._totalScore / self._quizCount

    