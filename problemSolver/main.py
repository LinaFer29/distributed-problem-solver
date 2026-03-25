import random
import socket
import json
import logging
import requests
from my_system import MySystem
from problems_Solver.fizzbuzz_creator import FizzBuzzCreator
from problems_Solver.prime_classifier_creator import PrimeClassifierCreator
from problems_Solver.fibonacci_verifier_creator import FibonacciVerifierCreator

logging.basicConfig(filename='system.log',
          filemode='a',
          format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
          datefmt='%Y-%m-%d %H:%M:%S',
          level=logging.DEBUG)

def shutdown_request_data_server(route):
        url = "https://1c8cd0ab-1058-4932-9a7e-e7c73ea9cc4d-00-h7zud3vznxpb.kirk.replit.dev"
        path = url + "/" + route
        response = requests.get(path)
        response_json = response.json()
        print(response_json)


def manage_problem(problem):
    url = "https://1c8cd0ab-1058-4932-9a7e-e7c73ea9cc4d-00-h7zud3vznxpb.kirk.replit.dev"
    if problem == "fizzbuzz":
        fizzbuzz = FizzBuzzCreator()
        logging.info('Initializing FizzBuzz problem')
        return MySystem(fizzbuzz,url)
    if problem == "fibonacciverifier":
        fibonacci = FibonacciVerifierCreator()
        logging.info('Initializing FibonacciVerifier problem')
        return MySystem(fibonacci,url)
    if problem == "primeclassifier":
        prime = PrimeClassifierCreator()
        logging.info('Initializing PrimeClassifier problem')
        return MySystem(prime,url)

def manage_system(data_json):
    response = {}
    problem = data_json['problem']
    if problem == 'shutdown':
        shutdown_request_data_server("shutdown")
        flag = data_json['status']
        logging.info('Shutdown problemSolver')
        response = {"flag": flag, "message": "Shutting down ProblemSolver"}
    else:
        quantity = data_json['quantity']
        lower = data_json['lower']
        upper = data_json['upper']
        output = data_json['output']

        print("Problem:",problem," - Quantity:", quantity," - Lower limit:", lower," - Upper limit:",upper," - Output:",output)

        my_system = manage_problem(problem.lower()) 
        data_server_json = my_system.encrypt_content(quantity,lower,upper) # return  '{"quantity": sdfdg33, "lower": ewrwe4, "upper": 245tfrg}'
        numbers =my_system.data_request_post(data_server_json,"generateData") # return {"numbers": [dfrughfvmfhfv,fbfdrfgrfhhrheh]}  --> [0] key -[1] lista  
        decrypted_numbers = my_system.decrypt_content(numbers)# return -> [1,2,3,45,...]
        results = my_system.run_problem_solver(decrypted_numbers) # parameter -> [1,2,3,45,...]  |  return [{ "number":3, "result":"fizz"}, { "number":5, "result":"buzz"}, { "number":15, "result":"fizzbuzz"}]
        results_json = my_system.generate_json(results) #return '[{ "number":3, "result":"fizz"}, { "number":5, "result":"buzz"}, { "number":15, "result":"fizzbuzz"}]'
        response = {"flag": True, "message": results_json}
        #print(results_json)
    return response

def client_connection():

    HOST ="localhost"
    PORT = 8000
    flag = True
        
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket_connection:
        try:
            socket_connection.bind((HOST,PORT))
            socket_connection.listen()
        except OSError as error:
            print(error)
            logging.error(f'{error} - can\'t run Problem Solver')
        else:
            while flag:
                conn, addr = socket_connection.accept()
                with conn:
                    print(f'\nConnected by {addr}')
                    data = conn.recv(1024)
                    data_json = json.loads(data.decode('utf-8'))
                    response = manage_system(data_json)
                    flag = response['flag']
                    conn.send(response['message'].encode('utf-8'))
                    conn.close() 
    socket_connection.close()

def main():
  client_connection()

if __name__ == "__main__":
  main()