import socket
from tkinter import *
from datetime import datetime


def send(l1,e1):
    message = e1.get()
    client.send(bytes(message,"utf_8"))
    l1.insert(END, "Server " + message + " " + datetime.now().strftime("%H:%M:%S"))
    receive(l1)
    e1.delete(0, END)
def receive(l2):
    message_from_client = client.recv(100)
    l2.insert(END,"Client : "+ message_from_client.decode("utf_8") + " " +  datetime.now().strftime("%H:%M:%S"))
    #print("Client: ", message_from_client.decode("utf-8"))

root = Tk()
root.geometry("500x500")
root.title("Server")
listbox = Listbox(root,bg ="white")
listbox.pack(side=TOP,fill=BOTH,expand=YES)
entry = Entry(root,bg ="white")
entry.pack(side=BOTTOM)
button = Button(root,text="Send Message",command=lambda:send(listbox,entry))
button.pack()

receive_button = Button(root,text="Receive Message",command=lambda:receive(listbox))
receive_button.pack()



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.bind((HOST_NAME, PORT))

s.listen(5) #Maximum number of connection
client, address = s.accept()

root.mainloop()
