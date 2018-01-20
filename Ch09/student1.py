## For Ch09 P9.8
from grade import Grade

class Student:
    
    def __init__(self, name):
        
        self._name = name
        self._totalScore = 0.0
        self._quizCount = 0
    
    def getName(self):
        return self._name
    
    def addQuiz(self, inputGrade):
        letterGrade = Grade(inputGrade)
        self._totalScore += letterGrade.getNumericGrade()
        self._quizCount += 1
    
    def getTotalScore(self):
        return self._totalScore
    
    def getGPA(self):
        return self._totalScore / self._quizCount

    