#------------------------------------------------------------------------------
#   Projekt:    Chatprogramm (Clientseite)
#   Datei:      pyChatClient.py
#   Autor:      GleAn, GleCh
#   Datum:      12.06.2020
#   Version:    v0.2
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Log:
#   v0.1:   - Datei "pyChatClient.py" erstellt
#           - Kommentare hinzugefügt
#
#   v0.2:   - added exception handler
#
# Beschreibung:
#   Dieses Programm ermöglicht die Kommunikation mehrerer Clients über einen
#   Server. Um dies realisieren zu können werden SOCKETS verwendet. Hier
#   befindet sich die Clientseite.
#------------------------------------------------------------------------------

#----- import -----------------------------------------------------------------
import socket, sys

#----- variablen --------------------------------------------------------------
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = 'localhost'
port = 2222

#----- subroutines ------------------------------------------------------------
def nameHandler():
    name = input("What's your name?: ")
    client.sendall(name.encode("UTF8"))
    return name

#----- main routine -----------------------------------------------------------
def main():
    try:
        client.connect((address, port))
        name = nameHandler()
        while True:
            msg = client.recv(1024)
            print(msg)
            data = input("<%s>" % name)
            client.sendall(data.encode("UTF8"))
    finally:
        client.close()

if __name__ == '__main__':  # nur beim Ausführen. NICHT beim Importieren.
    main()

# [] END OF FILE
