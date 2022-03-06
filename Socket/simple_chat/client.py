import socket
import threading
import tkinter as tk
import tkinter.scrolledtext
from tkinter import simpledialog


HOST = "127.0.0.1"
PORT = 9999


class Client():

    def __init__(self, host, port):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tk.Tk()
        msg.withdraw()

        self.nickname = simpledialog.askstring(
            "Nickname", "please input youe nickname", parent=msg)

        self.gui_done = False
        self.running = False

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):

        self.win = tk.Tk()
        self.win.configure(bg="lightgray")

        self.chat_label = tk.Label(self.win, text="Chat:", bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state="disabled")

        self.msg_label = tk.Label(self.win, text="Chat:", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tk.Text(self.win, height=5)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tk.Button(self.win, text="send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True
        self.win.protocol("WM_DELETE_WINDOW", self.stop)
        self.win.mainloop()

    def write(self):
        message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
        self.sock.send(message.encode('utf_8'))
        self.input_area.delete('1.0', 'end')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def receive(self):
        while self.running:
            try:
                msg = self.sock.recv(1024).decode('utf_8')
                if msg == "NICK":
                    self.sock.send(self.nickname.encode('utf_8'))
                else:
                    if self.gui_done:
                        self.text_area.config(state="normal")
                        self.text_area.insert("end", msg)
                        self.text_area.yview("end")
                        self.text_area.config(state="disabled")
            except ConnectionAbortedError:
                break
            except Exception:
                print("error")
                self.sock.close()
                break


Client(HOST, PORT)