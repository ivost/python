# https://github.com/drbild/sslpsk

import socket
import ssl
import sslpsk

# preshared keys
PSKS = {'server1': 'abcdef',
        'server2': 'uvwxyz'}


def client(host, port, psk):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('ssl-psk client connecting to {}:{}'.format(host, port))
    tcp_socket.connect((host, port))

    ssl_sock = sslpsk.wrap_socket(tcp_socket,
                                  ssl_version=ssl.PROTOCOL_TLSv1,
                                  psk=lambda hint: (PSKS[hint], 'client1'))

    ssl_sock.sendall("ping")
    msg = ssl_sock.recv(4)
    print('Client received: %s' % (msg))

    ssl_sock.shutdown(socket.SHUT_RDWR)
    ssl_sock.close()


def main():
    host = '127.0.0.1'
    port = 6000
    client(host, port, PSKS)


if __name__ == '__main__':
    main()
