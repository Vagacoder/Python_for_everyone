## For Ch09 P9.11

class Letter:
    
    def __init__(self, letterFrom, letterTo):
        self._sender = letterFrom
        self._receiver = letterTo
        self._body = ''
    
    
    def addLine(self, line):
        self._body += line
        self._body += '\n'
    
    def getText(self):
        text = ''
        text += 'Dear ' + self._receiver
        text += ':\n\n'
        text += self._body
        text += '\n'
        text += 'Sincerely,\n\n'
        text += self._sender
        return text