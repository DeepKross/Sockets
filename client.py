import socket
import logging

HOST = '127.0.0.1'
PORT = 1028


class Client:

    def __init__(self):
        try:
            new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM,) # try to create a new socket
            logging.getLogger("Client")
            logging.basicConfig(filename="myClient.log",
                                level=logging.INFO,
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                filemode='a',
                                )

            logging.info('Client started.')

            new_socket.connect((HOST, PORT)) #try to connect to server
            logging.info("Connected to a server.")
            while True:
                data = new_socket.recv(256).decode('utf-8')
                print(data)
                if data.__contains__("to stop the program"):
                    break
            logging.info('Welcoming message.')
            while True:
                data = input('Send request:\n')
                new_socket.send(data.encode('utf-8'))
                logging.info('Sent request: ' + data)
                data = new_socket.recv(256).decode('utf-8')
                logging.info('Received message: ' + data)
                print('Answer: ', data)
                if 'Stop' in data or 'STOP' in data:
                    new_socket.close()
                    logging.info("End of session")
                    break
            print('Connection lost.')
            logging.info('Connection lost.')
        except Exception as e:
            print(f'Happened exception: {e}')
            logging.info('Error')

    @staticmethod
    def reconnect():
        while True:
            answer = input("Do you want to reconnect? Y/n: ")
            if answer.lower() in 'yn':
                break
        if answer.lower() == 'y':
            return True
        else:
            return False


def main():
    client = Client()


if __name__ == "__main__":
    main()
