import evb
import socket
import tkinter

PORT = 65000  # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as board_socket:
    board_socket.connect(('localhost', PORT))
    root = tkinter.Tk()
    board = evb.Evb(root, board_socket)
    root.mainloop()
