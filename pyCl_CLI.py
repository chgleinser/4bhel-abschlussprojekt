#------------------------------------------------------------------------------
#   Project:    Chatprogram (Clientside)
#   File:       pyCl_CLI.py
#   Author:     GleAn, GleCh
#   Date:       22.06.2020
#   Version:    v0.2
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Log:
#   v0.1:   - copied "pyCl.py" and renamed to "pyCl_CLI.py"
#           - added comments
#           - created main routine
#
# Description:
#   This program realises a chatprogram with the help of the functionality of
#   sockets. The Server is the "chatroom" to which the clients connect to. The
#   clients can communicate with each other over the chatroom. This program is
#   the clientside of the project. This program should be ready for use in a
#   CLI.
#------------------------------------------------------------------------------

#----- imports ----------------------------------------------------------------
import socket, sys, threading
import tkinter as tk

#----- networking variables ---------------------------------------------------
cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = sys.argv[1]
port = int(sys.argv[2])

#----- classes ----------------------------------------------------------------

# Class: recvThread
# -----------------
# handles messages being received,
# parallel to input
class recvThread(threading.Thread):

    # Function: __init__
    # ------------------
    # initializes thread
    #
    # return:   nothing
    def __init__(self):
        threading.Thread.__init__(self)

    # Function: run
    # -------------
    # mainloop of the thread
    #
    # return:   nothing
    def run(self):
        while True:
            try:
                msg = cl.recv(1024).decode('UTF-8')
                print(msg)
            except OSError:
                break

#----- subroutines ------------------------------------------------------------

# Function: namHandler
# -----------------
# handles name for sending to server
#
# return:   name
def nameHandler():
    name = input()
    cl.send(bytes(name, 'UTF-8'))
    msg = cl.recv(1024).decode('UTF-8')
    print(msg)
    return name

#----- main routine -----------------------------------------------------------
def main():

    #----- initialization -----------------------------------------------------
    cl.connect((address, port))
    name = nameHandler()
    newThread = recvThread()
    newThread.start()

    #----- main loop ----------------------------------------------------------
    while True:
        try:
            data = input("<%s>" % name)
            cl.send(bytes(data, 'UTF-8'))
            if msg == "bye":
                break

    #----- closing connection -------------------------------------------------
    cl.close()

if __name__ == '__main__':
    main()

# [] END OF FILE
