from abc import ABCMeta, abstractmethod


class Fruit(metaclass=ABCMeta):
    @abstractmethod
    def taste(self):
        pass

    @abstractmethod
    def originated(self):
        pass


class Apple(Fruit):
    def taste(self):
        return "Sweet"
    
    def originated(self):
        return "Central Asia"


apple = Apple()
print(apple.originated())