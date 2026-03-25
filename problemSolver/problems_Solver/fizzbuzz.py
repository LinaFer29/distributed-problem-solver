from typing import List
from .i_problem_solver import IProblemSolver  

class FizzBuzz(IProblemSolver):
    def compute_results(self, data: List[int]) -> List[dict]:
      result = []
      for number in data:
        fizzbuzz = self._fizzbuzz(number)
        aux = {"number":number, "result":fizzbuzz}
      #   aux = str(number) + " " + fizzbuzz
        result.append(aux)
      return result
    
    def _fizzbuzz(self,number):
       if number % 15 == 0:
          return "FizzBuzz"
       if number % 5 == 0:
          return "Buzz"
       if number % 3 == 0:
          return "Fizz"
       return str(number)