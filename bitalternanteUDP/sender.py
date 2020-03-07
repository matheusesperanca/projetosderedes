#
# Arquitetura e Redes de Comunicação de Sistemas Embarcados
#
# Projeto I – Transporte confiável de dados utilizando protocolo de bit alternante
#
# sender.py (script para envio dos dados)
# receiver.py (script para envio dos dados)
#
# Instrucoes para uso disponiveis no arquivo README.md
#
# MATHEUS ARCANGELO ESPERANÇA
# RA 150007034
#

import os
from socket import *

#entrada do endereco IP do receiver
server_name = input('IP receiver: ') 
#valida se é um dígito válido e encerra o script em caso de erro
ping = os.system("ping -c 1 " + server_name)
if ping != 0:
    print("IP receiver invalido...")
    quit()

#entrada do numero da porta a ser utilizada
server_port = int(input('PORTA: '))
#valida se o numero esta dentro do intervalo definido
if server_port < 10001 or server_port > 11000:
    print("Porta invalida...")
    quit()

#entrada do numero de mensagens a serem enviadas ao receiver
MSGS = input('MSGS: ')
#valida se é um dígito válido e encerra o script em caso de erro
if MSGS.isdigit() == 0:
    print("N mensagens invalido...")
    quit()

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)

SEQNO = 0
sent_MSGS = 0

while sent_MSGS < int(MSGS):
    
    print('')
    DATA = input('DATA: ')
    if DATA.isdigit() == 0:
        print("Dado invalido...")
        quit()        

    ack_received = False
    while not ack_received:

        message = str(SEQNO) + ' ' + DATA + ' ' + MSGS
        print('SEND: ' + message)
        client_socket.sendto(message.encode() , (server_name, server_port))

        try:
            response, server_address = client_socket.recvfrom(2048)

        except timeout:
            print("RECV: timeout")

        else:
            print('RECV: ' + response.decode())
            ack_seq = response[3] - 48
            if ack_seq == SEQNO:
                ack_received = True

    SEQNO = 1 - SEQNO
    sent_MSGS = 1 + sent_MSGS

print('')
print("Envio concluido...")
print('')

client_socket.close()