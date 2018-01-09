# https://github.com/drbild/sslpsk

import socket
import ssl
import sslpsk

# preshared keys

PSKS = {'client1': 'abcdef',
        'client2': '123456'}


def server(host, port):
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.bind((host, port))

    print('ssl-psk server listening on {}:{}'.format(host, port))

    tcp_sock.listen(1)

    sock, _ = tcp_sock.accept()

    ssl_sock = sslpsk.wrap_socket(sock,
                                  server_side=True,
                                  ssl_version=ssl.PROTOCOL_TLSv1,
                                  psk=lambda identity: PSKS['identity'],
                                  hint='server1')

    msg = ssl_sock.recv(4)
    print('Server received: ' + msg)
    ssl_sock.sendall("pong")

    ssl_sock.shutdown(socket.SHUT_RDWR)
    ssl_sock.close()


def main():
    host = '127.0.0.1'
    port = 6000
    server(host, port)


if __name__ == '__main__':
    main()