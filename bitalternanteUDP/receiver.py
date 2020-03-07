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

from socket import *

#entrada do numero da porta a ser utilizada
server_port = int(input('PORTA: '))
#valida se é um dígito válido e encerra o script em caso de erro
if server_port < 10001 or server_port > 11000:
    print('Porta invalida...')
    quit()

#abertura do socket
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))

#inicializacao de variaveis de controle
expecting_seq = 0
received_MSGS = 0

while True:
    #le o pacote recebido e mostra no terminal
    package, client_address = server_socket.recvfrom(2048)
    print('')
    print("RECV: " + package.decode())

    #separa os dados recebidos no pacote
    message = package.decode().split(' ')
    SEQNO = message[0]
    DATA = message[1]
    MSGS = message[2]

    #envia ACK da sequencia atual
    ans = "ACK" + SEQNO
    server_socket.sendto(ans.encode(), client_address)
    print("SEND: " + ans)

    #se a sequencia é a esperada, incrementa a contagem
    if int(SEQNO) == expecting_seq:
        expecting_seq = 1 - expecting_seq
        received_MSGS = 1 + received_MSGS
    
    #termina o script após o recebimento do ultimo dado
    if received_MSGS >= int(MSGS):
        print('')
        print("Recepcao concluida...")
        print('')
        quit()