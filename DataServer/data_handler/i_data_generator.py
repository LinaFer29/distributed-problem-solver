from abc import ABC, abstractmethod
from typing import List

class IDataGenerator(ABC):
    @abstractmethod
    def generate_numbers(self,quantity,lower,upper) -> List:
        pass