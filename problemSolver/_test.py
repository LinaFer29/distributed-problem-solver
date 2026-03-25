import base64
import pytest
from problems_Solver.fizzbuzz import FizzBuzz
from problems_Solver.fibonacci_verifier import FibonacciVerifier
from problems_Solver.prime_classifier import PrimeClassifier
from my_system import MySystem
from problems_Solver.fizzbuzz_creator import FizzBuzzCreator
from cryptography.fernet import Fernet

def test_fizzbuzz():
    expected = data = [{'number': 108450, 'result': 'FizzBuzz'}, {'number': 15155, 'result': 'Buzz'}, {'number': 31854, 'result': 'Fizz'}, {'number': 111086, 'result': '111086'}, {'number': 118118, 'result': '118118'}, {'number': 15804, 'result': 'Fizz'}, {'number': 15025, 'result': 'Buzz'}]
    data = [108450, 15155, 31854, 111086, 118118, 15804, 15025]

    fizzbuzz_problem = FizzBuzz()
    output = fizzbuzz_problem.compute_results(data)

    assert output == expected

def test_fibonacci_verifier():
  expected = [{'number': 4506, 'result': 'False'}, {'number': 233, 'result': 'True'}, {'number': 614, 'result': 'False'}, {'number': 55, 'result': 'True'}, {'number': 4426, 'result': 'False'}, {'number': 3984, 'result': 'False'}, {'number': 987, 'result': 'True'}, {'number': 6765, 'result': 'True'}, {'number': 3561, 'result': 'False'}, {'number': 4181, 'result': 'True'}]

  fibonacci_problem = FibonacciVerifier()
  data = [4506, 233, 614, 55, 4426, 3984, 987, 6765, 3561, 4181]
  output = fibonacci_problem.compute_results(data)

  assert output == expected

def test_prime_classifier():
    expected = [{'number': 2, 'result': 'Prime'}, {'number': 4, 'result': 'Quadratic-Semiprime'}, {'number': 5, 'result': 'Prime'}, {'number': 6, 'result': 'Semiprime'}, {'number': 7, 'result': 'Prime'}, {'number': 8, 'result': '8'}, {'number': 35, 'result': 'Semiprime'}, {'number': 121, 'result': 'Quadratic-Semiprime'}, {'number': 16487, 'result': 'Prime'}, {'number': 27, 'result': '27'}, {'number': 15, 'result': 'Semiprime'}, {'number': 49, 'result': 'Quadratic-Semiprime'}, {'number': 97, 'result': 'Prime'}]

    data = [2, 4, 5, 6, 7, 8, 35, 121, 16487, 27, 15, 49,97]
    prime_problem = PrimeClassifier()
    output = prime_problem.compute_results(data)

    assert output == expected

# verify that the encryption works, decrypting the encrypted 
# message and testing that it matches the original message
def test_encrypt():
    expected = "Hello World!"
    my_system = MySystem(FizzBuzzCreator(),"")
    encrypted_message =  my_system.encrypt("Hello World!")
    decoded_key = base64.urlsafe_b64decode(encrypted_message[0].encode('utf-8'))
    decoded_message = base64.urlsafe_b64decode(encrypted_message[1].encode('utf-8'))

    fernet = Fernet(decoded_key)
    decrypted_message = fernet.decrypt(decoded_message).decode('utf-8')
    assert decrypted_message == expected

def test_decrypt():
    expected = "Hello World!"
    my_system = MySystem(FizzBuzzCreator(),"")
    data_encripted = my_system.encrypt("Hello World!")
    data_decrypted = my_system.decrypt(data_encripted)
    assert data_decrypted == expected








