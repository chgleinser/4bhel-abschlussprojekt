#------------------------------------------------------------------------------
#   Projekt:    Chatprogramm (Clientseite)
#   Datei:      pyChatClient.py
#   Autor:      GleAn, GleCh
#   Datum:      12.06.2020
#   Version:    v0.1
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Log:
#   v0.1:   - Datei "pyChatClient.py" erstellt
#           - Kommentare hinzugefügt
#
# Beschreibung:
#   Dieses Programm ermöglicht die Kommunikation mehrerer Clients über einen
#   Server. Um dies realisieren zu können werden SOCKETS verwendet. Hier
#   befindet sich die Clientseite.
#------------------------------------------------------------------------------

#----- import -----------------------------------------------------------------
import socket, threading

#----- variablen --------------------------------------------------------------
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = 'localhost'
port = 2222

#----- main routine -----------------------------------------------------------
def main:
    client.bind(address, port)

if __name__ == '__main__':  # nur beim Ausführen. NICHT beim Importieren.
    main()

# [] END OF FILE
