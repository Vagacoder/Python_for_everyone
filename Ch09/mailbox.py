## class mailbox for Ch09 P9.25

class MailBox:
    
    def __init__(self):
        
        self._messageList = []
        
    
    def addMessage(self, message):
        self._messageList.append(message)
    
    
    def getMessage(self, index):
        return self._messageList[index]
    
    def removeMessage(self, index):
        self._messageList.pop(index)
    
    