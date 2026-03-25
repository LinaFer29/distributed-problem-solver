import json 
import base64
from cryptography.fernet import Fernet
from data_handler.i_data_generator import IDataGenerator
import logging

logging.basicConfig(filename='dataServer.log',
      filemode='a',
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
      datefmt='%Y-%m-%d %H:%M:%S',
      level=logging.DEBUG)

class DataServer:
    def __init__(self, data_generator_instance : IDataGenerator):
        self.data_generator = data_generator_instance

    def generate_data(self,quantity,lower,upper):
        numbers = self.data_generator.generate_numbers(quantity,lower,upper)
        #print("\n", numbers)
        numbers_str = json.dumps(numbers)
        numbers_encrypted = self.encrypt(numbers_str)
        numbers_json = {"numbers": numbers_encrypted}
        
        return numbers_json

    def encrypt(self,message):
        data = []
        key = Fernet.generate_key()
        data.append(base64.urlsafe_b64encode(key).decode('utf-8'))  
        encrypt_f = Fernet(key)
        message_encrypted = encrypt_f.encrypt(message.encode('utf-8'))
        data.append(base64.urlsafe_b64encode(message_encrypted).decode('utf-8'))   # Convert the encrypted message to a string
        return data

    def decrypt(self, encrypted_data): #encrypted_data = ['key','encrypted_data']
        try:
            key = base64.urlsafe_b64decode(encrypted_data[0].encode('utf-8'))  # Decode the key
            message_encrypted = base64.urlsafe_b64decode(encrypted_data[1].encode('utf-8'))  # Decode the encrypted message
            decrypt_f = Fernet(key)
        except TypeError as error:
            print(error)
            logging.error(f'{error} - can\'t decrypt data')
        else:
            message_decrypted = decrypt_f.decrypt(message_encrypted).decode('utf-8')  # Decrypt the message and convert to string
      
            return message_decrypted # str
        
    def shutdown(self):
        return "Shutting down DataServer"