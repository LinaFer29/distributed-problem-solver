from typing import List
from .i_problem_solver import IProblemSolver  

class FibonacciVerifier(IProblemSolver):
    def compute_results(self, data: List[int]) -> List[str]:
      result = []
      for number in data:
        number_int = int(number)
        is_fibonacci = self._is_fibonacci(number_int)
        aux = {"number":number, "result":str(is_fibonacci)}
        # aux = str(number_int) + " " + str(is_fibonacci)
        result.append(aux)
      return result

    def _is_fibonacci(self,number: int) -> bool:
      first = -1
      second = 1
      fibonacci = 0
      while fibonacci < number:
          fibonacci =  second + first
          first = second 
          second = fibonacci

      return fibonacci == number