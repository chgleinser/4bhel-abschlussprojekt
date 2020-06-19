#------------------------------------------------------------------------------
#   Projekt:    Chatprogramm (Serverseite)
#   Datei:      pyChatServer.py
#   Autor:      GleAn, GleCh
#   Datum:      12.06.2020
#   Version:    v0.2
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Log:
#   v0.1:   - Datei "pyChat.py" erstellt
#           - Kommentare hinzugefügt
#           - Datei auf "pyChatServer.py" umbenennt.
#
#   v0.2:   - Funktion fürs Verbindungs handling erstellt
#
# Beschreibung:
#   Dieses Programm ermöglicht die Kommunikation mehrerer Clients über einen
#   Server. Um dies realisieren zu können werden SOCKETS verwendet. Hier
#   befindet sich die Serverseite.
#------------------------------------------------------------------------------

#----- import -----------------------------------------------------------------
import socket, threading, sys

#----- variablen --------------------------------------------------------------
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = 'localhost'
port = 2222

#----- classes ----------------------------------------------------------------
class clientThread(threading.Thread):
    def __init__(self, clientAddr, clientSocket):
        threading.Thread.__init__(self)
        self.csocket = clientSocket
    def nameHandler(self):
        name = ''
        data = self.csocket.recv(1024).decode("UTF8")
        if not name: # check, if name is empty
            name = data
            print("<%s has entered the chatroom>" % name)
            self.csocket.sendall(data.encode("UTF8"))
        return name
    def run(self):
        while True:
            data = self.csocket.recv(1024).decode("UTF8")
            print("<%s> " % name, data)
            self.csocket.sendall(data.encode("UTF8"))

#----- main routine -----------------------------------------------------------
def main():
    server.bind((address, port))
    server.listen(1)
    try:
        while True:
            (clientSocket, clientAddr) = server.accept()
            client = clientThread(clientAddr, clientSocket)
            client.nameHandler()
            client.start()
    finally:
        server.close()

if __name__ == '__main__':  # nur beim Ausführen. NICHT beim Importieren.
    main()

# [] END OF FILE
