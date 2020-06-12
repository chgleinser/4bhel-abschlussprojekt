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
import socket, threading

#----- variablen --------------------------------------------------------------
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = 'localhost'
port = 2222

#----- main routine -----------------------------------------------------------
def handleConn:
    while True:
        (clientSocket, clientAddr) = server.accept()

def main:
    server.bind(address, port)
    server.listen(1)
    handleConn()

if __name__ == '__main__':  # nur beim Ausführen. NICHT beim Importieren.
    main()

# [] END OF FILE
