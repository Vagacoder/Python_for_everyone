## Ch09 P9.25

from mailbox import MailBox
from message import Message

m1 = Message('Harry Morgan', 'Rudolf Reindeer')
m1.append('I\'ll see you in classroom.')

m2 = Message('Alex Smith', 'Bob Walhberg')
m2.append('I need call you, please let me what time is convinient for you. Thanks!')

mbox = MailBox()
mbox.addMessage(m1)
mbox.addMessage(m2)
newMessage = mbox.getMessage(0)
print(newMessage.toString())
mbox.removeMessage(0)
newMessage = mbox.getMessage(0)
print(newMessage.toString())

