#------------------------------------------------------------------------------
#   Project:    Chatprogram (Clientside)
#   File:       pyCl.py
#   Author:     GleAn, GleCh
#   Date:       22.06.2020
#   Version:    v0.1
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Log:
#   v0.1:   - created file "pyClient.py"
#           - added comments
#           - created main routine
#
# Description:
#   This program realises a chatprogram with the help of the functionality of
#   sockets. The Server is the "chatroom" to which the clients connect to. The
#   clients can communicate with each other over the chatroom. This program is
#   the clientside of the project. This program should be ready for use in a
#   CLI and a GUI-Framework like tkinter.
#------------------------------------------------------------------------------

#----- imports ----------------------------------------------------------------
import socket, sys, select

#----- variables --------------------------------------------------------------
cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = sys.argv[1]
port = 2222

#----- subroutines ------------------------------------------------------------

# Function: receiveMsg
# --------------------
# handles messages being received
#
# return:   nothing
def receiveMsg():
    msgRecv = cl.recv(1024).decode('UTF-8')
    print(msgRecv)

# Function: nameHandler
# ---------------------
# Awaits input for a name and sends it to the server
#
# return:   name
def nameHandler():
    name = input("Please input name for chatroom: ")
    cl.send(bytes(name, 'UTF-8'))
    receiveMsg()
    return name

#----- main routine -----------------------------------------------------------
def main():

    #----- initialization -----------------------------------------------------
    cl.connect((address, port))
    name = nameHandler()

    #----- main loop ----------------------------------------------------------
    while True:
        msgSend = input("<%s>" % name)
        cl.send(bytes(msgSend, 'UTF-8'))
        if msgSend == 'bye':
            print("<Sucessfully Disconnected!>")
            break

if __name__ == '__main__':
    main()

# [] END OF FILE
