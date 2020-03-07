# Arquitetura e Redes de Comunicação de Sistemas Embarcados
# Projeto I – Transporte confiável de dados utilizando protocolo de bit alternante
# MATHEUS ARCANGELO ESPERANÇA
# RA 150007034

# Arquivos necessarios
sender.py (script para envio dos dados)
receiver.py (script para envio dos dados)

# Ambiente utilizado
Para o desenvolvimento e testes dos scripts foram utilizados dois computadores, 
ambos com a IDE Visual Studio Code e a extensão Python devidamenta instalada e habilitada
É necessário também que os computadores estejam na mesma rede

# Projeto
O projeto consiste na implementação de um script para transporte confiável de dados
entre em sender RTD 3.0 e um receiver RTD 2.2, utilizando o protocolo de bit alternante

# Funcionamento
O protocolo basicamente implementa um numero de sequencia para os pacotes que sao enviados
a cada troca de mensagens entre o sender e o receiver, tendo como ação o reenvio dos dados
em caso de perda do pacote ou no descarte de mensagens duplicadas ao serem comparados os
numero de sequência e ACK.

# Uso
Para testar o protocolo é necessário rodar em uma máquina o arquivo "receiver.py" e na outra
o arquivo "sender.py", respectivamente.

No computador que será o "receiver" insira o numero da porta a ser utilizada, com um valor
entre 10001 e 11000.

No computador que será o "sender" insira o endereço IP do "receiver", o numero da porta
(o mesmo utilizado no receivar) e o número de mensagens "MSGS" a serem enviadas.

Neste momento devem ser inseridos no "sender" os dados, um a um, até que a contagem do
numero de mensagens enviadas com sucesso chegue ao final. Neste momento, se nao houverem
nenhum erro de comunicação entre os dispositivos, ambos irão apresentar uma mensagem
informando o final da transmissão dos dados e encerrarão os scripts


