import math
from typing import List
from .i_problem_solver import IProblemSolver  

class PrimeClassifier(IProblemSolver):
    def compute_results(self, data: List[int]) -> List[str]:
      result = []
      for number in data:
        number_int = int(number)
        classification = self._prime_classification(number_int)
        aux = {"number":number, "result":classification}
        # aux = str(number_int) + " " + classification
        result.append(aux)
      return result
    
    def _is_prime(self,number):
        if number < 2:
            return False
        # if number == 4:
        #     return False
        for i in range(2, math.isqrt(number) + 1):
            if number % i == 0:
                return False
        return True

    def _prime_classification(self,number: int):
        if number == 1 or number == 0:
            return str(number)
    
        if self._is_prime(number):
            return "Prime"
        
        divisors_count = 0
        prime_divisors_count = 0
        for i in range(2, number):
            if number % i == 0:
                divisors_count += 1
                if self._is_prime(i):
                    prime_divisors_count += 1
        
        if divisors_count == 2 and prime_divisors_count == 2:
            return "Semiprime"
        
        raiz = math.isqrt(number)
        if raiz * raiz == number and self._is_prime(raiz):
            return "Quadratic-Semiprime"
        
        return str(number)
   