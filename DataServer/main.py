import json

from flask import Flask, jsonify, request
import random
import logging

from data_server.data_server import DataServer
from data_handler.normal_generator import NormalGenerator
from data_handler.uniform_generator import UniformGenerator

logging.basicConfig(filename='dataServer.log',
      filemode='a',
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
      datefmt='%Y-%m-%d %H:%M:%S',
      level=logging.DEBUG)

def initiaze_data_server():
    flag = random.choice([True, False])
    if flag:
        data_generator = NormalGenerator()
        logging.info(f"Injecting NormalGenerator dependecy")
    else:
        data_generator = UniformGenerator()
        logging.info(f"Injecting UniformGenerator dependecy")

    data_server = DataServer(data_generator)
    return data_server

app = Flask(__name__)


@app.route('/')
def index():
    return "Hi! I'm DataServer",200

@app.route('/generateData',methods=['GET','POST'])
def generate_data():
    if request.method == "POST":        
        request_data = request.get_json()
        data_server = initiaze_data_server()
        try:
            quantity = data_server.decrypt(request_data["quantity"])
            lower = data_server.decrypt(request_data["lower"])
            upper = data_server.decrypt(request_data["upper"])
        except TypeError as error:
            print(error)
            logging.error(f'{error} - can\'t decrypt data')
        else:
            
            print(quantity,lower,upper)
            numbers_json = data_server.generate_data(quantity,lower,upper)
            return jsonify(numbers_json),200
    return "Bad request",400

@app.route('/shutdown',methods=['GET'])
def shutdown():
    data_server = DataServer(NormalGenerator())
    logging.info("Shutting down DataServer")
    msg = data_server.shutdown()
    return jsonify(msg),200

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
