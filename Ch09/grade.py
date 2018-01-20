## For Ch09 P9.8

class Grade:
    
    def __init__(self, letterGrade):
        
        self._letterGrade = letterGrade.upper()
    
    def getNumericGrade(self):

        if self._letterGrade == 'A' or self._letterGrade == 'A+':
            numericGrade = 4.0
        elif self._letterGrade == 'A-':
            numericGrade = 3.7
        elif self._letterGrade == 'B+':
            numericGrade = 3.3
        elif self._letterGrade == 'B':
            numericGrade = 3.0
        elif self._letterGrade == 'B-':
            numericGrade = 2.7
        elif self._letterGrade == 'C+':
            numericGrade = 2.3
        elif self._letterGrade == 'C':
            numericGrade = 2.0
        elif self._letterGrade == 'C-':
            numericGrade = 1.7
        elif self._letterGrade == 'D+':
            numericGrade = 1.3
        elif self._letterGrade == 'D':
            numericGrade = 1.0
        elif self._letterGrade == 'D-':
            numericGrade = 0.7
        else:
            numericGrade = 0.0

        return numericGrade