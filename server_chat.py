###########################################################################
##  project : Chatprogramm
##  file    : server_chat.py
##  author  : Andreas und Christoph Gleinser
##  date    : 19.06.2020
###########################################################################
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

#Chat
def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s hat sich verbunden." % client_address) #Nachricht wenn sich jmd verbindet
        client.send(bytes("Geben Sie Ihren Namen ein", "utf8")) #Namensgebung
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

#Chat
def handle_client(client):
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Willkommen im Chat %s! Um zu beenden, geben Sie {quit} ein.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s ist den Chat beigetreten!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name + ": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s hat den Chat verlassen." % name, "utf8"))
            break

# Broadcast an alle Clients
def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Warten auf Verbindung...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()