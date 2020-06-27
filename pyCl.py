#------------------------------------------------------------------------------
#   Project:    Chatprogram (Clientside)
#   File:       pyCl.py
#   Author:     GleAn, GleCh
#   Date:       22.06.2020
#   Version:    v0.2
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Log:
#   v0.1:   - created file "pyClient.py"
#           - added comments
#           - created main routine
#
#   v0.2:   - added gui through tkinter, because it's easier to program the
#             client, than with a CLI Version
#
#   v0.3:   - finished program. note to self: don't try to program the client
#             for CLI-use. NO REALLY! it's gonna make it more complicated
#
# Description:
#   This program realises a chatprogram with the help of the functionality of
#   sockets. The Server is the "chatroom" to which the clients connect to. The
#   clients can communicate with each other over the chatroom. This program is
#   the clientside of the project. This program should be ready for use in a
#   CLI (that CLI-part is a LIE!) and a GUI-Framework like tkinter.
#------------------------------------------------------------------------------

#----- imports ----------------------------------------------------------------
import socket, sys, threading
import tkinter as tk

#----- networking variables ---------------------------------------------------
cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = sys.argv[1]
port = int(sys.argv[2])

#----- tkinter variables ------------------------------------------------------
window = tk.Tk()
chatroom = tk.Text(window)
msgField = tk.Entry(window)

#----- subroutines ------------------------------------------------------------

# Function: sendMsg
# -----------------
# handles message for sending to server
#
# entry:    tkinter Entry for reading the Text
#
# return:   nothing
def sendMsg():
    msg = msgField.get()
    cl.send(bytes(msg, 'UTF-8'))
    if msg == "bye":
        window.destroy()
    msgField.delete(0, 'end')

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
                chatroom.insert(tk.END, msg + '\n')
            except OSError:
                break

#----- main routine -----------------------------------------------------------
def main():

    #----- initialization -----------------------------------------------------
    cl.connect((address, port))
    sendButton = tk.Button(window, text="Send", command=sendMsg)
    chatroom.pack()
    msgField.pack()
    sendButton.pack()

    #----- main loop ----------------------------------------------------------
    newThread = recvThread()
    window.after(0, newThread.start())
    window.mainloop()

    #----- closing connection -------------------------------------------------
    cl.close()

if __name__ == '__main__':
    main()

# [] END OF FILE
