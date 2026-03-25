import base64
import json
import logging
from cryptography.fernet import Fernet
import requests
from problems_Solver.fizzbuzz_creator import FizzBuzzCreator
from problems_Solver.problem_solver_creator import ProblemSolverCreator

logging.basicConfig(filename='system.log',
          filemode='a',
          format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
          datefmt='%Y-%m-%d %H:%M:%S',
          level=logging.DEBUG)

class MySystem:

    def __init__(self,problem_creator_instance : ProblemSolverCreator, url):
        self.problem_creator = problem_creator_instance
        self.base_url = url
    
    def run_problem_solver(self,data):
        results = self.problem_creator.problemSolver_management(data)
        return results
    
    def generate_json(self,data):
        data_json = json.dumps(data)
        return data_json
    
    def encrypt(self, message):
        data = []
        key = Fernet.generate_key()
        data.append(base64.urlsafe_b64encode(key).decode('utf-8'))  # Convert key to string
        encrypt_f = Fernet(key)
        message_encrypted = encrypt_f.encrypt(message.encode('utf-8'))
        data.append(base64.urlsafe_b64encode(message_encrypted).decode('utf-8'))  # Convert the encrypted message to a string
        return data
    
    def encrypt_content(self,quantity,lower,upper):

        quantity_encrypted = self.encrypt(quantity)
        lower_encrypted = self.encrypt(lower)
        upper_encrypted = self.encrypt(upper)
        
        data_server_dict = {"quantity": quantity_encrypted, "lower":lower_encrypted, "upper":upper_encrypted}
        data_json = json.dumps(data_server_dict)
        return data_json

    def decrypt(self, encrypted_data):
        
        key = base64.urlsafe_b64decode(encrypted_data[0].encode('utf-8'))  # Decode the key
        message_encrypted = base64.urlsafe_b64decode(encrypted_data[1].encode('utf-8'))  # Decode the encrypted message
        decrypt_f = Fernet(key)
        message_decrypted = decrypt_f.decrypt(message_encrypted).decode('utf-8')  # Decrypt the message and convert to string
        return message_decrypted
    
    def decrypt_content(self,numbers):
        #numbers_json = json.loads(numbers)
        numbers_encrypted = numbers['numbers']
        numbers_decrypted = self.decrypt(numbers_encrypted)
        data_list = json.loads(numbers_decrypted)
        # print(type(data_list))
        return data_list
    
    def data_request_post(self,data,route):
        path = self.base_url + "/" +route
        try:
            data_json = json.loads(data)
            # print(data_json)
            response = requests.post(path, json=data_json)
            response_json = response.json()
        except json.JSONDecodeError as error:
            logging.error(f'{error} -  Unexpected Response From DataServer')
            print(error)
        else:
            #print(response_json)
            return response_json
