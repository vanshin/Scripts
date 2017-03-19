#encoding=utf8

import socket

def get_info():
    try:
        info = raw_input()
        buffer = []
        name, port = info.split(" ")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(name), int(port)))
        index_s = b'GET / HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n' % (name)
        s.send(index_s)
        while True:
            d = s.recv(1024)
            if d:
                buffer.append(d)
            else:
                break
        data = "".join(buffer)
        return data
    except Exception as e:
        print e
    finally:
        s.close()
    
def send_mess():
    pass

def main():
    mess = get_info()
    print mess

if __name__ == '__main__':
    main()