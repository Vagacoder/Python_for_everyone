## For Ch09 P9.24

class Message:
    
    def __init__(self, sender, recipient):
        self._sender = sender
        self._recipient = recipient
        self._text = ''

        
    def append(self, line):
        self._text += line
        self._text += '\n'
    
    
    def toString(self):
        text = 'From: ' + self._sender +'\nTo: ' + self._recipient + '\n' + self._text
        return text