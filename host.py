import socket
import subprocess
import os

PORT = 65000
FRAME = 1024
"wiadomość  bitów, pierwszy bit to numer funkcji"


def functions(message):
    f = int(message[0])
    if f == 1:
        what = int(message[1])
        if what == 1:
            cmd = "amixer -D pulse sset Master 10%-"
        else:
            cmd = "amixer -D pulse sset Master 10%+"
        subprocess.call(cmd, shell=True)
        return ""
    if f == 2:
        cmd = "amixer -D pulse get Master | awk -F 'Left:|[][]' '{ print $3 }' | tr -d '%' | tr -d '\n' > temp"
        subprocess.call(cmd, shell=True)
        with open("temp", 'r') as file:
            vol = file.read()
        os.remove("temp")
        return "{}{}".format(2, vol[:len(vol)-1])
    if f == 3:
        "test"
        return "random text"
    if f == 4:
        pass
    if f == 5:
        pass
    if f == 6:
        pass


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as host_socket:
    host_socket.bind(('localhost', PORT))
    host_socket.listen(1)
    connection, address = host_socket.accept()
    with connection:
        print('Connected by', address)
        data = ''
        while True:
            msg = connection.recv(FRAME)
            print(msg)
            msg = msg.decode("utf-8")
            print(msg)
            data += msg
            if len(data) > 0:
                func = functions(data)
                to_send = "{}".format(func)
                connection.send(bytes(to_send, "utf-8"))
                data = ''
