class Temperature:
    def __init__(self, temperature=0):
        self._temperature = temperature
    
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, updated_temperature):
        if isinstance(updated_temperature, int):
            self._temperature = updated_temperature
        else:
            raise ValueError("updated_temperature must be a valid int")


temp = Temperature()
temp.temperature = 32
print(temp.temperature)