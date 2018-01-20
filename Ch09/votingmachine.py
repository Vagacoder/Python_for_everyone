## For Ch09 P9.10

class VotingMachine:
    
    def __init__(self):
        self._demo = 0
        self._repu = 0
    
    def reset(self):
        self._demo = 0
        self._repu = 0        
    
    def voteForDemo(self):
        self._demo += 1
    
    def voteForRepu(self):
        self._repu += 1
    
    def tally(self):
        print('Democrat: %d' %self._demo)
        print('Republican: %d' %self._repu)
