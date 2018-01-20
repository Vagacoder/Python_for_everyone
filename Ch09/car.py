## For Ch09 P9.6

class Car:
    
    def __init__(self, fuelEff):
        self._fuelEfficiency = fuelEff
        self._fuelTankVol = 14.0
        self._fuelLevel = 0.0
    
    def drive(self, miles):
        gasCosumption = miles / self._fuelEfficiency
        if gasCosumption < self._fuelLevel:
            self._fuelLevel -= gasCosumption
        else:
            self._fuelLevel = 0
    
    
    def addGas(self, gasVol):
        if gasVol + self._fuelLevel < self._fuelTankVol:
            self._fuelLevel += gasVol
        else:
            self._fuelLevel = self._fuelTankVol
    
    def getGasLevel(self):
        return self._fuelLevel
