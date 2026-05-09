#The program is written to creat a client for chat application
import socket
from tkinter import *
from datetime import datetime

def send(l1,e1):
    message = e1.get()
    s.send(bytes(message, "utf-8"))
    l1.insert(END, "Client : " + message + " " + datetime.now().strftime("%H:%M:%S"))
    receive(l1)
    e1.delete(0, END)
def receive(l2):
    message = s.recv(100)
    l2.insert(END, "Server : "+ message.decode("utf_8") + " " +  datetime.now().strftime("%H:%M:%S"))

root = Tk()
root.geometry("500x500")
root.title("Client")
listbox = Listbox(root,bg ="white")

listbox.pack(fill="both",expand="yes")
entry = Entry(root,bg ="white")
entry.pack(side=BOTTOM)
button = Button(root,text="Send Message",command=lambda:send(listbox,entry))
button.pack()

receive_button = Button(root,text="Receive Message",command=lambda:receive(listbox))
receive_button.pack()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.connect((HOST_NAME, PORT))

root.mainloop()
