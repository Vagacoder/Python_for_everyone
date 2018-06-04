## Ch10 P10.2

from questions import Question
from fillinquestion import FillInQuestion

fq1 = FillInQuestion("The inventor of Python was _Guido van Rossum_")
fq1.display()
print(fq1.checkAnswer('Guido van Rossum'))
print(fq1.checkAnswer('uido van Rossum'))