import time
import struct
import socket
from gnocchiclient import auth
from gnocchiclient.v1 import client
import datetime

MCAST_GRP = '225.0.0.37'
MCAST_PORT = 1406

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((MCAST_GRP, MCAST_PORT))
mreq = struct.pack('4sl', socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print("Conectando no Gnocchi...")
 

auth_plugin = auth.GnocchiBasicPlugin(user="admin", endpoint="http://10.7.52.84:8041")
gnocchi = client.Client(session_options={'auth': auth_plugin})
 
date_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S-03:00')


corrente=0
tensao=0
def recebeValor():
    valor = sock.recv(1024) #.decode('utf-8')
    novoValor = struct.unpack('cf',valor)
    return novoValor


def sendGrafana(corrente,tensao_final,potencia_final):

	date_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S-03:00')
	#print("HORA: " + str(date_time))
        #print("Inserindo tensao...")
        medidas = [{'timestamp': date_time, 'value': tensao_final}] 
        response = gnocchi.metric.add_measures('tensao', medidas, 'e5cb7d74-ba18-51a0-8f3e-3ec57458255b')
        #print(response)
         
       # print("Inserindo corrente...")
        medidas = [{'timestamp': date_time, 'value': corrente}] 
        response = gnocchi.metric.add_measures('corrente', medidas, 'e5cb7d74-ba18-51a0-8f3e-3ec57458255b')
        #print(response)

       # print("Inserindo potencia...")
        medidas = [{'timestamp': date_time, 'value': potencia_final}] 
        response = gnocchi.metric.add_measures('potencia', medidas, 'e5cb7d74-ba18-51a0-8f3e-3ec57458255b')
       # print(response)
        

	
       # print("Inserindo tensao...")
        medidas = [{'timestamp': date_time, 'value': tensao_final}] 
        response = gnocchi.metric.add_measures('tensao', medidas, '4c41964f-f6ae-5629-aab8-7ccaf26e9ba6')
       # print(response)

        #print("Inserindo corrente...")
        medidas = [{'timestamp': date_time, 'value': corrente}] 
        response = gnocchi.metric.add_measures('corrente', medidas, '4c41964f-f6ae-5629-aab8-7ccaf26e9ba6')
       # print(response)

       # print("Inserindo potencia...")
        medidas = [{'timestamp': date_time, 'value': potencia_final}] 
        response = gnocchi.metric.add_measures('potencia', medidas, '4c41964f-f6ae-5629-aab8-7ccaf26e9ba6')
        #print(response)
	

	
       # print("Inserindo tensao...")
        medidas = [{'timestamp': date_time, 'value': tensao_final}] 
        response = gnocchi.metric.add_measures('tensao', medidas, 'e7a04919-5d09-5793-a361-e7762d8fb3a0')
        #print(response)

       # print("Inserindo corrente...")
        medidas = [{'timestamp': date_time, 'value': corrente}] 
        response = gnocchi.metric.add_measures('corrente', medidas, 'e7a04919-5d09-5793-a361-e7762d8fb3a0')
       # print(response)

       # print("Inserindo potencia...")
        medidas = [{'timestamp': date_time, 'value': potencia_final}] 
        response = gnocchi.metric.add_measures('potencia', medidas, 'e7a04919-5d09-5793-a361-e7762d8fb3a0')
        #print(response)

        print("\n"+"========================================================="+ "\n")




def run():
    flagCorrente = 0
    flagTensao=0
    tempoInicial = time.time()
    cont=1
    while True:
                valor = recebeValor()
                if(valor[0] =='c'):
                    corrente = valor[1]
                    #print(corrente)
                    flagCorrente = 1
                if(valor[0] =='t'):
                    tensao = valor[1]
                    flagTensao = 1
                   # print(tensao)
                if(flagCorrente ==1 and flagTensao==1):
                    print('coleta finalizada, enviando dados para o Grafana')
                    flagCorrente = 0
                    flagTensao=0
                    
                    #print(tensao)
                   # print(corrente)
                    
                    tensao_final = (220*tensao/12)
                    potencia_final = tensao_final*corrente
                    
                    #print("a corrente medida pelo sensor é: "+str(corrente))
                    #print("a tensao medida pelo sensor é: "+str(tensao))

                    #print("a tensao final é: "+str(tensao_final))
                    #print("a potencia é: "+str(potencia_final))

                    sendGrafana(corrente,tensao_final,potencia_final)

print('servidor rodando')

run()
