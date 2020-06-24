#------------------------------------------------------------------------------
#   Project:    Chatprogram (Serverside)
#   File:       pySrv.py
#   Author:     GleAn, GleCh
#   Date:       22.06.2020
#   Version:    v0.2
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Log:
#   v0.1:   - created file "pySrv.py"
#           - added comments
#           - created main routine
#
#   v0.2:   - added multithreading capability
#           - added name handling
#
#   v0.3:   - added list for keeping track of clients
#           - created function for broadcasting to other clients
#           - program made CLI-Ready
#
# Description:
#   This program realises a chatprogram with the help of the functionality of
#   sockets. The Server is the "chatroom" to which the clients connect to. The
#   clients can communicate with each other over the chatroom. This program is
#   the serverside of things. This will handle incoming messages and send them
#   to other users. This doesn't necessarily need a GUI.
#------------------------------------------------------------------------------

#----- imports ----------------------------------------------------------------
import socket, threading

#----- variables --------------------------------------------------------------
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
address = 'localhost'
port = 2222
clientList = []

#----- subroutines ------------------------------------------------------------

# Function: broadcast
# -------------------
# Sends the message to other clients
#
# msg:      the message to be sent
# sock:     the socket from where the message was sent
#
# return:   nothing
def broadcast(msg, sock):
    for client in clientList:
        if sock != client:
            client.send(bytes(msg, 'UTF-8'))

#----- classes ----------------------------------------------------------------

# Class: clThread
# ---------------
# Is used to create an object, that gets its own thread.
class clThread(threading.Thread):

    # Function: __init__
    # ------------------
    # Is executed when class is initialized. It's specifically used to add an
    # incoming connection in this program.
    #
    # clSocket: the socket of the client
    #
    # return:   nothing
    def __init__(self, sock):

        #----- initialization -------------------------------------------------
        threading.Thread.__init__(self)
        self.clSocket = sock
        clientList.append(self.clSocket)

        #----- name handling --------------------------------------------------
        self.name = self.clSocket.recv(1024).decode('UTF-8')
        msg = "<%s has joined>" % self.name
        print(msg)
        self.clSocket.send(bytes("<Succesfully Connected!>", 'UTF-8'))

        #----- broadcast to other clients -------------------------------------
        broadcast(msg, self.clSocket)

    # Function: run
    # -------------
    # Is executed when called with .start() or .run() method
    #
    # return:   nothing
    def run(self):
        while True:

            #----- handle message ---------------------------------------------
            data = self.clSocket.recv(1024).decode('UTF-8')
            if data == 'bye':
                break
            msg = "<%s>" % self.name + data
            print(msg)

            #----- broadcast to other clients ---------------------------------
            broadcast(msg, self.clSocket)

        #----- client has disconnected ----------------------------------------
        msg = "<%s has left>" % self.name
        print(msg)
        clientList.remove(self.clSocket)

#----- main routine -----------------------------------------------------------
def main():

    #----- initialization -----------------------------------------------------
    srv.bind((address, port))

    #----- main loop ----------------------------------------------------------
    while True:
        srv.listen(1)
        clSocket, clAddress = srv.accept()
        newThread = clThread(clSocket)
        newThread.start()

if __name__ == '__main__':
    main()

# [] END OF FILE
