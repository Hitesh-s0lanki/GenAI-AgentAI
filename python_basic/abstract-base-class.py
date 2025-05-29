from abc import ABC, abstractmethod

## Define an abstract class
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

