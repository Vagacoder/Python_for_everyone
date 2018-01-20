## Class ComboLock for Ch09 P9.9

class ComboLock:
    
    def __init__(self, secret1, secret2, secret3):
        self._pass = []
        self._inputPass = []
        self._currentPosition = 0
        
        if isinstance(secret1, int) and isinstance(secret2, int) and isinstance(secret3, int):
            
            if (secret1 >39 and secret1 < 0) and (secret2 >39 and secret2 < 0) and (secret3 >39 and secret3 < 0):
                print('Input range: 0 - 39.')

            else:
                self._pass.append(secret1)
                
                if secret2 >= secret1:
                    self._pass.append(secret2 -40)
                else:
                    self._pass.append(secret2)
                
                if secret3 >= secret2:
                    self._pass.append(secret3)
                else:
                    self._pass.append(secret3 + 40)
        else:
            print('Wrong password, please enter 3 integers.')
            
                  
    def reset(self):
        self._inputPass = []
        self._currentPosition = 0
    
    def turnLeft(self, ticks):
        self._currentPosition -= ticks
        self._inputPass.append(self._currentPosition)
    
    def turnRight(self, ticks):
        self._currentPosition += ticks

        self._inputPass.append(self._currentPosition)
    
    def open(self):
        if self._inputPass == self._pass:
            return True
        else:
            return False
